# AI Product Strategy Certification — Course Architecture

**Product School | 6 sessions x 2 hours | Senior PMs, AI-aware**

---

## Positioning

**Reforge** = How to *lead* in the AI era (internal)
**Maven** = How to *build* AI products (tactical)
**Product School** = How to *win* with AI products (strategic + applied)

The only AI product strategy certification where you build your actual strategy — economics model, eval spec, moat analysis, governance framework, and board pitch — across 6 live sessions on your real product.

We learn from the best material out there — Reforge, Maven, top Substack voices — and synthesize it into one coherent arc with our own advanced take. Where there's overlap across sources, it validates the topic. Where there's a gap, we fill it.

---

## Target Audience

Senior product leaders who already understand AI fundamentals (tokens, RAG, fine-tuning, prompting). They've taken AIPC or equivalent. They're here because they need to make strategic decisions about AI products — what to build, how to defend it, how to price it, how to govern it, and how to pitch it to their board.

**This is not a foundations course. This is not an entrepreneurship course.** Participants pick a product at their company and build the AI strategy around it. They don't build a company from scratch — they bring a real product they're responsible for.

Backup: provide example products for anyone not currently at a company, but they assume the PM role for a real product.

---

## The Arc: Six Strategic Questions

Each module answers one question a CPO or board member actually asks. The arc is sequential — each answer depends on the last.

| Module | Title | Strategic Question |
|--------|-------|-------------------|
| M1 | **The Bet** | What should we build, and how do we know fast? |
| M2 | **The Moat** | Why won't this get copied in 6 months? |
| M3 | **The Margin** | Will this make money or bleed it? |
| M4 | **The Contract** | Why will users trust a probabilistic system? |
| M5 | **The Guardrails** | What breaks when this scales? |
| M6 | **The Pitch** | How do you get this funded, shipped, and adopted? |

### Why AI strategy is different (explicit — name it in M1, reinforce every module)

Traditional product strategy assumes deterministic outputs, fixed infrastructure costs, clear competitive boundaries, trust by default, and annual planning cycles. AI product strategy breaks all five:

| Traditional | AI |
|------------|-----|
| Feature works or it doesn't | Outputs are probabilistic — accuracy, hallucination, drift |
| Infra scales predictably | Inference costs scale with usage, not users |
| Your product vs. theirs | Your feature becomes a platform's checkbox overnight |
| Software does what it says | Users must be convinced to trust uncertain outputs |
| Annual planning cycles | Capabilities change weekly — bets, not plans |

This isn't a footnote. It's the reason the course exists. M1 should open with this table before any framework. Each module should tie back to the specific assumption it breaks.

### The underlying shifts (per module)

- M1: Certainty → Probabilistic thinking
- M2: Features → Defensible systems
- M3: Growth-at-all-costs → Margin-aware AI economics
- M4: Shipping functionality → Engineering reliability
- M5: Compliance checklist → Compounding systems that scale
- M6: Roadmap owner → AI systems architect + executive translator

---

## The Throughline Artifact: The Living Strategy

Not a document. Not a PRD. Not a dissertation. A **living strategy repo** — version-controlled, compounding, collaborative. A PRD on steroids that lives in GitHub. Something that beats at a higher frequency than an annual review cycle. Others can contribute via PRs without making this an annual rewrite.

Participants fork a template repo in M1 and build into it across all 6 sessions. Five component folders built across M1–M5 (`01-the-bet/` through `05-the-guardrails/`). M6 finalizes `06-the-pitch/` and the top-level `README.md` — then presents the whole strategy to the room.

| Session | Component | What It Contains | Visual Artifact |
|---------|-----------|------------------|-----------------|
| M1 | **The Bet** | What we're building, for whom, why now, validation evidence, probabilistic confidence level | Vulnerability heat bars (3-axis), archetype card |
| M2 | **The Moat** | Data flywheel map, defensibility analysis, competitive positioning, vendor portability plan, encroachment defense | Flywheel radar chart, competitive positioning map |
| M3 | **The Margin** | Cost model with cascading, pricing strategy, P&L projection, stress tests, scenario modeling | Live cost curve with what-if sliders |
| M4 | **The Contract** | Eval spec, reliability targets, confidence UX design, HITL plan, golden dataset strategy | Trust maturity meter |
| M5 | **The Guardrails** | Compounding system design, governance framework, agent topology, feedback loops | AI maturity radar/spider chart, risk badge |

**M6 = Integration.** Finalize `README.md` with complete summaries, build `06-the-pitch/roadmap.md`, and present the repo to the room as a board simulation.

The repo is the central artifact — not a sixth separate exercise. Every module pushes real files to specific folders. The top-level `README.md` serves as the living strategy dashboard — a single page that links to and summarizes all components. Share the repo link with your board Monday morning.

Each component connects to the others — they're pillars of one strategy, not sequential steps in a checklist. The build order is sequential (you can't price what you can't defend), but the iteration order may differ in practice.

**They don't leave with a certificate. They leave with a weapon.**

---

## Eight Design Principles

### 1. Build in every session

Every module includes a hands-on build moment that produces something tangible they take home. Not just a feeling — something they didn't have yesterday.

| Module | Build Moment | Tangible Output |
|--------|-------------|-----------------|
| M1 | Prototype a product concept with AI tools (v0, Cursor, Lovable) | Shareable link to working prototype |
| M2 | Map your data flywheel, score it, and position against competitors | Scored flywheel map + competitive positioning map + portability checklist |
| M3 | Build a cost curve, pricing model, and explore scenarios with live sliders | Cost model with stress tests + scenario lab with interactive margin curve |
| M4 | Spec an eval dashboard with metrics, judges, drift alerts | Eval dashboard spec + reliability contract |
| M5 | Design a compounding system + governance policy | System architecture + governance policy |
| M6 | Finalize README.md, build roadmap, present repo to the room | Complete strategy repo — 6 folders, board-ready README |

Each session's build connects to the final artifact. By M6, they don't start from scratch — they assemble 5 components they've already built.

### 2. Opinionated throughout

The True/False opening in M1 sets the tone: conventional wisdom is wrong, and here's why. That energy should pervade every module. Each module opens with one provocation:

- **M1:** "You can't predict which AI feature wins. Stop pretending you can."
- **M2:** "Your data is not your moat. Your workflow is."
- **M3:** "AI will compress your margins before it expands them."
- **M4:** "95% accuracy with no audit trail loses to 85% with one."
- **M5:** "Your governance framework is a sales asset, not a compliance burden."
- **M6:** "The roadmap is an output, not your job description."

One provocation per module — the opinionated tone is sustained, not exhausted in the first hour.

### 3. One case study format, repeated

The Klarna 3-act structure (Bet → Crack → Correction) is clean pedagogy. Use it consistently across all 6 modules:

| Module | Case Study Direction | Example Candidates |
|--------|--------------------|--------------------|
| M1 | Company that validated fast vs. one that shipped blind | Notion's 4-day AI research sprint; a cautionary counter-example |
| M2 | Company that built a real moat vs. one that got encroached | Jasper vs. ChatGPT native writing features |
| M3 | Company that got AI economics right vs. one that didn't | Klarna's Automator overcorrection (moves here from M1) |
| M4 | Company that engineered trust vs. one that lost it | Air Canada chatbot liability ruling |
| M5 | Company that governed well vs. one that didn't | Samsung data leak → internal governance response |
| M6 | Company that pitched the board and won AI investment | Duolingo's AI transformation narrative to investors |

### 4. Peer challenge is structural, not incidental

The people in the room are assets — but "pair work" is a format, not a mechanism. Make the challenge explicit and escalating module over module:

| Module | Challenge Mechanic |
|--------|--------------------|
| M1 | Partner challenges your diagnostic scores |
| M2 | Partner attacks your moat: "here's who kills you" |
| M3 | Partner stress-tests your pricing: "what if inference costs 3x" |
| M5 | Partner audits your system: "what feedback loop is broken" |
| M6 | Full room challenges your pitch (board simulation) |

Stakes escalate. By M6, participants present to a hostile (friendly) board. The discomfort is the pedagogy.

### 5. External-first language everywhere

Per Carlos's directive: every module question is about the product, not the PM. Audit all learning objectives for "you" language vs. "your product" language.

| Instead of... | Write... |
|--------------|----------|
| "Reframe your discovery process" | "Validate your AI product bet in days, not quarters" |
| "Build a governance framework" | "Ship a governance posture that accelerates enterprise deals" |
| "Design a production-grade eval system" | "Make reliability a product feature your users can see" |
| "Model the real economics of your AI product" | "Build a cost curve you can defend to your board" |

### 6. Frameworks are mental models, not templates

Every framework in this course (5 archetypes, 8 moats, cost curve, eval dashboard, reliability contract, governance policy) is a thinking tool participants adapt to their context — not a form to fill in. The on-slide structure gives them a starting shape. The instructor's job is to push them to break it for their own product.

Coaching pattern per framework:
1. Present the framework with a concrete example (someone else's product)
2. Show where the framework *doesn't* perfectly fit that example — name what was adapted
3. Participants apply to their own product and identify which parts they'd change, drop, or add
4. Peer challenge tests whether the adapted version holds up

If someone's artifact looks exactly like the template, that's a smell. The goal is that they leave with a customized mental model for their product — not a filled-in worksheet.

### 7. AI strategy is different — say it explicitly

The course opens (M1) with an explicit comparison of traditional vs. AI product strategy. This isn't subtext — it's the headline. Each module reinforces one specific assumption it breaks:

| Module | Traditional assumption it breaks |
|--------|----------------------------------|
| M1 | "We can plan with certainty" → Outputs are probabilistic |
| M2 | "Our product boundary is clear" → Platforms encroach overnight |
| M3 | "Margins are stable at scale" → Inference costs are variable and usage-driven |
| M4 | "Users trust software by default" → Trust must be designed into uncertain outputs |
| M5 | "Compliance is a one-time checklist" → AI systems compound or degrade silently |
| M6 | "The roadmap speaks for itself" → Boards need a new vocabulary for AI risk/reward |

Name the broken assumption in the first 2 minutes of each module. It connects the provocation to the rest of the session.

### 8. Use AI to evaluate your own strategy

The ultimate proof that participants internalized the frameworks: they can use AI to systematically evaluate any bet against all five components. This is a progressive thread that culminates in M6:

- **After each module:** Participants can optionally feed their latest component into a structured AI prompt for self-assessment
- **M6 capstone exercise:** Before the board simulation, participants run their complete strategy through an AI evaluation workflow that checks:
  - Is the bet validated with evidence, or just conviction?
  - What capabilities need to be developed, and are they realistic?
  - Does the moat hold under platform encroachment pressure?
  - Are the economics viable under 2-3x cost stress?
  - Is the trust/reliability contract explicit and measurable?
  - Can governance scale without breaking the product?

This creates a reusable tool: after the course, they can evaluate any future bet against the same dimensions. The frameworks become a permanent analytical lens, not a classroom exercise.

---

## Module Summaries

### M1: The Bet — What should we build, and how do we know fast?

**Learning Objective:** Validate your AI product bet in days, not quarters — using probabilistic thinking and AI-powered discovery to kill bad ideas before they consume a roadmap.

**Key content:**
- Annual planning cycles are obsolete; AI capability curves don't respect fiscal years
- AI-powered discovery: synthetic personas, automated insight synthesis, real-time segment simulation (10x velocity)
- 5 AI Value Archetypes as a fast filter for which type of AI product you're actually building
- Probabilistic prioritization: confidence intervals, not commitments

**Case study:** Company that validated fast vs. one that shipped blind

**Build moment:** Prototype one AI product idea using v0/Cursor/Lovable — bring it to M2

**Peer challenge:** Partner challenges your diagnostic scores and names one AI-native competitor attacking your vulnerability

**Artifact component:** The Bet — what you're building, for whom, why now, validation evidence

**Bridge to M2:** "You now know what you're betting on. M2 answers: can anyone else copy this in 6 months?"

---

### M2: The Moat — Why won't this get copied in 6 months?

**Learning Objective:** Build a defensible data moat by mapping proprietary data loops, identifying encroachment threats, and designing a vendor portability plan executable in under 48 hours.

**Key content:**
- Proprietary data loops: System of Intelligence vs. System of Record
- Zero-party data acquisition through correction/feedback UX
- Cold-start survival: synthetic seeding, transfer learning, partnerships
- Contextual moats via vertical depth + deep workflow embedding (high switching costs)
- Platform encroachment defense + Model Dependency Kill Switch (abstraction layers, unified APIs, multi-model routing)

**Case study:** Jasper vs. ChatGPT — how native AI features encroached a $1.5B wrapper

**Build moment:** Map your data flywheel, score each loop, identify the single weakest link. Build a competitive positioning map — place your product and 3-5 competitors on two strategic axes (interactive canvas with draggable dots).

**Peer challenge:** Partner plays the Big Tech attacker — "here's exactly how I kill your product"

**Artifact component:** The Moat — data flywheel map, defensibility scores, competitive positioning map, vendor portability checklist

**Bridge to M3:** "You know what's defensible. M3 answers: will the economics actually work, or will inference costs eat your margin?"

---

### M3: The Margin — Will this make money or bleed it?

**Learning Objective:** Build a cost curve and pricing model you can defend to your board — including inference budgets, cascading architecture, and a hybrid pricing strategy that captures AI value without destroying gross margins.

**Key content:**
- The margin war: 80% SaaS margins collapsing to 40-60% with AI inference costs
- Model cascading: cheap triage model → frontier model for hard cases
- CPO-level LLMOps levers: quantization, caching, routing, observability, GPU forecasting
- Pricing evolution: hybrid/blended (base + usage/outcome/credit tiers), outcome-based (per task/lead/% savings), dynamic adjustments for agents and power users
- Usage-based value capture: old SaaS revenue ($50/seat) vs. AI usage/outcome revenue ($2/successful automation)

**Case study:** Klarna — The Automator That Overcorrected (bet → crack → correction arc)

**Build moment:** Build a cost curve + cascading model + hybrid pricing strategy; compare old SaaS revenue vs. AI usage revenue for board/sales enablement. Then explore the Scenario Lab — drag sliders for inference cost multiplier, volume growth, and cascading ratio to see how your margin curve behaves in real time.

**Peer challenge:** Partner stress-tests the model — "what happens when inference costs 3x? When your heaviest user segment doubles?"

**Artifact component:** The Margin — cost model with cascading, pricing strategy, scenario analysis, P&L projection with stress tests

**Bridge to M4:** "The economics work on paper. M4 answers: will users actually trust the output enough to pay for it?"

---

### M4: The Contract — Why will users trust a probabilistic system?

**Learning Objective:** Make reliability a product feature your users can see — by designing an evaluation system, confidence UX, and human-in-the-loop architecture that turns probabilistic outputs into trusted decisions.

**Key content:**
- Golden datasets and ground truth as product infrastructure
- Human-in-the-loop design for 99.9% reliability in regulated verticals
- LLM-as-a-Judge for regression testing, scaling evals, and drift detection
- Confidence scores and probabilistic UX primitives (showing uncertainty, not hiding it)
- Trust ≠ accuracy: perceived control matters more than percentage points

**Case study:** Air Canada chatbot liability — when an AI product made promises the company had to honor

**Build moment:** Spec a production eval dashboard — metrics, judge configuration, drift alerts, UX integration points

**Artifact component:** The Contract — eval spec, reliability targets, confidence UX design, HITL architecture, golden dataset plan

**Bridge to M5:** "Users trust the system. M5 answers: what happens when you scale it, and how do you build systems that compound instead of collapse?"

---

### M5: The Guardrails — What breaks when this scales?

**Learning Objective:** Build systems that compound — governance that accelerates deals, feedback loops that improve quality with every iteration, and infrastructure that scales without breaking trust.

**Key content:**
- **Building compounding systems:** How to create infrastructure where quality improves with usage — recursive learning, feedback loops, knowledge that compounds across teams and domains instead of siloing
- **Connecting context:** Breaking domain silos so knowledge flows across products and teams. The system learns from every interaction, not just the ones in your silo.
- Responsible AI as competitive differentiator + board risk translation (EU AI Act, explainability requirements)
- Multi-agent orchestration governance: autonomy boundaries, tool-calling safety, memory management
- ROI evaluation for agentic systems vs. traditional automation
- Shadow AI audit: identifying unsanctioned AI spend/tools across the org (Spotify example: 1,000 tools → 15 after audit, massive cost savings)

**Case study:** Samsung data leak — how an internal AI failure became an external governance story

**Build moment:** Design a compounding system architecture for their product + draft governance policy + shadow AI audit of their org

**Peer challenge:** Partner audits the system — "what feedback loop is broken? What agent boundary is too loose? What's your exposure if a regulator calls tomorrow?"

**Artifact component:** The Guardrails — compounding system design, governance framework, agent topology, feedback loops, shadow AI audit

**Bridge to M6:** "You have the full strategy: bet, moat, margin, trust, guardrails. M6 is about making it sing — the narrative that gets this funded and shipped."

---

### M6: The Pitch — How do you get this funded, shipped, and adopted?

**Learning Objective:** Present a complete, board-ready AI Product Strategy — a continuous roadmap, margin model, eval spec, moat plan, and governance framework — that you can use Monday morning.

**Key content:**
- Multi-horizon roadmaps in the continuous-sprint era (quick wins + bets + moonshots)
- AI-specific metrics: hallucination rate, drift velocity, trust scores, inference ROI
- Pilot-to-production change management and adoption barriers
- Board-ready storytelling: translating AI system complexity into investment narratives
- AI GTM frictions: outcome packaging, trust barriers, demo strategy for probabilistic products

**Case study:** Duolingo's AI transformation narrative — how they told the investor story

**Build moment:** Finalize and present the complete living strategy

**Peer challenge:** Full room challenges each pitch — board simulation. "Why should we fund this? What's the risk you haven't addressed?"

**Artifact component:** Integration — the complete strategy, stress-tested and pitch-ready

**Capstone (60-75 min):** Present the full strategy:
  - Continuous roadmap
  - Margin/P&L with cascading, pricing, stress tests
  - Eval strategy and dashboard spec
  - Data moat + encroachment/portability plan
  - Compounding system design + governance framework

---

## What This Course Has That Nobody Else Does

1. **The full strategic stack in one program.** Reforge splits bet/moat/margin/evals/governance across 6 separate paid courses. This threads them into one coherent arc where each piece depends on the last.

2. **A living repo, not a certificate.** Participants leave with a GitHub repo built on their actual product — six folders of interconnected strategy artifacts, stress-tested by peers, shareable Monday morning. Version-controlled. Portable. Alive.

3. **Economics depth.** Nobody does a full module on AI unit economics with cascading models, cost curves, and hybrid pricing. This is the most underserved topic in AI product education. M3 could be the module people talk about.

4. **The build-every-session cadence.** In a market of lecture-heavy and reading-heavy courses, participants building something tangible in every session is genuinely differentiated — and it proves the course's thesis (AI accelerates everything, including how you learn strategy).

5. **The opinionated spine.** Most courses hedge. This one has a point of view: data isn't your moat, margins will compress before they expand, governance is a sales weapon. Opinions attract senior audiences; balanced summaries attract beginners.

---

## Open Design Decisions

- [ ] **Module titles:** Does "The Bet / The Moat / The Margin / The Contract / The Guardrails / The Pitch" resonate, or do we keep the evolution framing as the primary label?
- [ ] **M4/M5 overlap with standalone courses:** How much should Evals (M4) and Governance (M5) overlap with Product School's dedicated courses on those topics? Recommendation: cover the strategic 20% a product leader needs, not the operational 80%. Carlos wants to see how tangible these are — especially M5.
- [ ] **Opinionated tone commitment:** The True/False opening in M1 is bold. If we commit to that edge in all 6 modules, it becomes the course's signature. If we soften after M1, it feels like bait-and-switch.
- [x] **5 AI Value Archetypes:** Defined in M1 slides — Automator, Copilot, Oracle, Creator, Orchestrator. Each with margin profile, governance burden, and example.
- [x] **Prototype Bet logistics:** Defined in M1 slides — 15 min, v0/Cursor/Lovable, minimum output is a shareable link, account setup as pre-work.
- [x] **Own product vs. shared fictive company:** RESOLVED (Mar 13). Case studies during class for shared examples. Applied work on their own product at their company. NOT entrepreneurship. Backup examples for anyone not at a company.
- [x] **Artifact format:** RESOLVED (Mar 13). Not a document/PRD/dissertation. A "living strategy" — interactive, compounding, co-creating. Five interconnected components (not layers, not steps).
