# Course Glossary

*A cumulative reference for the terms used across the course. Cumulative through Module 3 - it grows after each session. Use it as a quick lookup when something on a slide or in your repo work doesn't quite click.*

The glossary has three sections:

1. **AI/ML Foundations** - the technical vocabulary you keep hearing.
2. **Strategy Concepts** - the frameworks and ideas that show up across the modules.
3. **Economics & Pricing** - everything from Module 3 about how AI products make and lose money.

Each entry is one or two sentences, plus a `Seen in:` pointer back to the module and slide where the term first lands.

---

## 1. AI/ML Foundations

### Abstraction layer

A piece of code that sits between your product and any specific AI provider so the rest of the codebase calls a generic interface (something like `ai_gateway.search()`) instead of OpenAI or Anthropic directly. Without one, swapping providers means rewriting calls everywhere.
*Seen in: M2, Slide 18 (The Kill Switch).*

### Agent

An AI system that can take multiple steps on its own to complete a task - calling tools, making decisions, looping until done - rather than producing a single response. Agents are powerful and expensive: one running for a day can burn through more cost than a hundred regular conversations.
*Seen in: M3, Slide 9 (a $200/month plan blew up because users ran agent workflows on it).*

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

The most powerful (and most expensive) tier of model from a provider - GPT-5, Claude Opus, Gemini Pro, etc. Use it for genuinely hard work. Default everything to it and your cost curve will hurt.
*Seen in: M3, Slides 6, 7, 17 (cascading is the discipline of not using frontier when you don't need it).*

### Hallucination

When the model produces an answer that sounds confident but is factually wrong. The reason AI products need eval harnesses, golden datasets (Module 4), and human review for high-stakes outputs.
*Seen in: M1, Slide 6 (the probabilistic outputs row).*

### Inference

Running a request through a model to get a response - the live, in-production cost of using AI. Distinct from training. When people say "inference cost," they mean what each call costs you in real time.
*Seen in: M3, Slide 5 (the provocation question: what is your inference cost per user per month?).*

### Model

The trained AI system that takes input and produces output. Models come in tiers (small / cheap / frontier) and from different providers. Your product is almost always making choices about which model to call for which task.
*Seen in: M1, Slide 6; foundational throughout.*

### Multi-model routing

Logic that decides, for each request, which model to send it to - based on cost, latency, quality, or task type. The Routing dimension of the Kill Switch audit and the mechanism that makes cascading possible.
*Seen in: M2, Slide 18; M3, Slide 7.*

### Prompt

The instruction (and any context) you send to the model. Prompt design directly affects cost (longer prompts = more tokens) and quality.
*Seen in: foundational throughout.*

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
