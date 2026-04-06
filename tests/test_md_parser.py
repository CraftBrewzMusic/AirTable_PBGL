"""Tests for atp.md_parser."""
from __future__ import annotations

from pathlib import Path

import pytest

from atp.md_parser import find_project_root, load_tables, writable_fields


def test_load_tables_returns_correct_count(tmp_md_dir: Path) -> None:
    tables = load_tables(tmp_md_dir)
    assert len(tables) == 2


def test_load_tables_skips_artists_copy(tmp_md_dir: Path) -> None:
    tables = load_tables(tmp_md_dir)
    names = [t["name"] for t in tables]
    assert "Artists Copy" not in names


def test_load_tables_returns_table_info_structure(tmp_md_dir: Path) -> None:
    tables = load_tables(tmp_md_dir)
    for table in tables:
        assert set(table.keys()) >= {"name", "table_id", "base_id", "fields", "operations"}


def test_load_tables_parses_ids(tmp_md_dir: Path) -> None:
    tables = load_tables(tmp_md_dir)
    ids = {t["table_id"] for t in tables}
    assert "tblABC123" in ids
    assert "tblDEF456" in ids


def test_load_tables_parses_base_id(tmp_md_dir: Path) -> None:
    tables = load_tables(tmp_md_dir)
    for table in tables:
        assert table["base_id"] == "appTEST0001"


def test_load_tables_parses_operations(tmp_md_dir: Path) -> None:
    tables = load_tables(tmp_md_dir)
    artists = next(t for t in tables if t["name"] == "Artists")
    assert artists["operations"]["list"]["method"] == "GET"
    assert artists["operations"]["create"]["method"] == "POST"


def test_writable_fields_excludes_formula(tmp_md_dir: Path) -> None:
    tables = load_tables(tmp_md_dir)
    artists = next(t for t in tables if t["name"] == "Artists")
    types = [f["type"].lower() for f in writable_fields(artists)]
    assert "formula" not in types


def test_writable_fields_excludes_count(tmp_md_dir: Path) -> None:
    tables = load_tables(tmp_md_dir)
    artists = next(t for t in tables if t["name"] == "Artists")
    types = [f["type"].lower() for f in writable_fields(artists)]
    assert "count" not in types


def test_writable_fields_keeps_text(tmp_md_dir: Path) -> None:
    tables = load_tables(tmp_md_dir)
    artists = next(t for t in tables if t["name"] == "Artists")
    types = [f["type"].lower() for f in writable_fields(artists)]
    assert "text" in types


def test_find_project_root_has_pyproject() -> None:
    root = find_project_root()
    assert (root / "pyproject.toml").exists()
