"""Parse Airtable HTML docs into committed markdown schema files."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

from bs4 import BeautifulSoup, Tag

from .common import find_project_root
from .config import AIRTABLE_DOCS_DIRNAME, BASE_ID, DOCS_DIRNAME

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


def default_output_dir() -> Path:
    return find_project_root() / DOCS_DIRNAME / AIRTABLE_DOCS_DIRNAME


def load_soup(filepath: Path) -> BeautifulSoup:
    print(f"Loading {filepath} ...", file=sys.stderr)
    with filepath.open(encoding="utf-8") as fh:
        return BeautifulSoup(fh, "lxml")


def extract_tables(soup: BeautifulSoup) -> list[dict[str, object]]:
    tables: list[dict[str, object]] = []
    table_divs = soup.find_all("div", attrs={"ng-repeat": "table in application.tables"})

    for div in table_divs:
        h1 = div.find("h1", attrs={"section-name": re.compile(r"^table:[^:]+$")})
        if h1 is None:
            continue

        section_name = h1.get("section-name", "")
        table_key = unquote(section_name.removeprefix("table:")).strip()
        display_name = h1.get_text(strip=True).removesuffix(" Table").strip()
        table_id_tag = div.find("span", class_="tableId")
        table_id = table_id_tag.get_text(strip=True) if table_id_tag else ""

        fields = extract_fields(div)
        operations: dict[str, dict[str, object]] = {}
        for op in OPERATION_LABELS:
            op_data = extract_operation(div, table_key, op)
            if op_data:
                operations[op] = op_data

        tables.append({
            "key": table_key,
            "display_name": display_name,
            "table_id": table_id,
            "fields": fields,
            "operations": operations,
        })
        print(f"  parsed: {display_name} ({len(fields)} fields)", file=sys.stderr)

    return tables


def extract_fields(table_div: Tag) -> list[dict[str, str]]:
    fields: list[dict[str, str]] = []
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
        description = ""
        if desc_tag:
            for vt in desc_tag.find_all(class_="valueType"):
                vt.decompose()
            description = " ".join(desc_tag.get_text(" ", strip=True).split())

        if name:
            fields.append({
                "name": name,
                "id": field_id,
                "type": field_type,
                "description": description,
            })

    return fields


def _extract_curl(section_div: Tag) -> list[str]:
    curl_blocks: list[str] = []
    for pre in section_div.find_all("pre"):
        code = pre.find("code")
        if code:
            stripped = code.get_text().strip()
            if stripped.startswith("curl"):
                curl_blocks.append(stripped)
    return curl_blocks


def _extract_description(section_div: Tag) -> str:
    text_div = section_div.find("div", class_="text")
    if text_div is None:
        return ""
    paragraphs: list[str] = []
    for paragraph in text_div.find_all("p", recursive=True):
        text = " ".join(paragraph.get_text(" ", strip=True).split())
        if text and len(text) > 20:
            paragraphs.append(text)
            if len(paragraphs) == 2:
                break
    return "\n\n".join(paragraphs)


def _extract_parameters(section_div: Tag) -> list[dict[str, str]]:
    params: list[dict[str, str]] = []
    for name_div in section_div.find_all("div", class_="paginationName"):
        raw = name_div.get_text(" ", strip=True)
        code_type = name_div.find("code", class_="type")
        param_type = code_type.get_text(strip=True) if code_type else ""
        required_tag = name_div.find("span", class_="required")
        optional_tag = name_div.find("span", class_="optional")
        required = "required" if required_tag else "optional"

        name = raw
        if code_type:
            name = name.replace(code_type.get_text(strip=True), "").strip()
        if required_tag:
            name = name.replace("required", "").strip()
        if optional_tag:
            name = name.replace("optional", "").strip()

        desc = ""
        next_sib = name_div.find_next_sibling("div", class_="paginationDescription")
        if next_sib:
            desc = " ".join(next_sib.get_text(" ", strip=True).split())[:300]

        params.append({
            "name": name,
            "type": param_type,
            "required": required,
            "description": desc,
        })
    return params


def extract_operation(table_div: Tag, table_key: str, op: str) -> dict[str, object] | None:
    h2 = table_div.find(
        "h2",
        attrs={"section-name": lambda v: v and unquote(v) == f"table:{table_key}:{op}"},
    )
    if h2 is None or h2.parent is None:
        return None

    return {
        "op": op,
        "description": _extract_description(h2.parent),
        "curl_commands": _extract_curl(h2.parent),
        "parameters": _extract_parameters(h2.parent) if op == "list" else [],
    }


def _safe_filename(name: str) -> str:
    safe = re.sub(r"[^\w\s-]", " ", name.lower())
    safe = re.sub(r"[\s_]+", "-", safe.strip()).strip("-")
    return f"{safe}.md"


def _escape_md(text: str) -> str:
    return text.replace("|", "\\|")


def render_markdown(table: dict[str, object]) -> str:
    lines: list[str] = []
    display_name = str(table["display_name"])
    table_id = str(table["table_id"])
    lines.append(f"# {display_name}\n")
    lines.append(f"**Table ID:** `{table_id}`  ")
    lines.append(f"**Base ID:** `{BASE_ID}`\n")
    lines.append("---\n")
    lines.append("## Fields\n")

    fields = table["fields"]
    if isinstance(fields, list) and fields:
        lines.append("| Field Name | Field ID | Type | Description |")
        lines.append("|------------|----------|------|-------------|")
        for field in fields:
            if not isinstance(field, dict):
                continue
            lines.append(
                "| "
                f"{_escape_md(str(field.get('name', '')))} | "
                f"`{_escape_md(str(field.get('id', '')))} `".replace(" `", "`")
                + " | "
                f"{_escape_md(str(field.get('type', '')))} | "
                f"{_escape_md(str(field.get('description', '')))} |"
            )
    else:
        lines.append("_No fields found._")
    lines.append("")

    operations = table["operations"]
    if isinstance(operations, dict):
        for op, label in OPERATION_LABELS.items():
            if op not in operations:
                continue
            op_data = operations[op]
            if not isinstance(op_data, dict):
                continue
            lines.append("---\n")
            lines.append(f"## {label}\n")
            lines.append(f"**Endpoint:** `{OPERATION_METHODS[op]} /v0/{BASE_ID}/{table['key']}`\n")
            description = str(op_data.get("description", ""))
            if description:
                lines.append(description)
                lines.append("")

            curl_commands = op_data.get("curl_commands")
            if isinstance(curl_commands, list):
                for curl in curl_commands:
                    lines.append("```bash")
                    lines.append(str(curl))
                    lines.append("```\n")

            parameters = op_data.get("parameters")
            if isinstance(parameters, list) and parameters:
                lines.append("### Query Parameters\n")
                lines.append("| Parameter | Type | Required | Description |")
                lines.append("|-----------|------|----------|-------------|")
                for param in parameters:
                    if not isinstance(param, dict):
                        continue
                    lines.append(
                        f"| `{_escape_md(str(param.get('name', '')))}` | "
                        f"{_escape_md(str(param.get('type', '')))} | "
                        f"{param.get('required', '')} | "
                        f"{_escape_md(str(param.get('description', '')))} |"
                    )
                lines.append("")

    return "\n".join(lines) + "\n"


def parse_html_to_markdown(html_file: Path, output_dir: Path | None = None) -> list[Path]:
    target_dir = output_dir or default_output_dir()
    target_dir.mkdir(parents=True, exist_ok=True)

    soup = load_soup(html_file)
    tables = extract_tables(soup)
    written: list[Path] = []

    print(f"\nWriting {len(tables)} markdown files to {target_dir}/", file=sys.stderr)
    for table in tables:
        filename = _safe_filename(str(table["display_name"]))
        out_path = target_dir / filename
        out_path.write_text(render_markdown(table), encoding="utf-8")
        written.append(out_path)
        print(f"  -> {out_path}", file=sys.stderr)

    print("\nDone.", file=sys.stderr)
    return written
