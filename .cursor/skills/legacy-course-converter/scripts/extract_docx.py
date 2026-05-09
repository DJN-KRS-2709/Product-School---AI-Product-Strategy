#!/usr/bin/env python3
"""Extract a .docx file to markdown in insights/extracted/.

Usage:
    python extract_docx.py <path-to-doc.docx> [--out <output-dir>]

Preserves heading levels, bullet/numbered lists with nesting, tables, bold
and italic emphasis, and footnotes (appended at the bottom under
`## Footnotes`).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    from docx import Document
    from docx.oxml.ns import qn
    from docx.text.paragraph import Paragraph
except ImportError:
    sys.stderr.write(
        "python-docx not installed. Run: pip install -r requirements.txt\n"
    )
    sys.exit(1)


HEADING_RE = re.compile(r"^Heading (\d)$")


def get_list_level(paragraph: Paragraph) -> int | None:
    pPr = paragraph._p.find(qn("w:pPr"))
    if pPr is None:
        return None
    numPr = pPr.find(qn("w:numPr"))
    if numPr is None:
        return None
    ilvl = numPr.find(qn("w:ilvl"))
    if ilvl is None:
        return 0
    try:
        return int(ilvl.get(qn("w:val"), "0"))
    except (TypeError, ValueError):
        return 0


def render_run(run) -> str:
    text = run.text
    if not text:
        return ""
    if run.bold and run.italic:
        return f"***{text}***"
    if run.bold:
        return f"**{text}**"
    if run.italic:
        return f"*{text}*"
    return text


def render_paragraph(paragraph: Paragraph) -> str:
    text = "".join(render_run(r) for r in paragraph.runs).strip()
    if not text:
        return ""

    style = (paragraph.style.name or "").strip()
    h_match = HEADING_RE.match(style)
    if h_match:
        level = min(int(h_match.group(1)), 6)
        return f"{'#' * level} {text}"
    if style == "Title":
        return f"# {text}"
    if style == "Subtitle":
        return f"## {text}"

    list_level = get_list_level(paragraph)
    if list_level is not None:
        indent = "  " * list_level
        marker = "-" if "Number" not in style else "1."
        return f"{indent}{marker} {text}"

    return text


def render_table(table) -> str:
    rows: list[str] = []
    for row in table.rows:
        cells = [cell.text.strip().replace("\n", " ") or " " for cell in row.cells]
        rows.append("| " + " | ".join(cells) + " |")
    if not rows:
        return ""
    sep = "| " + " | ".join(["---"] * len(table.columns)) + " |"
    return "\n".join([rows[0], sep, *rows[1:]])


def iter_block_items(parent):
    """Yield paragraphs and tables in document order from a docx element."""
    body = parent.element.body
    for child in body.iterchildren():
        if child.tag == qn("w:p"):
            yield Paragraph(child, parent)
        elif child.tag == qn("w:tbl"):
            from docx.table import Table

            yield Table(child, parent)


def extract_footnotes(doc) -> list[str]:
    """Pull footnote text in document order. Returns markdown lines."""
    notes: list[str] = []
    try:
        part = doc.part.footnotes_part
    except (AttributeError, KeyError):
        return notes
    if part is None:
        return notes
    root = part.element
    for fn in root.findall(qn("w:footnote")):
        fn_id = fn.get(qn("w:id"))
        if fn_id in {"0", "-1"}:
            continue
        text_runs: list[str] = []
        for p in fn.findall(qn("w:p")):
            for t in p.iter(qn("w:t")):
                if t.text:
                    text_runs.append(t.text)
        body = " ".join(text_runs).strip()
        if body:
            notes.append(f"{fn_id}. {body}")
    return notes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="Path to the .docx file")
    parser.add_argument("--out", default=None, help="Output directory")
    args = parser.parse_args()

    in_path = Path(args.input).expanduser().resolve()
    if not in_path.exists():
        sys.stderr.write(f"File not found: {in_path}\n")
        return 1

    out_dir = (
        Path(args.out).expanduser().resolve()
        if args.out
        else Path.cwd() / "insights" / "extracted"
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{in_path.stem}.md"

    doc = Document(str(in_path))
    blocks: list[str] = [
        f"# {in_path.name}",
        "",
        f"Extracted from `{in_path}`.",
        "",
        "---",
        "",
    ]

    from docx.table import Table

    for block in iter_block_items(doc):
        if isinstance(block, Paragraph):
            rendered = render_paragraph(block)
            if rendered:
                blocks.append(rendered)
                blocks.append("")
        elif isinstance(block, Table):
            tbl = render_table(block)
            if tbl:
                blocks.append(tbl)
                blocks.append("")

    footnotes = extract_footnotes(doc)
    if footnotes:
        blocks.extend(["---", "", "## Footnotes", ""])
        blocks.extend(footnotes)
        blocks.append("")

    out_path.write_text("\n".join(blocks).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
