# Frameworks Reference Card

*A compact, print-friendly consolidation of every framework introduced through Module 3. Keep it open while you do the labs. Each framework gets: what it answers, the structure, and one anchor example.*

For full term definitions, see [`Glossary.md`](./Glossary.md). For the narrative behind any of these, see the corresponding `Module N - Notes (Shareable).md`.

---

## Module 1 - The Bet

### Three-Axis Diagnostic

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

### Five AI Value Archetypes

**What it answers:** What kind of AI product are you actually building?
**How to use it:** Most products blend two or three. Identify which archetype's economics and trust profile *dominates* yours - that's what shapes your pricing (M3) and eval design (M4).

| Archetype | Does | Margin profile | Governance | Example |
|---|---|---|---|---|
| **Automator** | Replaces tasks | Volume play, cost pressure | High if errors hurt | UiPath |
| **Copilot** | Augments people | Scales with seats | Human-in-loop | GitHub Copilot |
| **Oracle** | Surfaces hidden signals | Premium pricing | High - drives calls | Palantir |
| **Creator** | Makes new assets | Copycats fast | Low unless regulated | Midjourney |
| **Orchestrator** | Chains agents/tools | High value, infra spend | Autonomy risk | Zapier AI |

---

## Module 2 - The Moat

### The 8 Moats

**What it answers:** Why won't this get copied in 6 months?
**How to use it:** Don't try to claim all eight. Identify the one or two that are actually real for your product. For AI, **Data** and **Workflow** are the two that hold up most often.

| Moat | What makes it hard to copy | Example |
|---|---|---|
| **Data** | Proprietary data that compounds with usage | Bloomberg |
| **Workflow** | Deep process embedding and switching cost | Salesforce |
| **Regulatory** | Compliance, certifications, approvals | Palantir |
| **Distribution** | Owned channels and default access | Apple |
| **Ecosystem** | Third-party integrations and interdependence | Shopify |
| **Network** | Each new user makes the product more valuable | LinkedIn |
| **Physical** | Hardware, infrastructure, real-world assets | Tesla |
| **Scale** | Cost advantage from volume | AWS |

---

### Workflow Depth Spectrum

**What it answers:** How hard would it be for your users to switch?
**How to use it:** Find your honest position. The deeper you sit, the harder a competitor can copy your value by copying the feature.

| Depth | Description | Switching cost |
|---|---|---|
| **Chatbot** | Standalone conversational layer | Users can switch in a day |
| **Embedded feature** | AI inside a tool users already use | Days to weeks |
| **Workflow layer** | Coordinates multiple steps in a job | Weeks to months |
| **Operating system** | The way the business actually works | Switching = rebuilding the org |

**The uncomfortable test:** Could your users switch in a weekend?

**Anchor examples:** Zendesk AI (embedded), Notion AI (workflow), GitHub Copilot (workflow), NetSuite (operating system).

---

### Data Flywheel - 4 Loops

**What it answers:** Does your product get smarter every time someone uses it?
**How to use it:** Score each loop 1-5. Total out of 20. Your weakest loop is your vulnerability - it's where competitors attack first.

| Loop | What it measures | Score 1 | Score 5 |
|---|---|---|---|
| **Correction** | Do users fix AI outputs, and is that signal reused? | No capture | Automated retraining |
| **Preference** | Does the product learn individual or team preferences? | Stateless | Deep personalization |
| **Domain Context** | Does usage in one area improve quality elsewhere? | Siloed | Cross-domain transfer |
| **Network** | Does each new user or team make the product better for everyone? | Isolated | Strong network effects |

**Lives in:** `02-the-moat/data-flywheel.md`.

---

### Encroachment Threat Vectors

**What it answers:** Who attacks you, from where, and how fast?
**How to use it:** For each vector, capture: attacker, vector, time-to-threat, percent of value at risk.

| Vector | Description | Example attacker |
|---|---|---|
| **Platform Encroachment** | A platform ships your core feature natively | OpenAI, Google, Apple, Microsoft, Salesforce, Adobe |
| **Vertical Competitor** | A startup goes deeper than you in one narrow niche | A focused YC startup in your sub-domain |
| **Adjacent Expansion** | A nearby tool adds your feature using its existing distribution | Notion adding the thing your tool sells |

**Anchor exercise:** The 90-Day Encroachment Plan - a partner says "I am Head of Product at [company]. Here is my 90-day plan to steal your users." Best attacks target the defender's weakest flywheel loop.

---

### Kill Switch - 3 Layers

**What it answers:** Could you swap AI providers in under 48 hours?
**How to use it:** Audit each layer. Then write three actions: this week, this month, this quarter.

| Layer | What it does | What "good" looks like |
|---|---|---|
| **Abstraction Layer** | Product code calls a generic interface, not a specific provider | All embedding calls behind `ai_gateway.search()` |
| **Multi-Model Routing** | Tasks route by cost, latency, and quality | Routing rules per task type, observable in production |
| **Eval Harness** | Automated tests prove a replacement provider meets your quality bar | A test suite that runs on every model swap |

**Specificity test:** "Build abstraction layer" is a weak action. "Move all embedding calls behind `ai_gateway.search()` by Friday" is a strong one.
**Lives in:** `02-the-moat/kill-switch.md`.

---

## Module 3 - The Margin

### Three Pricing Models

**What it answers:** *How* should you charge? (Not how much.)
**How to use it:** Match the unit of charge to the unit of value the customer recognizes.

| Model | What you charge for | When it fits | Example |
|---|---|---|---|
| **Seat-based access** | Login / per-user license | Pure collaboration tools where access is the value | Most classic SaaS |
| **Hybrid** | Base fee + usage on top | Most AI products today | GitHub Copilot ($19/seat with usage caps) |
| **Outcome-based** | The unit of work itself | When you can cleanly measure the work the customer values | Intercom Fin (per resolved conversation) |

**Market data:** 59% of AI products bundle, 23% sell as add-on, 18% go standalone.

---

### Leader / Filler / Killer + 70% Rule

**What it answers:** What gets bundled into the main plan, and what gets priced separately?
**How to use it:** Apply the 70% rule. If more than 70% of users touch a feature, bundle it. If fewer, price it separately.

| Role | What it is in your product | Big Mac analogy |
|---|---|---|
| **Leader** | Your core intelligence - the reason customers came | The burger |
| **Filler** | Lightweight features that bump value (summaries, suggestions) | Fries and a Coke |
| **Killer** | Heavy inference (image generation, agent workflows) - too expensive to bundle | Coffee - sell separately |

**Caveat:** It's a lens, not a prescription. If your buyer doesn't think about your product as a bundle, this framing isn't the right one.
**Lives in:** Packaging block in `03-the-margin/cost-curve.md`.

---

### Three Pricing Strategies

**What it answers:** What posture should you take in the market?
**How to use it:** Pick one. Then name the unit of work you'd meter, then set the structure.

| Strategy | Posture | Anchor company |
|---|---|---|
| **Skim** | Premium, capture high value from a willing-to-pay segment | Apple |
| **Penetrate** | Lower price to win share quickly | Amazon |
| **Maximize** | Capture the highest value through hybrid or outcome pricing | Microsoft / GitHub Copilot |

**Anchor example:** GitHub Copilot at $19/user is 4.75x a typical SaaS seat - and nobody blinks, because developers complete tasks 55% faster. The price is justified by outcome, not features.
**Lives in:** Pricing block in `03-the-margin/cost-curve.md`.

---

### Model Cascading - 80/20

**What it answers:** How do you protect AI margin without dropping quality?
**How to use it:** Route by task complexity, not by default. Tune the ratio to your domain.

| Tier | Share of requests | What it handles |
|---|---|---|
| **Small / cheap model** | ~80% (starting scaffold) | Simple, common, low-stakes work - autocomplete, lookups, classification |
| **Frontier model** | ~20% (starting scaffold) | Hard reasoning, edge cases, high-stakes outputs |

**Three other margin levers worth knowing:** caching, quantization, prompt optimization.
**Lives in:** Cascading Strategy section of `03-the-margin/cost-curve.md`.

**Caveat:** 80/20 is a starting scaffold. In practice it might be 95/5 or 60/40. Tune to your context.

---

## Cross-module map

| Module | Framework | Repo location |
|---|---|---|
| M1 | Three-Axis Diagnostic | `01-the-bet/diagnostic.md` |
| M1 | Five AI Value Archetypes | (used in framing - not a separate file) |
| M2 | The 8 Moats | (used in framing) |
| M2 | Workflow Depth Spectrum | (used in framing) |
| M2 | Data Flywheel - 4 Loops | `02-the-moat/data-flywheel.md` |
| M2 | Encroachment Threat Vectors | `02-the-moat/data-flywheel.md` |
| M2 | Kill Switch - 3 Layers | `02-the-moat/kill-switch.md` |
| M3 | Three Pricing Models | `03-the-margin/cost-curve.md` |
| M3 | Leader / Filler / Killer + 70% Rule | `03-the-margin/cost-curve.md` |
| M3 | Three Pricing Strategies | `03-the-margin/cost-curve.md` |
| M3 | Model Cascading 80/20 | `03-the-margin/cost-curve.md` |

For every term that appears here, the full definition lives in [`Glossary.md`](./Glossary.md).
