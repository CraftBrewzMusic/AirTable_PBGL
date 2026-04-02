"""Shared helpers for CLI commands."""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

import typer
from dotenv import load_dotenv

from .api import AirtableClient
from .config import ENV_TOKEN_NAME


def find_project_root() -> Path:
    """Walk up from this file to the directory containing pyproject.toml."""
    for parent in Path(__file__).resolve().parents:
        if (parent / "pyproject.toml").exists():
            return parent
    raise FileNotFoundError("Could not find project root (no pyproject.toml found)")


def load_project_env() -> None:
    """Load the repo .env when it exists."""
    env_path = find_project_root() / ".env"
    if env_path.exists():
        load_dotenv(env_path)


def resolve_token() -> str:
    load_project_env()
    return os.getenv(ENV_TOKEN_NAME, "")


def require_token() -> str:
    token = resolve_token()
    if not token:
        typer.echo(f"{ENV_TOKEN_NAME} not set.", err=True)
        raise typer.Exit(1)
    return token


def parse_episode_filter(value: str | None) -> set[int] | None:
    """Parse a comma-separated episode filter into a set of ints."""
    if value is None:
        return None
    parts = [part.strip() for part in value.split(",") if part.strip()]
    result: set[int] = set()
    for part in parts:
        try:
            result.add(int(part))
        except ValueError:
            typer.echo(f"Invalid episode number: {part!r}", err=True)
            raise typer.Exit(1)
    return result


def list_all_records(client: AirtableClient, table_id: str) -> list[dict[str, Any]]:
    """Fetch every record from a table by following offset pagination."""
    all_records: list[dict[str, Any]] = []
    offset = ""
    while True:
        result = client.list_records(table_id, offset=offset)
        records = result.get("records")
        if isinstance(records, list):
            all_records.extend(records)
        next_offset = result.get("offset")
        if not next_offset:
            break
        offset = str(next_offset)
    return all_records


def parse_field_pairs(field_pairs: list[str]) -> dict[str, str]:
    fields: dict[str, str] = {}
    for pair in field_pairs:
        key, _, value = pair.partition("=")
        if key:
            fields[key.strip()] = value
    return fields


def emit_json(data: Any) -> None:
    typer.echo(json.dumps(data, indent=2))
