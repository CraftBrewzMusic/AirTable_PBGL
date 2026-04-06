"""Set Primary Artist = Pat Boone on all Releases and Recordings linked from
Chevy Showroom Dist Mgmt rows.

Pat Boone's AirTable artist record ID: recLWgt9qnlgDkkAo

Traversal:
  Chevy rows → Release field  → Releases  → patch Primary Artist if missing
  Chevy rows → Recordings field → Recordings → patch Primary Artist if missing

Idempotent: records that already have Pat Boone as Primary Artist are skipped.
Records that already have a *different* Primary Artist are logged as warnings and
still patched (the user's intent is that every Chevy Release/Recording belongs
to Pat Boone).

Usage:
    uv run python scripts/patch_chevy_primary_artist.py --dry-run
    uv run python scripts/patch_chevy_primary_artist.py --episodes 60
    uv run python scripts/patch_chevy_primary_artist.py
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import typer
from dotenv import load_dotenv

from airtable_tui.api import AirtableClient

CHEVY_TABLE_ID = "tblRqFtQrPCNB1fwT"
RELEASES_TABLE_ID = "tbl7rjVKUd5faZ7fV"
RECORDINGS_TABLE_ID = "tblESvQQmOBbEXAH0"
BASE_ID = "appEurfA8kXQE3slK"

PAT_BOONE_RECORD_ID = "recLWgt9qnlgDkkAo"
BATCH_SIZE = 10

app = typer.Typer(add_completion=False)


# ---------------------------------------------------------------------------
# Helpers
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


def parse_episodes(value: str | None) -> set[int] | None:
    if value is None:
        return None
    result: set[int] = set()
    for part in value.split(","):
        part = part.strip()
        if not part:
            continue
        try:
            result.add(int(part))
        except ValueError:
            typer.secho(f"Invalid episode number: {part!r}", fg=typer.colors.RED, err=True)
            raise typer.Exit(1)
    return result


def collect_linked_ids(
    chevy_records: list[dict[str, object]],
    episode_filter: set[int] | None,
) -> tuple[list[str], list[str]]:
    """Return (release_ids, recording_ids) from Chevy rows, respecting episode filter.

    Deduplicates IDs while preserving first-seen order.
    """
    seen_releases: set[str] = set()
    seen_recordings: set[str] = set()
    release_ids: list[str] = []
    recording_ids: list[str] = []

    for rec in chevy_records:
        fields = rec.get("fields")
        if not isinstance(fields, dict):
            continue

        if episode_filter is not None:
            ep_str = str(fields.get("Episode #", "")).strip()
            try:
                ep_num = int(ep_str)
            except ValueError:
                continue
            if ep_num not in episode_filter:
                continue

        for rid in fields.get("Release", []):  # type: ignore[union-attr]
            if isinstance(rid, str) and rid not in seen_releases:
                seen_releases.add(rid)
                release_ids.append(rid)

        for rid in fields.get("Recordings", []):  # type: ignore[union-attr]
            if isinstance(rid, str) and rid not in seen_recordings:
                seen_recordings.add(rid)
                recording_ids.append(rid)

    return release_ids, recording_ids


def find_missing(
    client: AirtableClient,
    table_id: str,
    record_ids: list[str],
    table_label: str,
) -> list[dict[str, object]]:
    """Return patch dicts for records whose Primary Artist != Pat Boone.

    Logs skips (already correct) and warnings (overwriting a different artist).
    """
    patches: list[dict[str, object]] = []

    for record_id in record_ids:
        rec = client.retrieve_record(table_id, record_id)
        fields = rec.get("fields")
        if not isinstance(fields, dict):
            typer.secho(
                f"  WARNING: could not read fields for {table_label}/{record_id}",
                fg=typer.colors.YELLOW,
                err=True,
            )
            continue

        current: list[str] = fields.get("Primary Artist", [])  # type: ignore[assignment]
        if isinstance(current, list) and PAT_BOONE_RECORD_ID in current:
            # Already correct — skip
            continue

        if current:
            typer.secho(
                f"  OVERWRITING Primary Artist on {table_label}/{record_id}"
                f" (was: {current})",
                fg=typer.colors.YELLOW,
                err=True,
            )
        patches.append({"id": record_id, "fields": {"Primary Artist": [PAT_BOONE_RECORD_ID]}})

    return patches


def apply_patches(
    client: AirtableClient,
    table_id: str,
    patches: list[dict[str, object]],
    table_label: str,
) -> None:
    """Batch-PATCH records in groups of BATCH_SIZE."""
    total = len(patches)
    updated = 0
    for i in range(0, total, BATCH_SIZE):
        batch = patches[i : i + BATCH_SIZE]
        result = client.update_records(table_id, batch)
        if "error" in result:
            typer.secho(
                f"  AirTable error patching {table_label}: {result['error']}",
                fg=typer.colors.RED,
                err=True,
            )
            raise typer.Exit(1)
        n = len(result.get("records", []))  # type: ignore[arg-type]
        updated += n
        typer.echo(
            f"  {table_label}: patched {updated}/{total}",
            err=True,
        )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


@app.command()
def main(
    dry_run: bool = typer.Option(False, "--dry-run", help="Print patch plan to stdout; no API writes."),
    episodes: str | None = typer.Option(
        None,
        "--episodes",
        help="Comma-separated episode numbers to process (e.g. '60' or '60,61'). Default: all rows.",
    ),
) -> None:
    """Ensure Pat Boone is Primary Artist on all Chevy-linked Releases and Recordings."""
    project_root = Path(__file__).parent.parent
    load_dotenv(project_root / ".env")
    token = os.environ.get("AIRTABLE_API_TOKEN")
    if not token:
        typer.secho("AIRTABLE_API_TOKEN is not set — check your .env file.", fg=typer.colors.RED, err=True)
        raise typer.Exit(1)

    client = AirtableClient(token=token, base_id=BASE_ID)

    episode_filter = parse_episodes(episodes)
    if episode_filter is not None:
        typer.echo(f"Filtering to episodes: {sorted(episode_filter)}", err=True)

    typer.echo("Fetching all Chevy Showroom Dist Mgmt rows…", err=True)
    chevy_records = list_all_records(client, CHEVY_TABLE_ID)
    typer.echo(f"  {len(chevy_records)} rows found.", err=True)

    release_ids, recording_ids = collect_linked_ids(chevy_records, episode_filter)
    typer.echo(f"  {len(release_ids)} linked Releases, {len(recording_ids)} linked Recordings.", err=True)

    typer.echo("Checking Releases for missing Primary Artist…", err=True)
    release_patches = find_missing(client, RELEASES_TABLE_ID, release_ids, "Releases")
    typer.echo(f"  {len(release_patches)} Releases need patching.", err=True)

    typer.echo("Checking Recordings for missing Primary Artist…", err=True)
    recording_patches = find_missing(client, RECORDINGS_TABLE_ID, recording_ids, "Recordings")
    typer.echo(f"  {len(recording_patches)} Recordings need patching.", err=True)

    if not release_patches and not recording_patches:
        typer.echo("All records already have Pat Boone as Primary Artist. Nothing to do.", err=True)
        return

    if dry_run:
        json.dump(
            {"releases": release_patches, "recordings": recording_patches},
            sys.stdout,
            indent=2,
        )
        sys.stdout.write("\n")
        return

    if release_patches:
        typer.echo(f"Patching {len(release_patches)} Releases…", err=True)
        apply_patches(client, RELEASES_TABLE_ID, release_patches, "Releases")

    if recording_patches:
        typer.echo(f"Patching {len(recording_patches)} Recordings…", err=True)
        apply_patches(client, RECORDINGS_TABLE_ID, recording_patches, "Recordings")

    typer.echo(
        f"Done. {len(release_patches)} Releases and {len(recording_patches)} Recordings updated.",
        err=True,
    )


if __name__ == "__main__":
    app()
