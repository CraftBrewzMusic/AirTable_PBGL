"""Create Releases and Recordings for unlinked Chevy Showroom Dist Mgmt rows.

Each unlinked Chevy row gets one Release and one Recording wired up via four
phases that mirror AirTable's bidirectional link requirements:

  Phase 1 — Create Release (links Release → Chevy; Chevy.Release auto-populates)
  Phase 2 — Create Recording (links Recording → Release via Original Release)
  Phase 3 — Patch Release with Recordings link
  Phase 4 — Patch Chevy row with Recordings link

Idempotent: rows that already have a Release linked are skipped.

Usage:
    uv run python scripts/link_chevy_releases.py --dry-run
    uv run python scripts/link_chevy_releases.py --episodes 60
    uv run python scripts/link_chevy_releases.py --episodes 60,61,62
    uv run python scripts/link_chevy_releases.py
"""
from __future__ import annotations

import typer

from .api import AirtableClient
from .common import emit_json, list_all_records, parse_episode_filter, require_token
from .config import BASE_ID, CHEVY_TABLE_ID, DEFAULT_BATCH_SIZE, RECORDINGS_TABLE_ID, RELEASES_TABLE_ID


def fetch_unlinked_chevy_rows(
    client: AirtableClient,
    episode_filter: set[int] | None,
) -> list[dict[str, object]]:
    """Return Chevy rows that have no Release link yet."""
    all_records = list_all_records(client, CHEVY_TABLE_ID)
    unlinked = []
    for rec in all_records:
        fields = rec.get("fields")
        if not isinstance(fields, dict):
            continue
        # Skip rows that already have a Release linked
        if fields.get("Release"):
            continue
        # Apply optional episode filter
        if episode_filter is not None:
            ep_str = str(fields.get("Episode #", "")).strip()
            try:
                ep_num = int(ep_str)
            except ValueError:
                continue
            if ep_num not in episode_filter:
                continue
        unlinked.append(rec)
    return unlinked


def build_pending(records: list[dict[str, object]]) -> list[dict[str, object]]:
    """Map raw AirTable records to a flat list of pending rows.

    Each entry contains the Chevy record ID, song title, album title, and
    episode number. The release_id and recording_id slots start empty and are
    filled in by the phase functions.

    Rows missing Album Release Title or Recording Title are skipped.
    """
    pending = []
    for rec in records:
        fields = rec.get("fields")
        if not isinstance(fields, dict):
            continue
        chevy_id = str(rec.get("id", "")).strip()
        song_title = str(fields.get("Recording Title", "")).strip()
        album_title = str(fields.get("Album Release Title", "")).strip()
        episode = str(fields.get("Episode #", "")).strip()
        if not chevy_id or not song_title or not album_title:
            continue
        pending.append({
            "chevy_id": chevy_id,
            "song_title": song_title,
            "album_title": album_title,
            "episode": episode,
            "release_id": "",
            "recording_id": "",
        })
    return pending


def _check_response(result: dict[str, object], phase: str) -> None:
    """Raise a clear error if AirTable returned an error payload."""
    if "error" in result:
        err = result["error"]
        raise typer.Exit(
            typer.secho(
                f"  AirTable error in {phase}: {err}",
                fg=typer.colors.RED,
                err=True,
            )
            or 1
        )
    if "records" not in result:
        raise typer.Exit(
            typer.secho(
                f"  Unexpected response in {phase} (no 'records' key): {result}",
                fg=typer.colors.RED,
                err=True,
            )
            or 1
        )


def phase1_create_releases(
    client: AirtableClient,
    pending: list[dict[str, object]],
) -> None:
    """Create one Release per pending row; mutates each row with its release_id.

    Setting Releases.Chevy Showroom Dist Mgmt causes AirTable to auto-populate
    the reverse ChesvyShowroom.Release field for free.
    """
    for i in range(0, len(pending), DEFAULT_BATCH_SIZE):
        batch = pending[i : i + DEFAULT_BATCH_SIZE]
        fields_list = [
            {
                "Release Title": row["album_title"],
                "Chevy Showroom Dist Mgmt": [row["chevy_id"]],
            }
            for row in batch
        ]
        result = client.create_records(RELEASES_TABLE_ID, fields_list)
        _check_response(result, "Phase 1 (create releases)")
        created = result["records"]
        for j, rec in enumerate(created):  # type: ignore[union-attr]
            batch[j]["release_id"] = rec["id"]  # type: ignore[index]
        typer.echo(
            f"  Phase 1: created {len(created)}/{len(batch)} releases"
            f" (total {i + len(created)}/{len(pending)})",
            err=True,
        )


def phase2_create_recordings(
    client: AirtableClient,
    pending: list[dict[str, object]],
) -> None:
    """Create one Recording per pending row; mutates each row with its recording_id."""
    for i in range(0, len(pending), DEFAULT_BATCH_SIZE):
        batch = pending[i : i + DEFAULT_BATCH_SIZE]
        fields_list = [
            {
                "Title of Recording": row["song_title"],
                "Original Release": [row["release_id"]],
            }
            for row in batch
        ]
        result = client.create_records(RECORDINGS_TABLE_ID, fields_list)
        _check_response(result, "Phase 2 (create recordings)")
        created = result["records"]
        for j, rec in enumerate(created):  # type: ignore[union-attr]
            batch[j]["recording_id"] = rec["id"]  # type: ignore[index]
        typer.echo(
            f"  Phase 2: created {len(created)}/{len(batch)} recordings"
            f" (total {i + len(created)}/{len(pending)})",
            err=True,
        )


def phase3_update_releases(
    client: AirtableClient,
    pending: list[dict[str, object]],
) -> None:
    """Patch each Release with its Recordings link."""
    for i in range(0, len(pending), DEFAULT_BATCH_SIZE):
        batch = pending[i : i + DEFAULT_BATCH_SIZE]
        records = [
            {"id": row["release_id"], "fields": {"Recordings": [row["recording_id"]]}}
            for row in batch
        ]
        result = client.update_records(RELEASES_TABLE_ID, records)
        _check_response(result, "Phase 3 (update releases)")
        updated = result["records"]
        typer.echo(
            f"  Phase 3: updated {len(updated)}/{len(batch)} releases"
            f" (total {i + len(updated)}/{len(pending)})",
            err=True,
        )


def phase4_update_chevy(
    client: AirtableClient,
    pending: list[dict[str, object]],
) -> None:
    """Patch each Chevy row with its Recordings link."""
    for i in range(0, len(pending), DEFAULT_BATCH_SIZE):
        batch = pending[i : i + DEFAULT_BATCH_SIZE]
        records = [
            {"id": row["chevy_id"], "fields": {"Recordings": [row["recording_id"]]}}
            for row in batch
        ]
        result = client.update_records(CHEVY_TABLE_ID, records)
        _check_response(result, "Phase 4 (update Chevy rows)")
        updated = result["records"]
        typer.echo(
            f"  Phase 4: updated {len(updated)}/{len(batch)} Chevy rows"
            f" (total {i + len(updated)}/{len(pending)})",
            err=True,
        )


def main(
    apply: bool = typer.Option(False, "--apply", help="Apply the live Airtable writes."),
    episodes: str | None = typer.Option(
        None,
        "--episodes",
        help="Comma-separated episode numbers (e.g. '60' or '60,61,62'). Default: all unlinked rows.",
    ),
) -> None:
    """Create Releases + Recordings for unlinked Chevy Showroom Dist Mgmt rows."""
    client = AirtableClient(token=require_token(), base_id=BASE_ID)
    episode_filter = parse_episode_filter(episodes)
    if episode_filter is not None:
        typer.echo(f"Filtering to episodes: {sorted(episode_filter)}", err=True)
    else:
        typer.echo("Processing all unlinked rows.", err=True)

    typer.echo("Fetching unlinked Chevy rows…", err=True)
    unlinked = fetch_unlinked_chevy_rows(client, episode_filter)
    typer.echo(f"  {len(unlinked)} unlinked rows found.", err=True)

    pending = build_pending(unlinked)
    skipped = len(unlinked) - len(pending)
    if skipped:
        typer.echo(f"  {skipped} rows skipped (missing required fields).", err=True)

    if not pending:
        typer.echo("0 rows need linking.", err=True)
        return

    if not apply:
        emit_json(pending)
        return

    typer.echo(f"Processing {len(pending)} rows in 4 phases…", err=True)
    phase1_create_releases(client, pending)
    phase2_create_recordings(client, pending)
    phase3_update_releases(client, pending)
    phase4_update_chevy(client, pending)
    typer.echo(f"Done. {len(pending)} rows linked.", err=True)
