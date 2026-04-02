"""Parse committed Airtable schema markdown into table metadata."""
from __future__ import annotations

import re
from pathlib import Path
from typing import TypedDict

from .common import find_project_root
from .config import AIRTABLE_DOCS_DIRNAME, DOCS_DIRNAME


class Field(TypedDict):
    name: str
    field_id: str
    type: str
    description: str


class Operation(TypedDict):
    method: str
    path: str


class TableInfo(TypedDict):
    name: str
    table_id: str
    base_id: str
    fields: list[Field]
    operations: dict[str, Operation]


_READONLY_TYPES = frozenset({
    "formula",
    "auto number",
    "created time",
    "created by",
    "last modified time",
    "last modified by",
    "count",
    "rollup",
    "lookup",
})

_SKIP_FILES = {"artists_copy.md"}

_HEADING_TO_OP = {
    "list records": "list",
    "retrieve": "retrieve",
    "create records": "create",
    "update": "update",
    "delete records": "delete",
}

def find_md_dir() -> Path:
    return find_project_root() / DOCS_DIRNAME / AIRTABLE_DOCS_DIRNAME


def load_tables(md_dir: Path) -> list[TableInfo]:
    """Load all .md files in md_dir and return a list of TableInfo dicts."""
    tables = []
    for md_file in sorted(md_dir.glob("*.md")):
        if md_file.name in _SKIP_FILES:
            continue
        table = _parse_md_file(md_file)
        if table is not None:
            tables.append(table)
    return tables


def writable_fields(table: TableInfo) -> list[Field]:
    """Return fields that can be written (non-computed types)."""
    return [f for f in table["fields"] if f["type"].lower() not in _READONLY_TYPES]


def _parse_md_file(path: Path) -> TableInfo | None:
    text = path.read_text(encoding="utf-8")

    name_m = re.search(r"^# (.+)$", text, re.MULTILINE)
    if not name_m:
        return None

    table_id_m = re.search(r"\*\*Table ID:\*\*\s*`([^`]+)`", text)
    base_id_m = re.search(r"\*\*Base ID:\*\*\s*`([^`]+)`", text)

    return TableInfo(
        name=name_m.group(1).strip(),
        table_id=table_id_m.group(1) if table_id_m else "",
        base_id=base_id_m.group(1) if base_id_m else "",
        fields=_parse_fields(text),
        operations=_parse_operations(text),
    )


def _parse_fields(text: str) -> list[Field]:
    section_m = re.search(r"## Fields\n(.*?)(?=\n---\n|\n## )", text, re.DOTALL)
    if not section_m:
        return []

    fields: list[Field] = []
    skip = 2  # skip header row + separator row
    for line in section_m.group(1).splitlines():
        if not line.startswith("|"):
            continue
        if skip > 0:
            skip -= 1
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 4:
            continue
        name, raw_fid, ftype, desc = cells[:4]
        fid = raw_fid.strip("`")
        if name and fid and not name.startswith("---"):
            fields.append(Field(name=name, field_id=fid, type=ftype, description=desc))

    return fields


def _parse_operations(text: str) -> dict[str, Operation]:
    ops: dict[str, Operation] = {}
    for part in re.split(r"\n(?=## )", text):
        heading = part.split("\n", 1)[0].lstrip("#").strip().lower()
        op_key = next((v for k, v in _HEADING_TO_OP.items() if k in heading), None)
        if op_key is None:
            continue
        m = re.search(r"\*\*Endpoint:\*\*\s*`([A-Z]+)\s+(/v0/[^`\s]+)`", part)
        if m:
            ops[op_key] = Operation(method=m.group(1), path=m.group(2))
    return ops
