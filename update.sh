#!/usr/bin/env bash
set -euo pipefail

say() {
  printf '%s\n' "$1"
}

need_cmd() {
  if ! command -v "$1" >/dev/null 2>&1; then
    say "Missing required command: $1"
    exit 1
  fi
}

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

if [ ! -f "pyproject.toml" ]; then
  say "update.sh must run from the AirTable_PBGL repo."
  exit 1
fi

need_cmd git
need_cmd uv

say "Fetching tags..."
git fetch --tags

LATEST_TAG="$(git tag --sort=-v:refname | head -n 1)"

if [ -z "$LATEST_TAG" ]; then
  say "No tags found. Updating current branch dependencies instead."
  uv sync
  exit 0
fi

say "Latest tagged release: $LATEST_TAG"
CURRENT_REF="$(git describe --tags --always 2>/dev/null || git rev-parse --short HEAD)"
say "Current version: $CURRENT_REF"

if [ "$CURRENT_REF" != "$LATEST_TAG" ]; then
  say "Checking out $LATEST_TAG..."
  git checkout "$LATEST_TAG"
fi

say "Syncing Python dependencies with uv..."
uv sync

say "Update complete."
