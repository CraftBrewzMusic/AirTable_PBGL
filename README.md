# AirTable PBGL

`atp` stands for `AirTable PBGL`.

This repo packages the PBGL Airtable tooling as one Python project with:

- a CLI-first automation surface
- a Textual TUI for guided table operations
- committed schema markdown under `DOCS/AIRTABLE_API/`
- setup and update scripts for teammate onboarding

## Setup

Requires Python 3.12+ and [`uv`](https://docs.astral.sh/uv/).

```bash
./setup.sh
```

Or, if you are already inside the repo:

```bash
uv sync
cp .env.example .env
```

Then set `AIRTABLE_API_TOKEN` in `.env`.

## Usage

Launch the TUI:

```bash
uv run atp
```

Use the CLI:

```bash
uv run atp records list Artists
uv run atp records retrieve Releases recXXXXXXXXXXXXXX --expand
uv run atp records create Artists --field "Name=Example"        # preview
uv run atp records create Artists --field "Name=Example" --apply
uv run atp schema redoc /path/to/airtable-export.html
uv run atp chevy import-songs --episodes 60                     # preview
uv run atp chevy import-songs --episodes 60 --apply
```

Mutating CLI commands preview by default. Pass `--apply` to make live Airtable changes.

## Layout

```text
AirTable_PBGL/
├── setup.sh
├── update.sh
├── pyproject.toml
├── src/atp/
├── DOCS/
│   ├── AIRTABLE_API/
│   ├── DEPENDENCIES.md
│   ├── RELEASING.md
│   └── data-model.md
└── tests/
```

## Notes

- The committed markdown files in `DOCS/AIRTABLE_API/` are the metadata source of truth for v1.
- The TUI stays focused on generic Airtable record operations.
- The Chevy/PBGL workflows are exposed through `atp chevy ...`.
