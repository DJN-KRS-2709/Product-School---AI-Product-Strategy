#!/usr/bin/env python3
"""Extract a .pdf file to markdown in insights/extracted/.

Usage:
    python extract_pdf.py <path-to-file.pdf> [--out <output-dir>]

Each page becomes a `## Page N` section. Tables detected on a page are
rendered as markdown tables under a `### Tables on page N` subheading.
Pages with no extractable text are flagged.

PDF is a low-fidelity source. Always prefer original .pptx, .docx, or .xlsx.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import pdfplumber
except ImportError:
    sys.stderr.write(
        "pdfplumber not installed. Run: pip install -r requirements.txt\n"
    )
    sys.exit(1)


def render_table(rows) -> str:
    rows = [
        [(c or "").strip().replace("\n", " ") or " " for c in row]
        for row in rows
        if any((c or "").strip() for c in row)
    ]
    if not rows:
        return ""
    width = max(len(r) for r in rows)
    rows = [r + [" "] * (width - len(r)) for r in rows]
    out = ["| " + " | ".join(rows[0]) + " |"]
    out.append("| " + " | ".join(["---"] * width) + " |")
    for r in rows[1:]:
        out.append("| " + " | ".join(r) + " |")
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="Path to the .pdf file")
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

    blocks: list[str] = [
        f"# {in_path.name}",
        "",
        f"Extracted from `{in_path}`.",
        "",
        "_PDF is a low-fidelity source. Layout-heavy pages may extract in the wrong reading order. "
        "Manual review recommended._",
        "",
        "---",
        "",
    ]

    with pdfplumber.open(str(in_path)) as pdf:
        page_count = len(pdf.pages)
        for page_idx, page in enumerate(pdf.pages, start=1):
            text = (page.extract_text() or "").strip()
            tables = page.extract_tables() or []

            blocks.append(f"## Page {page_idx}")
            blocks.append("")

            if not text and not tables:
                blocks.append(
                    f"_[Page {page_idx} — likely scanned/image-only, no text extracted]_"
                )
                blocks.append("")
                continue

            if text:
                blocks.append(text)
                blocks.append("")

            if tables:
                blocks.append(f"### Tables on page {page_idx}")
                blocks.append("")
                for tbl in tables:
                    rendered = render_table(tbl)
                    if rendered:
                        blocks.append(rendered)
                        blocks.append("")

    out_path.write_text("\n".join(blocks).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote {page_count} pages to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
