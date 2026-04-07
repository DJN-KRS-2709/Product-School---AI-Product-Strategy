---
name: course-module-builder
description: >-
  Build and maintain course modules with HTML slide decks, markdown speaker notes,
  interactive tools, and supporting materials. Use when the user asks to create a
  new module, add slides, write speaker notes, build interactive tools, collect
  insights, scaffold a course repo, or follow the established course structure.
---

# Course Module Builder

This skill documents a complete workflow for building course content: self-contained HTML slide decks, markdown speaker notes for the instructor, interactive HTML tools, insight collection, and a strategy repo template that students build into across sessions.

## Repository Structure

```
<Course Name>/
├── index.html                          # Redirect to pitch deck
├── course-architecture.md              # Full course arc, design principles, module summaries
├── storyline.md                        # Narrative arc and session rhythm
├── course-status.md                    # Module status tracker, open decisions, timeline
├── lenny-insights.md                   # Curated external insights organized by module
│
├── Modules/
│   ├── Module 1 - Slides.html          # Self-contained HTML slide deck
│   ├── Module 1 - Speaker Notes.md     # Instructor briefing (markdown)
│   ├── M1 - Vulnerability Scorecard.html   # Interactive tool for M1
│   ├── M2 - Flywheel Scorer.html       # Interactive tool for M2
│   ├── ...                             # Pattern: M{n} - {Tool Name}.html
│   ├── Strategy Repo Template.html     # Interactive template viewer
│   └── Living Strategy Builder.html    # Cross-module strategy builder
│
├── Pitch/
│   ├── AI Product Strategy - Pitch Deck.html
│   ├── Speaker Notes.md
│   └── Gamma Prompt.md                 # Paste-into-Gamma prompt for deck generation
│
├── insights/
│   ├── *.pptx                          # Source slide decks from collaborators
│   ├── *.txt                           # Raw speaker transcripts / notes
│   └── *.md                            # Synthesized insight summaries
│
├── strategy-repo-template/             # Forkable student template
│   ├── README.md                       # Living strategy dashboard
│   ├── 01-the-bet/
│   ├── 02-the-moat/
│   ├── ...                             # Numbered folders matching modules
│   └── 06-the-pitch/
│
├── meeting-notes/                      # Working session notes (YYYY-MM-DD-*.md)
│
└── .cursor/
    ├── mcp.json                        # MCP server config (e.g. Lenny's data)
    └── rules/
        ├── slide-design-standards.mdc  # Cursor rule for slide HTML
        └── speaker-notes-standards.mdc # Cursor rule for speaker notes
```

### Naming Conventions

| Asset | Pattern | Example |
|-------|---------|---------|
| Slide deck | `Module {N} - Slides.html` | `Module 3 - Slides.html` |
| Speaker notes | `Module {N} - Speaker Notes.md` | `Module 3 - Speaker Notes.md` |
| Interactive tool | `M{N} - {Tool Name}.html` | `M2 - Flywheel Scorer.html` |
| Meeting notes | `YYYY-MM-DD-{topic}.md` | `2025-03-10-working-session.md` |
| Strategy folders | `{NN}-the-{name}/` | `03-the-margin/` |

---

## Workflow: Creating a New Module

### Step 1: Define the module in course-architecture.md

Add a module summary with: title, strategic question, learning objective, key content, case study, build moment, peer challenge, artifact component, and bridge to next module.

### Step 2: Create the HTML slide deck

Create `Modules/Module {N} - Slides.html`. This is a **single self-contained HTML file** — no external dependencies besides Google Fonts. See [slide-template.md](slide-template.md) for the full template and CSS reference.

Key design rules (from `.cursor/rules/slide-design-standards.mdc`):
- **Module 2 is the reference deck.** Match its density and structure.
- Max 3 short lines of body text per concept. No paragraphs on slides.
- Use big numbers, icons, visual spectrums — not text explanations.
- Every concept needs a real company name. No abstract-only slides.
- Every 2-3 slides needs an interaction: poll, pair prompt, quick write.
- Put interaction prompts on-slide in colored boxes, not just in speaker notes.
- Case studies: lead with the big number, 3-act cards (Bet / Crack / Correction).
- Frameworks: tile grids, not row-based checklists.
- Comparisons: gradient bar with companies, not two-column text blocks.
- Fill-in blanks use `JetBrains Mono`, underscore placeholders.

Slide types use colored tags:
- `.tag-provocation` (red) — True/False openers
- `.tag-lecture` (blue) — Core concept slides
- `.tag-case` (yellow) — Case studies
- `.tag-exercise` (green) — Fill-in / build exercises
- `.tag-activity` (purple) — Pair/group activities
- `.tag-build` (pink) — Build moments
- `.tag-break` (grey) — Breaks
- `.tag-recall` (blue) — Recall from previous module
- `.tag-framework` (yellow) — Framework introductions

### Step 3: Write speaker notes

Create `Modules/Module {N} - Speaker Notes.md`. See [speaker-notes-template.md](speaker-notes-template.md) for the format reference.

Key rules (from `.cursor/rules/speaker-notes-standards.mdc`):
- **Module 3 is the reference.** Match its format across all modules.
- Written as a briefing memo for the instructor — like walking them through the plan over coffee.
- Explain the *thinking and intent* behind each slide, not what's on the slide.
- Conversational paragraphs, not bullet-point lists.

Document structure:
```markdown
# Module N — Title
## Speaker Briefing for {Instructor Name}

### What this module is about
[Emotional arc, what students leave with, connection to prior modules]

### The flow and why it's structured this way
[Rationale for slide ordering, where energy shifts happen]

---

### Slide 1 — Title
[1-3 paragraphs: why this slide exists, what should happen in the room,
how it connects to what came before and what follows]

### Slide 2 — ...
```

Per-slide notes cover:
- Why this slide exists at this position
- What should happen in the room
- How it connects to prior and next slides
- For interactive tools: mention naturally ("The interactive tool link is on this slide...")
- For activity slides: pedagogical reasoning, what good/bad answers look like
- For repositioned slides: explain why (e.g. "moved based on feedback from X")

### Step 4: Build interactive tools

Create `Modules/M{N} - {Tool Name}.html`. Each tool is a self-contained HTML file with the same dark theme (`#07162C` background, Poppins/Lato fonts, `#1241B0` accent blue). See [interactive-tools-reference.md](interactive-tools-reference.md) for patterns.

Interactive tools follow these patterns:
- Scorecards: grid of dimensions with score inputs, auto-calculated totals
- Calculators: input fields with live-updating calculations and sliders
- Audits: step-by-step workflows with exportable results
- Builders: multi-panel fill-in layouts that generate structured output
- Checklists: categorized items with Y/N toggles and coverage scoring

All tools:
- Save state to `localStorage` so data persists across sessions
- Use the same visual design system as slides (dark theme, same fonts/colors)
- Are linkable from slides for in-class use
- Export results as markdown or structured text

### Step 5: Update course-status.md

Mark the module status and note what's complete (Speaker Notes, HTML Slides, tools).

---

## Workflow: Collecting & Integrating Insights

### External sources

1. **MCP integration**: Query external knowledge bases (e.g. Lenny Rachitsky's archive via MCP) for relevant content on product management, AI strategy, growth, pricing, etc.
2. **Source slide decks**: Store collaborator `.pptx` files in `insights/` for reference.
3. **Raw transcripts**: Store speaker transcripts as `.txt` in `insights/`.
4. **Curated summaries**: Synthesize insights into markdown files organized by module (like `lenny-insights.md` at the repo root).

### Integration pattern

When integrating insights into modules:
1. Identify which module the insight maps to
2. Find the specific slide or concept it reinforces
3. Add the company/data point to the slide (slides need real company examples)
4. Update speaker notes with context on the source ("Madhavan Ramanujam's work...", "Gokul Rajaram's thread...")
5. Update `course-status.md` to note the integration

---

## Workflow: Pitch Deck via Gamma

For pitch decks or high-level overviews:
1. Write a `Gamma Prompt.md` file with slide-by-slide outline + design notes
2. Format: `## Slide N — Title` followed by content description
3. Include `## Design Notes for Gamma` at the end (theme, fonts, key visual moments)
4. Paste the content into Gamma's "Paste an outline" feature

---

## Workflow: Strategy Repo Template

The `strategy-repo-template/` folder is a forkable scaffold students use across all sessions:

- Numbered folders `01-the-bet/` through `06-the-pitch/` match modules
- `README.md` is the living strategy dashboard linking all components
- Each folder has markdown files for that module's artifact (e.g. `diagnostic.md`, `cost-curve.md`)
- Students fill it in progressively — each module adds to the repo

When creating a new course, scaffold this structure to match your module arc.

---

## Cursor Rules

Two `.mdc` rule files in `.cursor/rules/` enforce consistency:

1. **`slide-design-standards.mdc`** — Applies to `Modules/*Slides*.html`. References Module 2 as the gold standard. Covers text density, visual structure, company examples, interactive moments, build exercises.

2. **`speaker-notes-standards.mdc`** — Applies to `Modules/*Speaker Notes*.md`. References Module 3 as the gold standard. Covers tone (briefing memo), document structure, per-slide format, content rules.

When starting a new course, create equivalent `.mdc` files with your reference module and instructor name.

---

## Course-Level Documents

| File | Purpose | When to update |
|------|---------|----------------|
| `course-architecture.md` | Full arc, design principles, module summaries, competitive positioning | When course structure changes |
| `storyline.md` | Narrative flow, session rhythm, emotional arc | When resequencing modules or adjusting tone |
| `course-status.md` | Module completion status, open decisions, timeline | After every work session |
| `lenny-insights.md` (or similar) | Curated external insights organized by module | When integrating new source material |
| `index.html` | Entry point redirect | Set once to point to pitch deck |

---

## Quick Start: New Course from Scratch

1. Create the repo with the directory structure above
2. Write `course-architecture.md` — define the arc, audience, design principles, module summaries
3. Write `storyline.md` — the narrative thread connecting all modules
4. Create `.cursor/rules/` with slide and speaker notes standards (pick your reference modules)
5. Scaffold `strategy-repo-template/` (or equivalent student artifact)
6. Build Module 1: Slides HTML → Speaker Notes → Interactive tool(s)
7. Create `course-status.md` to track progress
8. Repeat for each module, integrating insights as you go
9. Build the pitch deck via Gamma Prompt when ready to present to stakeholders
10. Configure `.cursor/mcp.json` for any external knowledge base integrations
