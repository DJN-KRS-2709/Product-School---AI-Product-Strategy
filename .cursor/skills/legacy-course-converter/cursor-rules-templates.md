# Agent Guidance Templates

Persistent guidance the agent reads on every edit in the new course repo, so the slide design + speaker notes standards stay enforced even when this skill isn't actively running.

Two delivery formats depending on which agent you use:

- *Claude Code*: paste the rule contents into a single `AGENTS.md` file at the repo root.
- *Cursor*: save each rule as a separate `.mdc` file in `.cursor/rules/`.

In Step 5 of the workflow, fill in the template for the agent the user is on. Replace `{Reference Module}` and `{Instructor Name}` with the values from the new course's content audit.

## For Claude Code: `AGENTS.md`

Single file at the repo root. Combine all three rule blocks below under one `## Slide design standards`, `## Speaker notes standards`, `## Shareable notes standards` heading structure. The Claude Code agent automatically reads `AGENTS.md` on every session.

## For Cursor: `.cursor/rules/*.mdc`

One `.mdc` file per rule, in `.cursor/rules/`. Use the YAML frontmatter exactly as shown — it tells Cursor when to apply each rule (the `globs` field).

---

## 1. `.cursor/rules/slide-design-standards.mdc`

```markdown
---
description: Slide deck design standards for HTML presentation modules
globs: Modules/*Slides*.html
alwaysApply: false
---

# Slide Design Standards

{Reference Module — e.g. "Module 2"} is the reference deck. Match its density and structure across all modules.

## Text Density
- Lecture slides: max 3 short lines of body text per concept. No paragraphs.
- Subtitles: 1 short line, never 2-3.
- If you can't scan a slide in 5 seconds, it has too much text.

## Visual Structure
- Use big numbers, icons, and visual spectrums instead of text explanations.
- Case studies: lead with the big number (e.g. "$1.5B"), one-line context below. Three cards side by side (Bet / Crack / Fall). No paragraph descriptions.
- Frameworks: use tile grids (Y/N boxes, score boxes) not row-based checklists.
- Comparisons: use a visual spectrum (gradient bar with labeled endpoints) and named companies along it — not two-column text blocks.
- Flywheels: circular layout with a center symbol, not sequential vertical lists.

## Company Examples
- Every concept needs a real company name. No abstract-only slides.
- Use the company as the proof, not the explanation. "Bloomberg" next to "Data" > a paragraph about data moats.

## Interactive Moments
- Every 2-3 slides needs an interaction: poll, show-of-hands, pair prompt, point-to-answer, or quick write.
- Put the prompt on-slide (in a colored box), not just in speaker notes.

## Build Moments / Exercises
- Use card-based layouts with labeled panels (e.g. "1. What's your setup?" / "2. Stress test" / "3. Three actions").
- Fill-in blanks use JetBrains Mono font, underscore placeholders.
- Avoid long vertical checklists with dots — use horizontal tile grids instead.

## Reference Slides
- Slide N (case study): big-number cards, minimal text
- Slide N (depth spectrum): gradient bar with company examples
- Slide N (framework grid): one company per cell
- Slide N (build exercise): three-panel card layout
```

---

## 2. `.cursor/rules/speaker-notes-standards.mdc`

```markdown
---
description: Speaker notes standards for module briefings
globs: Modules/*Speaker Notes*.md
alwaysApply: false
---

# Speaker Notes Standards

{Reference Module — e.g. "Module 3"} Speaker Notes is the reference. Match this format across all modules.

## Tone
- Briefing memo for {Instructor Name} — like walking them through the plan over coffee
- Explain the thinking and intent behind each slide, not what's on the slide (they can see that themselves)
- Written as "here's why this slide exists and what you should accomplish with it"
- Conversational paragraphs, not bullet-point lists

## Document Structure
- Open with `# Module N — Title` and `## Speaker Briefing for {Instructor Name}`
- Preamble section `### What this module is about` — emotional arc, what students leave with, how it connects to prior modules
- Preamble section `### The flow and why it's structured this way` — rationale for the slide ordering, where the energy shifts happen
- Horizontal rule (`---`) before slide-by-slide notes

## Structure Per Slide
- `### Slide N — Title` as H3 heading
- 1-3 paragraphs covering: why this slide exists here, what should happen in the room, how it connects to what came before and what follows
- If a slide has an interactive tool, mention it naturally: "The interactive tool link is on this slide — students can open the [Tool Name]..."
- If a slide was repositioned based on feedback, explain why (e.g. "We moved this here based on {Reviewer}'s feedback")

## Content Rules
- Name real companies as examples, matching the slide
- Reference source material where relevant (e.g. "Madhavan Ramanujam's work")
- Spell out acronyms on first use (ToS = Terms of Service, HITL = Human-in-the-Loop)
- If a slide has a fill-in exercise, note what "good" vs "bad" answers look like so {Instructor Name} can coach
- For activity slides, explain the pedagogical reasoning: why it's standalone, what the follow-up question should surface
```

---

## 3. (Optional) `.cursor/rules/shareable-notes-standards.mdc`

If the course distributes shareable notes to participants, add this third rule:

```markdown
---
description: Shareable companion notes standards
globs: Modules/*Notes (Shareable)*.md
alwaysApply: false
---

# Shareable Notes Standards

{Reference Module — e.g. "Module 1"} Shareable Notes is the reference. Match this format across all modules.

## Tone
- Reader-facing companion, not instructor briefing
- Third person, neutral voice ("By the end of the session, students have...")
- Edited, magazine-article quality — not transcript

## Document Structure
- Open with `# Module N — Title` and the italicized companion blurb
- `## What this module is about` summary (1-2 paragraphs)
- Horizontal rule (`---`) before slide-by-slide notes
- Skip transitional slides (Agenda, Recall, Breaks)
- Close with `## What you take home` and `## Going deeper`

## Per Slide
- `### Slide N — Title` as H3 heading
- 1-2 short paragraphs summarizing the slide's argument
- Tables for any comparison the slides showed
- Bold the named frameworks and concepts
- Italicize source attributions
- Real company names — never generic placeholders
```

---

## How the agent uses these templates

In Step 5 of the workflow:

1. Detect which agent is running. If you see `.claude/skills/legacy-course-converter/` in the path, the user is on Claude Code → produce `AGENTS.md`. If you see `.cursor/skills/...`, the user is on Cursor → produce `.mdc` files. If unclear, ask the user.
2. Read the **Course Identity** section of `content-audit.md` to find `{Instructor Name}`.
3. Read the **Module Arc** section to choose `{Reference Module}` for slides (typically Module 2 by the time it's built) and for speaker notes (typically Module 3).
4. Until the new course has its own gold-standard modules, point at the AI Product Strategy course modules as the reference: `Module 2` for slides, `Module 3` for speaker notes, `Module 1` for shareable notes.
5. *For Claude Code*: write a single `AGENTS.md` at the repo root combining all three rule contents under three `##` sections. Drop the YAML frontmatter and the `globs:` lines — Claude Code doesn't use them.
6. *For Cursor*: create `.cursor/rules/` if it doesn't exist, then write each `.mdc` file separately with its frontmatter intact.
