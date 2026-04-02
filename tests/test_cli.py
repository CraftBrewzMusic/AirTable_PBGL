"""Tests for atp.main (CLI entry point)."""
from __future__ import annotations

from unittest.mock import patch

from typer.testing import CliRunner

from atp.main import app

runner = CliRunner()


def test_records_list_exits_1_without_token() -> None:
    with patch("atp.main.require_token", side_effect=SystemExit(1)):
        result = runner.invoke(app, ["records", "list", "Artists"])
    assert result.exit_code == 1


def test_records_create_previews_by_default() -> None:
    with patch(
        "atp.main._find_table",
        return_value={"name": "Artists", "table_id": "tblABC123", "base_id": "appTEST0001"},
    ):
        result = runner.invoke(app, ["records", "create", "Artists", "--field", "Name=Alice"])
    assert result.exit_code == 0
    assert '"action": "create"' in result.stdout
    assert '"apply": false' in result.stdout


def test_records_create_apply_calls_live_client() -> None:
    fake_client = type("FakeClient", (), {"create_records": lambda self, table_id, rows: {"table_id": table_id, "rows": rows}})()
    with patch(
        "atp.main._find_table",
        return_value={"name": "Artists", "table_id": "tblABC123", "base_id": "appTEST0001"},
    ), patch("atp.main.require_token", return_value="token"), patch("atp.main.AirtableClient", return_value=fake_client):
        result = runner.invoke(app, ["records", "create", "Artists", "--field", "Name=Alice", "--apply"])
    assert result.exit_code == 0
    assert '"table_id": "tblABC123"' in result.stdout


def test_atp_help_mentions_airtable_pbgl() -> None:
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "AirTable PBGL" in result.stdout
