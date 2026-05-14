# Course Glossary

*A cumulative reference for the terms used across the course. Cumulative through Module 5 - it grows after each session. Use it as a quick lookup when something on a slide or in your repo work doesn't quite click.*

The glossary has five sections:

1. **AI/ML Foundations** - the technical vocabulary you keep hearing.
2. **Strategy Concepts** - the frameworks and ideas that show up across the modules.
3. **Economics & Pricing** - everything from Module 3 about how AI products make and lose money.
4. **Trust & Reliability** - the Module 4 vocabulary for evals, confidence UX, and reliability contracts.
5. **Governance & Compounding** - the Module 5 vocabulary for agents, governance, the user-side reframe of shadow AI, and feedback loops that actually learn.

Each entry is one or two sentences, plus a `Seen in:` pointer back to the module and slide where the term first lands.

---

## 1. AI/ML Foundations

### Abstraction layer

A piece of code that sits between your product and any specific AI provider so the rest of the codebase calls a generic interface (something like `ai_gateway.search()`) instead of OpenAI or Anthropic directly. Without one, swapping providers means rewriting calls everywhere.
*Seen in: M2, Slide 18 (The Kill Switch).*

### Adversarial / Boundary / Edge cases

Three flavors of test inputs that show up in a golden dataset. **Edge cases** are at the limits of normal usage (very long input, very short input, unusual characters). **Boundary cases** sit right at a decision threshold (just-above vs just-below the cutoff for "send to human"). **Adversarial cases** are deliberately designed to break the system - prompt injection attempts, jailbreaks, misleading phrasing. All three belong in a real golden dataset.
*Seen in: M4, Slide 9 (Define Your Golden Dataset).*

### Agent

An AI system that can take multiple steps on its own to complete a task - calling tools, making decisions, looping until done - rather than producing a single response. Agents are powerful and expensive: one running for a day can burn through more cost than a hundred regular conversations. M5 introduces the four governance knobs that make agents safe to ship.
*Seen in: M3, Slide 9 (a $200/month plan blew up because users ran agent workflows on it). Expanded in M5, Slide 10.*

### Caching

Storing AI responses so the next time the same question (or a similar one) is asked, you serve the saved answer instead of paying for a new model call. One of the four levers for protecting AI margin.
*Seen in: M3, Slide 7 (Model Cascading).*

### Context window

The amount of text (measured in tokens) the model can see at once when generating a response. Longer windows let you feed in more documents or history but cost more per call.
*Seen in: M3, Slide 5 (longer context windows are one of the ways usage intensity rises even when token prices fall).*

### Drift

When model behavior shifts over time - either because the provider updates the underlying model, or because the data the model sees in production changes. A real product needs evals to catch drift before users do.
*Seen in: M1, Slide 6 (probabilistic outputs row of Traditional vs. AI).*

### Embedding

A numerical representation of a piece of text (or image, audio, etc.) that captures its meaning, so the system can compare it to other content and retrieve what is most relevant. They are how RAG systems "look things up." They are also called more often than people expect, which is why they show up as a cost trap.
*Seen in: M3, Slide 17 ("you will underestimate how often embeddings get called").*

### Eval / Eval harness

An automated test suite that scores whether the AI is producing good outputs against a known set of expected answers. The eval harness is what proves a replacement model meets your quality bar before you switch.
*Seen in: M2, Slide 18 (the Eval dimension of the Kill Switch audit). Goes much deeper in M4.*

### Fine-tuning

Taking a base model and continuing to train it on your own data so it gets better at a specific task or domain. Distinct from prompting - fine-tuning changes the model itself.
*Seen in: implicit in M2, Slide 11 (the "automated retraining" end of the Correction loop).*

### Frontier model

The most powerful (and most expensive) tier of model from a provider - GPT-5, Claude Opus, Gemini Pro, etc. Use it for genuinely hard work. Default everything to it and your cost curve will hurt. Module 5's *frontier cycle* refers to the ~3-month cadence at which new frontier models ship.
*Seen in: M3, Slides 6, 7, 17 (cascading is the discipline of not using frontier when you don't need it). Re-anchored in M5, Slide 8 (freeze test).*

### Golden dataset

A labeled-truth fixture that defines "good" for *your* product. Not a public benchmark - your domain, your edge cases, versioned in your repo like code. Rule of thumb: 100-500 rows, adversarial cases included, ten on day one, ~150 at v1 ship. Used for regression, drift detection, and as a sales artifact when buyers ask "show me how you test this."
*Seen in: M4, Slides 7 and 9.*

### Hallucination

When the model produces an answer that sounds confident but is factually wrong. The reason AI products need eval harnesses, golden datasets (Module 4), and human review for high-stakes outputs.
*Seen in: M1, Slide 6 (the probabilistic outputs row).*

### HITL (Human-in-the-Loop)

A pattern where humans review or approve AI outputs at specific moments rather than blindly accepting them. Module 4's framing: HITL as a *shrinking queue*, not permanent babysitting. Triggers (confidence below threshold, safety flag, high-stakes action) route to a human; the human's corrections feed back into the golden dataset. Done right, the queue shrinks over time as the model improves.
*Seen in: M4, Slides 10 and 18 (HITL Architecture).*

### Inference

Running a request through a model to get a response - the live, in-production cost of using AI. Distinct from training. When people say "inference cost," they mean what each call costs you in real time.
*Seen in: M3, Slide 5 (the provocation question: what is your inference cost per user per month?).*

### LLM-as-Judge

A pattern where another LLM (calibrated against your golden dataset) automatically scores live outputs - catching regressions before users do. The judge can run continuously and at high volume, but only meaningful if anchored to your golden dataset; without that anchor, an LLM-as-Judge is just another opinion. Vendors (LangSmith, Braintrust, Humanloop) provide the judge infrastructure; you own the labels and the rubric.
*Seen in: M4, Slide 15.*

### Model

The trained AI system that takes input and produces output. Models come in tiers (small / cheap / frontier) and from different providers. Your product is almost always making choices about which model to call for which task.
*Seen in: M1, Slide 6; foundational throughout.*

### Multi-model routing

Logic that decides, for each request, which model to send it to - based on cost, latency, quality, or task type. The Routing dimension of the Kill Switch audit and the mechanism that makes cascading possible.
*Seen in: M2, Slide 18; M3, Slide 7.*

### Prompt

The instruction (and any context) you send to the model. Prompt design directly affects cost (longer prompts = more tokens) and quality.
*Seen in: foundational throughout.*

### Prompt injection

An attack where malicious instructions are embedded in a tool's input (a document, a webpage, a customer message) to make the AI ignore its system prompt and do something it shouldn't. The reason rate-limiting, tool allow-listing, and adversarial test cases matter - they cap or surface the blast radius when (not if) an injection lands.
*Seen in: M5, Slide 10 (Agent Governance).*

### Prompt optimization

Rewriting prompts to get the same (or better) quality with fewer tokens or fewer model calls. One of the four levers for protecting AI margin.
*Seen in: M3, Slide 7.*

### Quantization

Compressing a model so it runs cheaper and faster, usually with a small quality trade-off. Shows up alongside caching and prompt optimization as a margin lever.
*Seen in: M3, Slide 7.*

### Retrieval-Augmented Generation (RAG)

A pattern where the system first searches your own data (using embeddings) for the most relevant snippets, then feeds those snippets into the model alongside the user's question. This is how AI products get answers grounded in proprietary or recent information instead of just the model's training data.
*Seen in: implicit in M2 throughout (proprietary domain context is what RAG retrieves over).*

### Small / cheap model

The lower-tier models - GPT-mini, Claude Haiku, Llama variants, etc. Cheap, fast, often "good enough" for the bulk of requests. The 80% in an 80/20 cascade.
*Seen in: M3, Slide 7.*

### Token

The unit AI providers bill in. Roughly speaking, one token is about three-quarters of an English word. Both your input (prompt) and the model's output cost tokens. Every cost calculation in Module 3 ultimately resolves to tokens.
*Seen in: M3, Slide 6.*

---

## 2. Strategy Concepts

### AI Value Archetypes (the 5)

Five categories that capture what an AI product fundamentally does, each with a different margin profile and governance burden: **Automator** (replaces tasks - UiPath), **Copilot** (augments people - GitHub Copilot), **Oracle** (surfaces hidden signals - Palantir), **Creator** (generates new assets - Midjourney), **Orchestrator** (chains agents and tools - Zapier AI). Most products blend two or three; what matters is which one dominates your economics.
*Seen in: M1, Slide 14.*

### Contextual Moat

How embedded your product is in the way people actually work. The first axis of the Three-Axis Diagnostic. Workflow depth multiplied by switching cost.
*Seen in: M1, Slide 18.*

### Correction loop

One of the four loops in the Data Flywheel. Measures whether users fix the AI's outputs and whether that signal gets reused to improve the system. Score 1 = no capture; Score 5 = automated retraining.
*Seen in: M2, Slide 11.*

### Data Advantage

The second axis of the Three-Axis Diagnostic. Not "we have data" - it's specifically about whether your product gets smarter every time someone uses it. A stockpile is not an advantage; a flywheel is.
*Seen in: M1, Slide 18.*

### Data Flywheel

The mechanism by which usage creates proprietary signal, that signal improves the product, and the improved product drives more usage. The central reframe of Module 2: **the moat is loops, not data.**
*Seen in: M2, Slide 10.*

### Domain Context loop

One of the four loops in the Data Flywheel. Measures whether the product learns details that generic models don't know - and whether usage in one area improves quality elsewhere. Score 1 = siloed; Score 5 = cross-domain transfer.
*Seen in: M2, Slide 11.*

### Encroachment

When a competitor moves into your space. Module 2 names three vectors: **Platform encroachment** (a platform like Microsoft or Salesforce ships your feature natively), **Vertical competitor** (a startup goes deeper than you in one narrow niche), **Adjacent expansion** (a nearby tool adds your feature using its existing distribution).
*Seen in: M2, Slide 14.*

### The 8 Moats

The classic moat types: **Data, Workflow, Regulatory, Distribution, Ecosystem, Network, Physical, Scale.** For AI products, the two that usually matter most are Data and Workflow.
*Seen in: M2, Slide 6.*

### Kill criteria

The conditions under which you stop a bet, written down before the bet starts. The thing that turns "we'll see how it goes" into an actual learning loop.
*Seen in: M1, Slide 12 (the OLD vs. NEW reframe: "70% this hits Y - here's how we'll know, and when we stop").*

### Kill Switch

The strategy for escaping AI vendor lock-in. The audit in `02-the-moat/kill-switch.md` runs across **four dimensions**: **Provider** (who you depend on), **Abstraction** (a generic interface in your code), **Routing** (multi-model routing by cost / latency / quality), and **Eval** (automated tests that prove a replacement model meets your quality bar). Each dimension gets an H / M / L risk rating and a 48-hour action. The whole stack gets a Portability Score: Ready / Partial / Locked. The test: could you swap providers in under 48 hours?
*Seen in: M2, Slide 18.*

### Network loop

One of the four loops in the Data Flywheel. Measures whether each new user or team makes the product better for everyone. Score 1 = isolated; Score 5 = strong network effects.
*Seen in: M2, Slide 11.*

### Platform Exposure

The third axis of the Three-Axis Diagnostic. The risk that a platform (OpenAI, Google, Apple, Microsoft) ships your wedge as a free native feature tomorrow.
*Seen in: M1, Slide 18.*

### Preference loop

One of the four loops in the Data Flywheel. Measures whether the product learns individual or team preferences over time. Score 1 = stateless; Score 5 = deep personalization.
*Seen in: M2, Slide 11.*

### Probabilistic vs. Deterministic

The core reframe of Module 1. Traditional software is deterministic - it does the same thing every time. AI is probabilistic - outputs are distributions, not point estimates. Strategy has to shift from "ship X by Q3 → Y result" to "70% this hits Y - here's how we'll know, and when we stop."
*Seen in: M1, Slide 12.*

### Three-Axis Diagnostic

The Module 1 framework for scoring your AI vulnerability across **Contextual Moat, Data Advantage, and Platform Exposure**, each on a 1-5 scale. Calibration: Figma is a deep moat, a thin ChatGPT wrapper is shallow.
*Seen in: M1, Slide 18.*

### Workflow depth

A spectrum from shallow to deep: **Chatbot → Embedded feature → Workflow layer → Operating system.** The deeper your product sits in how the business actually works, the harder it is for a competitor to copy the value by copying the feature.
*Seen in: M2, Slide 8.*

### Wrapper vs. Workflow

The framing for Module 2. A **wrapper** is a thin UI on top of someone else's model - features get eaten when the model provider ships them natively (Jasper is the cautionary tale). A **workflow** is embedded deeply enough in how users work that it survives.
*Seen in: M2, Slide 7.*

---

## 3. Economics & Pricing

### 70% Rule

The bundling threshold. If more than 70% of users touch a feature, bundle it into the main plan. If fewer, price it separately as an add-on. Otherwise you are subsidizing your heaviest users with everyone else's subscription.
*Seen in: M3, Slide 11.*

### 80/20 split

The starting cascade ratio: 80% of requests routed to a cheap model, 20% to a frontier model. Cursor and GitHub Copilot ship variations of this in production. Tune the ratio to your domain - it might be 95/5 or 60/40.
*Seen in: M3, Slide 7.*

### AI COGS

The portion of your Cost of Goods Sold that comes specifically from AI: tokens, inference calls, embeddings, retrieval, evals, human review. The number Module 3's Margin Calculator helps you put a value on per user.
*Seen in: M3, Slide 6.*

### Base fee + per-unit pricing

A hybrid pricing structure: customers pay a recurring base for access plus a usage fee per unit of work. Example from Module 3: $49/month base + $0.75 per resolved support conversation.
*Seen in: M3, Slide 18.*

### Board one-pager

A before-and-after comparison of your current vs. AI-enhanced model that shows revenue, cost, gross margin, and the net margin shift that justifies the bet. The closing section of `03-the-margin/cost-curve.md` after Cost Model, Cascading Strategy, Pricing Model, and Stress Tests.
*Seen in: M3, Slides 19-20.*

### Break-even

The point where revenue covers cost. In Module 3, break-even thinking shows up across the **Pricing Model** section (current vs. proposed pricing, and the unit you charge for) and the **Stress Tests** table of `cost-curve.md` — what survives if inference costs 3x, your heaviest segment doubles, or your model provider raises prices 50%. The Board One-Pager then captures the net margin shift that justifies the bet.
*Seen in: M3, Slides 18, 20.*

### COGS (Cost of Goods Sold)

The direct cost of delivering your product. In classic SaaS this is mostly fixed (servers, hosting). In AI it includes a large variable component (tokens, inference) that scales with usage.
*Seen in: M3, Slide 6.*

### Cost curve

A map of how your AI cost grows as usage grows. Built by tagging every AI feature in your product with a model tier and a per-call estimate. Captured in the **Cost Model** table and **Cascading Strategy** section of `03-the-margin/cost-curve.md`.
*Seen in: M3, Slides 16-17.*

### Fixed vs. variable cost

Fixed costs don't change with usage (servers, salaries). Variable costs do (tokens, inference, retrieval). The Module 3 punchline: AI shifts a meaningful share of cost from fixed to variable, which is why scale alone doesn't fix unit economics.
*Seen in: M3, Slides 5-6.*

### Gross margin

Revenue minus COGS, expressed as a percentage. Classic SaaS runs at 80%+. AI products often run at 40-65% before you apply the levers. A lower margin can still be a winning move if revenue and gross profit are both up.
*Seen in: M3, Slides 6, 13, 20.*

### Hybrid pricing

A pricing model that combines a base fee for access with a usage fee for the work done. The middle ground between pure seat pricing and pure outcome pricing.
*Seen in: M3, Slide 9.*

### Leader / Filler / Killer

The bundling lens, told through a Big Mac. The **Leader** is what the customer comes for (your core intelligence). The **Filler** bumps the average order (lightweight features). The **Killer** is too heavy or too different to bundle (image generation, agent workflows) - sell it separately.
*Seen in: M3, Slide 11.*

### Margin compression

When the percentage profit per unit shrinks. Module 3's premise: AI compresses margins before it expands revenue, because variable costs land before pricing can adapt.
*Seen in: M3, Slides 5-6.*

### Maximize strategy

A pricing posture that captures the highest possible value from each customer through hybrid or outcome-based pricing - the GitHub Copilot or Microsoft model.
*Seen in: M3, Slide 18.*

### Model cascading

Routing each request to the cheapest model that can handle it well, and saving the frontier model for the hard cases. The single highest-leverage lever for protecting AI margin.
*Seen in: M3, Slide 7.*

### Outcome-based pricing

Charging for the unit of work the customer actually values - a resolved support conversation, a generated lead, a completed task. Intercom Fin is the standout example.
*Seen in: M3, Slide 9.*

### Penetrate strategy

A pricing posture that uses lower prices to win share quickly - the Amazon model.
*Seen in: M3, Slide 18.*

### Seat-based pricing

Charging per user with access to the product. Standard in classic SaaS. Breaks both ways for AI: heavy users get away with massive value for the same price, while light users churn because they don't see enough value to renew.
*Seen in: M3, Slides 5, 9.*

### Skim strategy

A pricing posture that captures premium value from a smaller, willing-to-pay segment - the Apple model.
*Seen in: M3, Slide 18.*

### Unit economics

The cost and revenue of a single unit (a user, a transaction, a conversation). When unit economics are negative, scaling makes the loss bigger and faster - the inverse of the classic SaaS playbook.
*Seen in: M3, Slide 5.*

---

## 4. Trust & Reliability

### Confidence tiers

The three explicit modes a good AI product ships with, not one. **Confident (>90%):** direct answer, no hedge, often auto-applied. **Uncertain (50-90%):** softening language, confidence bar, "double-check this," surfaced citations or alternatives. **Not confident (<50%):** block, escalate, route to human queue - with the *why* visible to the user.
*Seen in: M4, Slide 12.*

### Confidence UX

The product surface that makes the model's uncertainty visible to users - confidence scores, source citations, "I'm not sure" copy, alternative suggestions, soft hedges, override buttons. Module 4's central design move: legibility is what makes a probabilistic system feel controllable, and *understandable and controllable beats accurate-but-opaque every time.*
*Seen in: M4, Slides 6 and 12.*

### Eval Dashboard

The screen-shareable view that ties trust infrastructure together. Four blocks: metrics (quality, latency, confidence spread, HITL percentage, override rate); judge setup (model, rubric, gold-set rows, thresholds); drift alerts (automatic pings when something slips); UX hooks (confidence in the product, citations, thumbs feedback). The acid test: can you screen-share this in a sales call?
*Seen in: M4, Slide 16.*

### Legibility (vs. accuracy)

Module 4's central reframe of trust. Users don't need perfect AI - they need to understand when it's confident, when it's uncertain, and when to override. A legible 85% system with confidence scores, citations, and an override button beats a black-box 95% system every time. Trust is a function of perceived control, not the accuracy percentage.
*Seen in: M4, Slide 6.*

### Reliability contract

The explicit promise your product makes to users about quality, response time, escalation, and feedback loops. Captured as a four-row table - **Metric / Target / Measurement / Alert** - in `04-the-contract/golden-dataset.md`. Specific numbers only; aspirational targets fail in audits. The artifact that survives a board question of "what if you're wrong?"
*Seen in: M4, Slides 17-18.*

### Trust ≠ Accuracy

The headline reframe of Module 4. Trust comes from perceived control - confidence signals, override paths, citations - not from a benchmark percentage. The implication for product design: invest in legibility surface area before chasing the last accuracy points.
*Seen in: M4, Slides 5-6.*

---

## 5. Governance & Compounding

### Adjacent spend

The total monthly amount your *users* are paying for external AI tools to do things adjacent to your product (ChatGPT Plus to summarize your exports, Zapier+OpenAI to enrich your output, etc.). The third summary stat in the M5 Shadow AI Audit, and the one that turns roadmap-review heads - it's the budget that becomes available the moment you ship the native version. Renamed from "hidden spend" in the reframed user-side audit (see *Shadow AI* for the two lenses).
*Seen in: M5, Slide 19; M5 - Shadow AI Audit tool.*

### Active / Broken / Missing

The three honest status labels for a feedback loop. **Active** = shipping and learning today. **Broken** = exists on paper but doesn't actually feed back (corrections logged but never reviewed). **Missing** = the loop just isn't there. Most rows on most products come back `missing` and that *is* the finding.
*Seen in: M5, Slide 8.*

### Agent topology

A short map of who can do what, drawn at the system level. For each agent: what it can do, what it can't do, and who approves what. Optional block in `compounding-system.md` - skip unless your product actually ships agents.
*Seen in: M5, Slide 14.*

### Allow-list (whitelist)

The explicit list of tools, APIs, or actions an agent is permitted to call. The opposite of a deny-list: everything not on the list is forbidden by default. One of the three sub-controls under the Tool Calls governance knob (allow-list + rate-limit + log).
*Seen in: M5, Slide 10.*

### Audit cadence

How often you review the AI system's outputs and decisions against your golden dataset or live traffic. Real-time / daily / weekly / monthly / quarterly. Naming the *owner* matters as much as picking the cadence - "weekly" without an owner is aspirational.
*Seen in: M5, Slides 13-14.*

### Autonomy boundaries

What an agent can do solo vs. what needs a human. Two key splits: *draft ≠ send* (it can write the email; sending requires approval) and *read ≠ write* (it can pull data; modifying or sending it is gated). One of the four agent governance knobs.
*Seen in: M5, Slides 10 and 14.*

### Build / Partner / Ignore

The three decisions in the user-side Shadow AI Audit. **Build** = absorb the capability natively into your product (you kill the workaround by making it unnecessary). **Partner** = strike an official integration with the external tool users are already chaining. **Ignore** = accept that some users will keep doing it externally - it's not strategic for you to own. *Ignore* is a legitimate decision; the trap is calling everything "Build" because building feels like ambition. Replaces the older *keep / govern / kill* triage from the CISO-flavored audit (see that entry for the mapping).
*Seen in: M5, Slide 19; M5 - Shadow AI Audit tool.*

### Bias posture

Your public stance on how the AI handles fairness, demographic differences, and edge-case populations - and what mitigations you've put in place. Part of the Level-3 (Governance = GTM) maturity story; appears in enterprise procurement questionnaires.
*Seen in: M5, Slide 9.*

### Chain (agent chain)

A sequence of agents where one agent's output is the next agent's input. The governance question: when agent B fails on agent A's output, who owns the handoff? The fourth governance knob is about naming ownership at each handoff and having a "stop the chain" trigger if any agent in the line fails its eval.
*Seen in: M5, Slide 10.*

### Compounding system

A product whose value grows non-linearly with use because each interaction makes the next one better. Distinct from a product that merely *scales* (more users, same quality). The economic difference is that compounding products have falling cost per win over time; scaling products have linear cost.
*Seen in: M5, Slide 6.*

### Context connectivity

How knowledge flows across teams, products, or domains inside an org - and where it silos. A context-connectivity break is the single most common reason a feedback loop dies: the support team's corrections never reach the eng team's models, so the product never actually learns from real usage.
*Seen in: M5, Slide 8.*

### Cross-domain transfer

Compounding mechanism where improvements in one product or feature lift adjacent products or features that share context. ServiceTitan is the anchor: 32 products on one vertical stack, where HVAC scheduling data makes invoicing smarter, which makes dispatching smarter.
*Seen in: M5, Slide 6.*

### DPA (Data Processing Agreement)

A contract between a customer and a vendor that defines how the vendor will handle the customer's data - retention, access, geography, training-data use. Step 2 of the shadow AI audit is partly about asking "does this tool have a DPA we've signed?" Many shadow AI tools don't, which *is* the risk.
*Seen in: M5, Slide 13.*

### Escalation triggers

When the AI must hand off to a human. Common triggers: confidence below threshold, customer-facing novel content, anything legal / financial / medical, anything irreversible, repeated turns in a single conversation. The M5 governance policy field; specifying them is what separates a real policy from a wish-list.
*Seen in: M5, Slide 14.*

### EU AI Act

The European Union's regulation of AI systems by risk tier - minimal, limited, high, and prohibited. Force of law in the EU. Most B2B products land in *limited risk*; some in *high risk*. The first thing to reference in the Regulatory Exposure field of your governance policy.
*Seen in: M5, Slides 5, 9, 14.*

### Feedback loop

A single learning circuit in your product. The minimal description has four parts: input, output, compounds Y/N, and status (active / broken / missing). Module 5's first lab maps three feedback loops per product.
*Seen in: M5, Slide 8.*

### Freeze test

The forcing function for telling compounding from scaling. Mentally freeze the product for **3 months** (one frontier-model cycle) - no updates, no model swaps, no improvements. If it's still winning, you're scaling, not compounding. The 12-month version is too long for an AI cycle; 3 months is more honest.
*Seen in: M5, Slide 8.*

### Frontier cycle

A rough unit of time in AI - about 3 months between major frontier-model releases. Used in the freeze test as a more honest forcing function than the older 12-month version.
*Seen in: M5, Slide 8.*

### GDPR (General Data Protection Regulation)

EU privacy regulation governing personal data of EU residents, regardless of where the data is processed. In an AI context: minimize personal data in prompts, don't train on customer PII without consent, document a lawful basis. Standard line in the Regulatory Exposure field.
*Seen in: M5, Slides 5 and 14.*

### Governance = GTM

Level 3 of the Responsible AI Maturity ladder. The reframe that governance done well is a *sales asset*, not a compliance burden. Salesforce's Einstein Trust Layer is the textbook case - they sell governance as part of the product pitch.
*Seen in: M5, Slide 9.*

### HIPAA (Health Insurance Portability and Accountability Act)

US healthcare-data privacy law. Relevant for any product that handles patient data; impacts memory class choices (you almost never want long-term or shared memory for PHI), audit cadence, and Business Associate Agreements with vendors.
*Seen in: M5, Slides 10 and 14.*

### Keep / Govern / Kill

The original triage labels for the internal/CISO-flavored shadow AI audit: **Keep** (safe, in use), **Govern** (useful but needs guardrails), **Kill** (data path unsafe, no realistic fix). M5 uses the user-side reframe, where the equivalent decisions are **Build / Partner / Ignore** — same three slots, different question (what does this workaround tell us to do with our roadmap?). The repo template's placeholder still shows `keep / govern / kill` because the template is frozen — overwrite it with build/partner/ignore when you fill in your audit.
*Seen in: M5, Slide 19 (mapped onto Build/Partner/Ignore).*

### Memory (short / long / shared)

What an AI agent remembers between turns and between users. Three explicit classes: **short-term** (just this session, then wiped), **long-term** (persists across sessions for the same user), **shared** (across users - usually a hard no for customer-facing). The third governance knob.
*Seen in: M5, Slide 10.*

### Model card

A short, public-ish document that describes a model's intended use, limitations, evaluation results, and known biases. Originated at Google. A standard Level-3 maturity artifact and a common enterprise-procurement ask.
*Seen in: M5, Slide 9.*

### Network intelligence

Compounding mechanism where patterns across the whole user base or fleet improve individual interactions - privacy-gated, usually anonymized. The aggregate is smarter than any single user's history.
*Seen in: M5, Slide 6.*

### Rate-limiting

A cap on how often an agent can call a particular tool (e.g. 10 refunds per hour). Pairs with allow-listing: even a permitted tool shouldn't be callable infinitely. One of the three sub-controls under the Tool Calls governance knob.
*Seen in: M5, Slide 10.*

### Recursive learning

Compounding mechanism where the product's own outputs (and corrections to them) feed back into the model. The cleanest anchor: every Duolingo learner interaction sharpens lesson difficulty for the next learner.
*Seen in: M5, Slide 6.*

### Regulatory exposure

Which legal regimes apply to your AI product - EU AI Act risk tier, plus GDPR / CCPA / HIPAA / SOC 2 / sector-specific (finance, healthcare, education). The M5 governance policy field. Be specific about both the regime and the risk tier inside it.
*Seen in: M5, Slide 14.*

### Responsible AI Maturity ladder

The three-level reframe of compliance. **Level 1: Compliance** (EU AI Act, GDPR - minimum bar). **Level 2: Trust Architecture** (evals, confidence UX, reliability contracts - what M4 built). **Level 3: Governance = GTM** (governance as a deal-closer). Most orgs plateau at Level 1 or 2.
*Seen in: M5, Slide 9.*

### Scales vs. compounds

The central reframe of the first half of M5. *Scales*: ↑ volume, flat quality, linear cost - a commodity with variable costs. *Compounds*: each touch → smarter next touch, falling cost per win. Most AI products scale without compounding and don't realise it until a competitor's compounding loop eats their lunch.
*Seen in: M5, Slide 6.*

### Shadow AI

Two related lenses, only one of which is a PM's job:

- **Internal / CISO lens (Samsung-style):** AI tools in use inside your org without sanctioned governance, allow-listing, or oversight. Includes unauthorized external SaaS (ChatGPT, Claude, niche copilots) and employee-paid personal subscriptions used for work. Real problem, but structurally it's a security/IT/CISO responsibility, not product. The Samsung case is the canonical "what happens when shadow AI meets real data" story for this lens.
- **User-side / PM lens (the M5 framing):** What your *users* are building with AI on top of, alongside, or to replace pieces of your product. Pasting your exports into ChatGPT to summarize them, wiring Zapier into your API for LLM enrichment, asking ChatGPT to interpret your pricing page. This is what M5 redirects the Shadow AI Audit toward, because it's the lens PMs can actually act on — every workaround is either a feature request you weren't reading as one, or a capability someone else will ship before you do.

*Seen in: M5, Slide 12 (Samsung / CISO lens), Slides 13, 18-19 (user-side / PM lens).*

### Shadow AI Audit (user-side)

The M5 reframed audit: a four-step diagnostic - **Discover → Signal → Prioritize → Decide** - that surfaces the AI workarounds your users have built around your product, classifies the signal each one carries, and decides whether to build, partner, or ignore. Output is a five-row table plus three summary stats (Workarounds found · Build candidates · Adjacent spend). Read as roadmap discovery research, not as a compliance audit.
*Seen in: M5, Slides 13, 18-19; M5 - Shadow AI Audit tool.*

### Signal types (workflow / trust / capability / pricing)

The four labels used to classify each user-side AI workaround in the Shadow AI Audit. **Workflow gap** - users are chaining your output into another step you don't support natively. **Trust gap** - users are double-checking your output with another model because they don't trust yours. **Capability gap** - users want something your product doesn't do at all. **Pricing gap** - users are getting the value externally because it's cheaper or metered differently. Each signal type points to a different roadmap move: workflow → Partner, trust → re-open M4 (reliability contract / confidence UX), capability → Build, pricing → re-examine packaging before assuming you need to build more.
*Seen in: M5, Slides 13, 19; M5 - Shadow AI Audit tool.*

### SOC 2

A widely-used set of security and operational controls audited by an independent firm. Relevant for AI products because log retention, access control, and incident response sit inside the SOC 2 boundary. Often appears in the Regulatory Exposure field alongside (not instead of) EU AI Act and GDPR.
*Seen in: M5, Slide 14.*

### Tool calls

The function calls an agent makes to external systems - search, refund, send email, query database, etc. Every tool call is a potential risk surface, which is why the second governance knob bundles three controls together: allow-list (which tools), rate-limit (how often), log (every call, with reasoning and result).
*Seen in: M5, Slide 10.*

### Traditional RPA (Robotic Process Automation)

Pre-AI workflow automation - UiPath, Automation Anywhere, Blue Prism. Fixed paths, deterministic, breaks on edge cases, linear ROI. M5 contrasts it with agentic automation because finance teams will compare agent investments to the RPA budget line and the economics are completely different.
*Seen in: M5, Slide 11.*

### Trust Architecture

Level 2 of the Responsible AI Maturity ladder. What you built in M4 - golden datasets, confidence UX, reliability contracts, eval dashboards. Trust-as-infrastructure rather than trust-as-marketing. Most teams that take AI seriously land here; the jump to Level 3 (GTM) is what's left undone.
*Seen in: M5, Slide 9.*
