# Module 5 - The Guardrails (Pre-Read)

*Twenty minutes of reading and one short noticing exercise. Done before the session, this is the difference between hearing the M5 ideas for the first time in the room and walking in already chewing on them. Especially worth doing if "compounding," "shadow AI," or "agent governance" still feel like buzzwords.*

---

## 1. Why this session matters

Modules 1 to 4 gave you a bet, a moat, the economics, and a contract. Module 5 is where the strategy stops being a *story you tell* and becomes a *system that survives contact with reality* — frontier model releases, internal misuse, regulators, and three years from now.

The session has two halves that are joined at the hip:

- **Compounding** — does your AI get smarter the more it's used, or does it just scale? Most products only scale. The ones that compound are the ones still standing after the next frontier release closes the model gap.
- **Governance** — when something goes wrong (and something will), did you have a written line about what your AI is and isn't allowed to do — or are you arguing in real time with a CISO, a regulator, or a journalist?

By the end of the session you'll leave with one updated repo file — `05-the-guardrails/compounding-system.md` — covering five sections: **Feedback Loops** (with a broken loop and fix plan), **Context Connectivity**, **Governance Policy**, **Agent Topology**, and a **Shadow AI Audit**.

This is also the session where students who think "we'll handle governance later" realize what later actually costs.

---

## 2. The one idea to walk in already chewing on

> **Your governance framework is a sales asset, not a compliance burden.**

This is the central reframe of Module 5, and it cuts against the default PM instinct. The instinct says governance is a cost — slow, lawyer-driven, deserves a one-pager in a quarterly review. The reframe says governance is a *line item in your sales motion* — proof that the AI you're selling won't get the customer fired.

**The compliance-burden version** lives in a Notion doc nobody reads. It's the CISO's problem. It gets reviewed when something breaks. It slows the team down on purpose.

**The sales-asset version** is on the product page. Salesforce sells *Einstein Trust Layer* as a product. The EU AI Act is live and customers ask about it on every enterprise call. The model card, the bias posture, the audit cadence — these are answers to procurement questions you'd otherwise lose.

Pair this with the **freeze test**: *if you froze your model for three months — roughly one frontier cycle — would you still win?* If yes, you have something compounding. If no, you're rented advantage from the latest release, and the next one will quietly close your gap.

Sit with both ideas for a minute. The whole module hinges on them.

---

## 3. A 20-minute "noticing" exercise to do before class

Pick **three** AI products you actually use this week. For each one, ask the same question: *what's compounding here?* What gets smarter the more I use it — and how would I know? You're not building, you're just paying attention.

| Product | What to look for |
|---|---|
| **Cursor / GitHub Copilot** | Does it feel smarter this week than last? What signal would tell you — fewer rejected suggestions, better code style match, faster acceptance? |
| **Perplexity** | When you correct a citation or follow up, does the *next* answer change shape? Or does every session start from zero? |
| **Notion AI / Granola** | Does it learn your writing voice or stay generic? Notice whether tone / structure adapt over weeks. |
| **Klarna AI / Intercom Fin** (if you encounter them) | Deflection rate is the loop. Are escalations going down or staying flat? You can sometimes see this in their public posts. |
| **Tesla Autopilot / ADAS** | Fleet learning shows up in release notes — try to spot the week a new capability shipped. That's network intelligence in the wild. |
| **Spotify DJ / Discover Weekly** | Does the recommendation quality drift as you skip more, or stay generic? The skip-signal is the loop. |

Twenty minutes total. No notes required. The goal is to walk into Module 5 with **felt examples** of compounding vs. just-scaling. When the slide goes up that says "design your three loops," you'll have a library to draw from.

If you have ten extra minutes, do one more thing: notice **one piece of shadow AI** inside your own org. The Slack message someone drafted in ChatGPT, the spreadsheet auto-filled by an unauthorized plugin, the colleague using a personal Claude account for customer comms. You don't have to confront anyone — just notice. That observation is going to matter in section 6.

---

## 4. Vocabulary you'll keep hearing

Full definitions go in the cumulative [`Glossary.md`](./Glossary.md) after the session. One-liner each here so the words don't trip you up in the room.

- **Feedback loop** - any system where the output of a process becomes input to the next iteration. In M5: the engine of compounding.
- **Compounding system** - a product where each use makes the next use better. Different from a scaling system, where more use just means more volume at the same quality.
- **Recursive learning** - outputs (and corrections) feed back into the model. The clearest form of compounding.
- **Cross-domain transfer** - winning in one area lifts an adjacent area for free. Duolingo's lessons getting better across languages. ServiceTitan's data lifting 32 products on one stack.
- **Network intelligence** - fleet-level patterns improve each individual node. Tesla's fleet, Waze, fraud detection. Privacy-gated, but powerful.
- **Freeze test** - if you froze your model for three months (~one frontier cycle), would you still win? Diagnoses compounding moat vs. rented model advantage.
- **Shadow AI** - any AI tool being used inside your company that you didn't sanction, can't see, and don't govern. Samsung found out the hard way.
- **Agent** - software that *picks actions and chains tools*, not just steps. Agents make agentic ROI economics fuzzier than RPA — and the governance harder.
- **Autonomy boundary** - the explicit line between what AI does alone, what needs human approval, and what's never allowed at all. The hardest line is "human approval *even when confidence is high.*"
- **Tool calls** - the API calls an agent makes on your behalf. Each one is an exfiltration risk if you don't whitelist, rate-limit, and log.
- **Agent topology** - the map of what each agent can do, can't do, and who approves what. Mandatory if you ship agents.
- **Trust ladder** - the three-tier maturity model: **Compliance** (floor) → **Trust Architecture** (M4's confidence UX, evals, reliability contracts) → **Governance = GTM** (model cards, trust layer in the pitch).
- **Risk tier** - the EU AI Act's three buckets: **minimal**, **limited**, **high**. Customer service is usually limited. Hiring tools, credit decisions, medical advice — high.

---

## 5. A real story we'll dig into

> **Teaser - no spoilers.** A global electronics company let employees use a public AI chatbot freely. Engineers pasted source code into it to "debug." Someone else uploaded sensitive meeting notes. Within roughly a month, *three separate confidential leaks* were sitting in a vendor's training pipeline.
>
> There was no policy. No logging. No way to claw the data back. The first response was a blanket ban. That didn't work either.

We'll walk through what actually happened, what they should have done, and what the lesson is for your team. Come ready to think about which of your colleagues might be unintentionally re-running this story right now.

Also: the **Air Canada chatbot** lesson from M4 comes back. M4 was about the *contract* the AI made. M5 is about the *policy* the company should have had so the chatbot couldn't make that contract in the first place.

---

## 6. Two questions to come ready to answer

These will become warmups in the session. Showing up with honest answers pays off in the room.

### Question 1 - Freeze your model for three months. Do you still win?

About one frontier cycle. Not a literal freeze — a thought experiment. If GPT/Claude/Gemini paused at today's capability for the next quarter, what would happen to your moat?

- **If your win is "we have the latest model" -** the next release closes your gap. Name your real moat (distribution, brand, integrations, regulated data) or build one real learning loop.
- **If your win is "we have proprietary data that gets better with every use" -** congratulations, you have a compounding loop. Be honest about whether that's *one* loop or *several*, and whether any of them are broken.

Write down your one-sentence honest answer.

### Question 2 - Who in your company is using AI tools you didn't sanction?

And what data are they pasting in? Honest answer beats clean answer. The most common honest answer is *"I have no idea, and that's part of the problem."* That's fine — write it down.

If you do know: which tools, which teams, which data, what risk tier? Even a rough list is a head-start on the Shadow AI Audit you'll do in the room.

---

## 7. What to bring

- All four prior artifacts: `01-the-bet/`, `02-the-moat/`, `03-the-margin/`, `04-the-contract/`.
- A rough list (informal is fine) of: every AI tool / feature your product team ships, **and** every AI tool your colleagues use internally. The Notion AI, the Granola, the personal ChatGPT, the IDE assistant. All of it.
- Honest answers to the two questions above.
- The willingness to be pressure-tested by a partner on what your governance policy doesn't cover.

---

*See you in the room.*
