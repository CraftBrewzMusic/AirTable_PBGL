"""Textual TUI for AirTable CRUD operations."""
from __future__ import annotations

import json
from typing import override

import requests
from textual import on
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.css.query import NoMatches
from textual.widget import Widget
from textual.widgets import (
    Button,
    Checkbox,
    Footer,
    Header,
    Input,
    Label,
    ListItem,
    ListView,
    Static,
    TextArea,
)

from .api import AirtableClient
from .config import DEFAULT_EXPAND_DEPTH
from .md_parser import TableInfo, find_md_dir, load_tables, writable_fields

_TABLE_DISPLAY_NAMES: dict[str, str] = {
    "REGISTRATION PROJECT (PRO +MLC)": "Reg: PRO + MLC",
    "REGISTRATION PROJECT (SOUNDEXCHANGE)": "Reg: SoundExchange",
}

_OPERATIONS = [
    ("list", "List Records"),
    ("retrieve", "Retrieve Record"),
    ("create", "Create Record"),
    ("update", "Update Record"),
    ("delete", "Delete Record(s)"),
]


class AirtableTUI(App[None]):
    TITLE = "AirTable PBGL"
    SUB_TITLE = "ATP: AirTable PBGL"

    CSS = """
    Screen {
        layout: horizontal;
    }

    #tables-pane {
        width: 22;
        height: 100%;
        border: solid $primary;
    }

    #ops-pane {
        width: 26;
        height: 100%;
        border: solid $primary;
    }

    #params-pane {
        width: 1fr;
        height: 100%;
        border: solid $primary;
        layout: vertical;
    }

    .pane-title {
        background: $primary;
        color: $background;
        padding: 0 1;
        text-align: center;
        height: 1;
        width: 100%;
    }

    ListView {
        height: 1fr;
    }

    #params-inputs {
        height: 40%;
        width: 100%;
        padding: 0 1;
    }

    .param-label {
        margin-top: 1;
        height: 1;
        color: $text-muted;
    }

    #btn-row {
        height: auto;
        margin: 1 2;
    }

    #btn-row Button {
        width: 1fr;
        margin: 0 1;
    }

    #response-area {
        height: 1fr;
        width: 100%;
    }

    #copy-response-btn {
        width: 100%;
        height: auto;
        margin: 0;
    }
    """

    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("ctrl+r", "refresh_tables", "Refresh"),
    ]

    @override
    def __init__(self, token: str = "") -> None:
        super().__init__()
        self._token = token
        self._tables: list[TableInfo] = []
        self._selected_table: TableInfo | None = None
        self._selected_op: str | None = None
        self._client: AirtableClient | None = None

    @override
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with Horizontal():
            with Vertical(id="tables-pane"):
                yield Label("Tables", classes="pane-title")
                yield ListView(id="tables-list")
            with Vertical(id="ops-pane"):
                yield Label("Operations", classes="pane-title")
                yield ListView(id="ops-list")
            with Vertical(id="params-pane"):
                yield Label("Params / Response", classes="pane-title")
                with VerticalScroll(id="params-inputs"):
                    yield Static("← Select a table and operation", id="params-hint")
                with Horizontal(id="btn-row"):
                    yield Button("Execute", id="execute-btn", variant="primary", disabled=True)
                    yield Button("Copy as curl", id="copy-curl-btn", disabled=True)
                    yield Button("Copy as CLI", id="copy-cli-btn", disabled=True)
                yield TextArea(
                    "",
                    id="response-area",
                    read_only=True,
                    show_line_numbers=False,
                    language="json",
                )
                yield Button("Copy response", id="copy-response-btn")
        yield Footer()

    @override
    def on_mount(self) -> None:
        self._load_data()

    def _load_data(self) -> None:
        self._tables = load_tables(find_md_dir())

        tables_list = self.query_one("#tables-list", ListView)
        for table in self._tables:
            display = _TABLE_DISPLAY_NAMES.get(table["name"], table["name"])
            tables_list.append(ListItem(Label(display)))

        if self._tables and self._token:
            base_id = self._tables[0]["base_id"]
            self._client = AirtableClient(token=self._token, base_id=base_id)
        elif not self._token:
            self.notify(
                "AIRTABLE_API_TOKEN not set — add it to .env or set the env var.",
                severity="warning",
                timeout=8,
            )

    @on(ListView.Selected, "#tables-list")
    async def _on_table_selected(self, event: ListView.Selected) -> None:
        idx = event.list_view.index
        if idx is None or idx >= len(self._tables):
            return
        self._selected_table = self._tables[idx]
        self._selected_op = None

        ops_list = self.query_one("#ops-list", ListView)
        ops_list.clear()
        for _, label in _OPERATIONS:
            ops_list.append(ListItem(Label(label)))

        await self._clear_params()
        for btn_id in ("#execute-btn", "#copy-curl-btn", "#copy-cli-btn"):
            self.query_one(btn_id, Button).disabled = True

    @on(ListView.Selected, "#ops-list")
    async def _on_op_selected(self, event: ListView.Selected) -> None:
        if self._selected_table is None:
            return
        idx = event.list_view.index
        if idx is None or idx >= len(_OPERATIONS):
            return
        self._selected_op = _OPERATIONS[idx][0]
        await self._build_params()
        for btn_id in ("#execute-btn", "#copy-curl-btn", "#copy-cli-btn"):
            self.query_one(btn_id, Button).disabled = False

    async def _clear_params(self) -> None:
        container = self.query_one("#params-inputs", VerticalScroll)
        await container.remove_children()
        await container.mount(Static("← Select an operation", id="params-hint"))

    async def _build_params(self) -> None:
        container = self.query_one("#params-inputs", VerticalScroll)
        await container.remove_children()
        widgets = self._make_param_widgets()
        if widgets:
            await container.mount(*widgets)

    def _make_param_widgets(self) -> list[Widget]:
        op = self._selected_op
        table = self._selected_table
        assert table is not None

        if op == "list":
            return [
                Label("filterByFormula (optional):", classes="param-label"),
                Input(placeholder="e.g. {Name}='John'", id="param-filter"),
                Label("maxRecords (optional):", classes="param-label"),
                Input(placeholder="e.g. 10", id="param-max-records"),
                Label("view (optional):", classes="param-label"),
                Input(placeholder="e.g. Default", id="param-view"),
                Label("Expand linked records:", classes="param-label"),
                Checkbox("Expand", id="param-expand"),
                Label("Depth (default 5):", classes="param-label"),
                Input(value="5", placeholder="5", id="param-depth"),
            ]

        if op == "retrieve":
            return [
                Label("Record ID (required):", classes="param-label"),
                Input(placeholder="recXXXXXXXXXXXXXX", id="param-record-id"),
                Label("Expand linked records:", classes="param-label"),
                Checkbox("Expand", id="param-expand"),
                Label("Depth (default 5):", classes="param-label"),
                Input(value="5", placeholder="5", id="param-depth"),
            ]

        if op == "create":
            widgets: list[Widget] = []
            for field in writable_fields(table):
                widgets.append(Label(f"{field['name']} ({field['type']}):", classes="param-label"))
                widgets.append(Input(placeholder="", id=f"param-field-{field['field_id']}"))
            widgets.append(Label("Apply live changes:", classes="param-label"))
            widgets.append(Checkbox("Apply now", id="param-apply"))
            return widgets

        if op == "update":
            widgets = [
                Label("Record ID (required):", classes="param-label"),
                Input(placeholder="recXXXXXXXXXXXXXX", id="param-record-id"),
            ]
            for field in writable_fields(table):
                widgets.append(
                    Label(
                        f"{field['name']} ({field['type']}) – leave empty to skip:",
                        classes="param-label",
                    )
                )
                widgets.append(Input(placeholder="", id=f"param-field-{field['field_id']}"))
            widgets.append(Label("Apply live changes:", classes="param-label"))
            widgets.append(Checkbox("Apply now", id="param-apply"))
            return widgets

        if op == "delete":
            return [
                Label("Record ID(s), comma-separated:", classes="param-label"),
                Input(placeholder="recXXXX, recYYYY", id="param-record-ids"),
                Label("Apply live changes:", classes="param-label"),
                Checkbox("Apply now", id="param-apply"),
            ]

        return []

    @on(Button.Pressed, "#execute-btn")
    def _on_execute(self, _event: Button.Pressed) -> None:
        if self._selected_op in {"list", "retrieve"} and self._client is None:
            self.notify("API token not configured!", severity="error")
            return
        if self._selected_op in {"create", "update", "delete"} and self._apply_enabled() and self._client is None:
            self.notify("API token not configured!", severity="error")
            return
        if self._selected_table is None or self._selected_op is None:
            return

        response_area = self.query_one("#response-area", TextArea)
        response_area.load_text("Requesting…")

        try:
            result = self._call_api(self._selected_table, self._selected_op)
            response_area.load_text(json.dumps(result, indent=2))
        except requests.exceptions.RequestException as exc:
            response_area.load_text(f"Error: {exc}")

    def _call_api(self, table: TableInfo, op: str) -> dict[str, object]:
        tid = table["table_id"] or table["name"]

        if op == "list":
            assert self._client is not None
            result = self._client.list_records(
                tid,
                filter_formula=self._input_val("#param-filter"),
                max_records=self._int_input("#param-max-records"),
                view=self._input_val("#param-view"),
            )
            if self._expand_enabled():
                from .expand import expand_api_response
                depth = self._int_input("#param-depth") or DEFAULT_EXPAND_DEPTH
                result = expand_api_response(result, tid, self._tables, self._client, depth)  # type: ignore[arg-type]
            return result

        if op == "retrieve":
            assert self._client is not None
            result = self._client.retrieve_record(tid, self._input_val("#param-record-id"))
            if self._expand_enabled():
                from .expand import expand_api_response
                depth = self._int_input("#param-depth") or DEFAULT_EXPAND_DEPTH
                result = expand_api_response(result, tid, self._tables, self._client, depth)  # type: ignore[arg-type]
            return result

        if op == "create":
            fields_dict: dict[str, str] = {}
            for field in writable_fields(table):
                val = self._input_val(f"#param-field-{field['field_id']}")
                if val:
                    fields_dict[field["name"]] = val
            if not self._apply_enabled():
                return self._preview_payload(table, op, {"records": [{"fields": fields_dict}]})
            assert self._client is not None
            return self._client.create_records(tid, [fields_dict])

        if op == "update":
            record_id = self._input_val("#param-record-id")
            fields_dict = {}
            for field in writable_fields(table):
                val = self._input_val(f"#param-field-{field['field_id']}")
                if val:
                    fields_dict[field["name"]] = val
            if not self._apply_enabled():
                return self._preview_payload(table, op, {"records": [{"id": record_id, "fields": fields_dict}]})
            assert self._client is not None
            return self._client.update_records(tid, [{"id": record_id, "fields": fields_dict}])

        if op == "delete":
            ids_raw = self._input_val("#param-record-ids")
            ids = [rid.strip() for rid in ids_raw.split(",") if rid.strip()]
            if not self._apply_enabled():
                return self._preview_payload(table, op, {"records": ids})
            assert self._client is not None
            return self._client.delete_records(tid, ids)

        return {}

    def _expand_enabled(self) -> bool:
        try:
            return self.query_one("#param-expand", Checkbox).value
        except NoMatches:
            return False

    def _apply_enabled(self) -> bool:
        try:
            return self.query_one("#param-apply", Checkbox).value
        except NoMatches:
            return False

    def _preview_payload(self, table: TableInfo, op: str, payload: dict[str, object]) -> dict[str, object]:
        return {
            "action": op,
            "apply": False,
            "table": table["name"],
            "table_id": table["table_id"] or table["name"],
            "payload": payload,
        }

    def _input_val(self, selector: str) -> str:
        try:
            return self.query_one(selector, Input).value
        except NoMatches:
            return ""

    def _int_input(self, selector: str) -> int:
        val = self._input_val(selector).strip()
        return int(val) if val.isdigit() else 0

    @on(Button.Pressed, "#copy-response-btn")
    def _on_copy_response(self, _event: Button.Pressed) -> None:
        text = self.query_one("#response-area", TextArea).text
        if text.strip():
            self.copy_to_clipboard(text)
            self.notify("Response copied to clipboard.", timeout=2)

    @on(Button.Pressed, "#copy-curl-btn")
    def _on_copy_curl(self, _event: Button.Pressed) -> None:
        cmd = self._build_curl()
        if cmd:
            self.copy_to_clipboard(cmd)
            self.notify("curl command copied to clipboard.", timeout=2)

    @on(Button.Pressed, "#copy-cli-btn")
    def _on_copy_cli(self, _event: Button.Pressed) -> None:
        cmd = self._build_cli_command()
        if cmd:
            self.copy_to_clipboard(cmd)
            self.notify("CLI command copied to clipboard.", timeout=2)

    def _build_curl(self) -> str:
        table = self._selected_table
        op = self._selected_op
        if not table or not op:
            return ""

        tid = table["table_id"] or table["name"]
        base_url = f"https://api.airtable.com/v0/{table['base_id']}/{tid}"
        auth = '-H "Authorization: Bearer $AIRTABLE_API_TOKEN"'
        ct = '-H "Content-Type: application/json"'

        if op == "list":
            params = []
            if f := self._input_val("#param-filter"):
                params.append(f"filterByFormula={f}")
            if m := self._input_val("#param-max-records"):
                params.append(f"maxRecords={m}")
            if v := self._input_val("#param-view"):
                params.append(f"view={v}")
            qs = ("?" + "&".join(params)) if params else ""
            return f'curl "{base_url}{qs}" \\\n  {auth}'

        if op == "retrieve":
            rid = self._input_val("#param-record-id")
            return f'curl "{base_url}/{rid}" \\\n  {auth}'

        if op == "create":
            fields_dict = {
                field["name"]: val
                for field in writable_fields(table)
                if (val := self._input_val(f"#param-field-{field['field_id']}"))
            }
            body = json.dumps({"records": [{"fields": fields_dict}]})
            return f'curl -X POST "{base_url}" \\\n  {auth} \\\n  {ct} \\\n  -d \'{body}\''

        if op == "update":
            rid = self._input_val("#param-record-id")
            fields_dict = {
                field["name"]: val
                for field in writable_fields(table)
                if (val := self._input_val(f"#param-field-{field['field_id']}"))
            }
            body = json.dumps({"records": [{"id": rid, "fields": fields_dict}]})
            return f'curl -X PATCH "{base_url}" \\\n  {auth} \\\n  {ct} \\\n  -d \'{body}\''

        if op == "delete":
            ids_raw = self._input_val("#param-record-ids")
            ids = [r.strip() for r in ids_raw.split(",") if r.strip()]
            qs = "?" + "&".join(f"records[]={r}" for r in ids) if ids else ""
            return f'curl -X DELETE "{base_url}{qs}" \\\n  {auth}'

        return ""

    def _build_cli_command(self) -> str:
        table = self._selected_table
        op = self._selected_op
        if not table or not op:
            return ""

        name = table["name"]
        t_arg = f'"{name}"' if " " in name else name

        if op == "list":
            parts = [f"atp records list {t_arg}"]
            if f := self._input_val("#param-filter"):
                parts.append(f'--filter "{f}"')
            if m := self._input_val("#param-max-records"):
                parts.append(f"--max-records {m}")
            if v := self._input_val("#param-view"):
                parts.append(f'--view "{v}"')
            if self._expand_enabled():
                parts.append("--expand")
                if (d := self._int_input("#param-depth")) and d != 5:
                    parts.append(f"--depth {d}")
            return " ".join(parts)

        if op == "retrieve":
            rid = self._input_val("#param-record-id")
            cmd = f"atp records retrieve {t_arg} {rid}"
            if self._expand_enabled():
                cmd += " --expand"
                if (d := self._int_input("#param-depth")) and d != 5:
                    cmd += f" --depth {d}"
            return cmd

        if op == "create":
            parts = [f"atp records create {t_arg}"]
            for field in writable_fields(table):
                if val := self._input_val(f"#param-field-{field['field_id']}"):
                    parts.append(f'--field "{field["name"]}={val}"')
            if self._apply_enabled():
                parts.append("--apply")
            return " ".join(parts)

        if op == "update":
            rid = self._input_val("#param-record-id")
            parts = [f"atp records update {t_arg} {rid}"]
            for field in writable_fields(table):
                if val := self._input_val(f"#param-field-{field['field_id']}"):
                    parts.append(f'--field "{field["name"]}={val}"')
            if self._apply_enabled():
                parts.append("--apply")
            return " ".join(parts)

        if op == "delete":
            ids_raw = self._input_val("#param-record-ids")
            ids = [r.strip() for r in ids_raw.split(",") if r.strip()]
            cmd = f"atp records delete {t_arg} {' '.join(ids)}"
            if self._apply_enabled():
                cmd += " --apply"
            return cmd

        return ""

    def action_refresh_tables(self) -> None:
        tables_list = self.query_one("#tables-list", ListView)
        tables_list.clear()
        self._tables = load_tables(find_md_dir())
        for table in self._tables:
            display = _TABLE_DISPLAY_NAMES.get(table["name"], table["name"])
            tables_list.append(ListItem(Label(display)))
        self.notify("Tables refreshed.", timeout=2)
