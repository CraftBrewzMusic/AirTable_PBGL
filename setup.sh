#!/usr/bin/env bash
set -euo pipefail

REPO_URL="https://github.com/CraftBrewzMusic/AirTable_PBGL.git"

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

say "AirTable PBGL setup"
say "This script installs dependencies and prepares a local .env file."

need_cmd git
need_cmd uv

if [ ! -f "$ROOT/pyproject.toml" ]; then
  say "This copy of setup.sh expects to run from a cloned AirTable_PBGL repo."
  say "Clone the repo first with: git clone $REPO_URL"
  exit 1
fi

cd "$ROOT"

say "Syncing Python dependencies with uv..."
uv sync

if [ ! -f ".env" ] && [ -f ".env.example" ]; then
  cp ".env.example" ".env"
  say "Created .env from .env.example"
fi

say "Next step: add AIRTABLE_API_TOKEN to .env"
say "Launch with: uv run atp"
