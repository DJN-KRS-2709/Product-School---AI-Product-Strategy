# Module 2 Frameworks Reference Card

*The frameworks introduced in Module 2 - The Moat. For M1 frameworks see [`Module 1 - Frameworks Reference Card.md`](./Module%201%20-%20Frameworks%20Reference%20Card.md). For the full course-wide reference, see [`Frameworks Reference Card.md`](./Frameworks%20Reference%20Card.md). For term definitions, see [`Module 2 - Glossary.md`](./Module%202%20-%20Glossary.md).*

Each framework gets: what it answers, the structure, and one anchor example.

---

## The 8 Moats

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

## Workflow Depth Spectrum

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

## Data Flywheel - 4 Loops

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

## Encroachment Threat Vectors

**What it answers:** Who attacks you, from where, and how fast?
**How to use it:** For each vector, capture: attacker, vector, time-to-threat, percent of value at risk.

| Vector | Description | Example attacker |
|---|---|---|
| **Platform Encroachment** | A platform ships your core feature natively | OpenAI, Google, Apple, Microsoft, Salesforce, Adobe |
| **Vertical Competitor** | A startup goes deeper than you in one narrow niche | A focused YC startup in your sub-domain |
| **Adjacent Expansion** | A nearby tool adds your feature using its existing distribution | Notion adding the thing your tool sells |

**Anchor exercise:** The 90-Day Encroachment Plan - a partner says "I am Head of Product at [company]. Here is my 90-day plan to steal your users." Best attacks target the defender's weakest flywheel loop.

---

## Kill Switch - 4-Dimension Audit

**What it answers:** Could you swap AI providers in under 48 hours?
**How to use it:** Score each dimension H / M / L for risk. Attach a 48-hour action to each. Then assign a Portability Score for the whole stack: Ready / Partial / Locked.

| Dimension | What it covers | What "low risk" looks like |
|---|---|---|
| **Provider** | Who you depend on, and how concentrated that dependency is | Multiple providers in production, no single point of failure |
| **Abstraction** | Product code calls a generic interface, not a specific provider | All embedding calls behind `ai_gateway.search()` |
| **Routing** | Tasks route by cost, latency, and quality | Routing rules per task type, observable in production |
| **Eval** | Automated tests prove a replacement provider meets your quality bar | A test suite that runs on every model swap |

**Specificity test:** "Build abstraction layer" is a weak action. "Move all embedding calls behind `ai_gateway.search()` by Friday" is a strong one.
**Stress scenarios** (also in the artifact): *If [primary vendor] doubles pricing tomorrow* → 48-hour response. *If [primary vendor] ships a competing product* → what's defensible that they can't replicate?
**Lives in:** `02-the-moat/kill-switch.md`.
