# Course Scaffold Templates

The four course-level documents and the strategy-repo-template structure. Use these in Step 5 of the workflow to finalize the course.

References from the AI Product Strategy course:

- `course-architecture.md` — full arc, principles, audience, positioning
- `storyline.md` — narrative thread connecting all modules
- `course-status.md` — module completion tracker
- `strategy-repo-template/README.md` — living dashboard for student forks

---

## 1. course-architecture.md

```markdown
# {Course Name} — Course Architecture

**{Provider} | {N} sessions x {Hours} hours | {Audience}**

---

## Positioning

[1-2 paragraphs explaining who this course is for and why it exists. Compare to adjacent courses or programs. Name the gap this course fills.]

---

## Target Audience

[Who is in the room. What they already know. What they DON'T need taught. The product or context they bring.]

**This is not a {what it isn't} course.** Participants {what they actually do — bring a real product, etc.}.

---

## The Arc: {N} Strategic Questions

Each module answers one question {your stakeholder} actually asks. The arc is sequential — each answer depends on the last.

| Module | Title | Strategic Question |
|--------|-------|-------------------|
| M1 | **{Title}** | {Question} |
| M2 | **{Title}** | {Question} |
| M3 | **{Title}** | {Question} |
| ... | | |

### Why {course topic} is different (explicit — name it in M1, reinforce every module)

[The thesis table. List the assumptions traditional thinking holds, and what your domain actually does. Each row should map to one of the modules ahead.]

| Traditional | {Course Topic} |
|------------|-----|
| {Assumption 1} | {Reality 1} |
| {Assumption 2} | {Reality 2} |
| ... | |

---

## The Throughline Artifact: {The Living Thing}

[1-2 paragraphs describing the single artifact students build across all sessions. Why it's better than a slide deck or a written deliverable. How it compounds across modules.]

| Session | Component | What It Contains | Visual Artifact |
|---------|-----------|------------------|-----------------|
| M1 | **{Component}** | {Contents} | {Visual} |
| M2 | **{Component}** | {Contents} | {Visual} |
| ... | | | |

**M{Last} = Integration.** [How the final module ties everything together.]

---

## {N} Design Principles

[Numbered list of the principles that govern every design decision in the course. Each principle gets 1-2 sentences. These are non-negotiable.]

### 1. {Principle name}

[Explanation.]

### 2. {Principle name}

[Explanation.]

...

---

## Module Summaries

### Module 1 — {Title}

- **Strategic question:** {Question}
- **Learning objective:** {What they leave able to do}
- **Key content:** {Frameworks, concepts}
- **Case study:** {Company + the moment}
- **Build moment:** {What they make in the session}
- **Peer challenge:** {The interaction with another participant}
- **Artifact component:** {What goes into the strategy repo}
- **Bridge to next module:** {The handoff sentence}

### Module 2 — {Title}

[Same structure for each module.]

...
```

---

## 2. storyline.md

```markdown
# {Course Name} — The Storyline

## The One-Sentence Promise

[The promise the course makes. What the participant leaves with. Concrete, not aspirational.]

---

## The Setup: Why This Course Exists

[1-2 paragraphs on the audience's pain point. The thing they can't currently do that this course solves. Should make a reader nod by the second sentence.]

### Why {course topic} is different from {adjacent topic}

[The reframe table. Same as in course-architecture.md but here you can expand on the implications.]

### {N} course-level principles

1. **{Principle headline}** — {one sentence explanation}.
2. **{Principle headline}** — {one sentence explanation}.
...

### Why this course over alternatives

[1-2 paragraphs explaining what makes this course different from the alternatives. Name them. Be specific about the gap.]

---

## The Module-by-Module Narrative

### Module 1 — {Title}

[2-3 paragraphs telling the story of this module. The emotional arc (curiosity → tension → reframe → resolution). The pivotal moment. The takeaway sentence.]

### Module 2 — {Title}

[Same structure for each module.]

...

---

## The Session Rhythm

[How a typical session is structured. The recurring beats. Where the energy shifts happen.]

| Beat | Duration | What happens |
|------|----------|-------------|
| Open | {X} min | {Recall or provocation} |
| Lecture 1 | {X} min | {Core concept} |
| Case study | {X} min | {Company example} |
| Break | {X} min | |
| Build | {X} min | {Hands-on artifact creation} |
| Peer review | {X} min | {Pair or group exchange} |
| Synthesis | {X} min | {Bridge to next module} |

---

## Action Plan

[The concrete delivery plan: when each module gets built, who reviews it, when the dry run happens, when the course goes live.]
```

---

## 3. course-status.md

```markdown
# {Course Name} — Course Status

**Last updated:** {Date}

---

## Standing Design Principles

These were established in the {date} working session with {stakeholder} and are non-negotiable unless revisited.

1. **{Principle}.** {Explanation in 1 sentence.}
2. **{Principle}.** {Explanation in 1 sentence.}
...

---

## Module Status

| Module | Title | Status | Notes |
|--------|-------|--------|-------|
| M1 | {Title} | Not started | |
| M2 | {Title} | Not started | |
| M3 | {Title} | Not started | |
| M4 | {Title} | Not started | |
| M5 | {Title} | Not started | |
| M6 | {Title} | Not started | |

**Status values**: `Not started` → `Audit complete` → `Slides drafted` → `Speaker notes drafted` → `Shareable notes drafted` → `Tool added` → `Draft complete` → `Reviewed` → `Live`.

---

## Open Decisions

| Decision | Options | Status |
|----------|---------|--------|
| {Question} | {A vs B vs C} | {Proposed / Awaiting / Resolved} |
| | | |

---

## Key Documents

| Document | Location | Purpose |
|----------|----------|---------|
| Course Architecture | `course-architecture.md` | Full arc, principles, audience |
| Storyline | `storyline.md` | Narrative thread, session rhythm |
| Content Audit | `content-audit.md` | Legacy → new mapping |
| M1–M{N} Speaker Notes | `Modules/Module N - Speaker Notes.md` | Per-slide instructor briefing |
| M1–M{N} HTML Slides | `Modules/Module N - Slides.html` | Standalone scrollable decks |
| M1–M{N} Shareable Notes | `Modules/Module N - Notes (Shareable).md` | Reader-facing companion |
| Strategy Repo Template | `strategy-repo-template/` | Forkable student artifact |
| Original sources | `insights/` | Read-only legacy material |

---

## Timeline

| Milestone | Target date | Owner | Status |
|-----------|------------|-------|--------|
| Audit complete | | | |
| M1 draft | | | |
| Dry run | | | |
| Course live | | | |
```

---

## 4. strategy-repo-template/README.md

```markdown
# My {Course Domain} Strategy

> A living strategy built across {N} sessions. Each module adds one component. By Module {N}, this repo IS your strategy — version-controlled, board-ready, portable.

---

## Strategy at a Glance

| Component | Module | Status | Key Artifact |
|-----------|--------|--------|-------------|
| **{Component 1}** | M1 | [ ] | `01-{name}/` |
| **{Component 2}** | M2 | [ ] | `02-{name}/` |
| **{Component 3}** | M3 | [ ] | `03-{name}/` |
| **{Component 4}** | M4 | [ ] | `04-{name}/` |
| **{Component 5}** | M5 | [ ] | `05-{name}/` |
| **{Component 6}** | M6 | [ ] | `06-{name}/` |

---

## {Component 1} (M1)

**{One-line description of what this component answers.}**

- **{Field 1}:**
- **{Field 2}:**
- **{Field 3}:**
- **{Score field}:** __/5
- **Confidence:** H / M / L

→ Details: [`01-{name}/`](01-{name}/)

---

[Repeat the same `## {Component} (M{N})` block for each module. Each component gets 4-7 short fields the student fills in. Keep each block to half a screen.]

...
```

---

## 5. Strategy repo folder contents

Each `0N-{name}/` folder contains 1-3 markdown files matching the artifacts that module produces. Examples from the AI Product Strategy course:

```
strategy-repo-template/
├── 01-the-bet/
│   ├── diagnostic.md          # Vulnerability scorecard fill-in
│   └── prototype.md           # Prototype documentation template
├── 02-the-moat/
│   ├── data-flywheel.md       # Flywheel scoring template
│   └── kill-switch.md         # Vendor portability checklist
├── 03-the-margin/
│   └── cost-curve.md
├── ...
```

Each markdown file is a fill-in template — heading skeleton with placeholders. Students replace placeholders with their answers. The agent generates one file per `target slide` in the audit that produces a take-home artifact.

---

## How the agent uses these templates

In Step 5 of the workflow:

1. Read the audit's **Course Identity** section. Substitute `{Course Name}`, `{Audience}`, `{N}` everywhere.
2. Read the audit's **Module Arc** section. Substitute the module titles and strategic questions everywhere.
3. Read the audit's **Strategy Repo Template Plan**. Generate one folder per module with the listed markdown files.
4. Use the actual content from the speaker notes you wrote in Step 4 to fill in `course-architecture.md` Module Summaries (don't re-invent — reference what you already produced).
5. Save all four documents at the course repo root. Save the strategy template at `strategy-repo-template/`.
