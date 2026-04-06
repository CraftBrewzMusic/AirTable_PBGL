"""Shared fixtures for the ParseAirTableAPI test suite."""
from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock

import pytest


@pytest.fixture
def mock_session() -> MagicMock:
    """A plain MagicMock that stands in for requests.Session."""
    return MagicMock()


# ---------------------------------------------------------------------------
# Synthetic .md content
# Two real tables + the one file that must be skipped.
# ---------------------------------------------------------------------------

_ARTISTS_MD = """\
# Artists

**Table ID:** `tblABC123`
**Base ID:** `appTEST0001`

## Fields

| Name | Field ID | Type | Description |
| ---- | -------- | ---- | ----------- |
| Artist Name | `fldABC001` | Text | The artist name |
| Genre Formula | `fldABC002` | Formula | Auto-computed |
| Track Count | `fldABC003` | Count | Count rollup |

---

## List Records

**Endpoint:** `GET /v0/appTEST0001/tblABC123`

## Create Records

**Endpoint:** `POST /v0/appTEST0001/tblABC123`

## Update

**Endpoint:** `PATCH /v0/appTEST0001/tblABC123`

## Delete Records

**Endpoint:** `DELETE /v0/appTEST0001/tblABC123`
"""

_RECORDINGS_MD = """\
# Recordings

**Table ID:** `tblDEF456`
**Base ID:** `appTEST0001`

## Fields

| Name | Field ID | Type | Description |
| ---- | -------- | ---- | ----------- |
| Title | `fldDEF001` | Text | Track title |

---

## List Records

**Endpoint:** `GET /v0/appTEST0001/tblDEF456`

## Create Records

**Endpoint:** `POST /v0/appTEST0001/tblDEF456`
"""

_ARTISTS_COPY_MD = """\
# Artists Copy

**Table ID:** `tblGHI789`
**Base ID:** `appTEST0001`
"""

# ---------------------------------------------------------------------------
# Linked-field .md content for expand tests
# ---------------------------------------------------------------------------

_RELEASES_LINK_MD = """\
# Releases

**Table ID:** `tblREL001`
**Base ID:** `appTEST0001`

## Fields

| Name | Field ID | Type | Description |
| ---- | -------- | ---- | ----------- |
| Name | `fldREL001` | Text | Release name |
| Recordings | `fldREL002` | Link to another record | Array of linked records IDs from the Recordings table. |

---

## List Records

**Endpoint:** `GET /v0/appTEST0001/tblREL001`
"""

_RECORDINGS_LINK_MD = """\
# Recordings

**Table ID:** `tblREC001`
**Base ID:** `appTEST0001`

## Fields

| Name | Field ID | Type | Description |
| ---- | -------- | ---- | ----------- |
| Title | `fldREC001` | Text | Track title |
| Compositions | `fldREC002` | Link to another record | Array of linked records IDs from the Compositions table. |

---

## List Records

**Endpoint:** `GET /v0/appTEST0001/tblREC001`
"""

_COMPOSITIONS_LINK_MD = """\
# Compositions

**Table ID:** `tblCOM001`
**Base ID:** `appTEST0001`

## Fields

| Name | Field ID | Type | Description |
| ---- | -------- | ---- | ----------- |
| Title | `fldCOM001` | Text | Composition title |

---

## List Records

**Endpoint:** `GET /v0/appTEST0001/tblCOM001`
"""


@pytest.fixture
def tmp_md_dir(tmp_path: Path) -> Path:
    """A temp directory with two valid .md files and the skip-listed artists_copy.md."""
    (tmp_path / "artists.md").write_text(_ARTISTS_MD, encoding="utf-8")
    (tmp_path / "recordings.md").write_text(_RECORDINGS_MD, encoding="utf-8")
    (tmp_path / "artists_copy.md").write_text(_ARTISTS_COPY_MD, encoding="utf-8")
    return tmp_path


@pytest.fixture
def tmp_link_md_dir(tmp_path: Path) -> Path:
    """A temp directory with three tables that have 'Link to another record' fields."""
    (tmp_path / "releases.md").write_text(_RELEASES_LINK_MD, encoding="utf-8")
    (tmp_path / "recordings.md").write_text(_RECORDINGS_LINK_MD, encoding="utf-8")
    (tmp_path / "compositions.md").write_text(_COMPOSITIONS_LINK_MD, encoding="utf-8")
    return tmp_path
