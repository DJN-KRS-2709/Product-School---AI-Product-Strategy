# Ingestion Guide — Per-Format Recipes

How to get legacy course material into a clean markdown corpus the agent can read.

All extracted markdown lands in `insights/extracted/` so the audit step has a single folder to read.

---

## Setup (once per repo)

```bash
pip install -r .claude/skills/legacy-course-converter/scripts/requirements.txt
```

(Substitute `.cursor/skills/...` if you're using Cursor instead of Claude Code.)

This installs `python-pptx`, `python-docx`, `openpyxl`, and `pdfplumber`.

---

## PowerPoint and Keynote (`.pptx`, `.key`)

**Most common source format for legacy decks.**

```bash
python .claude/skills/legacy-course-converter/scripts/extract_pptx.py insights/old-deck.pptx
```

The script writes `insights/extracted/old-deck.md` containing one section per source slide:

```markdown
## Slide 3 — Slide Title (if any)

- First-level bullet
  - Sub-bullet

> Speaker notes from the slide notes pane go here as a quote block.

[Image: chart-1.png — placement at slide 3]
```

**Keynote**: open in Keynote → File → Export To → PowerPoint → save as `.pptx`. Then run the script.

**Google Slides**: File → Download → Microsoft PowerPoint (.pptx). Then run the script.

### What the script handles

- Slide titles (from the title placeholder)
- Body text in placeholders and text frames (preserves bullet hierarchy)
- Speaker notes from the notes slide
- Image references (logged as placeholders — actual images are not copied)
- Tables (rendered as markdown tables)

### What the script does NOT handle

- SmartArt graphics (logged as `[SmartArt — manual review]`)
- Embedded videos / audio (logged as placeholders)
- Animations and transitions (irrelevant — the new format scroll-snaps)
- Speaker notes formatting (rich text becomes plain text)

---

## Word and Google Docs (`.docx`, `.gdoc`)

**Common source for course outlines, instructor scripts, learning objectives.**

```bash
python .claude/skills/legacy-course-converter/scripts/extract_docx.py insights/outline.docx
```

The script writes `insights/extracted/outline.md` preserving:

- Heading levels (`Heading 1` → `#`, `Heading 2` → `##`, etc.)
- Paragraph text
- Bullet and numbered lists with nesting
- Tables (rendered as markdown)
- Bold and italic emphasis

**Google Docs**: File → Download → Microsoft Word (.docx). Then run the script.

### What the script does NOT handle

- Comments and suggestions (ignored — review the original doc separately)
- Embedded images (logged as placeholders)
- Footnotes and endnotes (appended at the bottom of the file in an `## Footnotes` section)
- Track changes (only the accepted version is extracted)

---

## Excel and Google Sheets (`.xlsx`, `.csv`)

**Common source for module sequencing, learning objective matrices, exercise inventories.**

```bash
python .claude/skills/legacy-course-converter/scripts/extract_xlsx.py insights/syllabus.xlsx
```

The script writes `insights/extracted/syllabus.md` with one section per sheet:

```markdown
## Sheet: Module Arc

| Module | Title | Question | Hours | Build Moment |
|--------|-------|----------|-------|--------------|
| ...    | ...   | ...      | ...   | ...          |
```

**Google Sheets**: File → Download → Microsoft Excel (.xlsx). Then run the script.

**CSV files**: drop directly into `insights/`. The script auto-detects them.

### Tips

- If the source sheet has merged cells, the script unmerges them and back-fills the value into each cell. Review the output.
- Hidden sheets are skipped by default. Pass `--include-hidden` to include them.
- Formulas are evaluated and the cached value is exported. If a sheet was opened only in Google Sheets and never in Excel, formula values may be `None` — re-open in Excel once before exporting.

---

## PDF (`.pdf`)

**Fallback for locked exports of slides or docs you can't get a source file for.**

```bash
python .claude/skills/legacy-course-converter/scripts/extract_pdf.py insights/locked-export.pdf
```

The script writes `insights/extracted/locked-export.md` with text per page:

```markdown
## Page 7

[Extracted body text from this page.]
```

### Quality caveats

- PDF is the **lowest fidelity source**. Always prefer the original `.pptx`, `.docx`, or `.xlsx` if available.
- Layout-heavy slides (multi-column, side-by-side cards) often extract in the wrong reading order. Manual review is required.
- Text in images (screenshots of slides) does NOT extract. The script logs `[Page N — likely scanned/image-only, no text extracted]` so you know.
- For scanned PDFs, run them through OCR first (e.g. macOS Preview's Export with Text Recognition, or Adobe Acrobat OCR) and re-export.

---

## Plain text and markdown (`.txt`, `.md`)

No extraction needed. Drop them in `insights/` directly. The audit step will read them as-is.

Use this for:

- Speaker transcripts from past sessions
- Verbatim notes from prior course delivery
- Brain-dumps, design memos, anything textual

---

## Google Drive folder of mixed files

If the user shares a Google Drive folder with mixed `.gdoc`, `.gslide`, `.gsheet` files:

1. Ask the user to download the whole folder as a `.zip` (Drive lets you do this from the right-click menu on the folder).
2. The zip contains `.docx`, `.pptx`, `.xlsx` versions of each Google file plus original PDFs of anything else.
3. Unzip into `insights/` and run the appropriate extractor for each format.

---

## After extraction — what to expect

```
insights/
├── old-deck.pptx                 (original)
├── outline.docx                  (original)
├── syllabus.xlsx                 (original)
└── extracted/
    ├── old-deck.md
    ├── outline.md
    └── syllabus.md
```

The agent reads everything in `insights/extracted/` for the audit step (Step 3 in `SKILL.md`). The original files in `insights/` stay untouched as the source of truth.
