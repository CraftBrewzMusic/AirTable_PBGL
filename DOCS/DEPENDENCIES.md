# Dependencies

This tool is distributed as a Python application, but the dependency chain starts earlier than Python packages alone.

## Dependency Chain

```text
macOS
└── Xcode Command Line Tools
    └── Homebrew (optional but recommended)
        ├── gh
        ├── uv
        │   ├── Python 3.12+
        │   └── project packages
        └── git
            └── AirTable_PBGL repo
                └── AIRTABLE_API_TOKEN in .env
```

## Required Runtime Pieces

- `git`: clone, fetch, tag-based updates
- `uv`: install Python and project dependencies
- Python 3.12+: runtime for CLI, TUI, and schema tooling
- `AIRTABLE_API_TOKEN`: required for live Airtable reads and writes

## Project Dependencies

- `typer`: CLI surface
- `textual`: TUI
- `requests`: Airtable HTTP client
- `python-dotenv`: local env loading
- `beautifulsoup4` and `lxml`: Airtable HTML doc parsing for `atp schema redoc`

## Schema Assets

The app reads committed schema markdown from `DOCS/AIRTABLE_API/`. Those files are regenerated from an Airtable HTML export with:

```bash
uv run atp schema redoc /path/to/export.html
```
