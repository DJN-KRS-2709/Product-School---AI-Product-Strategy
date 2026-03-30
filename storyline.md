# AI Product Strategy — The Storyline

## The One-Sentence Promise

You will build a living AI product strategy — on your real product — across 6 sessions. Not theory. Not frameworks on a whiteboard. A working strategy with an economics model, an eval spec, a moat analysis, a compounding system design, and a pitch you can deliver Monday morning.

---

## The Setup: Why This Course Exists

Every senior PM in the room already knows AI is changing the game. They've taken the intro courses. They can prompt. They know what RAG is. But when their CEO asks "what's our AI strategy?" — they hesitate.

Not because they don't know AI. Because the strategic playbook they were trained on doesn't work anymore.

### Why AI strategy is different from standard strategy

The course opens with this thesis and reinforces it every session. Traditional product strategy assumes five things that AI breaks:

| Traditional assumption | AI reality |
|----------------------|------------|
| Feature works or it doesn't | Outputs are probabilistic — accuracy, hallucination, drift |
| Infra scales predictably | Inference costs scale with usage, not users |
| Your product vs. theirs | Your feature becomes a platform's checkbox overnight |
| Software does what it says | Users must be convinced to trust uncertain outputs |
| Annual planning cycles | Capabilities change weekly — bets, not plans |

Each module breaks one assumption. This isn't subtext — it's the headline that opens M1 and gets reinforced throughout.

### Three course-level principles

1. **AI strategy ≠ traditional strategy** — say it explicitly. M1 opens with the comparison table. Each module names which assumption it breaks in the first two minutes.

2. **Frameworks are mental models, not templates** — every framework (5 archetypes, 8 moats, cost curve, eval dashboard, reliability contract, governance policy) is a thinking tool participants adapt to their context. If someone's artifact looks exactly like the template, that's a smell. The goal is a customized mental model for their product.

3. **Use AI to evaluate your own strategy** — once participants have the full framework stack, they can use AI itself to systematically evaluate any bet across all dimensions: validation, capabilities, impact, defensibility, pricing alignment, trust, and governance. The AI Bet Evaluator tool makes this a reusable workflow they take back to work.

### Why this course over alternatives

This course exists because nobody is teaching the full strategic stack — bet, moat, margin, trust, guardrails, pitch — as one coherent arc. Reforge fragments it across 6 separate courses. Maven stays tactical. This program threads it all together and makes you build it on your real product.

We learn from the best — Reforge, Maven, the top Substack voices. Where there's overlap across sources, it validates the topic. Where there's a gap, we fill it.

---

## The Arc: Six Questions That Build One Strategy

The course follows six strategic questions. They're sequential — each answer depends on the last. Together, they produce one complete living strategy with five interconnected components.

```
THE BET → THE MOAT → THE MARGIN → THE CONTRACT → THE GUARDRAILS → THE PITCH
  What       Why it      Will it      Why users    What breaks     How you
  to build   survives    make money   will trust   when it scales  get it funded
```

**Important:** Participants bring a product from their company. Not a startup idea — a real product they're responsible for. Case studies during class for shared examples and frameworks. Applied work always on their own product.

---

### M1: THE BET — What should we build, and how do we know fast?

The old way: annual planning cycles, 6-8 week discovery sprints, deterministic commitments to outcomes.

The new reality: AI capability curves don't respect fiscal years. Traditional discovery is too slow. Outcomes are probability distributions, not guarantees.

**What participants learn:**
- Why annual planning cycles are obsolete and continuous AI-enabled sprints are the operating model
- How AI-powered discovery (synthetic personas, automated insight synthesis, real-time segment simulation) delivers signal in days instead of months
- The 5 AI Value Archetypes — a fast filter for which type of AI product you're actually building and what its margin/governance profile looks like
- How to make bets under irreducible uncertainty: probabilistic prioritization, not deterministic commitments

**What they build:**
- Their AI strategy baseline statement (revisited in M6 to see how far they've traveled)
- A diagnostic of where their current product strategy breaks under AI conditions
- A rough prototype of one AI product idea using v0/Cursor/Lovable

**What they take to M2:**
The Bet component of their living strategy — what they're building, for whom, why now, and their probabilistic confidence level. Plus the prototype.

**The bridge:** "You now know what you're betting on. But can anyone else copy this in 6 months? That's M2."

---

### M2: THE MOAT — Why won't this get copied in 6 months?

The provocation: "Your data is not your moat. Your workflow is."

Models get copied. Features get cloned. Data gets aggregated. The only durable advantage lives in three places: proprietary data loops that compound, workflow embedding that creates switching costs, and portability architecture that lets you survive vendor shocks.

**What participants learn:**
- Proprietary data loops: the difference between a System of Intelligence and a System of Record, and how zero-party data acquisition (correction/feedback UX) compounds over time
- The cold-start problem: synthetic seeding, transfer learning, and partnership strategies for when you have no data advantage yet
- Contextual moats: why vertical depth + deep workflow embedding creates switching costs that horizontal AI features can't replicate
- Platform encroachment defense: what happens when OpenAI/Google/Apple ships your feature natively, and the Kill Switch — a portability framework (abstraction layers, unified APIs, multi-model routing) for swapping vendors in under 48 hours

**What they build:**
- A data flywheel map for their product, scored loop by loop
- An encroachment threat assessment: who attacks them, from where, with what
- A vendor portability checklist for surviving price shocks or ToS changes

**What they take to M3:**
The Moat component — defensibility analysis, data flywheel, portability plan.

**The bridge:** "You know what's defensible. But will the economics actually work, or will inference costs eat your margin?"

---

### M3: THE MARGIN — Will this make money or bleed it?

The provocation: "AI will compress your margins before it expands them."

This is the module nobody else teaches at depth. Most AI courses mention pricing in passing. This one spends two hours on the economics — because a product with a broken cost model isn't a product, it's a charity.

**What participants learn:**
- The margin war: how 80% SaaS gross margins collapse to 40-60% with AI inference costs, and why most leaders walk into this blind
- Model cascading: cheap triage model handles the easy 80%; frontier model handles the hard 20%. How to architect this and what it does to your cost curve.
- CPO-level LLMOps levers: quantization, caching, semantic routing, observability, GPU forecasting — the operational choices that determine whether your product is profitable
- Pricing evolution: from seat-based SaaS to hybrid/blended models (base + usage/outcome/credit tiers), outcome-based pricing (per task, per lead, per percentage of savings), and dynamic adjustments for agents and power users
- The value capture comparison: old SaaS revenue ($50/seat/month) vs. AI usage revenue ($2/successful automation) — how to model this for board conversations and sales enablement

**What they build:**
- A cost curve with cascading architecture modeled
- A hybrid pricing strategy with stress tests (what if inference costs 3x? what if your heaviest segment doubles usage?)
- A before/after value capture comparison for their board

**What they take to M4:**
The Margin component — cost model, pricing strategy, P&L projection with stress tests.

**The bridge:** "The economics work on paper. But will users actually trust the output enough to pay for it?"

---

### M4: THE CONTRACT — Why will users trust a probabilistic system?

The provocation: "95% accuracy with no audit trail loses to 85% accuracy with one."

Trust is not a function of accuracy. It's a function of perceived control. This module treats reliability as a product feature — something users can see, understand, and rely on — not an engineering metric buried in a dashboard.

**What participants learn:**
- Golden datasets and ground truth as product infrastructure, not data science artifacts
- Human-in-the-loop design: where HITL is a product feature (not a crutch) and how to architect it for 99.9% reliability in regulated verticals
- LLM-as-a-Judge: using models to evaluate models at scale — for regression testing, scaling evals beyond what humans can review, and detecting drift before users do
- Confidence scores and probabilistic UX primitives: showing uncertainty instead of hiding it, giving users control over automation thresholds, making the system legible
- Why trust ≠ accuracy: the research and real-world evidence that perceived control matters more than percentage points

**What they build:**
- A production eval dashboard spec: metrics, judge configuration, drift alerts, UX integration points
- A reliability contract: what they promise users, what they measure, and what happens when the system falls below threshold

**What they take to M5:**
The Contract component — eval spec, reliability targets, confidence UX, HITL architecture.

**The bridge:** "Users trust the system. But what happens when you scale it? How do you build systems that compound instead of collapse?"

---

### M5: THE GUARDRAILS — What breaks when this scales?

The provocation: "Your governance framework is a sales asset, not a compliance burden."

This module is about two things: building systems that compound, and governing them so they don't break trust at scale. Most companies treat governance as the thing legal makes them do. The companies winning enterprise deals treat it as the thing that gets them shortlisted. And as AI systems gain autonomy, the question becomes: how do you build infrastructure that gets better with every iteration — across teams, across domains — while maintaining the guardrails that keep it safe?

**What participants learn:**
- **Building compounding systems:** How to create infrastructure where quality improves with usage. Recursive learning, feedback loops, connecting context across teams and domains so knowledge compounds instead of siloing. The system learns from every interaction, not just the ones in your silo.
- Responsible AI as competitive differentiator: how companies that can demonstrate auditable AI are closing larger contracts faster (EU AI Act as context, Salesforce Einstein Trust Layer as example)
- Multi-agent orchestration governance: autonomy boundaries (what can agents decide alone?), tool-calling safety (what can agents access?), memory management (what do agents retain?)
- ROI evaluation for agentic systems: when agents outperform traditional automation and when they don't — the decision framework
- Shadow AI audit: identifying unsanctioned AI spend and tools across the organization — the 5-minute checklist for visibility into hidden exposure (Spotify: 1,000 tools → 15 after audit)

**What they build:**
- A compounding system architecture for their product — feedback loops, domain connections, recursive learning design
- A governance policy for their AI/agent stack
- An agent onboarding checklist: proficiency levels, codified skills, invocation playbooks
- A shadow AI audit of their current organizational exposure

**What they take to M6:**
The Guardrails component — compounding system design, governance framework, agent topology, feedback loops, shadow AI audit.

**The bridge:** "You have the full strategy: bet, moat, margin, trust, guardrails. M6 is about making it sing — the narrative that gets this funded and shipped."

---

### M6: THE PITCH — How do you get this funded, shipped, and adopted?

The provocation: "The roadmap is an output, not your job description."

Everything built in M1–M5 now needs to become a story. Not a slide deck about what you learned in a course — a strategic narrative that gets budget approved, teams aligned, and users onboarded. The roadmap is the output of the strategy, not the job itself.

**What participants learn:**
- Multi-horizon roadmaps in the continuous-sprint era: quick wins (prove value now), bets (invest for 6-month payoff), moonshots (position for 18-month advantage)
- AI-specific metrics that boards care about: hallucination rate, drift velocity, trust scores, inference ROI — and how to translate them from engineering language to investment language
- Pilot-to-production change management: the adoption barriers specific to AI products (trust gap, behavior change, outcome uncertainty) and how to design for them
- Board-ready storytelling: translating AI system complexity into investment narratives — the narrative structure that works
- AI GTM frictions: how to demo probabilistic products, how to package outcomes instead of features, how to address the trust barrier in sales cycles

**What they build:**
The complete living strategy, integrated and stress-tested:
- Continuous roadmap (quick wins + bets + moonshots)
- Margin/P&L with cascading, pricing, and stress tests
- Eval strategy and dashboard spec
- Data moat + encroachment/portability plan
- Compounding system design + governance framework

**The AI Bet Evaluator (new in M6):**
Before the board simulation, participants use the AI Bet Evaluator tool to run their complete strategy through a structured AI evaluation. The tool generates a prompt that evaluates their bet across all dimensions learned in M1-M5: validation, capabilities, impact, defensibility, pricing alignment, trust, and governance. This is the meta-move — using AI to evaluate their own AI strategy. It also creates a reusable workflow: after the course, they can evaluate any future bet against the same dimensions.

**The capstone (~35 min):**
Present the full strategy to the room. The room plays the board. Challenges are real: "Why should we fund this? What's the risk you haven't addressed? What happens when OpenAI ships this natively?"

**What they leave with:**
A living strategy they can present Monday morning. Built on their real product. Challenged by peers who understand the domain. A reusable AI evaluation workflow for any future bet. Not a certificate — a weapon.

---

## The Rhythm (Consistent Across All 6 Sessions)

Every 2-hour session follows the same structure. Participants know what to expect, which lets them focus on the content rather than the format.

```
[5 min]   PROVOCATION — One bold claim that reframes the topic
[10 min]  LECTURE — Core concepts, evidence, frameworks
[5 min]   CASE STUDY — 3-act structure: Bet → Crack → Correction
[25-30 min] APPLIED WORK — Participants build on their own product
[10-15 min] PEER CHALLENGE — Partner attacks/stress-tests their work
[5 min]   BUILD MOMENT — Hands-on with AI tools or models
[5 min]   SYNTHESIS — Tie it back to the strategy, name the bridge to next session
[5 min]   BREAK (where applicable)
```

**Approximate total: 70-80 min active + 5 min break + buffer = 2 hours**

---

## What Needs to Happen Now

### Immediate (by Tuesday)

1. **Incorporate Mar 13 feedback into M1.** Update artifact framing (living strategy, not document), opening question (bring your product from your company), terminology (components not layers).

2. **Go deep into modules.** Carlos wants module-level detail starting Tuesday. M1 is built — now detail M2–M6 at the same depth.

3. **Design the living strategy template.** Five interconnected components. Lightweight enough to start in M1 but structured enough to be board-ready by M6. Must not feel like a document — interactive, compounding, something with a life of its own.

### Next week

4. **Detail M2 and M3.** M2 (moat, data flywheel, encroachment, portability) is well-defined. M3 (economics) is the biggest differentiator — needs the margin calculator/template built.

5. **Clarify M4 and M5 for Carlos.** He's not an expert on these yet. Make them tangible — show how M4 goes beyond evals, how M5 is about compounding systems not data policies.

### Following weeks

6. **Detail M4–M6** one per cycle. Prioritize making each module's wow moment concrete and tangible.

7. **Research and lock case studies.** One per module, all in the 3-act format (Bet → Crack → Correction). Candidates are proposed in `course-architecture.md`.

8. **Daria: build the design system.** Standardize the repo-based slide creation approach so it works across all Product School courses and enterprise clients.
