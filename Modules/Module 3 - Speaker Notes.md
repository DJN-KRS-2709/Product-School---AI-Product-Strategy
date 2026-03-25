# Module 3 — The Margin
## Speaker Briefing for Carlos

### What this module is about

This is the money module. In M1 they diagnosed where they're vulnerable, in M2 they built the defense. Now we're asking: does any of this actually make money? The emotional arc is different here — M1 and M2 were about threat and defensibility, which creates adrenaline. M3 is about math, which creates discomfort in a different way. Most PMs have never calculated their AI cost per user. That gap between "I think we're fine" and the actual number is where the learning happens.

They leave with three artifacts: a cost curve, a pricing strategy, and a board-ready one-pager. Those plus the interactive tools (Margin Calculator, Pricing Strategy Designer) give them something they can actually use at work on Monday.

### The flow and why it's structured this way

The first half is concept-heavy but we break it up with a case study (Klarna) and two standalone activity slides. This was based on Daria's feedback — she was right that pair activities buried inside theory slides get lost. So we pulled them out into their own full-screen moments where you can't miss them.

The second half is almost entirely hands-on: cost curve, pricing design, peer stress-test, and the board one-pager. That's where the real output gets created.

---

### Slide 1 — Title

Set the tone: this is calmer than M1/M2 but the pain is sharper when the math actually lands. The goal is to make them feel like they're about to learn something that will immediately change how they think about their product's economics.

### Slide 2 — Agenda

Just orientation. Don't linger. The point is to show them there are two big applied blocks after the break, so they know the lecture portion is front-loaded and it'll get hands-on.

### Slide 3 — Recall from M2

We need to connect the modules. The key message is: everything they built in M2 (flywheel, moat, kill switch) is meaningless if the economics don't work. This slide bridges that gap. The quick partner exercise ("name one AI call path that could spike costs") is there to get them thinking about money before we even start teaching. It also warms up the room — people have been sitting for a minute.

### Slide 4 — Provocation

The goal here is to create discomfort. We ask "who actually knows their inference cost per user per month?" and most hands won't go up. That's the point. If they already feel the gap in their knowledge, every concept in the next 30 minutes lands harder. We're challenging three beliefs that PMs carry around like security blankets: costs will come down, seat pricing works, scale fixes everything. None of these are reliably true for AI products.

### Slide 5 — The Margin War (80% → 40%)

This is the core economic argument of the module. Traditional SaaS runs at 80%+ gross margins because infrastructure costs are mostly fixed. AI products introduce variable costs (tokens, inference) that scale with usage, and power users can blow up your unit economics. We want them to actually see the math — have OpenAI and Anthropic pricing pages ready to show the real $/token gap between small and frontier models. The napkin math on screen should be done live if possible. When they see "1k calls × $0.03 = $30/user/month just in AI COGS" it hits differently than reading it.

### Slide 6 — Model Cascading

This is the answer to slide 5's problem. If the margin war is the disease, routing is the cure. The 80/20 split (80% cheap model, 20% frontier) is the single highest-leverage thing most AI products can do for their margins. Cursor and GitHub Copilot both do this. The three levers at the bottom (quantization, caching, prompt optimization) are there as a quick reference but don't need deep explanation — just name them so people know the toolkit exists.

### Slide 7 — Case: Klarna

We moved this here from later in the deck based on Daria's feedback. Six slides of concepts without real interaction is too long. Klarna is the perfect case because it's the most public story of "we automated everything" running into "variable COGS is messy." The debate format (headline pricing vs P&L pricing) gets voices in the room and resets the energy before the next theory block. The lesson isn't that Klarna failed — it's that the business model has to match the automation.

### Slide 8 — How You Charge > How Much

This is where we bring in Madhavan Ramanujam's work. He's consulted with 400+ companies and his core insight is that most pricing failures happen because teams never figured out HOW to charge, not how MUCH. The three models on screen (seat/access, hybrid, outcome) are the spectrum. The standout example is Intercom Fin — they charge per resolved conversation, which is the only real pricing model innovation in AI. The data from Palle Broe (59% bundle, 23% add-on, 18% standalone) gives context for what the market is actually doing. The pair activity was pulled out into its own slide (next one) so it doesn't get lost.

### Slide 9 — Activity: Access or Outcome?

This is a dedicated activity slide. The theory from slide 8 is useless if they don't apply it to their own product. The exercise is simple: point left (access) or right (outcome). But the follow-up question is where the learning happens — if most point left, challenge them: "Is your product doing work for them? Then why are you pricing access?" This is where people start to realize they might be leaving massive value on the table.

### Slide 10 — Leaders, Fillers & Killers

This is Madhavan's bundling framework. The Big Mac analogy makes it stick: burger is the leader (what you come for), fries and Coke are fillers (bumps the average order), coffee would kill the bundle (too different, sell separately). Applied to AI: your core intelligence is the leader, lightweight features like summaries are fillers, and heavy inference stuff like image gen or agent workflows are killers that should be priced as add-ons. The 70% rule from Palle Broe gives them a concrete decision threshold. Again, the pair activity is on its own slide next.

### Slide 11 — Activity: Name Your Leader, Filler & Killer

Same logic as slide 9 — dedicated activity moment. The fill-in cards with emoji are intentionally playful. If someone bundled their "killer" into the main plan, push them: "What % of users actually use it?" If it's under 70%, it's an add-on. This is the last activity before the Margin Calculator, so after this it's all hands-on.

### Slide 12 — Margin Calculator

This is where abstract becomes concrete. The sticky note exercise (write your gross margin %, hold it up) creates anonymous social pressure — nobody has to shout a number but everyone sees the range. Walk through the math live on screen. The interactive tool link is on this slide — students can open the Margin Calculator, plug in their numbers, and it auto-calculates everything including the stress tests. Way faster than doing it by hand and they can export the results.

### Slide 13 — Break

Reset before the heavy applied work. Suggest they pull up their provider's pricing page during the break — they'll need it for the cost curve exercise.

### Slide 14 — Build Your Cost Curve

This is 15 minutes of solo work where they map every AI feature in their product to a model tier and estimate the cost. The goal is honest tiering — most people's instinct is to say "we use frontier for everything" and this exercise shows them that's a 3× cost difference they can't sustain. Common traps to watch for: underestimating how often embeddings get called, defaulting everything to the most expensive model.

### Slide 15 — Design Your Pricing

This is where Madhavan's "Product-Market-Pricing Fit" concept lands. The exercise walks them through three steps: pick a strategy (skim like Apple, penetrate like Amazon, maximize like Microsoft), name the unit of work they'd meter, and set the structure (base + usage). The GitHub Copilot proof point on the slide is powerful: $19/user is 4.75× a typical SaaS seat, justified because developers complete tasks 55% faster. The Pricing Strategy Designer tool is linked here for anyone who wants the full guided experience.

### Slide 16 — Peer Stress-Test

Partner breaks your model. Two scenarios: inference costs 3× (what breaks first?) and heavy users double (they pay less than they burn). The written vulnerability per pair is important — it travels to Module 4. If pairs are being too polite, push them. The CFO won't be polite when they see 3× in a scenario plan.

### Slide 17 — Build Moment (Board One-Pager)

This is the most "real world" artifact in the module. 15 minutes to build a before/after comparison of their current model vs AI-enhanced model. The key reframe: lower margin % can be fine if revenue and gross profit are both up. AI can expand the numerator even if the percentage dips. This one-pager is what they'd actually present to a board. If someone asks "why is our margin lower?" — this is the answer.

### Slide 18 — Synthesis

Tie it all back to slide 4. Margin compression is the default for AI products. But now they have the levers (cascading, routing, pricing model, bundling) and the artifacts (cost curve, pricing strategy, board one-pager) to do something about it. Component 3 gets locked in here.

### Slide 19 — Bridge to M4

The connection: economics without trust doesn't convert. Module 4 is about reliability, contracts, and evaluation — the things that make customers actually adopt and keep using what they've priced and built. Everything from M3 (cost curve, pricing strategy, kill switch from M2) feeds directly into M4's vendor evaluation framework.

### Slide 20 — Survey

Quick close. Genuine thanks.
