"""
parse_airtable_docs.py

Parses the AirTable HTML API reference and produces one markdown file
per table inside ./output/.

Usage:
    uv run python parse_airtable_docs.py "Airtable API - The Gold Label Artists Database.html"
"""

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote

from bs4 import BeautifulSoup, Tag

BASE_ID = "appEurfA8kXQE3slK"

OPERATION_LABELS = {
    "list": "List Records",
    "retrieve": "Retrieve a Record",
    "create": "Create Records",
    "update": "Update / Upsert Records",
    "delete": "Delete Records",
}

OPERATION_METHODS = {
    "list": "GET",
    "retrieve": "GET",
    "create": "POST",
    "update": "PATCH",
    "delete": "DELETE",
}


# ---------------------------------------------------------------------------
# 1. Load
# ---------------------------------------------------------------------------

def load_soup(filepath: str) -> BeautifulSoup:
    print(f"Loading {filepath} …", file=sys.stderr)
    with open(filepath, encoding="utf-8") as fh:
        return BeautifulSoup(fh, "lxml")


# ---------------------------------------------------------------------------
# 2. Extract tables
# ---------------------------------------------------------------------------

def extract_tables(soup: BeautifulSoup) -> list[dict]:
    """Return a list of table dicts extracted from the soup."""
    tables = []

    # Each table lives inside a div[ng-repeat="table in application.tables"]
    table_divs = soup.find_all(
        "div", attrs={"ng-repeat": "table in application.tables"}
    )

    for div in table_divs:
        h1 = div.find("h1", attrs={"section-name": re.compile(r"^table:[^:]+$")})
        if h1 is None:
            continue

        section_name = h1.get("section-name", "")  # e.g. "table:compositions"
        table_key = unquote(section_name.removeprefix("table:")).strip()  # "compositions"
        display_name = h1.get_text(strip=True).removesuffix(" Table").strip()

        # Table ID — in the first docSection.fields > span.tableId
        table_id_tag = div.find("span", class_="tableId")
        table_id = table_id_tag.get_text(strip=True) if table_id_tag else ""

        # Fields
        fields = extract_fields(div, table_key)

        # Operations
        operations = {}
        for op in OPERATION_LABELS:
            op_data = extract_operation(div, table_key, op)
            if op_data:
                operations[op] = op_data

        tables.append(
            {
                "key": table_key,
                "display_name": display_name,
                "table_id": table_id,
                "fields": fields,
                "operations": operations,
            }
        )
        print(f"  parsed: {display_name} ({len(fields)} fields)", file=sys.stderr)

    return tables


# ---------------------------------------------------------------------------
# 3. Extract fields
# ---------------------------------------------------------------------------

def extract_fields(table_div: Tag, table_key: str) -> list[dict]:
    """Find all field rows for this table."""
    fields = []

    # Field rows live in div.docSection.fields.ng-scope (one div per field)
    # Each contains a div.fieldsRow (not the header one)
    for section in table_div.find_all("div", class_=lambda c: c and "fields" in c and "ng-scope" in c):
        row = section.find("div", class_="fieldsRow")
        if row is None:
            continue

        name_tag = row.find("span", class_="columnName")
        id_tag = row.find("span", class_="columnId")
        type_tag = row.find("div", class_="type")
        desc_tag = row.find("div", class_="description")

        name = name_tag.get_text(strip=True) if name_tag else ""
        field_id = id_tag.get_text(strip=True) if id_tag else ""
        field_type = type_tag.get_text(strip=True) if type_tag else ""
        # Strip valueType sub-div from description
        description = ""
        if desc_tag:
            # Remove the valueType span/div so we only get the prose
            for vt in desc_tag.find_all(class_="valueType"):
                vt.decompose()
            description = " ".join(desc_tag.get_text(" ", strip=True).split())

        if name:
            fields.append(
                {
                    "name": name,
                    "id": field_id,
                    "type": field_type,
                    "description": description,
                }
            )

    return fields


# ---------------------------------------------------------------------------
# 4. Extract a single operation
# ---------------------------------------------------------------------------

def _extract_curl(section_div: Tag) -> list[str]:
    """Return all curl command strings found in code blocks within section_div."""
    curl_blocks = []
    for pre in section_div.find_all("pre"):
        code = pre.find("code")
        if code:
            text = code.get_text()
            stripped = text.strip()
            if stripped.startswith("curl"):
                curl_blocks.append(stripped)
    return curl_blocks


def _extract_description(section_div: Tag) -> str:
    """Return the first meaningful paragraph of descriptive text."""
    text_div = section_div.find("div", class_="text")
    if text_div is None:
        return ""
    paragraphs = []
    for p in text_div.find_all("p", recursive=True):
        t = " ".join(p.get_text(" ", strip=True).split())
        if t and len(t) > 20:
            paragraphs.append(t)
            if len(paragraphs) == 2:
                break
    return "\n\n".join(paragraphs)


def _extract_parameters(section_div: Tag) -> list[dict]:
    """Return a list of {name, type, required, description} from pagination divs."""
    params = []
    for name_div in section_div.find_all("div", class_="paginationName"):
        raw = name_div.get_text(" ", strip=True)
        # First word(s) before a code.type tag is the param name
        code_type = name_div.find("code", class_="type")
        param_type = code_type.get_text(strip=True) if code_type else ""
        required_tag = name_div.find("span", class_="required")
        optional_tag = name_div.find("span", class_="optional")
        required = "required" if required_tag else "optional"

        # Derive name by removing the type and required/optional text
        name = raw
        if code_type:
            name = name.replace(code_type.get_text(strip=True), "").strip()
        if required_tag:
            name = name.replace("required", "").strip()
        if optional_tag:
            name = name.replace("optional", "").strip()

        # Description is in the next sibling div.paginationDescription
        desc = ""
        next_sib = name_div.find_next_sibling("div", class_="paginationDescription")
        if next_sib:
            desc = " ".join(next_sib.get_text(" ", strip=True).split())[:300]

        params.append(
            {
                "name": name,
                "type": param_type,
                "required": required,
                "description": desc,
            }
        )
    return params


def extract_operation(table_div: Tag, table_key: str, op: str) -> dict | None:
    """Return operation dict for op in ['list','retrieve','create','update','delete']."""
    url_key = table_key.replace(" ", "%20")
    # Match either encoded or plain section-name (BS4 gets raw attr value)
    h2 = table_div.find(
        "h2",
        attrs={"section-name": lambda v: v and unquote(v) == f"table:{table_key}:{op}"},
    )
    if h2 is None:
        return None

    # h2 is inside a div.docSection — that's our section container
    section_div = h2.parent
    if section_div is None:
        return None

    description = _extract_description(section_div)
    curl_commands = _extract_curl(section_div)
    parameters = _extract_parameters(section_div) if op == "list" else []

    return {
        "op": op,
        "description": description,
        "curl_commands": curl_commands,
        "parameters": parameters,
    }


# ---------------------------------------------------------------------------
# 5. Render markdown
# ---------------------------------------------------------------------------

def _safe_filename(name: str) -> str:
    """Convert a table display name to a safe, lowercase filename."""
    s = name.lower()
    # Remove special chars, keep alphanumeric and spaces
    s = re.sub(r"[^\w\s-]", " ", s)
    # Collapse whitespace to hyphens
    s = re.sub(r"[\s_]+", "-", s.strip())
    # Remove leading/trailing hyphens
    s = s.strip("-")
    return s + ".md"


def _escape_md(text: str) -> str:
    """Escape pipe characters inside markdown table cells."""
    return text.replace("|", "\\|")


def render_markdown(table: dict) -> str:
    lines: list[str] = []

    lines.append(f"# {table['display_name']}\n")
    lines.append(f"**Table ID:** `{table['table_id']}`  ")
    lines.append(f"**Base ID:** `{BASE_ID}`\n")
    lines.append("---\n")

    # --- Fields ---
    lines.append("## Fields\n")
    if table["fields"]:
        lines.append("| Field Name | Field ID | Type | Description |")
        lines.append("|------------|----------|------|-------------|")
        for f in table["fields"]:
            name = _escape_md(f["name"])
            fid = _escape_md(f["id"])
            ftype = _escape_md(f["type"])
            desc = _escape_md(f["description"])
            lines.append(f"| {name} | `{fid}` | {ftype} | {desc} |")
    else:
        lines.append("_No fields found._")
    lines.append("")

    # --- Operations ---
    for op, label in OPERATION_LABELS.items():
        if op not in table["operations"]:
            continue

        op_data = table["operations"][op]
        method = OPERATION_METHODS[op]
        table_url_name = table["key"].replace(" ", "%20")

        lines.append("---\n")
        lines.append(f"## {label}\n")
        lines.append(
            f"**Endpoint:** `{method} /v0/{BASE_ID}/{table_url_name}`\n"
        )

        if op_data["description"]:
            lines.append(op_data["description"])
            lines.append("")

        # Curl examples
        for curl in op_data["curl_commands"]:
            lines.append("```bash")
            lines.append(curl)
            lines.append("```\n")

        # Parameters (list only)
        if op_data["parameters"]:
            lines.append("### Query Parameters\n")
            lines.append("| Parameter | Type | Required | Description |")
            lines.append("|-----------|------|----------|-------------|")
            for p in op_data["parameters"]:
                pname = _escape_md(p["name"])
                ptype = _escape_md(p["type"])
                req = p["required"]
                desc = _escape_md(p["description"])
                lines.append(f"| `{pname}` | {ptype} | {req} | {desc} |")
            lines.append("")

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# 6. Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Parse AirTable HTML docs → per-table markdown files"
    )
    parser.add_argument("html_file", help="Path to the AirTable HTML doc")
    parser.add_argument(
        "-o", "--output-dir", default="output", help="Output directory (default: ./output)"
    )
    args = parser.parse_args()

    soup = load_soup(args.html_file)
    tables = extract_tables(soup)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"\nWriting {len(tables)} markdown files to {output_dir}/", file=sys.stderr)
    for table in tables:
        filename = _safe_filename(table["display_name"])
        md = render_markdown(table)
        out_path = output_dir / filename
        out_path.write_text(md, encoding="utf-8")
        print(f"  → {out_path}", file=sys.stderr)

    print("\nDone.", file=sys.stderr)


if __name__ == "__main__":
    main()
