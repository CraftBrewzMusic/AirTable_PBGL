"""Recursive linked-record expansion for AirTable API responses."""
from __future__ import annotations

import re
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Literal

if TYPE_CHECKING:
    from .api import AirtableClient
    from .md_parser import TableInfo

# table_id -> {field_name -> target_table_id}
LinkInfo = dict[str, dict[str, str]]

_LINK_PATTERN = re.compile(r"Array of linked records IDs from the (.+?) table\.")
_LINK_FIELD_TYPE = "Link to another record"

_REC_ID_RE = re.compile(r"^rec[A-Za-z0-9]{14}$")


def _is_raw_id_list(value: Any) -> bool:
    return (
        isinstance(value, list)
        and bool(value)
        and all(isinstance(v, str) and _REC_ID_RE.match(v) for v in value)
    )


@dataclass
class SpineEntry:
    """Traversal policy for one table in the ownership spine.

    Fields in `follow` (or matching `follow_re`) are recursively expanded.
    Fields in `name_only` (or matching `name_only_re`) are fetched as {id, _name}.
    All other linked fields are stripped from the output.
    """

    follow: frozenset[str] = field(default_factory=frozenset)
    name_only: frozenset[str] = field(default_factory=frozenset)
    follow_re: re.Pattern[str] | None = None
    name_only_re: re.Pattern[str] | None = None

    def classify(self, field_name: str) -> Literal["follow", "name_only", "skip"]:
        if field_name in self.follow or (self.follow_re and self.follow_re.match(field_name)):
            return "follow"
        if field_name in self.name_only or (self.name_only_re and self.name_only_re.match(field_name)):
            return "name_only"
        return "skip"


# Hardcoded traversal policy keyed by table ID.
# Tables not present here get an implicit empty SpineEntry — all linked fields stripped.
_SPINE: dict[str, SpineEntry] = {
    "tbl7rjVKUd5faZ7fV": SpineEntry(  # Releases
        follow=frozenset({"Recordings"}),
        name_only=frozenset({
            "Primary Artist",
            "Featured Artist(s)",
            "Original release label",
            "Current release label",
        }),
    ),
    "tblESvQQmOBbEXAH0": SpineEntry(  # Recordings
        follow=frozenset({"Compositions", "Compositions 2", "Compositions 3"}),
        name_only=frozenset({
            "Primary Artist",
            "Featured Artist",
            "Master Owner 1",
            "Master Owner 2",
            "Master Owner 3",
        }),
    ),
    "tblomWINKPjfgAVpo": SpineEntry(  # Compositions
        follow_re=re.compile(r"^Songwriter [1-9]$"),
        name_only_re=re.compile(r"^Songwriter [1-9] .*Pub"),
    ),
    "tbl2KLh2RIrS5AmSX": SpineEntry(),  # Songwriters — leaf
    "tbl6TNKQRPfY3hXZ2": SpineEntry(),  # Publishers — leaf
}


@dataclass
class ExpandConfig:
    """Pre-computed, traversal-invariant configuration for expand_record."""

    # table_id -> name of the primary (first) field, used for name-only resolution
    primary_field_map: dict[str, str] = field(default_factory=dict)
    # (table_id, record_id) -> display name; shared across all recursion branches
    name_cache: dict[tuple[str, str], str] = field(default_factory=dict)


def build_link_info(tables: list[TableInfo]) -> LinkInfo:
    """Build a map of table_id -> {field_name -> target_table_id} for linked fields."""
    name_to_id: dict[str, str] = {t["name"]: t["table_id"] for t in tables}
    link_info: LinkInfo = {}

    for table in tables:
        tid = table["table_id"]
        for fld in table["fields"]:
            if fld["type"] != _LINK_FIELD_TYPE:
                continue
            m = _LINK_PATTERN.search(fld["description"])
            if not m:
                continue
            target_name = m.group(1)
            target_id = name_to_id.get(target_name)
            if target_id is None:
                continue
            link_info.setdefault(tid, {})[fld["name"]] = target_id

    return link_info


def build_expand_config(tables: list[TableInfo]) -> ExpandConfig:
    """Build expansion config from loaded tables.

    Derives a primary-field map (first field per table, used for name resolution).
    """
    primary_field_map = {
        t["table_id"]: t["fields"][0]["name"]
        for t in tables
        if t["fields"]
    }
    return ExpandConfig(primary_field_map=primary_field_map)


def expand_api_response(
    result: dict[str, Any],
    table_id: str,
    tables: list[TableInfo],
    client: AirtableClient,
    depth: int,
    *,
    on_fetch: Callable[[str, str], None] | None = None,
) -> dict[str, Any]:
    """Expand linked records in a raw AirTable API response.

    Handles both list responses ({"records": [...]}) and single-record
    responses ({"id": ..., "fields": {...}}) by inspecting the result shape.
    """
    link_info = build_link_info(tables)
    config = build_expand_config(tables)

    if "records" in result:
        records = result.get("records", [])
        result["records"] = [
            expand_record(rec, table_id, link_info, client, depth,  # type: ignore[arg-type]
                          config=config, on_fetch=on_fetch)
            for rec in records  # type: ignore[union-attr]
        ]
        return result
    else:
        return expand_record(result, table_id, link_info, client, depth,
                             config=config, on_fetch=on_fetch)


def expand_record(
    record: dict[str, Any],
    table_id: str,
    link_info: LinkInfo,
    client: AirtableClient,
    depth: int,
    *,
    config: ExpandConfig | None = None,
    on_fetch: Callable[[str, str], None] | None = None,
) -> dict[str, Any]:
    """Recursively expand linked-record fields using the hardcoded ownership spine.

    Args:
        record: AirTable record dict {"id": ..., "fields": {...}}.
        table_id: The table this record belongs to.
        link_info: Built by build_link_info().
        client: AirtableClient for fetching linked records.
        depth: Remaining expansion depth; 0 strips all raw ID lists and returns.
        config: Pre-computed expansion config. Uses empty defaults if omitted.
        on_fetch: Called just before each HTTP request as on_fetch(table_id, record_id).
    """
    _config = config or ExpandConfig()

    if depth == 0:
        record["fields"] = {
            k: v for k, v in record.get("fields", {}).items() if not _is_raw_id_list(v)  # type: ignore[union-attr]
        }
        return record

    entry = _SPINE.get(table_id, SpineEntry())
    table_links = link_info.get(table_id, {})
    fields: dict[str, Any] = record.get("fields", {})  # type: ignore[assignment]

    for field_name, target_table_id in table_links.items():
        value = fields.get(field_name)
        if not isinstance(value, list) or not value:
            continue

        classification = entry.classify(field_name)

        if classification == "skip":
            del fields[field_name]
            continue

        expanded: list[dict[str, Any]] = []
        for linked_id in value:
            cache_key = (target_table_id, linked_id)
            if classification == "name_only":
                if cache_key in _config.name_cache:
                    expanded.append({"id": linked_id, "_name": _config.name_cache[cache_key]})
                else:
                    if on_fetch:
                        on_fetch(target_table_id, linked_id)
                    fetched: dict[str, Any] = client.retrieve_record(target_table_id, linked_id)  # type: ignore[assignment]
                    primary_field = _config.primary_field_map.get(target_table_id)
                    name_val = fetched.get("fields", {}).get(primary_field) if primary_field else None  # type: ignore[union-attr]
                    _config.name_cache[cache_key] = name_val  # type: ignore[assignment]
                    expanded.append({"id": linked_id, "_name": name_val})
            else:  # "follow"
                if on_fetch:
                    on_fetch(target_table_id, linked_id)
                linked_record: dict[str, Any] = client.retrieve_record(target_table_id, linked_id)  # type: ignore[assignment]
                expanded.append(
                    expand_record(
                        linked_record,
                        target_table_id,
                        link_info,
                        client,
                        depth - 1,
                        config=_config,
                        on_fetch=on_fetch,
                    )
                )
        fields[field_name] = expanded

    record["fields"] = {k: v for k, v in fields.items() if not _is_raw_id_list(v)}
    return record
