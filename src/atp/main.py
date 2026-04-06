"""CLI entry point for ATP: AirTable PBGL."""
from __future__ import annotations

from pathlib import Path
from typing import Any

import typer

from .api import AirtableClient
from .chevy_import_songs import main as chevy_import_songs
from .chevy_link_releases import main as chevy_link_releases
from .chevy_patch_featured_artists import main as chevy_patch_featured_artists
from .chevy_patch_primary_artist import main as chevy_patch_primary_artist
from .common import emit_json, parse_field_pairs, require_token, resolve_token
from .config import CLI_EXPANSION, CLI_NAME, DEFAULT_EXPAND_DEPTH
from .md_parser import TableInfo, find_md_dir, load_tables
from .schema_parser import parse_html_to_markdown

app = typer.Typer(
    name=CLI_NAME,
    help=f"{CLI_NAME} stands for {CLI_EXPANSION}. Default action launches the Textual TUI.",
    add_completion=False,
    context_settings={"help_option_names": ["-h", "--help"]},
)
records_app = typer.Typer(help="Generic Airtable record operations.")
schema_app = typer.Typer(help="Schema and metadata maintenance commands.")
chevy_app = typer.Typer(help="Chevy Showroom and PBGL-specific automation commands.")


def _find_table(table_name: str) -> TableInfo:
    tables = load_tables(find_md_dir())
    match = next((table for table in tables if table["name"].lower() == table_name.lower()), None)
    if match is None:
        names = ", ".join(table["name"] for table in tables)
        typer.echo(f"Table not found: {table_name!r}. Available: {names}", err=True)
        raise typer.Exit(1)
    return match


def _get_client_and_tables(table_name: str) -> tuple[AirtableClient, str, list[TableInfo]]:
    token = require_token()
    tables = load_tables(find_md_dir())
    match = next((table for table in tables if table["name"].lower() == table_name.lower()), None)
    if match is None:
        names = ", ".join(table["name"] for table in tables)
        typer.echo(f"Table not found: {table_name!r}. Available: {names}", err=True)
        raise typer.Exit(1)
    client = AirtableClient(token=token, base_id=match["base_id"])
    return client, match["table_id"] or match["name"], tables


def _preview(action: str, table: TableInfo, payload: dict[str, Any]) -> None:
    emit_json({
        "action": action,
        "apply": False,
        "table": table["name"],
        "table_id": table["table_id"] or table["name"],
        "payload": payload,
    })


@app.callback(invoke_without_command=True)
def default(ctx: typer.Context) -> None:
    """Launch the TUI when `atp` is run without a subcommand."""
    if ctx.invoked_subcommand is None:
        from .app import AirtableTUI

        AirtableTUI(token=resolve_token()).run()


@app.command()
def tui() -> None:
    """Launch the Textual TUI."""
    from .app import AirtableTUI

    AirtableTUI(token=resolve_token()).run()


@records_app.command("list")
def list_records(
    table: str = typer.Argument(..., help="Table name"),
    filter_formula: str = typer.Option("", "--filter", help="filterByFormula expression"),
    max_records: int = typer.Option(0, "--max-records", help="Max records to return"),
    view: str = typer.Option("", "--view", help="View name"),
    expand: bool = typer.Option(False, "--expand", help="Recursively expand linked records"),
    depth: int = typer.Option(DEFAULT_EXPAND_DEPTH, "--depth", min=0, help="Max expansion depth"),
) -> None:
    """List records from a table."""
    client, table_id, tables = _get_client_and_tables(table)
    typer.echo(f"-> GET {table}", err=True)
    result = client.list_records(table_id, filter_formula=filter_formula, max_records=max_records, view=view)
    if expand:
        from .expand import expand_api_response

        table_name_map = {table_info["table_id"]: table_info["name"] for table_info in tables}

        def on_fetch(fetch_table_id: str, record_id: str) -> None:
            typer.echo(f"  -> GET {table_name_map.get(fetch_table_id, fetch_table_id)} / {record_id}", err=True)

        result = expand_api_response(result, table_id, tables, client, depth, on_fetch=on_fetch)
    emit_json(result)


@records_app.command()
def retrieve(
    table: str = typer.Argument(..., help="Table name"),
    record_id: str = typer.Argument(..., help="Record ID (recXXXXXXXXXXXXXX)"),
    expand: bool = typer.Option(False, "--expand", help="Recursively expand linked records"),
    depth: int = typer.Option(DEFAULT_EXPAND_DEPTH, "--depth", min=0, help="Max expansion depth"),
) -> None:
    """Retrieve a single record by ID."""
    client, table_id, tables = _get_client_and_tables(table)
    typer.echo(f"-> GET {table} / {record_id}", err=True)
    result = client.retrieve_record(table_id, record_id)
    if expand:
        from .expand import expand_api_response

        table_name_map = {table_info["table_id"]: table_info["name"] for table_info in tables}

        def on_fetch(fetch_table_id: str, linked_record_id: str) -> None:
            typer.echo(f"  -> GET {table_name_map.get(fetch_table_id, fetch_table_id)} / {linked_record_id}", err=True)

        result = expand_api_response(result, table_id, tables, client, depth, on_fetch=on_fetch)
    emit_json(result)


@records_app.command()
def create(
    table: str = typer.Argument(..., help="Table name"),
    field: list[str] = typer.Option([], "--field", help="Field value as 'Name=value' (repeatable)"),
    apply: bool = typer.Option(False, "--apply", help="Apply the live Airtable write."),
) -> None:
    """Create a record. Defaults to preview mode unless `--apply` is passed."""
    table_info = _find_table(table)
    fields = parse_field_pairs(field)
    payload = {"records": [{"fields": fields}]}
    if not apply:
        _preview("create", table_info, payload)
        return
    client = AirtableClient(token=require_token(), base_id=table_info["base_id"])
    emit_json(client.create_records(table_info["table_id"] or table_info["name"], [fields]))


@records_app.command()
def update(
    table: str = typer.Argument(..., help="Table name"),
    record_id: str = typer.Argument(..., help="Record ID (recXXXXXXXXXXXXXX)"),
    field: list[str] = typer.Option([], "--field", help="Field value as 'Name=value' (repeatable)"),
    apply: bool = typer.Option(False, "--apply", help="Apply the live Airtable write."),
) -> None:
    """Update a record. Defaults to preview mode unless `--apply` is passed."""
    table_info = _find_table(table)
    payload = {"records": [{"id": record_id, "fields": parse_field_pairs(field)}]}
    if not apply:
        _preview("update", table_info, payload)
        return
    client = AirtableClient(token=require_token(), base_id=table_info["base_id"])
    emit_json(client.update_records(table_info["table_id"] or table_info["name"], payload["records"]))  # type: ignore[arg-type]


@records_app.command()
def delete(
    table: str = typer.Argument(..., help="Table name"),
    record_ids: list[str] = typer.Argument(..., help="One or more record IDs to delete"),
    apply: bool = typer.Option(False, "--apply", help="Apply the live Airtable delete."),
) -> None:
    """Delete one or more records. Defaults to preview mode unless `--apply` is passed."""
    table_info = _find_table(table)
    payload = {"records": record_ids}
    if not apply:
        _preview("delete", table_info, payload)
        return
    client = AirtableClient(token=require_token(), base_id=table_info["base_id"])
    emit_json(client.delete_records(table_info["table_id"] or table_info["name"], record_ids))


@schema_app.command("redoc")
def redoc(
    html_file: Path = typer.Argument(
        ...,
        help="Path to the Airtable HTML API reference file to re-parse.",
        exists=True,
        file_okay=True,
        dir_okay=False,
    ),
) -> None:
    """Re-parse Airtable HTML docs into committed markdown schema files."""
    written = parse_html_to_markdown(html_file, output_dir=find_md_dir())
    typer.echo(f"Wrote {len(written)} schema files.", err=True)


chevy_app.command("import-songs")(chevy_import_songs)
chevy_app.command("link-releases")(chevy_link_releases)
chevy_app.command("patch-primary-artist")(chevy_patch_primary_artist)
chevy_app.command("patch-featured-artists")(chevy_patch_featured_artists)

app.add_typer(records_app, name="records")
app.add_typer(schema_app, name="schema")
app.add_typer(chevy_app, name="chevy")
