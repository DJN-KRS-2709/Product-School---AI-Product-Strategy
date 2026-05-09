# Content Audit — `{Course Name}`

> **How to use:** copy this file to the root of the course repo as `content-audit.md`. The agent fills in every section by reading `insights/extracted/`. The user reviews before any module is built.

---

## Course Identity

| Field | Value |
|-------|-------|
| Course name | |
| Audience (one sentence) | |
| Outcome promise (what they leave with) | |
| Total session count | |
| Duration per session | |
| Instructor name (for speaker notes voice) | |
| Single throughline artifact (the "living strategy" equivalent) | |

---

## Section 1 — Module Arc

The new module structure. Order is sequential — each module depends on the prior one.

| # | Title | Strategic Question | Build Moment | Status |
|---|-------|-------------------|--------------|--------|
| 1 | | | | Not built |
| 2 | | | | Not built |
| 3 | | | | Not built |
| 4 | | | | Not built |
| 5 | | | | Not built |
| 6 | | | | Not built |

**Status values**: `Not built` → `Audit complete` → `Slides drafted` → `Speaker notes drafted` → `Shareable notes drafted` → `Tool added (optional)` → `Built`.

---

## Section 2 — Legacy → New Mapping

Every chunk of legacy material assigned to a target module + target slide. Cite the source by extracted file + section heading.

| Source file | Source section | Content type | Target module | Target slide # | Notes |
|-------------|----------------|-------------|---------------|----------------|-------|
| `extracted/old-deck.md` | Slide 12 — "Why AI Is Different" | Lecture | M1 | Slide 6 | Lead with the comparison table; pull table from `extracted/syllabus.md` Sheet 2 |
| `extracted/outline.md` | "Learning Objectives" | Course-level | — | — | Goes into `course-architecture.md` |
| `extracted/syllabus.md` | Sheet: Exercises | Exercise inventory | Multiple | — | Map each exercise to its module — see Section 4 |
| | | | | | |

**Content type values**: `Lecture` · `Case study` · `Exercise` · `Activity` · `Provocation` · `Recall` · `Build moment` · `Synthesis` · `Course-level` · `Discard`.

If a chunk has no clear target, mark it `Discard` with a one-sentence reason.

---

## Section 3 — Gaps and Adds

What the new format requires that the legacy material is missing. Every gap becomes a slide or section the agent will write from scratch.

| Module | Gap | Why it's needed | What to add | Source for the new content |
|--------|-----|----------------|-------------|---------------------------|
| M1 | No real company examples on the moat slide | Design rule: every concept needs a real company name | Add 3 named companies as 3-card grid | Use Bloomberg, Salesforce, Apple — or pull from `extracted/case-studies.md` |
| M2 | No interactive moments between slides 4 and 9 | Design rule: every 2-3 slides needs an interaction | Add a poll on slide 6 ("which moat is yours?") | Original deck had it as a verbal aside — make it a colored prompt box on-slide |
| | | | | |

**Required additions for every module** (these are non-negotiable design rules — flag the gap even if the legacy material doesn't have them):

- Title slide with 3 waypoints
- Recall slide if it's not Module 1
- At least 2 colored interaction prompts on-slide
- A case study with a single big number (e.g., `$1.5B`)
- A build moment producing a tangible artifact
- Bridge slide to the next module

---

## Section 4 — Exercise & Tool Inventory

Exercises in the legacy material that should become interactive HTML tools in the new format.

| Exercise from legacy | Module | Tool type | Tool file name | Notes |
|---------------------|--------|-----------|----------------|-------|
| "Score your competitive position" worksheet | M2 | Scorecard | `M2 - Positioning Map.html` | Two-axis canvas, draggable dots |
| "Calculate your unit economics" sheet | M3 | Calculator | `M3 - Margin Calculator.html` | Sliders for cost / volume / price |
| | | | | |

**Tool types**: `Scorecard` · `Calculator` · `Audit` · `Builder` · `Checklist` · `Positioning map`. See [interactive-tools-reference.md](interactive-tools-reference.md).

If an exercise is just "discuss in pairs" with no artifact, do NOT make a tool. Use an on-slide prompt box.

---

## Section 5 — Strategy Repo Template Plan

The forkable student artifact, mirroring the module arc.

| Folder | Contents (markdown files) | What students fill in |
|--------|---------------------------|----------------------|
| `01-{name}/` | | |
| `02-{name}/` | | |
| `03-{name}/` | | |
| `04-{name}/` | | |
| `05-{name}/` | | |
| `06-{name}/` | | |

`README.md` at the repo root is the living dashboard — see [course-scaffold-templates.md](course-scaffold-templates.md) for the format.

---

## Section 6 — Open Questions for the Instructor

Things that surfaced during the audit that need a human decision before any HTML is generated.

| Question | Options | Decision |
|----------|---------|----------|
| | | |
| | | |

Common questions:

- "The legacy course is 8 sessions. Should we keep 8 or compress to 6?"
- "There are two case studies for the same point. Which one stays?"
- "The original speaker notes are 3,000 words per module. Briefing memos are ~2,000. What gets cut?"
- "There's no build moment in Module 4 of the original. What should it be?"

---

## Sign-off

Once the user reviews and approves Sections 1–4, the agent can begin Step 4 of the workflow (build per module). Sections 5–6 can be finalized during Step 5.

| Reviewed by | Date | Notes |
|-------------|------|-------|
| | | |
