"""Resolve Chevy Showroom featured artist names to Artist record IDs and patch
linked Releases and Recordings.

Chevy rows store guest artists as text names in a Multiple select field
("Featured Artist"). The linked Releases and Recordings have Link-to-record
fields that need real Artist record IDs. This script bridges the gap.

Traversal:
  Chevy rows → Release field     → Releases   → patch "Featured Artist(s)"
  Chevy rows → Recordings field  → Recordings → patch "Featured Artist"

Idempotent: existing artist IDs are read and merged; only new IDs trigger a
PATCH call.

Usage:
    uv run python scripts/patch_chevy_featured_artists.py --dry-run
    uv run python scripts/patch_chevy_featured_artists.py --episodes 60,61,62
    uv run python scripts/patch_chevy_featured_artists.py   # all rows
"""
from __future__ import annotations

import typer

from .api import AirtableClient
from .common import emit_json, list_all_records, parse_episode_filter, require_token
from .config import (
    ARTISTS_TABLE_ID,
    BASE_ID,
    CHEVY_TABLE_ID,
    DEFAULT_BATCH_SIZE,
    RECORDINGS_TABLE_ID,
    RELEASES_TABLE_ID,
)

# Field names used in PATCH payloads
RELEASES_FA_FIELD = "Featured Artist(s)"
RECORDINGS_FA_FIELD = "Featured Artist"

def build_artist_name_map(client: AirtableClient) -> dict[str, str]:
    """Return lowercased name → record_id for every Artist record.

    Warns on name collisions (keeps first occurrence).
    """
    typer.echo("Fetching all Artist records to build name map…", err=True)
    records = list_all_records(client, ARTISTS_TABLE_ID)
    typer.echo(f"  {len(records)} Artist records found.", err=True)

    name_map: dict[str, str] = {}
    for rec in records:
        record_id = rec.get("id")
        fields = rec.get("fields")
        if not isinstance(record_id, str) or not isinstance(fields, dict):
            continue
        name = fields.get("Name")
        if not isinstance(name, str) or not name.strip():
            continue
        key = name.strip().lower()
        if key in name_map:
            typer.secho(
                f"  WARNING: duplicate artist name {name!r} — keeping {name_map[key]}, ignoring {record_id}",
                fg=typer.colors.YELLOW,
                err=True,
            )
        else:
            name_map[key] = record_id
    return name_map


def resolve_artist_names(
    names: list[str],
    name_map: dict[str, str],
    context: str,
) -> list[str]:
    """Resolve a list of text names to Artist record IDs.

    Warns for each unresolved name and returns only the successfully resolved IDs.
    """
    resolved: list[str] = []
    for name in names:
        key = name.strip().lower()
        record_id = name_map.get(key)
        if record_id is None:
            typer.secho(
                f"  WARNING: unresolved artist name {name!r} in {context} — skipping",
                fg=typer.colors.YELLOW,
                err=True,
            )
        else:
            resolved.append(record_id)
    return resolved


def accumulate_patches(
    chevy_records: list[dict[str, object]],
    episode_filter: set[int] | None,
    name_map: dict[str, str],
) -> tuple[dict[str, set[str]], dict[str, set[str]]]:
    """Walk qualifying Chevy rows and accumulate artist IDs per Release/Recording.

    Returns (release_patches, recording_patches) where each is a dict from
    record_id → set of artist record IDs that should appear in that record.
    """
    release_patches: dict[str, set[str]] = {}
    recording_patches: dict[str, set[str]] = {}

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

        raw_artists = fields.get("Featured Artist")
        if not raw_artists:
            continue
        if not isinstance(raw_artists, list):
            continue

        context = f"Chevy row {rec.get('id', '?')} (ep {fields.get('Episode #', '?')})"
        artist_ids = resolve_artist_names(raw_artists, name_map, context)  # type: ignore[arg-type]
        if not artist_ids:
            continue

        for release_id in fields.get("Release", []):  # type: ignore[union-attr]
            if isinstance(release_id, str):
                release_patches.setdefault(release_id, set()).update(artist_ids)

        for recording_id in fields.get("Recordings", []):  # type: ignore[union-attr]
            if isinstance(recording_id, str):
                recording_patches.setdefault(recording_id, set()).update(artist_ids)

    return release_patches, recording_patches


def build_patch_list(
    client: AirtableClient,
    table_id: str,
    patches: dict[str, set[str]],
    fa_field: str,
    table_label: str,
) -> list[dict[str, object]]:
    """For each record, fetch existing Featured Artist IDs and merge with new ones.

    Returns only records where the merged set is larger than the existing set
    (i.e. there are genuinely new IDs to add).
    """
    result: list[dict[str, object]] = []
    for record_id, new_ids in patches.items():
        rec = client.retrieve_record(table_id, record_id)
        fields = rec.get("fields")
        if not isinstance(fields, dict):
            typer.secho(
                f"  WARNING: could not read fields for {table_label}/{record_id}",
                fg=typer.colors.YELLOW,
                err=True,
            )
            continue

        existing: list[str] = fields.get(fa_field, [])  # type: ignore[assignment]
        if not isinstance(existing, list):
            existing = []

        existing_set = set(existing)
        merged = existing_set | new_ids

        if merged == existing_set:
            # Nothing to add
            continue

        result.append({"id": record_id, "fields": {fa_field: sorted(merged)}})
    return result


def apply_patches(
    client: AirtableClient,
    table_id: str,
    patches: list[dict[str, object]],
    table_label: str,
) -> None:
    """Batch-PATCH records in groups of BATCH_SIZE."""
    total = len(patches)
    updated = 0
    for i in range(0, total, DEFAULT_BATCH_SIZE):
        batch = patches[i : i + DEFAULT_BATCH_SIZE]
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
        typer.echo(f"  {table_label}: patched {updated}/{total}", err=True)


def main(
    apply: bool = typer.Option(False, "--apply", help="Apply the live Airtable patches."),
    episodes: str | None = typer.Option(
        None,
        "--episodes",
        help="Comma-separated episode numbers to process (e.g. '60' or '60,61'). Default: all rows.",
    ),
) -> None:
    """Patch Featured Artist links on Releases and Recordings linked from Chevy rows."""
    client = AirtableClient(token=require_token(), base_id=BASE_ID)
    episode_filter = parse_episode_filter(episodes)
    if episode_filter is not None:
        typer.echo(f"Filtering to episodes: {sorted(episode_filter)}", err=True)

    # Step 1 — build name map
    name_map = build_artist_name_map(client)

    # Step 2 — fetch Chevy rows
    typer.echo("Fetching all Chevy Showroom Dist Mgmt rows…", err=True)
    chevy_records = list_all_records(client, CHEVY_TABLE_ID)
    typer.echo(f"  {len(chevy_records)} rows found.", err=True)

    # Step 3 — accumulate patches
    release_acc, recording_acc = accumulate_patches(chevy_records, episode_filter, name_map)
    typer.echo(
        f"  {len(release_acc)} Releases and {len(recording_acc)} Recordings have featured artists to check.",
        err=True,
    )

    # Step 4 — idempotency check: build final patch lists
    typer.echo("Checking Releases for missing Featured Artist links…", err=True)
    release_patches = build_patch_list(client, RELEASES_TABLE_ID, release_acc, RELEASES_FA_FIELD, "Releases")
    typer.echo(f"  {len(release_patches)} Releases need patching.", err=True)

    typer.echo("Checking Recordings for missing Featured Artist links…", err=True)
    recording_patches = build_patch_list(client, RECORDINGS_TABLE_ID, recording_acc, RECORDINGS_FA_FIELD, "Recordings")
    typer.echo(f"  {len(recording_patches)} Recordings need patching.", err=True)

    if not release_patches and not recording_patches:
        typer.echo("All records already have correct Featured Artist links. Nothing to do.", err=True)
        return

    if not apply:
        emit_json({"releases": release_patches, "recordings": recording_patches})
        return

    # Step 5 — apply patches
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
