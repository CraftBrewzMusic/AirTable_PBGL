"""Tests for atp.api.AirtableClient."""
from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from atp.api import AirtableClient


@pytest.fixture
def client(mock_session: MagicMock) -> AirtableClient:
    return AirtableClient(token="faketoken", base_id="appTEST0001", session=mock_session)


def test_constructor_sets_auth_header(mock_session: MagicMock) -> None:
    AirtableClient(token="faketoken", base_id="appTEST0001", session=mock_session)
    mock_session.headers.update.assert_called_once_with({
        "Authorization": "Bearer faketoken",
        "Content-Type": "application/json",
    })


def test_list_records_calls_get(client: AirtableClient, mock_session: MagicMock) -> None:
    mock_session.get.return_value.json.return_value = {}
    client.list_records("tblABC123")
    mock_session.get.assert_called_once()
    url = mock_session.get.call_args.args[0]
    assert "appTEST0001" in url
    assert "tblABC123" in url


def test_list_records_passes_filter(client: AirtableClient, mock_session: MagicMock) -> None:
    mock_session.get.return_value.json.return_value = {}
    client.list_records("tblABC123", filter_formula="{Name}='Alice'")
    params = mock_session.get.call_args.kwargs["params"]
    assert params["filterByFormula"] == "{Name}='Alice'"


def test_list_records_passes_max_records(client: AirtableClient, mock_session: MagicMock) -> None:
    mock_session.get.return_value.json.return_value = {}
    client.list_records("tblABC123", max_records=10)
    params = mock_session.get.call_args.kwargs["params"]
    assert params["maxRecords"] == 10


def test_list_records_omits_empty_params(client: AirtableClient, mock_session: MagicMock) -> None:
    mock_session.get.return_value.json.return_value = {}
    client.list_records("tblABC123")
    params = mock_session.get.call_args.kwargs.get("params") or {}
    assert "filterByFormula" not in params
    assert "maxRecords" not in params


def test_retrieve_record_calls_get_with_record_id(client: AirtableClient, mock_session: MagicMock) -> None:
    mock_session.get.return_value.json.return_value = {}
    client.retrieve_record("tblABC123", "recABC123")
    url = mock_session.get.call_args.args[0]
    assert url.endswith("/recABC123")


def test_create_records_calls_post(client: AirtableClient, mock_session: MagicMock) -> None:
    mock_session.post.return_value.json.return_value = {}
    client.create_records("tblABC123", [{"Name": "Alice"}])
    body = mock_session.post.call_args.kwargs["json"]
    assert body == {"records": [{"fields": {"Name": "Alice"}}]}


def test_update_records_calls_patch(client: AirtableClient, mock_session: MagicMock) -> None:
    mock_session.patch.return_value.json.return_value = {}
    record: dict[str, object] = {"id": "recABC123", "fields": {"Name": "Bob"}}
    client.update_records("tblABC123", [record])
    body = mock_session.patch.call_args.kwargs["json"]
    assert body == {"records": [record]}


def test_delete_records_calls_delete(client: AirtableClient, mock_session: MagicMock) -> None:
    mock_session.delete.return_value.json.return_value = {}
    client.delete_records("tblABC123", ["recAAA", "recBBB"])
    params = mock_session.delete.call_args.kwargs["params"]
    assert params == [("records[]", "recAAA"), ("records[]", "recBBB")]
