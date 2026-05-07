# Concepts Primer (Pre-Read)

*A friendly orientation for the AI Product Strategy course. Read this before a session if you're new to AI vocabulary, or any time the room moves faster than feels comfortable. It is not a replacement for sessions - it's the on-ramp.*

---

## Why this exists

A lot of the course assumes a baseline familiarity with how AI products actually work and how they make and lose money. If your last serious exposure to "models" was a stats class, or you've shipped AI features without ever opening your provider's billing page, this read closes the gap quickly. Twenty minutes here makes every session land harder.

For full definitions of any term that shows up below, see [`Glossary.md`](./Glossary.md). For frameworks at a glance, see [`Frameworks Reference Card.md`](./Frameworks%20Reference%20Card.md).

---

## How an AI product actually works under the hood

Every modern AI product is, underneath the polish, doing some version of the same loop:

**A user does something → your product builds a prompt → the prompt is sent to a model → the model produces a response → your product shows the response.**

That sounds simple. The interesting decisions hide inside each arrow.

### The prompt

A prompt is the instruction (and any context) you send to the model. "Summarize this email" is a prompt. So is the much longer version your product actually sends, which probably looks something like:

> *You are a helpful sales assistant. Here is the customer's last 30 emails: [...]. Here is their CRM record: [...]. The user just clicked "draft a reply." Write a reply in their voice that addresses the pricing question and offers a meeting next week.*

That whole blob is the prompt. The longer it is, the more it costs.

### Tokens

Models bill per **token**, not per word or per request. A token is roughly three-quarters of an English word. Both the prompt going in and the response coming out cost tokens. Whenever someone in the course says "$0.03 per call," they're really shorthand for "this many tokens at this provider's per-token rate."

This matters strategically because cost scales with **how much text moves through your product**, not how many users you have. A single power user running a long workflow can move more tokens than a hundred casual ones.

### The model

The model is the trained AI system that turns the prompt into a response. Models come in **tiers**:

- **Frontier models** (GPT-5, Claude Opus, Gemini Pro) - the most capable and the most expensive. Use them for genuinely hard reasoning.
- **Small / cheap models** (GPT-mini, Claude Haiku, Llama variants) - fast, cheap, often "good enough" for the bulk of requests.

The single biggest mistake teams make in their first cost model is defaulting every call to a frontier model. Module 3 calls this out hard. Most products that run in the black do it by **routing** different requests to different tiers - this is called **model cascading**, and it's the #1 margin lever in AI.

### Context window

The context window is the amount of text the model can "see" in one go. Bigger windows let you stuff more documents, history, or instructions into a single call. They also cost more, because you pay for every token in the window. When models get bigger windows, teams tend to fill them, and total cost goes up even when per-token prices fall.

### Embeddings and RAG

If your product needs to answer questions using your customer's own data (their docs, their tickets, their CRM, etc.), it almost certainly uses something called **Retrieval-Augmented Generation, or RAG**.

The pattern:

1. Take all your customer's documents and convert them into **embeddings** - numerical fingerprints that capture meaning.
2. When a user asks a question, embed the question too.
3. Find the documents whose embeddings are most similar to the question.
4. Stuff those documents into the prompt alongside the question.
5. Send to the model.

You don't need to build this to understand it. But you should know that **embeddings get called constantly** - every search, every lookup, every "find me similar" feature. They are a frequently underestimated cost line in early cost models.

### Agents

An **agent** is an AI system that takes multiple steps on its own. Instead of a single prompt-and-response, it can call tools, make decisions, loop until done. Agents are powerful and expensive. One agent running for a day can cost more than a hundred regular conversations - which is why Module 3 keeps treating agent workflows as a "Killer" in bundling decisions: heavy enough to break a flat-rate plan.

### Why outputs are probabilistic

Traditional software is **deterministic**: same input, same output, every time. AI is **probabilistic**: the model is choosing the next token by sampling from a distribution. The same prompt can produce slightly different answers each time. Outputs can be confidently wrong (this is called a **hallucination**). Quality can shift over time as the underlying model is updated (this is called **drift**).

This is why every serious AI product needs **evals** - automated tests that score whether the model's outputs meet your quality bar. Module 4 goes deep on this. For now: just internalize that "the AI gave a bad answer" is not a bug to be fixed once - it is a baseline condition you have to design around.

---

## Where the money goes

Most PMs walking into Module 3 cannot answer a simple question: **what does it cost us to serve one user for one month?** The reason is that AI economics work differently from SaaS economics, and the gap between the two is where teams get into trouble.

### Classic SaaS: cost is mostly fixed

In classic SaaS, once you've built the product, adding another customer is almost free. You spin up a server. You add a row to the database. The marginal cost of one more user is tiny. That's why software companies historically run at 80%+ gross margins.

### AI: cost is mostly variable

In AI, every prompt, retrieval call, model call, eval, and generated answer can add cost. Cost scales with **what users do**, not just **how many they are**. Two products with the same number of users can have wildly different cost structures depending on how heavily their users use the AI.

### "AI COGS"

When the course says **AI COGS** (Cost of Goods Sold), it means everything you pay to deliver the AI part of your product:

- **Inference** - paying the provider for every model call.
- **Infrastructure** - hosting, storage, the servers that orchestrate calls.
- **Data and storage** - your vector database for embeddings, your retrieval indexes.
- **Human review** - the humans who check or correct AI outputs (often forgotten).

In the Margin Calculator you build in Module 3, this is what gets summed into "AI COGS per user per month."

### Why one power user can outweigh a hundred casual ones

Imagine two users on the same $20/month plan:

- **User A** logs in once a week, asks one question, leaves.
- **User B** runs a workflow that calls the AI 500 times a day.

Both pay $20. User A costs you maybe $0.50 a month in AI COGS. User B might cost you $80. You are losing $60 every month on User B, and you're being told by your sales team to "go close more users like B because they love the product." This is exactly the asymmetry Module 3 is designed to surface.

### The three "security blankets" that don't actually save you

Module 3 calls out three beliefs that feel reassuring but don't protect AI margins:

1. **"Costs will come down."** Token prices probably will keep falling. But if cheaper models tempt your team to add more agents, longer windows, more retries, total cost still goes up.
2. **"Seat pricing works."** Seat pricing charges for access. AI creates value by doing work. The two stop matching.
3. **"Scale fixes everything."** True for SaaS. False for AI when unit economics are negative. Scale just makes the loss faster.

The fix is not pessimism. The fix is **architecture plus pricing**: route simple work to cheap models, cache what can be reused, cap expensive workflows, package usage smartly, and price against the work the system actually performs. That's the whole back half of Module 3.

---

## Why AI strategy is "different"

Module 1's premise is that traditional product strategy quietly assumes five things that AI breaks. It's worth holding all five in your head as you go through the course - because each row is, basically, the question one of the modules answers.

| What traditional strategy assumes | What AI actually does |
|---|---|
| A feature works or it doesn't | Outputs are probabilistic - accuracy, hallucination, drift |
| Infrastructure scales predictably | Inference costs scale with usage, not users |
| Your product competes with theirs | Your feature becomes a platform's checkbox overnight |
| Software does what it says | Users have to be convinced to trust uncertain outputs |
| Annual planning cycles | Capabilities change weekly - bets, not plans |

The first row is why Module 4 (The Contract) exists. The second is why Module 3 (The Margin) exists. The third is why Module 2 (The Moat) exists. The fourth is also Module 4. The fifth is Module 1's whole premise.

A second, related point: **model curves don't follow fiscal years.** A capability you assume in your Q3 plan might arrive (or get commoditized) twice between now and then. This is why the course keeps pushing you toward **bets and kill criteria** instead of "ship X by date Y → outcome Z." The discipline is to write down what you'd need to see to keep going - and what would make you stop.

A third: **platform risk is a real category.** When OpenAI ships a feature inside ChatGPT, or Microsoft bundles something into Teams, the value of being a standalone tool that does the same thing collapses overnight. The Three-Axis Diagnostic in Module 1 forces you to score this honestly. Most first attempts at the diagnostic give Platform Risk a 4 ("we're fine") and the partner exercise lowers it to a 2.

---

## Vocabulary you'll keep hearing

These are the strategy terms that recur module-to-module. The full definitions live in [`Glossary.md`](./Glossary.md); a one-liner each here as a memory aid:

- **Moat** - whatever makes it hard for someone to copy you. Workflow depth and proprietary loops are the two that hold up best in AI.
- **Flywheel** - the loop where usage produces signal, signal improves the product, and the better product drives more usage. Module 2's central idea.
- **Kill switch** - the architecture (abstraction layer + multi-model routing + evals) that lets you swap AI providers in under 48 hours. Module 2.
- **Encroachment** - the three ways someone moves on your space: a platform shipping it natively, a vertical specialist going deeper, or an adjacent tool adding it as one more feature. Module 2.
- **Cascading** - routing each request to the cheapest model that can handle it well. Module 3's #1 margin lever.
- **Leader / Filler / Killer** - bundling lens. Leader is what users come for, Filler bumps the average order, Killer is too heavy or too different to bundle. Module 3.

---

## How to use the rest of the course materials

Each module gives you four things to draw on:

1. **The slide deck** (`Module N - Slides.html`) - what was on screen during the session.
2. **The shareable companion notes** (`Module N - Notes (Shareable).md`) - per-slide walkthrough in plain prose, for review at your own pace.
3. **The interactive tools** (`M{N} - {Tool Name}.html`) - calculators, scorecards, and audits that turn the framework into something you can actually fill in. Built to save state in your browser so you can come back to them.
4. **Your forked strategy repo** - the place where the artifacts you build in each module accumulate. By Module 6, the repo *is* your strategy.

If you ever feel lost mid-session, the order to reach for them is: **slides for what we covered → companion notes for the argument → glossary for the term → primer (this doc) for the underlying concept.** And come ready to ask questions in Slack.
