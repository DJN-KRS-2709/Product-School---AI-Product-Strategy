# Lenny's Newsletter & Podcast — Insights for AI Product Strategy Course

Pulled from Lenny Rachitsky's archive. Organized by module relevance.

---

## High-Value Sources (read these first)

| Source | Type | Why it matters |
|--------|------|----------------|
| **Counterintuitive advice for building AI products** | Newsletter (Jul 2024) | 20+ builders interviewed — lessons from Adobe, GitHub, Intercom, Perplexity, Canva, Runway, Superhuman. Directly maps to M1. |
| **Beyond vibe checks: A PM's complete guide to evals** | Newsletter (Apr 2025) | By Aman Khan (Arize AI, ex-Spotify/Cruise/Apple). The definitive evals guide for PMs. Core M4 material. |
| **Building eval systems that improve your AI product** | Newsletter (Sep 2025) | By Hamel Husain & Shreya Shankar (#1 Maven course on evals). Goes deeper than the first evals post — error analysis, LLM judges, continuous improvement flywheel. M4 gold. |
| **Pricing your AI product: Lessons from 400+ companies** | Podcast (Jul 2025) | Madhavan Ramanujam (Simon-Kucher, author of Monetizing Innovation). 250+ companies, 20+ unicorns. Core M3 material. |
| **Business strategy with Hamilton Helmer (7 Powers)** | Podcast (May 2024) | The original moats framework that Gokul's 8 Moats adapts. Power = benefit + barrier. Moat ≠ power. Directly maps to M2. |
| **Why your AI product needs a different development lifecycle** | Newsletter (Aug 2025) | CC/CD framework from 50+ AI implementations. Non-determinism, agency vs control tradeoff. Core M1 framing. |
| **OpenAI's CPO on moats, evals, and startup playbooks** | Podcast (Apr 2025) | Kevin Weil on why evals are a core PM skill, which markets OpenAI won't enter, and what skills matter in AI. M1/M4/M6. |
| **"Dumbest idea I've heard" to $100M ARR: Gamma** | Podcast (Nov 2025) | Grant Lee on building in a non-consumption market. 50M users, 30 people, profitable. Perfect M1 non-consumption example. |
| **25 proven tactics to accelerate AI adoption** | Newsletter (Aug 2025) | Shopify, Zapier, Duolingo, Intercom, Whoop, Ramp tactics. Shadow AI angle. Directly maps to M5. |
| **What AI means for your product strategy (Intercom)** | Podcast (Oct 2023) | Paul Adams on going all-in on AI. Early and honest look at the strategic bet. M1 framing. |

---

## Module 1 — The Bet

### "Counterintuitive advice for building AI products" (Newsletter)
- Interviewed 20+ builders from Adobe, GitHub, Intercom, Perplexity, Canva, Runway, HeyGen, Superhuman
- Key lesson: "You first need to learn to think differently" — AI products break traditional PM assumptions
- AI embracers vs. skeptics behave very differently — requires rethinking user segmentation
- Builders had to rethink their entire user testing approach for AI features

### "Why your AI product needs a different development lifecycle" (Newsletter)
- AI products are inherently **non-deterministic** — unpredictability on both input and output side
- Every AI product negotiates a tradeoff between **agency** and **control**
- The CC/CD (Continuous Calibration / Continuous Development) framework from 50+ implementations
- "You can't build AI products like other products" — reinforces the probabilistic thinking lecture
- Demo → production gap is where most teams fail

### Gamma Podcast — Grant Lee
- Built a presentation tool that investors called "the dumbest idea" — now $100M ARR, $2B valuation
- 50M users with a 30-person team, profitable
- **Non-consumption market in action**: didn't improve PowerPoint — created a new behavior
- Perfect case study for the non-consumption insight already in M1

### AI Engineering 101 — Chip Huyen (Nvidia, Stanford)
- "A lot of companies are building AI products. A lot of companies are not having a good time."
- Most companies try AI, it doesn't do a lot, they stop — the execution gap
- Focus on user feedback over keeping up with AI news: "If you talk to users and understand what they want, you can improve the application way more"
- "People are somehow stuck. They don't know what to build." — validates the M1 diagnostic approach

### Microsoft CPO — Aparna Chennapragada
- Oversees AI product strategy for Microsoft's productivity tools and agents
- Prototyping with AI is essential — "if you aren't prototyping with AI, you're doing it wrong"
- Reinforces the Prototype Bet exercise in M1

---

## Module 2 — The Moat

### Hamilton Helmer — 7 Powers (Podcast)
- **Power = benefit + barrier**. Moat is the barrier part only. You can have a moat around an undesirable property
- "Operational excellence can be mimicked" — speed/execution are not powers
- **Power progression**: certain types of power become available at certain times
- His understanding changed: strategy isn't just post-PMF — you should think about it from day one
- Warren Buffett: "I look for economic castles protected by unbreachable moats"
- Directly connects to Gokul's 8 Moats framework (Gokul adapted Helmer's 7 Powers for AI)

### Andrew Wilkinson — 75+ Businesses (Podcast)
- Looks for moats like Buffett: brand, switching costs, network effects, regulatory
- "Switching costs" in practice: "If you're running your business on Shopify, and you've got thousands of products, and all your analytics are there — you're not switching"
- Some businesses have no moat — they fall apart when a competitor enters

### OpenAI CPO — Kevin Weil
- On which markets OpenAI won't go after: they won't launch verticalized products (e.g. an AI sales agent) — that's the opportunity for startups with domain knowledge
- Reinforces the "platform exposure" axis — knowing where OpenAI/Google WON'T go is strategic

---

## Module 3 — The Margin

### Madhavan Ramanujam — Pricing AI Products (Podcast)
- Author of Monetizing Innovation, worked with 250+ companies (Uber, Asana, DoorDash, LinkedIn)
- "Price is a measure of value" — not just a dollar figure
- 72% of innovations fail from a monetization/commercial perspective because companies didn't validate willingness to pay early enough
- Pricing should sit in the product function, not finance: "Design the product around the price"
- Don't "build a product and slap on a price" — monetization must be part of discovery
- Reinforces M3's "design your pricing strategy" exercise

### Naomi Ionita — How to Price Your Product (Podcast)
- "Don't set it and forget it" — revisit pricing every 6-12 months like your roadmap
- Evernote went years before overhauling pricing — a cautionary tale
- First leaders in product-led growth and monetization (Evernote, Reforge)
- 42 mentions of pricing/margins/monetization — deep tactical resource

---

## Module 4 — The Contract

### "Beyond vibe checks: A PM's complete guide to evals" (Newsletter)
- **Evals are "the defining skill for AI PMs in 2025 and beyond"**
- "Every PM building with generative AI obsesses over prompts, yet almost no one masters evaluations"
- Key eval areas: hallucination, toxicity/tone, overall correctness, code generation, summarization quality, retrieval relevance
- Evals should be specific, battle-tested, and test for specific success areas
- Golden dataset angle: "Have a specific set of labeled test cases" with expected outputs
- Open-source tools: Phoenix (Arize), Ragas for RAG-specific evals

### "Building eval systems that improve your AI product" (Newsletter)
- **Phase 1: Error analysis** — ground evals in reality, not fashionable metrics
- Most common mistake: measuring "hallucination" or "toxicity" instead of your actual failure modes
- Designate a single principal domain expert as the arbiter of quality ("benevolent dictator")
- Start with 100 user interactions, do open coding (journaling), then axial coding (pattern-finding)
- "People are not good at specifying their complete requirements for an AI up front — criteria emerge through reviewing outputs"
- **Phase 2: Build evaluation suite** — choose right tool per failure mode (rule-based vs. judgment-based)
- **Phase 3: Operationalize** — create continuous improvement flywheel
- Warning: off-the-shelf metrics are only useful for sorting traces to discover patterns, not as dashboard scores

### OpenAI CPO — Kevin Weil
- "Learning the craft of writing evals is quickly becoming a core skill for product builders"
- Evals are necessary to know whether your model will behave correctly for certain tasks

---

## Module 5 — The Guardrails

### "25 proven tactics to accelerate AI adoption" (Newsletter)
- **"The biggest barrier to AI adoption isn't technology — it's organizational change"**
- Only 8% of US workers use AI daily (Gallup)
- Shopify: AI usage is a 1-5 scale in performance reviews
- Zapier: "code red" moment after ChatGPT launch, gave everyone a week off to practice
- Duolingo: went from 100 courses in 12 years to 150 courses in 12 months with AI
- Intercom CTO: embedded with individual teams weekly to find "2x" opportunities
- Ramp: publishes AI power users (5+ actions/week) by team — transparency creates accountability
- **Shadow AI angle**: "Most companies have long approval processes for AI tools. But employees are already using AI from personal accounts."
- Duolingo gave every employee $300 to try AI tools — cuts the procurement bottleneck
- "True AI adoption happens when teams become skeptical of flashy demos and demand to see rigor"

### Asha Sharma — Microsoft (Podcast)
- "How 80,000 companies build with AI"
- "Products as organisms, the death of org charts, agents will outnumber employees by 2026"
- Patterns across companies that succeed vs. struggle at building AI products

### Chip Huyen — AI Engineering 101
- "We are in an idea crisis — we have all these cool tools but people don't know what to build"
- Managers prefer headcount over AI subscriptions; VPs prefer AI subscriptions over headcount — organizational tension

---

## Module 6 — The Pitch

### Gamma — Grant Lee (Podcast)
- "The dumbest idea" became $100M ARR — narrative about outcomes, not technology
- Counter-intuitive GTM: influencer marketing drove massive growth
- Small team (30), profitable, $2B valuation — the board story writes itself
- Reinforces "lead with the investment thesis, not the architecture"

### Duolingo (from adoption tactics post)
- Went from 100 courses in 12 years → 150 in 12 months — board-ready stat
- CEO defined AI adoption as both "making products better" and "empowering employees"

### Hamilton Helmer — 7 Powers
- "The path to power is where the rubber meets the road"
- Board-level framing: power progression (when to develop which type of power)
- Investors think in terms of power/moats — your board does too

---

## Cross-Module Themes

### Non-determinism as a first principle
- Appears in: Counterintuitive advice, CC/CD framework, Chip Huyen, Kevin Weil
- AI products produce probability distributions, not guarantees — the fundamental shift

### Evals as the hidden lever
- Appears in: Both eval newsletters, Kevin Weil, Chip Huyen
- "Prompts make headlines, but evals quietly decide whether your product thrives or dies"

### Organizational change > technology
- Appears in: 25 tactics post, Asha Sharma, Brian Balfour, Chip Huyen
- Shadow AI, adoption bottlenecks, and governance are organizational problems, not tech problems

### Pricing must be product-led
- Appears in: Madhavan Ramanujam, Naomi Ionita
- 72% of innovations fail commercially because they didn't validate willingness to pay early
- "Design the product around the price" — not the other way around

### Moats require benefit + barrier
- Appears in: Hamilton Helmer, Andrew Wilkinson, Kevin Weil
- Execution speed is NOT a moat. Operational excellence can be mimicked.
- OpenAI won't go vertical — that's the startup opportunity
