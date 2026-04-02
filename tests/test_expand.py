"""Tests for atp.expand."""
from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock

from atp.expand import ExpandConfig, SpineEntry, build_link_info, expand_record
from atp.md_parser import Field, TableInfo, load_tables

# Real spine table IDs (from data-model.md)
_RELEASES_ID = "tbl7rjVKUd5faZ7fV"
_RECORDINGS_ID = "tblESvQQmOBbEXAH0"
_COMPOSITIONS_ID = "tblomWINKPjfgAVpo"
_SONGWRITERS_ID = "tbl2KLh2RIrS5AmSX"
_PUBLISHERS_ID = "tbl6TNKQRPfY3hXZ2"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_table(name: str, table_id: str, fields: list[Field]) -> TableInfo:
    return TableInfo(
        name=name,
        table_id=table_id,
        base_id="appTEST0001",
        fields=fields,
        operations={},
    )


def _link_field(name: str, target_table_name: str) -> Field:
    return Field(
        name=name,
        field_id=f"fld{name[:3].upper()}",
        type="Link to another record",
        description=f"Array of linked records IDs from the {target_table_name} table.",
    )


def _text_field(name: str) -> Field:
    return Field(name=name, field_id="fldTXT001", type="Text", description="A text field")


def _make_record(record_id: str, fields: dict) -> dict:
    return {"id": record_id, "fields": fields}


# ---------------------------------------------------------------------------
# build_link_info
# ---------------------------------------------------------------------------

def test_build_link_info_standard_link() -> None:
    releases = _make_table("Releases", "tblREL", [_link_field("Recordings", "Recordings")])
    recordings = _make_table("Recordings", "tblREC", [_text_field("Title")])
    result = build_link_info([releases, recordings])
    assert result == {"tblREL": {"Recordings": "tblREC"}}


def test_build_link_info_self_referential() -> None:
    publishers = _make_table("Publishers", "tblPUB", [_link_field("In Care Of", "Publishers")])
    result = build_link_info([publishers])
    assert result == {"tblPUB": {"In Care Of": "tblPUB"}}


def test_build_link_info_skips_no_pattern_match() -> None:
    field = Field(
        name="Misc",
        field_id="fldMISC",
        type="Link to another record",
        description="Some unrelated description",
    )
    table = _make_table("X", "tblX", [field])
    result = build_link_info([table])
    assert result == {}


def test_build_link_info_skips_missing_target_table() -> None:
    releases = _make_table("Releases", "tblREL", [_link_field("SCRATCH", "SCRATCH")])
    result = build_link_info([releases])
    assert result == {}


def test_build_link_info_excludes_non_link_fields() -> None:
    releases = _make_table("Releases", "tblREL", [_text_field("Title")])
    result = build_link_info([releases])
    assert result == {}


def test_build_link_info_with_loaded_tables(tmp_link_md_dir: Path) -> None:
    tables = load_tables(tmp_link_md_dir)
    link_info = build_link_info(tables)
    releases = next(t for t in tables if t["name"] == "Releases")
    recordings = next(t for t in tables if t["name"] == "Recordings")
    assert link_info[releases["table_id"]]["Recordings"] == recordings["table_id"]


# ---------------------------------------------------------------------------
# expand_record — basic behavior
# ---------------------------------------------------------------------------

def test_expand_record_depth_zero_strips_raw_id_lists() -> None:
    client = MagicMock()
    real_id = "recABCDEFGHIJKLMN"
    record = _make_record("recABC", {"Recordings": [real_id]})
    link_info = {"tblREL": {"Recordings": "tblREC"}}
    result = expand_record(record, "tblREL", link_info, client, depth=0)
    assert "Recordings" not in result["fields"]
    client.retrieve_record.assert_not_called()


def test_expand_record_field_not_in_link_info_untouched() -> None:
    client = MagicMock()
    record = _make_record("recABC", {"Title": "My Song"})
    link_info: dict = {}
    result = expand_record(record, "tblREL", link_info, client, depth=3)
    assert result["fields"]["Title"] == "My Song"
    client.retrieve_record.assert_not_called()


def test_expand_record_empty_list_field_not_fetched() -> None:
    client = MagicMock()
    record = _make_record("recABC", {"Recordings": []})
    link_info = {"tblREL": {"Recordings": "tblREC"}}
    result = expand_record(record, "tblREL", link_info, client, depth=3)
    client.retrieve_record.assert_not_called()
    assert result["fields"]["Recordings"] == []


def test_expand_record_table_not_in_spine_strips_all_linked_fields() -> None:
    """A table with no spine entry has all its non-empty linked fields stripped."""
    client = MagicMock()
    record = _make_record("recABC", {"Recordings": ["recREC001ABCDEFGH"], "Title": "Demo"})
    link_info = {"tblUNKNOWN": {"Recordings": "tblREC"}}
    result = expand_record(record, "tblUNKNOWN", link_info, client, depth=3)
    assert "Recordings" not in result["fields"]
    assert result["fields"]["Title"] == "Demo"
    client.retrieve_record.assert_not_called()


# ---------------------------------------------------------------------------
# expand_record — spine traversal: Releases
# ---------------------------------------------------------------------------

def test_expand_record_releases_follows_recordings() -> None:
    """Releases spine: Recordings is followed; unrecognized linked fields are stripped."""
    client = MagicMock()
    linked_record = _make_record("recREC001ABCDEFGH", {"Title": "Song A"})
    client.retrieve_record.return_value = linked_record
    record = _make_record("recREL001ABCDEFGH", {
        "Recordings": ["recREC001ABCDEFGH"],
        "Admin Link": ["recADM001ABCDEFGH"],
    })
    link_info = {
        _RELEASES_ID: {
            "Recordings": _RECORDINGS_ID,
            "Admin Link": "tblADMIN",
        }
    }
    result = expand_record(record, _RELEASES_ID, link_info, client, depth=1)
    assert "Admin Link" not in result["fields"]
    assert result["fields"]["Recordings"] == [linked_record]
    client.retrieve_record.assert_called_once_with(_RECORDINGS_ID, "recREC001ABCDEFGH")


def test_expand_record_releases_name_only_primary_artist() -> None:
    """Releases spine: Primary Artist is returned as {id, _name} without recursing."""
    client = MagicMock()
    artist_record = _make_record("recART001ABCDEFGH", {
        "Artist Name": "Kendrick Lamar",
        "Some Link": ["recOTH001ABCDEFGH"],
    })
    client.retrieve_record.return_value = artist_record
    record = _make_record("recREL001ABCDEFGH", {"Primary Artist": ["recART001ABCDEFGH"]})
    link_info = {_RELEASES_ID: {"Primary Artist": "tblARTISTS"}}
    config = ExpandConfig(primary_field_map={"tblARTISTS": "Artist Name"})
    result = expand_record(record, _RELEASES_ID, link_info, client, depth=3, config=config)
    assert result["fields"]["Primary Artist"] == [{"id": "recART001ABCDEFGH", "_name": "Kendrick Lamar"}]
    client.retrieve_record.assert_called_once_with("tblARTISTS", "recART001ABCDEFGH")


def test_expand_record_releases_name_only_uses_cache() -> None:
    """Name-only cache prevents duplicate HTTP fetches for the same record."""
    client = MagicMock()
    cache_key = ("tblARTISTS", "recART001ABCDEFGH")
    config = ExpandConfig(
        primary_field_map={"tblARTISTS": "Artist Name"},
        name_cache={cache_key: "Drake"},
    )
    record = _make_record("recREL001ABCDEFGH", {"Primary Artist": ["recART001ABCDEFGH"]})
    link_info = {_RELEASES_ID: {"Primary Artist": "tblARTISTS"}}
    result = expand_record(record, _RELEASES_ID, link_info, client, depth=3, config=config)
    assert result["fields"]["Primary Artist"] == [{"id": "recART001ABCDEFGH", "_name": "Drake"}]
    client.retrieve_record.assert_not_called()


# ---------------------------------------------------------------------------
# expand_record — spine traversal: Recordings
# ---------------------------------------------------------------------------

def test_expand_record_recordings_follows_compositions() -> None:
    """Recordings spine: Compositions is followed."""
    client = MagicMock()
    linked_record = _make_record("recCOM001ABCDEFGH", {"Title": "My Composition"})
    client.retrieve_record.return_value = linked_record
    record = _make_record("recREC001ABCDEFGH", {"Compositions": ["recCOM001ABCDEFGH"]})
    link_info = {_RECORDINGS_ID: {"Compositions": _COMPOSITIONS_ID}}
    result = expand_record(record, _RECORDINGS_ID, link_info, client, depth=1)
    assert result["fields"]["Compositions"] == [linked_record]
    client.retrieve_record.assert_called_once_with(_COMPOSITIONS_ID, "recCOM001ABCDEFGH")


def test_expand_record_recordings_strips_non_spine_link() -> None:
    """Recordings spine: A linked field not in follow or name_only is stripped."""
    client = MagicMock()
    client.retrieve_record.return_value = _make_record("recCOM001ABCDEFGH", {})
    record = _make_record("recREC001ABCDEFGH", {
        "Compositions": ["recCOM001ABCDEFGH"],
        "REGISTRATION PROJECT (PRO +MLC)": ["recREG001ABCDEFGH"],
    })
    link_info = {
        _RECORDINGS_ID: {
            "Compositions": _COMPOSITIONS_ID,
            "REGISTRATION PROJECT (PRO +MLC)": "tblREGPRO",
        }
    }
    result = expand_record(record, _RECORDINGS_ID, link_info, client, depth=1)
    assert "REGISTRATION PROJECT (PRO +MLC)" not in result["fields"]


# ---------------------------------------------------------------------------
# expand_record — spine traversal: Compositions
# ---------------------------------------------------------------------------

def test_expand_record_compositions_songwriter_regex_followed() -> None:
    """Compositions spine: 'Songwriter 1' matches follow_re and is expanded."""
    client = MagicMock()
    sw_record = _make_record("recSW1001ABCDEFGH", {"Name": "Alice"})
    client.retrieve_record.return_value = sw_record
    record = _make_record("recCOM001ABCDEFGH", {"Songwriter 1": ["recSW1001ABCDEFGH"]})
    link_info = {_COMPOSITIONS_ID: {"Songwriter 1": _SONGWRITERS_ID}}
    result = expand_record(record, _COMPOSITIONS_ID, link_info, client, depth=1)
    assert result["fields"]["Songwriter 1"] == [sw_record]
    client.retrieve_record.assert_called_once_with(_SONGWRITERS_ID, "recSW1001ABCDEFGH")


def test_expand_record_compositions_publisher_regex_name_only() -> None:
    """Compositions spine: 'Songwriter 1 Original Pub 1' matches name_only_re."""
    client = MagicMock()
    pub_record = _make_record("recPUB001ABCDEFGH", {
        "Publisher Name": "ASCAP Music",
        "Other Link": ["recOTH001ABCDEFGH"],
    })
    client.retrieve_record.return_value = pub_record
    record = _make_record("recCOM001ABCDEFGH", {
        "Songwriter 1 Original Pub 1": ["recPUB001ABCDEFGH"],
    })
    link_info = {_COMPOSITIONS_ID: {"Songwriter 1 Original Pub 1": _PUBLISHERS_ID}}
    config = ExpandConfig(primary_field_map={_PUBLISHERS_ID: "Publisher Name"})
    result = expand_record(record, _COMPOSITIONS_ID, link_info, client, depth=3, config=config)
    assert result["fields"]["Songwriter 1 Original Pub 1"] == [
        {"id": "recPUB001ABCDEFGH", "_name": "ASCAP Music"}
    ]


def test_expand_record_compositions_strips_back_reference() -> None:
    """Compositions spine: 'All Releases' is not in follow or name_only → stripped."""
    client = MagicMock()
    record = _make_record("recCOM001ABCDEFGH", {"All Releases": ["recREL001ABCDEFGH"]})
    link_info = {_COMPOSITIONS_ID: {"All Releases": _RELEASES_ID}}
    result = expand_record(record, _COMPOSITIONS_ID, link_info, client, depth=3)
    assert "All Releases" not in result["fields"]
    client.retrieve_record.assert_not_called()


# ---------------------------------------------------------------------------
# expand_record — spine traversal: leaf tables
# ---------------------------------------------------------------------------

def test_expand_record_songwriters_leaf_strips_linked_preserves_scalars() -> None:
    """Songwriters is a leaf: all linked fields stripped, scalar fields preserved."""
    client = MagicMock()
    record = _make_record("recSW1001ABCDEFGH", {
        "Name": "Alice",
        "PRO": "ASCAP",
        "Publisher": ["recPUB001ABCDEFGH"],
    })
    link_info = {_SONGWRITERS_ID: {"Publisher": _PUBLISHERS_ID}}
    result = expand_record(record, _SONGWRITERS_ID, link_info, client, depth=3)
    assert result["fields"]["Name"] == "Alice"
    assert result["fields"]["PRO"] == "ASCAP"
    assert "Publisher" not in result["fields"]
    client.retrieve_record.assert_not_called()


def test_expand_record_publishers_leaf_strips_linked_preserves_scalars() -> None:
    """Publishers is a leaf: all linked fields stripped, scalar fields preserved."""
    client = MagicMock()
    record = _make_record("recPUB001ABCDEFGH", {
        "Publisher Name": "BMI Sub-Publisher",
        "In Care Of": ["recPUB002ABCDEFGH"],
    })
    link_info = {_PUBLISHERS_ID: {"In Care Of": _PUBLISHERS_ID}}
    result = expand_record(record, _PUBLISHERS_ID, link_info, client, depth=3)
    assert result["fields"]["Publisher Name"] == "BMI Sub-Publisher"
    assert "In Care Of" not in result["fields"]
    client.retrieve_record.assert_not_called()


# ---------------------------------------------------------------------------
# expand_record — depth limiting
# ---------------------------------------------------------------------------

def test_expand_record_depth_limits_recursion() -> None:
    """depth=1: Releases→Recordings is expanded; Recordings→Compositions is stripped."""
    rec_id = "recREC001ABCDEFGH"
    com_id = "recCOM001ABCDEFGH"
    child = _make_record(rec_id, {"Compositions": [com_id]})
    client = MagicMock()
    client.retrieve_record.return_value = child
    record = _make_record("recREL001ABCDEFGH", {"Recordings": [rec_id]})
    link_info = {
        _RELEASES_ID: {"Recordings": _RECORDINGS_ID},
        _RECORDINGS_ID: {"Compositions": _COMPOSITIONS_ID},
    }
    result = expand_record(record, _RELEASES_ID, link_info, client, depth=1)
    client.retrieve_record.assert_called_once_with(_RECORDINGS_ID, rec_id)
    assert "Compositions" not in result["fields"]["Recordings"][0]["fields"]
