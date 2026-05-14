# Module 5 Frameworks Reference Card

*The frameworks introduced in Module 5 - The Guardrails. For earlier modules see [`Module 1 - Frameworks Reference Card.md`](./Module%201%20-%20Frameworks%20Reference%20Card.md), [`Module 2 - Frameworks Reference Card.md`](./Module%202%20-%20Frameworks%20Reference%20Card.md), [`Module 3 - Frameworks Reference Card.md`](./Module%203%20-%20Frameworks%20Reference%20Card.md), and [`Module 4 - Frameworks Reference Card.md`](./Module%204%20-%20Frameworks%20Reference%20Card.md). For the full course-wide reference, see [`Frameworks Reference Card.md`](./Frameworks%20Reference%20Card.md). For term definitions, see [`Module 5 - Glossary.md`](./Module%205%20-%20Glossary.md).*

Each framework gets: what it answers, the structure, and one anchor example.

---

## The Three Compounding Mechanisms

**What it answers:** Does your product actually get smarter the more it's used, or does it just scale?
**How to use it:** Sketch each loop in `compounding-system.md`. Name the input, the output, whether it compounds, and its status.

| Mechanism | What feeds it | Anchor company |
|---|---|---|
| **Recursive Learning** | Your product's own outputs and the corrections users make to them | Duolingo - learner struggles sharpen the next learner's lesson |
| **Cross-Domain Transfer** | Wins in product A lifting product B next door (shared context, shared data) | ServiceTitan - 32 products on one vertical stack feeding each other |
| **Network Intelligence** | Patterns across the whole fleet / user base, privacy-gated | Duolingo at the global lesson-difficulty level; fleet-learning products |

**Forcing function:** Most rows on most products come back `missing` or `broken` rather than `active`. That's the finding, not a failure of the exercise.
**Lives in:** Feedback Loops table + Context Connectivity field of `05-the-guardrails/compounding-system.md`.

---

## The Freeze Test

**What it answers:** Is your product compounding, or just scaling on top of model upgrades?
**How to use it:** Mentally pause the product for one frontier cycle. If it's still winning, you don't have a compounding system - you have a beneficiary of someone else's improvement.

| Setup | Question | Verdict |
|---|---|---|
| Freeze the product for **3 months** (≈ one frontier-model cycle) | After 3 months: still ahead? | If **yes** → you're scaling, not compounding. If **no** → name *what* would visibly degrade. That's the loop that's working. |

**Why 3 months and not 12:** AI cycles too fast. Twelve months of frozen anything is "ten years" in AI time, so the test stops separating real compounding from "we haven't fallen behind GPT-5 yet."
**Anchor example:** A team marked Recursive Learning as `active` because users could thumbs-up answers. Freeze test: would 3 months without retraining hurt? Answer: no, because the thumbs-ups never reached the training pipeline. Reality check, status changed to `broken`.
**Lives in:** the diagnostic at the bottom of Slide 8 and inside the **Compounding System Designer** tool.

---

## Responsible AI Maturity Ladder

**What it answers:** Where does your org actually sit on the responsibility-to-revenue spectrum, and what's the upside of climbing a level?
**How to use it:** Locate yourself honestly. Most teams plateau at Level 1 or 2. Level 3 is the move that converts trust infrastructure into closed enterprise deals.

| Level | Posture | What it looks like | Anchor |
|---|---|---|---|
| **1. Compliance** | Minimum bar | EU AI Act, GDPR, CCPA. Defensive. Necessary, not differentiating. | Most orgs today |
| **2. Trust Architecture** | Internal craft | Evals, confidence UX, reliability contracts (everything from M4). Trust as infrastructure. | Most "AI-serious" teams |
| **3. Governance = GTM** | External story | Model cards, bias posture, governance artifacts in the sales pitch and procurement responses. | **Salesforce** Einstein Trust Layer |

**Counter-anchor:** Google Gemini's image-generation incident - the product paused publicly for remediation, in front of the entire market. A velocity-vs-safety decision made on stage. The kind of event that makes Level 1 feel inadequate.
**Lives in:** the framing for Slide 9 and the structure of the **AI Maturity Scorer** tool (self-paced from the Tools Overview).

---

## The Four Agent Governance Knobs

**What it answers:** How do you govern a system that picks its own actions, in a way that survives the next model swap?
**How to use it:** Walk one of your agents (real or planned) through all four knobs. Anything you can't answer concretely is a policy gap.

| Knob | What it controls | Concrete move |
|---|---|---|
| **Autonomy** | Draft ≠ send. Read ≠ write. | Best practice: draft anything, send nothing without human approval until eval data proves >99% on the action. Side-effecting actions (money, customer contact) stay human-in-the-loop. |
| **Tool Calls** | Every call is a risk surface. | **Allow-list** which tools can be called. **Rate-limit** each one (e.g. 10 refunds/hour). **Log** every call with reasoning + result. |
| **Memory** | What persists between sessions, and who can read it. | Three explicit classes: short-term (this session only), long-term (per-user, persistent), shared (across users - usually a hard no for anything customer-facing). |
| **Chain** | When agent B fails on agent A's output, who owns the handoff? | Named ownership per handoff. A "stop the chain" trigger if any agent in the line fails its eval. No silent chains. |

**Principle that survives model churn:** *Design around principles, not model names.* Specific models churn every six months; the four knobs survive that churn.
**Anchor example:** Microsoft Copilot with Graph + plugins - logs and whitelists like any production system, and tiers autonomy explicitly (read calendar = auto; draft email = auto; send email = one-click human approval).
**Lives in:** Agent Topology section of `05-the-guardrails/compounding-system.md`.

---

## The Shadow AI Audit Framework (user-side)

**What it answers:** What AI capabilities are your *users* building around your product that you didn't ship, and what should you do about each one?
**How to use it:** Read it as roadmap discovery research, not as a compliance audit. The CISO-flavored version of shadow AI (Samsung-style employee tool sprawl) is real but it's not a PM's job. The PM-facing version is the user-side one — every workaround your users have hacked together is either a feature request you weren't reading as one or a capability someone else will ship before you do. Run the four steps once with realistic scope (your top user segment, your top feature, one quarter of support tickets).

| Step | What you do | Where to look |
|---|---|---|
| **1. Discover** | Find evidence of user-side AI use | Support tickets (search "ChatGPT," "Claude," "Zapier"); user interviews; public forums and Reddit; Zapier/Make recipe directories; API usage patterns (big exports without writes-back = enrichment elsewhere); social media |
| **2. Signal** | Classify what each workaround tells you | **Workflow gap** (chained into another step you don't support) · **Trust gap** (double-checking your output) · **Capability gap** (you don't do it at all) · **Pricing gap** (cheaper or metered differently externally) |
| **3. Prioritize** | Frequency × strategic relevance | A workaround mentioned once is a curiosity. One you see in fifteen tickets, six interviews, and four Zapier recipes is a feature you should already be building |
| **4. Decide** | Build · Partner · Ignore | **Build**: absorb the capability natively. **Partner**: official integration with the external tool. **Ignore**: not strategic, users keep doing it externally. *Ignore* is a legitimate answer; the trap is calling everything "Build" |

**Signal → decision mapping (rough):** Workflow gap → usually Partner. Trust gap → re-open M4 (reliability contract + confidence UX) before adding more features. Capability gap → cleanest Build candidate. Pricing gap → look at packaging before assuming you need to build more.
**Decision column note (Build / Partner / Ignore vs. Keep / Govern / Kill):** The repo template's column placeholder still shows the older `keep / govern / kill` verbs because the template is frozen. Use the user-side labels in your audit and overwrite the placeholder text — it's a 1:1 mapping (keep ≈ ignore, govern ≈ partner, kill ≈ build).
**Anchor case:** Samsung lives one slide earlier as the cautionary CISO-side case. The user-side anchor is messier — every B2B SaaS PM has at least one example of users routing their product's output through ChatGPT to do something the product doesn't do natively. Pick one from your own product right now.
**Lives in:** Shadow AI Audit table + 3 summary stats (Workarounds found · Build candidates · Adjacent spend) in `compounding-system.md`. Backed by the **Shadow AI Audit** tool.

---

## The Governance Policy Template

**What it answers:** What does a one-page AI governance policy that your CISO wouldn't redline on sight actually contain?
**How to use it:** Fill in all five fields, plus the Agent Topology strip if your product ships agents. Be specific - "AI in our company" is mush; "all customer-facing AI features in our SMB product line" is a policy.

| Field | What it covers | Worked example (SupportCopilot v1.2) |
|---|---|---|
| **Scope** | Which products / features / teams this policy applies to | "Automated reply drafting, routing, and resolution scoring in the SupportCopilot product line. Excludes internal-only analytics dashboards." |
| **Autonomy boundaries** | What agents do solo vs. what needs a human | Drafting replies — auto. Sending under $0 risk — auto. Sending with promised remedies — human approval required. Closing tickets without reply — never auto. |
| **Escalation triggers** | When a human must enter | Confidence < 70%; legal/medical/distressed flag; any refund/credit/exception mentioned; customer asks for human; ≥3 turns. |
| **Audit cadence** | How often we review (real-time / daily / weekly / monthly / quarterly) | Weekly automated eval (PM: Sam); monthly human review of 50 random + all escalations (Legal: Priya); quarterly full policy review (CTO sign-off). |
| **Regulatory exposure** | EU AI Act tier + GDPR + sector regimes | EU AI Act = limited risk; GDPR applies (data minimization, no training on customer PII); SOC 2 controls in place for log retention. |

**Optional - Agent Topology strip:** For each agent, two short lines - what it *can* do, what it *cannot* do, and who approves what.
**Test of a good policy:** Could you hand it to legal, ops, or an enterprise buyer and have them actually evaluate it? "We have a governance policy" fails that test; the worked example above passes it.
**Lives in:** Governance Policy + Agent Topology sections of `05-the-guardrails/compounding-system.md`. Backed by the **Governance Policy Drafter** tool.

---

## The Samsung Three-Act Structure

**What it answers:** What's the predictable failure mode when AI tools enter an org without governance, and how do you tell the story to your exec team?
**How to use it:** Use as a teaching frame, not a forecast. The three acts compress on the same arc every time - the only variable is how much you lose between Act Two and Act Three.

| Act | What happens | The lesson |
|---|---|---|
| **Act One — The Bet** | AI tools adopted broadly. Fast wins, broad enthusiasm, no guardrails. | Adoption without governance feels like velocity. |
| **Act Two — The Crack** | Data leaks or incidents. No policy, no audit trail, panic. | The cost shows up after the fact, in the audit trail you don't have. |
| **Act Three — The Correction** | Ban and rebuild from scratch. Massive productivity hit while the org reorganises around governed alternatives. | The ban costs more than the leaks. |

**Punchline:** *The absence of governance isn't a compliance gap - it's a strategy failure.* The reflex reaction in every cohort is "this couldn't happen at my company." In every cohort, that bet has been wrong.
**Lives in:** Slide 12, and behind the Shadow AI Audit framework on Slide 13 - the audit exists to prevent Act Two before it happens.
