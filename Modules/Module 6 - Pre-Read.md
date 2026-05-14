# Module 6 - The Pitch (Pre-Read)

*Twenty minutes of reading, one short noticing exercise, and a baseline you'll re-read out loud at the end of class. Done before the session, this is the difference between standing up to present and standing up to **deliver**. Especially worth doing if you're already a little nervous about the board simulation — most of that nervous energy is fuel once the frameworks are pre-loaded.*

---

## 1. Why this session matters

Five sessions of building. One session of assembling. M6 is the capstone — the part where the bet, the moat, the margin, the contract, and the guardrails stop being separate worksheets and become one *story you say out loud*. To a room. With Q&A. From your repo, with no slide deck.

If that sentence made you flinch a little, good. That flinch is half of what we're working with today.

The emotional arc of the session is performance anxiety turning into confidence. Most of you are walking in thinking the simulation is the scary part. By the time we get there, you'll have your README polished by the Strategy Assembler, your strategy stress-tested by the AI Evaluator, your roadmap committed via the Roadmap Builder, and your pitch drafted in the Pitch Builder. The nerves turn into confidence the moment you realize you've already done the hard work — for five sessions.

You'll leave with **four artifacts**:

- A finalized **living strategy repo** with all five component folders plus a board-ready README.
- A multi-horizon **roadmap** committed to `06-the-pitch/roadmap.md` — H1 Ship, H2 Validate, H3 Explore, with kill criteria for the H2 bets.
- A board-ready **pitch** drafted to a specific audience and saved to the same file.
- A **before/after** comparison of your M1 baseline against your M6 answer. That last one is genuinely the part most students take home and remember.

One ground rule for the simulation: **the repo is the artifact**. No Google Slides. No deck. You present from the repo. The whole arc of this course was "stop putting strategy in slides" — M6 is where we live that.

---

## 2. The one idea to walk in already chewing on

> **A roadmap is not a strategy.**

This is the central reframe of the whole module, and it's the one most PMs have never quite said out loud. Look at what you actually present in your quarterly reviews. Features. Timelines. Resources. That's a *delivery plan*. A strategy explains why those decisions and not others. *Why this bet. Why now. Why us.*

A roadmap without a thesis is a to-do list with deadlines on it.

The model to copy is Stripe. Stripe doesn't start with epics. They write the strategy document first — public memos, principles, named bets — then derive the roadmap from it. Epics follow strategy, not the other way around. Once you separate the two cleanly, you can't unsee it. And the next time someone asks "what's the strategy?" and hands you a Gantt chart, you'll know what's missing.

Sit with that for a minute. The whole module hinges on it.

---

## 3. A 20-minute "noticing" exercise to do before class

Pick **three companies** that have publicly pitched an AI product in the last 18 months. For each one, find one piece of their actual external communication — a launch blog, an investor letter, a keynote clip, a product page, a podcast — and read or watch it with one question in mind: *did they lead with the thesis or with the tech?*

The pattern you're looking for is binary. Either the opening sentence is about *what changes for the user / market / business* (thesis-first), or it's about *which model is in the loop* (tech-first). Both pitches can use GPT-4. Only one of them survives the board.

| Pitch | What to watch for |
|---|---|
| **Stripe** (annual letter, Sessions keynote) | The thesis-first canonical. "More economic activity moves online" → developers are the wedge → products follow. Look at the opening 90 seconds of any Sessions keynote — it's the move you're stealing on Monday. |
| **Notion AI** (product page + early launch posts) | A wedge bet positioned as workflow, not as a model. "AI inside the workspace you already trust" — distribution as moat, not capability as moat. |
| **Duolingo + GPT-4** (early 2023 press, then late 2023 / 2024 retro) | A *tech-first* opening that the market punished, followed by a reframe toward learning outcomes. Both versions of the pitch exist publicly — read them in order. The delta is the lesson. |
| **Klarna AI assistant** (post-launch comms) | Mixed — the deflection metric ("equivalent to 700 FTEs") was the right thesis but they led with it as a cost story. Investors heard "margin," some users heard "layoffs." Notice how a *true* metric can still misframe the bet. |
| **Shopify Sidekick** (launch + Tobi's commentary) | A clean three-horizon narrative if you read it that way. H1 commerce stack, H2 Sidekick, H3 platform ambition. One company, three time horizons, three different vocabularies. |
| **Anthropic** (Claude system cards + model launches) | Notice how the *governance pack* (constitutional AI, safety levels) is sold as product surface, not back-office. M5 idea, M6 execution. |

Twenty minutes total. No notes required. The goal is to walk into M6 with **felt examples** of thesis-first pitches and **felt counter-examples** of tech-first pitches. When the slide goes up that says "lead with the thesis, not the model," you'll have a library to draw from.

If you have ten extra minutes, do one more thing: pick **one tech-first opening** from the list above (Duolingo's first 2023 pitch is the easiest) and **rewrite the first sentence user-first** in your own words. That tiny exercise is most of what we'll be drilling in the simulation.

---

## 4. Vocabulary you'll keep hearing

Full definitions go in the cumulative [`Glossary.md`](./Glossary.md) after the session. One-liner each here so the words don't trip you up in the room.

- **Living strategy** — strategy as a version-controlled artifact instead of a slide deck. Lives in your repo, updates monthly, gets sharper with every commit.
- **Three Horizons (AI-compressed)** — McKinsey's classic, but on AI-native timeframes. **H1 Ship** (0–4 weeks, high confidence, execute). **H2 Validate** (1–3 months, medium confidence, named kill criteria). **H3 Explore** (3–6 months, low confidence, small investment). Traditional roadmaps run quarterly; AI roadmaps run monthly.
- **Kill criteria** — Stripe-style "if we don't see X by week 6, we stop." Every H2 bet needs one. Kills are what separates a strategy from a hope.
- **Thesis-first pitch** — opens with the world change, the user problem, or the bet — *not* the model in the loop. The opposite is the tech-first pitch (the one the board doesn't fund).
- **The Case / The Model / The Risks** — the three buckets a board mentally sorts your pitch into. *The Case* = Bet + Moat (why invest, why can't this be copied). *The Model* = Margin (does the math hold). *The Risks* = Contract + Guardrails (trust, failure modes, scale). Don't open with the model — open with the case.
- **Hallucination rate** — % of outputs containing fabricated facts. Good: <1%. Bad: >5%. Liability signal.
- **Drift velocity** — rate at which model accuracy degrades week-over-week without intervention. Good: <0.5%/week. Bad: >2% (your model is rotting silently).
- **Confidence distribution** — the histogram of model confidence across production outputs. Healthy products are bimodal: confident, or punting to a human. A fat middle is a warning sign.
- **HITL rate** — % of outputs requiring human review. Trending down = scaling well. Flat or up at scale = a unit-economics problem.
- **Inference ROI** — revenue per dollar of inference cost. Good: >10x. Bad: <3x.
- **Eval regression** — % of model updates that hold quality on the golden dataset pre-deploy. Caught in eval = safe. Caught in production = customer complaint.
- **Audience archetype** — the persona the Pitch Builder reweights for: CEO + leadership, founders / funding committee, external board / investors, CTO + Head of Product. Plus *custom* — the actual specific person whose "yes" you need on Monday.
- **The repo is the artifact** — the operating principle for the simulation and the rest of your career. If your strategy only lives in a deck, it's theater. If it lives in a repo, it's a system.

---

## 5. A real story we'll dig into

> **Teaser — no spoilers.** A 500M-user learning company partnered with a frontier model lab for an in-product capability that genuinely worked. The launch was loud. Within a quarter, the market shifted the question from *"is the feature cool?"* to *"does the AI actually improve learning outcomes?"* Investor reactions were, charitably, *mixed*. The stock took a hit.
>
> The fix wasn't a model change. It was a *narrative* change.

We'll walk through what happened, what they changed in their investor decks the next quarter, and the exact reframe that landed. The lesson is the same one most PMs need to internalize before they pitch any AI feature: *the technology becomes invisible, the user impact becomes the headline*. Lead with the outcome. The model is plumbing.

This is also the same muscle as board Q&A under scrutiny. Narrative repair is a skill, not a talent — and the room is where you practice it.

---

## 6. Two questions to come ready to answer

These become warmups in the session. Showing up with honest answers — even imperfect ones — pays off massively in the room.

### Question 1 — Who specifically do you need a "yes" from on Monday?

Not *the board*. *The board* is not a person. Be specific. A specific person whose decision changes whether your bet ships. Your CEO. Your CFO who's been worried about AI cost. The VP of Product who keeps pushing back on your roadmap. The investor whose follow-on you need next quarter. Whoever it is. **Name them.**

Why this matters: the Pitch Builder tool we'll use in class reweights the prompt by audience. A board pitch leads with TAM. A CTO pitch leads with the reliability contract. Founders care about why-now. CFOs care about the unit economics under stress. The frameworks are the same — the *opening sentence* is not. If you walk in with "the board" as your answer, the AI gives you a generic pitch. If you walk in with "Priya, our CFO, who has flagged inference cost as a 2026 budget risk," the AI gives you a pitch she will actually fund.

Write one name. One sentence on what they care about most. One sentence on what they're skeptical of. Three sentences total.

### Question 2 — Re-read your M1 three-sentence answer right now.

Open `01-the-bet/diagnostic.md`. Find the place you wrote your original three-sentence answer to *"What's our AI strategy?"* — the one you wrote in three minutes, before you had any frameworks.

Read it out loud. Don't edit it. Don't cringe (or do, but don't act on it). Just notice the gap between what's there and what you'd say now.

You'll re-do this exercise at the end of M6, with everything you've learned. The *delta* between the two answers is the entire course. We use the M1 baseline as the receipt. You'll be glad you re-read it cold before the session — the surprise lands harder that way.

---

## 7. What to bring

- All five prior artifacts committed and pushed: `01-the-bet/`, `02-the-moat/`, `03-the-margin/`, `04-the-contract/`, `05-the-guardrails/`. **Pushed to GitHub** is best — the AI tools we use today read directly from your repo URL. If your repo is private (or you haven't pushed yet), the same tools accept file uploads, so bring the markdown files on your laptop as a backup.
- A real **backlog export** you can use after class. A CSV from Jira / Linear / Notion / a spreadsheet — anything 8–15 rows of your actual work, last 6 months. The Roadmap Builder runs on real backlogs. The class demo uses a sample sheet, but the *value* of the tool is when you point it at your own work. Bring the export and you'll leave with a roadmap you can commit Monday morning.
- A **specific person** whose "yes" you need on Monday (from Question 1 above), with one sentence on what they care about most.
- The **M1 baseline** open in another tab. We'll need it for the M1-vs-Now reflection at the end.
- The willingness to **stand up and pitch out loud.** Two or three of you will present to the room as a board simulation. No slides. Five minutes plus three of Q&A. The format is hard and that is the point — if your pitch survives the room, it survives the actual board.

---

*See you in the room.*
