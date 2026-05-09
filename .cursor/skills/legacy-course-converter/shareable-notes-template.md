# Shareable Notes Template

The shareable notes are a **reader-facing companion** to the slide deck — the document a participant takes home after a session, or shares with a colleague who couldn't attend. They walk through the same slide arc as the speaker notes but in a third-person, reader-oriented voice.

## Output Format: HTML (default)

Anything sent directly to a student is delivered as **polished, self-contained HTML** using the shareable design system, **not markdown**. Save as `Modules/Module {N} - Notes (Shareable).html`.

- **Design system + component patterns**: see `.cursor/rules/shareable-student-docs-standards.mdc`.
- **Gold-standard reference file**: `Modules/Module 4 - Pre-Read (Shareable).html`. Copy its structure (hero → progress bar → chapter sections with `section-label` + `h2` → component blocks → footer) and swap in the per-slide content.
- **Module accent color** comes from the rule (M1 blue, M2 green, M3 gold, M4 purple, M5 red, M6 teal). Apply it to the hero radial gradient, pull-quote borders, vocab card hover states, and `<code>` background.

The legacy markdown form below is kept only as a **content scaffold** — it shows what to write. The actual deliverable is HTML rendered with the shareable design system.

---

## Content Scaffold (use as the source for the HTML)

The structure below is the *what to write*. Render the final document as HTML matching `Module 4 - Pre-Read (Shareable).html`. Each markdown section maps to a `<section class="chapter">` with a `section-label` + `h2` + appropriate component block. Tables become `.notice-table`, comparisons become `.compare` cards, named-concept callouts become pull-quotes, "what you take home" becomes a `bring-list`, etc.

```markdown
# Module N — Title

*Shareable companion notes. These walk you back through what each slide covered, in case you want to review the arguments, examples, and frameworks at your own pace.*

---

## What this module is about

[1-2 paragraph overview. Third person, reader-facing. Cover:]

- The thesis of the module
- The traditional assumption it challenges
- What students leave with (the artifact, the framework, the reframe)
- How this module fits in the course arc

Bold the key concepts (e.g. **probabilistic thinking**, **living strategy repo**) so a skim-reader catches them.

---

### Slide 1 — Title

[1 short paragraph: the strategic question the module answers, the three waypoints, the deliverable. Reads like the back-cover blurb of the session.]

### Slide 4 — Course Arc

[If the course has an explicit arc slide, summarize the full arc here as a bullet list:]

- **M1 — The Bet:** Where does strategy break?
- **M2 — The Moat:** Can anyone copy you?
- ...

### Slide 6 — {Concept Name}

[For lecture slides: explain the concept in 1-2 short paragraphs. Use:]

- Tables for comparisons (Traditional vs. AI, before vs. after, etc.)
- Bold for the named framework or concept
- Italic for the source attribution ("from Madhavan Ramanujam's Monetizing Innovation")
- Real company names as evidence (Bloomberg, Salesforce, Apple — not "a major SaaS company")

[For case study slides: tell the story in 2-3 paragraphs. Lead with the big number. Name the company, the bet, the crack, the correction or the fall.]

[For exercise slides: describe what the exercise asked the participant to do, what good answers looked like, and what insight the exercise was designed to surface. Do NOT include the speaker's coaching prompts — those live in Speaker Notes.]

[For provocations: state the claim and the answer (True / False) with a one-line proof point.]

### Slide N — {Slide Title}

[Continue for every substantive slide. Skip purely transitional slides like Agenda or Recall when they don't carry standalone meaning.]

---

## What you take home

- [Artifact 1 — the file or scorecard or map they built]
- [Artifact 2 — the framework or mental model they now own]
- [Artifact 3 — the question they can now answer about their product]

---

## Going deeper

- [Source 1 — book, post, or talk referenced in the module]
- [Source 2 — companion tool or template]
- [Source 3 — relevant module to revisit]
```

---

## Tone Rules

| Do | Don't |
|----|-------|
| Third person, reader-facing ("By the end of the session, students have...") | Second person to the instructor ("you should...") |
| Concise paragraphs that summarize the argument | Verbatim transcripts of what was said in the room |
| Bold the named frameworks and concepts | Bullet-list everything |
| Tables for any comparison the slides showed | Long prose where a table would do |
| Real company names | Generic placeholders ("a tech giant") |
| Italicize source attributions | Cite without context |
| Skip purely transitional slides | Force a section per slide |

---

## What's different from Speaker Notes

| Speaker Notes (`Module N - Speaker Notes.md`, markdown) | Shareable Notes (`Module N - Notes (Shareable).html`, HTML) |
|---|---|
| Internal — briefing memo for the instructor | External — reader companion for the participant |
| Markdown, plain | HTML with shareable design system |
| Second person to the instructor | Third person, neutral voice |
| Explains intent: "why this slide exists" | Explains content: "what the slide argued" |
| Conversational, like coffee chat | Edited, like a magazine article |
| Includes coaching prompts | Includes the framework, not the coaching |
| One section per slide, no skipping | Skip transitional slides; merge consecutive ones |
| ~2,000 words per module | ~1,500 words per module |

The two files cover the same arc but serve different readers. Generate them from the same audit row in Step 4.

---

## Content Checklist (HTML deliverable)

- [ ] Saved as `Modules/Module {N} - Notes (Shareable).html`
- [ ] Hero block with module tag, title (`em` on the named concept in module accent), and italic lede
- [ ] Reading-progress bar at top of page
- [ ] Each substantive slide has a `<section class="chapter">` with `section-label` + `h2`
- [ ] Transitional slides (agenda, recall, breaks) are skipped or merged
- [ ] Module accent color applied correctly (see `shareable-student-docs-standards.mdc`)
- [ ] Comparisons use `.compare` cards or `.notice-table`, not paragraphs
- [ ] Named-concept callouts use `.pull-quote`
- [ ] "What you take home" rendered as a `bring-list` with arrow markers
- [ ] Real company names match the slides
- [ ] Footer with module name and short closing message
- [ ] Tested by opening directly in a browser (no broken assets, fonts load)
