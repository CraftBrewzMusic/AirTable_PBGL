"""Import Pat Boone Chevy Showroom songs from song_index.csv into AirTable.

Usage:
    uv run python scripts/import_chevy_songs.py [--dry-run]
    uv run python scripts/import_chevy_songs.py --episodes 60
    uv run python scripts/import_chevy_songs.py --episodes 60,61,62
"""
from __future__ import annotations

import csv
import json
import os
import sys
from datetime import datetime
from pathlib import Path

import typer
from dotenv import load_dotenv

# Package is installed via uv; import directly.
from airtable_tui.api import AirtableClient

CHEVY_TABLE_ID = "tblRqFtQrPCNB1fwT"
BASE_ID = "appEurfA8kXQE3slK"
MIN_EPISODE = 60  # default lower bound when --episodes is not specified

CSV_PATH = Path(
    "/Users/daniellyons/Library/CloudStorage/Box-Box"
    "/The Gold Label/The Pat Boone Chevy Showroom"
    "/Episode Info/song_index.csv"
)

# CSV column positions (header has a duplicate "guest_artists" column — use positional access)
COL_EPISODE = 0
COL_TRACK = 1
COL_TITLE = 2
COL_DATE = 3
COL_GUEST = 4

app = typer.Typer(add_completion=False)


# ---------------------------------------------------------------------------
# Date helpers
# ---------------------------------------------------------------------------


def parse_iso_date(s: str) -> str:
    """'October 3, 1957' → '1957-10-03'."""
    return datetime.strptime(s.strip(), "%B %d, %Y").strftime("%Y-%m-%d")


def format_long_date(s: str) -> str:
    """'October 3, 1957' → 'October 3, 1957' (no leading zero on day)."""
    dt = datetime.strptime(s.strip(), "%B %d, %Y")
    return f"{dt.strftime('%B')} {dt.day}, {dt.year}"


# ---------------------------------------------------------------------------
# AirTable helpers
# ---------------------------------------------------------------------------


def list_all_records(client: AirtableClient, table_id: str) -> list[dict[str, object]]:
    """Fetch every record from *table_id*, following AirTable's offset pagination."""
    all_records: list[dict[str, object]] = []
    offset = ""
    while True:
        result = client.list_records(table_id, offset=offset)
        records = result.get("records")
        if isinstance(records, list):
            all_records.extend(records)  # type: ignore[arg-type]
        next_offset = result.get("offset")
        if not next_offset:
            break
        offset = str(next_offset)
    return all_records


def get_existing_keys(client: AirtableClient, table_id: str) -> set[tuple[str, str]]:
    """Return {(episode_str, title_str)} for all records already in *table_id*."""
    records = list_all_records(client, table_id)
    keys: set[tuple[str, str]] = set()
    for rec in records:
        fields = rec.get("fields")
        if not isinstance(fields, dict):
            continue
        ep = str(fields.get("Episode #", "")).strip()
        title = str(fields.get("Recording Title", "")).strip()
        if ep and title:
            keys.add((ep, title))
    return keys


# ---------------------------------------------------------------------------
# CSV → AirTable field mapping
# ---------------------------------------------------------------------------


def build_fields(row: list[str]) -> dict[str, object]:
    """Build the AirTable fields dict from a CSV row (positional columns)."""
    episode_num = row[COL_EPISODE].strip()
    track_num = row[COL_TRACK].strip()
    song_title = row[COL_TITLE].strip()
    raw_date = row[COL_DATE].strip()
    guest = row[COL_GUEST].strip() if len(row) > COL_GUEST else ""

    long_date = format_long_date(raw_date)
    album_title = f"{song_title} (Live On The Pat Boone Chevy Showroom, {long_date})"

    title_version = f"Live On The Pat Boone Chevy Showroom, {long_date}"

    fields: dict[str, object] = {
        "Recording Title": song_title,
        "Episode #": episode_num,
        "Date First Aired": parse_iso_date(raw_date),
        "Album Release Title": album_title,
        "Title Version": title_version,
        "Notes": f"Track #{track_num}",
    }
    if guest:
        fields["Featured Artist"] = [a.strip() for a in guest.split(",") if a.strip()]
    return fields


# ---------------------------------------------------------------------------
# Main command
# ---------------------------------------------------------------------------


def parse_episodes(value: str | None) -> set[int] | None:
    """Parse a comma-separated list of episode numbers into a set, or None if not provided."""
    if value is None:
        return None
    parts = [p.strip() for p in value.split(",") if p.strip()]
    result: set[int] = set()
    for part in parts:
        try:
            result.add(int(part))
        except ValueError:
            typer.secho(f"Invalid episode number: {part!r}", fg=typer.colors.RED, err=True)
            raise typer.Exit(1)
    return result


@app.command()
def main(
    csv_path: Path = typer.Option(CSV_PATH, "--csv", help="Path to song_index.csv"),
    dry_run: bool = typer.Option(False, "--dry-run", help="Print records without writing to AirTable"),
    episodes: str | None = typer.Option(None, "--episodes", help="Comma-separated episode numbers to import (e.g. '60' or '60,61,62'). Defaults to all episodes ≥60."),
) -> None:
    """Import Chevy Showroom songs from CSV into AirTable, skipping duplicates."""

    # Load API token
    project_root = Path(__file__).parent.parent
    load_dotenv(project_root / ".env")
    token = os.environ.get("AIRTABLE_API_TOKEN")
    if not token:
        typer.secho("AIRTABLE_API_TOKEN is not set — check your .env file.", fg=typer.colors.RED, err=True)
        raise typer.Exit(1)

    client = AirtableClient(token=token, base_id=BASE_ID)

    # Parse episode filter
    episode_filter = parse_episodes(episodes)
    if episode_filter is not None:
        typer.echo(f"Filtering to episodes: {sorted(episode_filter)}", err=True)
    else:
        typer.echo(f"Importing all episodes ≥{MIN_EPISODE}.", err=True)

    # Fetch existing records for duplicate detection
    typer.echo("Fetching existing records from AirTable…", err=True)
    existing_keys = get_existing_keys(client, CHEVY_TABLE_ID)
    typer.echo(f"  {len(existing_keys)} existing records found.", err=True)

    # Parse CSV and build import list
    rows_to_import: list[dict[str, object]] = []
    skipped_episode = 0
    skipped_blank = 0
    skipped_duplicate = 0

    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # skip header row
        for row in reader:
            if len(row) < 4:
                continue

            episode_str = row[COL_EPISODE].strip()
            song_title = row[COL_TITLE].strip()

            # Skip missing/non-numeric episode numbers
            if not episode_str:
                skipped_blank += 1
                continue
            try:
                episode_num = int(episode_str)
            except ValueError:
                skipped_blank += 1
                continue

            # Filter by selected episodes or default lower bound
            if episode_filter is not None:
                if episode_num not in episode_filter:
                    skipped_episode += 1
                    continue
            elif episode_num < MIN_EPISODE:
                skipped_episode += 1
                continue

            # Skip rows with no song title
            if not song_title:
                skipped_blank += 1
                continue

            # Skip duplicates already in AirTable
            if (episode_str, song_title) in existing_keys:
                skipped_duplicate += 1
                continue

            rows_to_import.append(build_fields(row))

    typer.echo(
        f"  Skipped {skipped_episode} rows (episodes ≤59), "
        f"{skipped_blank} blank, {skipped_duplicate} duplicates.",
        err=True,
    )
    typer.echo(f"  {len(rows_to_import)} records to import.", err=True)

    if not rows_to_import:
        typer.echo("Nothing to import.", err=True)
        return

    if dry_run:
        json.dump(rows_to_import, sys.stdout, indent=2)
        sys.stdout.write("\n")
        return

    # Batch-create in groups of 10 (AirTable limit per request)
    created = 0
    for i in range(0, len(rows_to_import), 10):
        batch = rows_to_import[i : i + 10]
        result = client.create_records(CHEVY_TABLE_ID, batch, typecast=True)
        n = len(result.get("records", []))  # type: ignore[arg-type]
        created += n
        typer.echo(f"  Created {created}/{len(rows_to_import)}…", err=True)

    typer.echo(f"Done. {created} records created.", err=True)


if __name__ == "__main__":
    app()
