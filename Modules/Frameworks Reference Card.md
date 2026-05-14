# Frameworks Reference Card

*A compact, print-friendly consolidation of every framework introduced through Module 5. Keep it open while you do the labs. Each framework gets: what it answers, the structure, and one anchor example.*

For full term definitions, see [`Glossary.md`](./Glossary.md). For the narrative behind any of these, see the corresponding `Module N - Notes (Shareable).md` (Modules 1-3 in Markdown, Modules 4-5 in HTML).

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

### Kill Switch - 4-Dimension Audit

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
**Lives in:** Pricing Model section of `03-the-margin/cost-curve.md` (it informs how you bundle vs. add-on).

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
**Lives in:** Pricing Model section of `03-the-margin/cost-curve.md`.

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

## Module 4 - The Contract

### Trust ≠ Accuracy (the reframe)

**What it answers:** Why do users trust some AI products and not others, even when the higher-accuracy one is the one they distrust?
**How to use it:** Stop optimizing for the last accuracy points. Invest in legibility surface area instead.

| System | Accuracy | What users see | Outcome |
|---|---|---|---|
| **Black Box** | 95% | No scores. No sources. No override. Surprises in production. | Confidently wrong → trust evaporates |
| **Legible System** | 85% | Confidence scores. Citations. "I'm not sure." User can correct. | Lower benchmark, higher trust, higher retention |

**Headline:** *Understandable and controllable beats accurate-but-opaque, every time.*
**Anchors:** Tesla / ADAS-style forced handoffs (the car *makes you* take the wheel when it's not sure); Perplexity and AI Overviews leading every answer with clickable sources.

---

### Golden Dataset Structure

**What it answers:** How do you prove your AI is good - in regression tests, drift detection, and procurement calls?
**How to use it:** Build a labeled-truth fixture in your repo. Version it like code.

| Field | What it captures |
|---|---|
| **Input** | The prompt or scenario the AI faces |
| **Expected output** | The "good" answer, written by a human who knows the domain |
| **Edge-case flag** | Y / N - is this an edge case, boundary, or adversarial input? |
| **Judge type** | Rule-based (string match, regex) or LLM-as-Judge with a rubric |

**Rule of thumb:** 100-500 rows, adversarial cases included. Ten on day one; ~150 at v1 ship.
**Sales test:** *"Here's how we test our AI."* The teams that can screen-share this close. The teams that can't, don't.
**Lives in:** `04-the-contract/golden-dataset.md`.

---

### Confidence UX (Three Tiers)

**What it answers:** What does the UI do when the AI isn't sure?
**How to use it:** Design three modes, not one. Each tier gets its own copy, surface treatment, and user control.

| Tier | Confidence | UX treatment |
|---|---|---|
| **Confident** | &gt;90% | Direct answer. No hedge. Often auto-applied. |
| **Uncertain** | 50-90% | Hedging language. Confidence bar. "Double-check this." Surfaced citations / alternatives. |
| **Not confident** | &lt;50% | Block, escalate, route to human. User sees *why*, not just *what*. |

**Anchors:** Grammarly varies the rewrite depth based on confidence; Copilot adds citations or softens tone when less sure.
**Lives in:** Confidence UX Design section of `04-the-contract/golden-dataset.md`.

---

### Reliability Contract (4-Row Table)

**What it answers:** What does your product promise users about quality, drift, latency, and escalation - in numbers you'd defend to a board?
**How to use it:** Specific targets only. Aspirational numbers fail audits.

| Metric | Target | Measurement | Alert |
|---|---|---|---|
| **Accuracy** | 92% | Weekly · 300 golden rows · LLM-as-Judge | &lt;88% → pages on-call PM |
| **Hallucination rate** | &lt;1% | Same run · safety rubric | &gt;2% → pause prod traffic, rollback |
| **Latency p95** | &lt;800ms | Continuous production monitoring | &gt;1200ms for 5 min → PagerDuty |
| **Drift velocity** | &lt;0.5%/wk | 4-week rolling accuracy trend | &gt;1% decay/wk → gold-set audit |

**Paired with HITL row:** confidence &lt;60% or safety flag → human reviewer (rotating on-call PM); corrections feed back into the weekly gold-set audit. Closes the loop.
**Lives in:** Reliability Contract + HITL Architecture sections of `04-the-contract/golden-dataset.md`.

---

### HITL as a Shrinking Queue

**What it answers:** When do humans step in, and why isn't this just permanent babysitting?
**How to use it:** Define triggers, capture corrections, escalate visibly. Watch the HITL percentage drop as the gold set grows.

| Element | What it does | Design target |
|---|---|---|
| **Thresholded review** | Confidence below threshold → human; above → auto | Triggers are explicit and tunable |
| **Corrections to gold** | Every human edit feeds back into the golden dataset | Every edit = training fuel |
| **Escalation UX** | Users opt into the handoff rather than being surprised | The handoff is part of the product, not an apology |

**Anchor:** Medical imaging tools and ambient clinical scribes - AI handles routine cases; clinicians sign off only on high-risk outputs. The HITL share *drops over time* as the model improves.
**Lives in:** HITL Architecture section of `04-the-contract/golden-dataset.md`.

---

## Module 5 - The Guardrails

### The Three Compounding Mechanisms

**What it answers:** Does your product actually get smarter the more it's used, or does it just scale?
**How to use it:** Sketch each loop in `compounding-system.md`. Name the input, the output, whether it compounds, and its status.

| Mechanism | What feeds it | Anchor company |
|---|---|---|
| **Recursive Learning** | Your product's own outputs and the corrections users make to them | Duolingo |
| **Cross-Domain Transfer** | Wins in product A lifting product B next door (shared context, shared data) | ServiceTitan |
| **Network Intelligence** | Patterns across the whole fleet / user base, privacy-gated | Fleet-learning products |

**Most rows on most products come back `missing` or `broken`, not `active`.** That's the finding, not a failure of the exercise.
**Lives in:** Feedback Loops table + Context Connectivity field of `05-the-guardrails/compounding-system.md`.

---

### The Freeze Test

**What it answers:** Is your product compounding, or just scaling on top of model upgrades?
**How to use it:** Mentally pause the product for one frontier cycle. If it's still winning, you don't have a compounding system - you have a beneficiary of someone else's improvement.

| Setup | Question | Verdict |
|---|---|---|
| Freeze for **3 months** (≈ one frontier-model cycle) | After 3 months: still ahead? | **Yes** → scaling, not compounding. **No** → name what would degrade. That's the loop that's working. |

**Why 3 months and not 12:** AI cycles too fast. Twelve months of frozen AI feels like ten years of frozen anything else.
**Lives in:** the diagnostic at the bottom of Slide 8 and inside the **Compounding System Designer** tool.

---

### Responsible AI Maturity Ladder

**What it answers:** Where does your org sit on the responsibility-to-revenue spectrum, and what's the upside of climbing a level?
**How to use it:** Locate yourself honestly. Most teams plateau at Level 1 or 2. Level 3 converts trust infrastructure into closed enterprise deals.

| Level | Posture | What it looks like | Anchor |
|---|---|---|---|
| **1. Compliance** | Minimum bar | EU AI Act, GDPR, CCPA. Defensive, not differentiating. | Most orgs today |
| **2. Trust Architecture** | Internal craft | Evals, confidence UX, reliability contracts (M4). Trust as infrastructure. | Most "AI-serious" teams |
| **3. Governance = GTM** | External story | Model cards, bias posture, governance in the sales pitch. | **Salesforce** Einstein Trust Layer |

**Counter-anchor:** Google Gemini's image-generation incident - the product paused publicly for remediation, on stage, in front of the whole market.

---

### The Four Agent Governance Knobs

**What it answers:** How do you govern a system that picks its own actions, in a way that survives the next model swap?
**How to use it:** Walk one of your agents through all four knobs. Anything you can't answer concretely is a policy gap.

| Knob | What it controls | Concrete move |
|---|---|---|
| **Autonomy** | Draft ≠ send. Read ≠ write. | Draft anything, send nothing without human approval until eval data proves >99%. Money / customer contact stays HITL. |
| **Tool Calls** | Every call is a risk surface. | **Allow-list** which tools. **Rate-limit** each one. **Log** every call with reasoning + result. |
| **Memory** | What persists, who reads it. | Three explicit classes: short-term (session), long-term (per-user), shared (usually a hard no for customer-facing). |
| **Chain** | Who owns the B-fails-on-A handoff? | Named ownership per handoff. "Stop the chain" trigger if any agent fails its eval. No silent chains. |

**Principle that survives model churn:** *Design around principles, not model names.*
**Anchor:** Microsoft Copilot + Graph/plugins - log + allow-list; tier autonomy explicitly (read calendar auto; draft email auto; send email one-click approval).
**Lives in:** Agent Topology section of `05-the-guardrails/compounding-system.md`.

---

### The Shadow AI Audit Framework (user-side)

**What it answers:** What AI capabilities are your *users* building around your product that you didn't ship, and what should you do about each one?
**How to use it:** Read this as roadmap discovery research, not as a compliance audit. The CISO-flavored shadow AI (Samsung-style internal tool sprawl) is real but it's not a PM's job. The PM-facing version is the user-side one — every workaround your users have hacked together is either a feature request you weren't reading as one or a capability someone else will ship before you do.

| Step | What you do | Where to look |
|---|---|---|
| **1. Discover** | Find evidence of user-side AI use | Support tickets (search "ChatGPT," "Claude," "Zapier"); user interviews; forums and Reddit; Zapier/Make recipe directories; API usage patterns; social media |
| **2. Signal** | Classify what each workaround tells you | Workflow gap · Trust gap · Capability gap · Pricing gap |
| **3. Prioritize** | Frequency × strategic relevance | Mentioned once = curiosity. Seen in fifteen tickets and four Zapier recipes = build candidate |
| **4. Decide** | Build · Partner · Ignore | *Build* = absorb natively. *Partner* = official integration. *Ignore* = legitimate when not strategic. The trap is defaulting to Build |

**Signal → decision mapping (rough):** Workflow gap → usually Partner. Trust gap → re-open M4 (reliability contract / confidence UX). Capability gap → cleanest Build candidate. Pricing gap → look at packaging first.
**Repo column note (Build / Partner / Ignore vs. Keep / Govern / Kill):** The frozen repo template still shows `keep / govern / kill` in the placeholder. Overwrite it with build/partner/ignore — 1:1 mapping (keep ≈ ignore, govern ≈ partner, kill ≈ build).
**Anchor case:** Samsung lives in the slide before this framework as the cautionary CISO-side case. The user-side anchor is your own product: every PM has one example of users routing their output through ChatGPT.
**Lives in:** Shadow AI Audit table + 3 summary stats (Workarounds found · Build candidates · Adjacent spend) in `05-the-guardrails/compounding-system.md`.

---

### The Governance Policy Template

**What it answers:** What does a one-page AI governance policy that your CISO wouldn't redline on sight actually contain?
**How to use it:** Fill in all five fields, plus Agent Topology if relevant. Be specific - "AI in our company" is mush; "all customer-facing AI features in our SMB product line" is a policy.

| Field | Worked example (SupportCopilot v1.2) |
|---|---|
| **Scope** | Automated reply drafting, routing, and resolution scoring in the SupportCopilot product line. Excludes internal-only analytics. |
| **Autonomy** | Drafting — auto. Sending under $0 risk — auto. Sending with promised remedies — human approval. Closing tickets without reply — never auto. |
| **Escalation** | Confidence <70%; legal/medical/distressed flag; refund/credit/exception mentioned; customer asks for human; ≥3 turns. |
| **Audit cadence** | Weekly automated eval (PM: Sam); monthly human review (Legal: Priya); quarterly full review (CTO sign-off). |
| **Regulatory** | EU AI Act = limited risk; GDPR applies (data minimization, no PII training); SOC 2 controls for log retention. |

**Test of a good policy:** Could you hand it to legal, ops, or an enterprise buyer and have them actually evaluate it?
**Lives in:** Governance Policy + Agent Topology sections of `05-the-guardrails/compounding-system.md`.

---

### Samsung Three-Act Structure (case study framing)

**What it answers:** What's the predictable failure mode when AI tools enter an org without governance?
**How to use it:** Use as a teaching frame. The arc compresses every time - the only variable is how much you lose between Act Two and Act Three.

| Act | What happens | The lesson |
|---|---|---|
| **The Bet** | AI tools adopted broadly. Fast wins, broad enthusiasm, no guardrails. | Adoption without governance feels like velocity. |
| **The Crack** | Data leaks or incidents. No policy, no audit trail, panic. | The cost shows up in the audit trail you don't have. |
| **The Correction** | Ban and rebuild from scratch. Massive productivity hit. | The ban costs more than the leaks. |

**Punchline:** *The absence of governance isn't a compliance gap - it's a strategy failure.*

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
| M2 | Kill Switch - 4-Dimension Audit | `02-the-moat/kill-switch.md` |
| M3 | Three Pricing Models | `03-the-margin/cost-curve.md` |
| M3 | Leader / Filler / Killer + 70% Rule | `03-the-margin/cost-curve.md` |
| M3 | Three Pricing Strategies | `03-the-margin/cost-curve.md` |
| M3 | Model Cascading 80/20 | `03-the-margin/cost-curve.md` |
| M4 | Trust ≠ Accuracy (reframe) | (used in framing) |
| M4 | Golden Dataset Structure | `04-the-contract/golden-dataset.md` |
| M4 | Confidence UX (Three Tiers) | `04-the-contract/golden-dataset.md` |
| M4 | Reliability Contract (4-Row Table) | `04-the-contract/golden-dataset.md` |
| M4 | HITL as a Shrinking Queue | `04-the-contract/golden-dataset.md` |
| M5 | Three Compounding Mechanisms | `05-the-guardrails/compounding-system.md` |
| M5 | The Freeze Test | `05-the-guardrails/compounding-system.md` (diagnostic) |
| M5 | Responsible AI Maturity Ladder | (used in framing) |
| M5 | Four Agent Governance Knobs | `05-the-guardrails/compounding-system.md` |
| M5 | Shadow AI Audit Framework | `05-the-guardrails/compounding-system.md` |
| M5 | Governance Policy Template | `05-the-guardrails/compounding-system.md` |
| M5 | Samsung Three-Act Structure | (used in framing) |

For every term that appears here, the full definition lives in [`Glossary.md`](./Glossary.md).
