# Module 1 Frameworks Reference Card

*The frameworks introduced in Module 1 - The Bet. For the full course-wide reference (every module's frameworks in one place), see [`Frameworks Reference Card.md`](./Frameworks%20Reference%20Card.md). For term definitions, see [`Module 1 - Glossary.md`](./Module%201%20-%20Glossary.md).*

Each framework gets: what it answers, the structure, and one anchor example.

---

## Three-Axis Diagnostic

**What it answers:** Where is your product most vulnerable?
**How to use it:** Score each axis 1-5 (1 = pain, 5 = strong). If everything is a 5, you haven't looked hard enough.

| Axis | What it measures | Calibration |
|---|---|---|
| **Contextual Moat** | Workflow depth × switching cost | Figma = 5, ChatGPT wrapper = 1 |
| **Data Advantage** | Proprietary signal that *compounds* with usage | Slack = 4, generic chatbot = 1 |
| **Platform Exposure** | What if OpenAI / Google / Apple ships your wedge as a free native feature tomorrow? | Standalone scheduler = 1 (very exposed), deeply embedded enterprise tool = 4 |

**Anchor example:** Linear scores Moat 2-3, Data 2, Platform Risk 4 - issue trackers are easy to switch and GitHub/Notion are absorbing project management natively.
**Lives in:** `01-the-bet/diagnostic.md`.

---

## Five AI Value Archetypes

**What it answers:** What kind of AI product are you actually building?
**How to use it:** Most products blend two or three. Identify which archetype's economics and trust profile *dominates* yours - that's what shapes your pricing (M3) and eval design (M4).

| Archetype | Does | Margin profile | Governance | Example |
|---|---|---|---|---|
| **Automator** | Replaces tasks | Volume play, cost pressure | High if errors hurt | UiPath |
| **Copilot** | Augments people | Scales with seats | Human-in-loop | GitHub Copilot |
| **Oracle** | Surfaces hidden signals | Premium pricing | High - drives calls | Palantir |
| **Creator** | Makes new assets | Copycats fast | Low unless regulated | Midjourney |
| **Orchestrator** | Chains agents/tools | High value, infra spend | Autonomy risk | Zapier AI |
