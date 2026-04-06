"""Tests for atp.schema_parser."""
from __future__ import annotations

from atp.schema_parser import parse_html_to_markdown


def test_parse_html_to_markdown_writes_markdown_files(tmp_path) -> None:
    html = """\
<html>
  <body>
    <div ng-repeat="table in application.tables">
      <h1 section-name="table:artists">Artists Table</h1>
      <span class="tableId">tblABC123</span>
      <div class="docSection fields ng-scope">
        <div class="fieldsRow">
          <span class="columnName">Artist Name</span>
          <span class="columnId">fldABC001</span>
          <div class="type">Text</div>
          <div class="description">The artist name</div>
        </div>
      </div>
      <div class="docSection">
        <h2 section-name="table:artists:list">List</h2>
        <div class="text"><p>List artist records.</p></div>
      </div>
    </div>
  </body>
</html>
"""
    html_path = tmp_path / "airtable.html"
    output_dir = tmp_path / "output"
    html_path.write_text(html, encoding="utf-8")

    written = parse_html_to_markdown(html_path, output_dir=output_dir)

    assert len(written) == 1
    assert written[0].name == "artists.md"
    assert written[0].exists()
