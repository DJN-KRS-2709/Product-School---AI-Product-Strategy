# Module 2 Glossary

*The terms introduced in Module 2 - The Moat. For Module 1's terms, see [`Module 1 - Glossary.md`](./Module%201%20-%20Glossary.md). For the full course-wide reference, see [`Glossary.md`](./Glossary.md).*

Two sections:

1. **AI/ML Foundations** - the technical terms that come up in moat and kill-switch work.
2. **Strategy Concepts** - the frameworks Module 2 introduces.

---

## 1. AI/ML Foundations

### Abstraction layer

A piece of code that sits between your product and any specific AI provider so the rest of the codebase calls a generic interface (something like `ai_gateway.search()`) instead of OpenAI or Anthropic directly. Without one, swapping providers means rewriting calls everywhere.
*Seen in: M2, Slide 18 (The Kill Switch).*

### Eval / Eval harness

An automated test suite that scores whether the AI is producing good outputs against a known set of expected answers. The eval harness is what proves a replacement model meets your quality bar before you switch.
*Seen in: M2, Slide 18 (the Eval dimension of the Kill Switch audit). Goes much deeper in M4.*

### Fine-tuning

Taking a base model and continuing to train it on your own data so it gets better at a specific task or domain. Distinct from prompting - fine-tuning changes the model itself.
*Seen in: M2, Slide 11 (the "automated retraining" end of the Correction loop).*

### Multi-model routing

Logic that decides, for each request, which model to send it to - based on cost, latency, quality, or task type. The Routing dimension of the Kill Switch audit and the mechanism that makes cascading possible (cascading itself shows up in M3).
*Seen in: M2, Slide 18.*

### Retrieval-Augmented Generation (RAG)

A pattern where the system first searches your own data (using embeddings) for the most relevant snippets, then feeds those snippets into the model alongside the user's question. This is how AI products get answers grounded in proprietary or recent information instead of just the model's training data.
*Seen in: M2 throughout (proprietary domain context is what RAG retrieves over).*

---

## 2. Strategy Concepts

### Correction loop

One of the four loops in the Data Flywheel. Measures whether users fix the AI's outputs and whether that signal gets reused to improve the system. Score 1 = no capture; Score 5 = automated retraining.
*Seen in: M2, Slide 11.*

### Data Flywheel

The mechanism by which usage creates proprietary signal, that signal improves the product, and the improved product drives more usage. The central reframe of Module 2: **the moat is loops, not data.**
*Seen in: M2, Slide 10.*

### Domain Context loop

One of the four loops in the Data Flywheel. Measures whether the product learns details that generic models don't know - and whether usage in one area improves quality elsewhere. Score 1 = siloed; Score 5 = cross-domain transfer.
*Seen in: M2, Slide 11.*

### Encroachment

When a competitor moves into your space. Module 2 names three vectors: **Platform encroachment** (a platform like Microsoft or Salesforce ships your feature natively), **Vertical competitor** (a startup goes deeper than you in one narrow niche), **Adjacent expansion** (a nearby tool adds your feature using its existing distribution).
*Seen in: M2, Slide 14.*

### Kill Switch

The strategy for escaping AI vendor lock-in. The audit in `02-the-moat/kill-switch.md` runs across **four dimensions**: **Provider** (who you depend on), **Abstraction** (a generic interface in your code), **Routing** (multi-model routing by cost / latency / quality), and **Eval** (automated tests that prove a replacement model meets your quality bar). Each dimension gets an H / M / L risk rating and a 48-hour action. The whole stack gets a Portability Score: Ready / Partial / Locked. The test: could you swap providers in under 48 hours?
*Seen in: M2, Slide 18.*

### Network loop

One of the four loops in the Data Flywheel. Measures whether each new user or team makes the product better for everyone. Score 1 = isolated; Score 5 = strong network effects.
*Seen in: M2, Slide 11.*

### Preference loop

One of the four loops in the Data Flywheel. Measures whether the product learns individual or team preferences over time. Score 1 = stateless; Score 5 = deep personalization.
*Seen in: M2, Slide 11.*

### The 8 Moats

The classic moat types: **Data, Workflow, Regulatory, Distribution, Ecosystem, Network, Physical, Scale.** For AI products, the two that usually matter most are Data and Workflow.
*Seen in: M2, Slide 6.*

### Workflow depth

A spectrum from shallow to deep: **Chatbot → Embedded feature → Workflow layer → Operating system.** The deeper your product sits in how the business actually works, the harder it is for a competitor to copy the value by copying the feature.
*Seen in: M2, Slide 8.*

### Wrapper vs. Workflow

The framing for Module 2. A **wrapper** is a thin UI on top of someone else's model - features get eaten when the model provider ships them natively (Jasper is the cautionary tale). A **workflow** is embedded deeply enough in how users work that it survives.
*Seen in: M2, Slide 7.*
