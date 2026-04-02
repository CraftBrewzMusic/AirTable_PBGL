"""Shared project configuration for AirTable PBGL."""
from __future__ import annotations

from pathlib import Path

APP_NAME = "AirTable PBGL"
CLI_NAME = "atp"
CLI_EXPANSION = "AirTable PBGL"
ENV_TOKEN_NAME = "AIRTABLE_API_TOKEN"
BASE_ID = "appEurfA8kXQE3slK"

CHEVY_TABLE_ID = "tblRqFtQrPCNB1fwT"
RELEASES_TABLE_ID = "tbl7rjVKUd5faZ7fV"
RECORDINGS_TABLE_ID = "tblESvQQmOBbEXAH0"
ARTISTS_TABLE_ID = "tbla7zxpHm76x0Aj9"
PAT_BOONE_RECORD_ID = "recLWgt9qnlgDkkAo"

DEFAULT_BATCH_SIZE = 10
DEFAULT_EXPAND_DEPTH = 5
DEFAULT_MIN_CHEVY_EPISODE = 60

DEFAULT_CHEVY_CSV_PATH = Path(
    "/Users/daniellyons/Library/CloudStorage/Box-Box"
    "/The Gold Label/The Pat Boone Chevy Showroom"
    "/Episode Info/song_index.csv"
)

DOCS_DIRNAME = "DOCS"
AIRTABLE_DOCS_DIRNAME = "AIRTABLE_API"
