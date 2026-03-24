# Module 3 — The Margin

## Slide 1 — Title
- Today is the money module — calmer tone than M1/M2 but the pain is sharper when the math lands
- They leave with a cost model, a pricing strategy, and Component 3
- Why we start here: moat without economics is a fantasy. This module puts the P&L layer on top of everything they've built

## Slide 2 — Agenda
- Quick 60-second overview so nobody feels lost
- Two applied blocks, peer stress-test, board one-pager at the end — we move fast

## Slide 3 — Recall from M2
- Flywheel + Components 1–2 + Kill Switch — short recap
- **Interactive:** turn to your partner, 20 seconds — name one AI call path in your product that could spike costs
- Why: moat + flywheel without unit economics is incomplete. Today adds the money layer
- Punch line: "pretty flywheel + ugly COGS = liability"

## Slide 4 — Provocation
- **Interactive:** hands up — who actually knows their inference cost per user per month? (Most won't. That's the point)
- Three false beliefs we challenge: costs will "eventually" come down, seat pricing always works, scale fixes everything
- Why we do this: the discomfort opens their ears for the Margin Calculator later. If they already feel "I don't know my $/user" — every concept lands harder

## Slide 5 — The Margin War (80% → 40%)
- **Interactive:** quick poll — gross margin today: <50%, 50-70%, 70%+?
- SaaS = mostly fixed infra, ~$5-8/user/mo → 80%+ margins. AI layer = variable $/token, power users ≠ average → margins 40-60%
- Have OpenAI and Anthropic pricing pages open — show the real $/1M tokens gap between mini/Haiku vs frontier (10-30×)
- Napkin math live: 1k calls × avg tokens × blended rate → COGS/user/mo
- Why: kills "we'll keep SaaS margins" fantasy. They need to see the numbers in real time

## Slide 6 — Model Cascading
- **Interactive:** thumbs — who's running 100% frontier in production? (Most are — that's the problem)
- 80/20 routing: 80% cheap small model, 20% frontier — blended COGS collapses
- Name Cursor, GitHub Copilot as examples of smart tiering
- Three cost levers: quantization (smaller footprint), semantic caching (skip repeated queries), prompt optimization (fewer tokens)
- Why: routing IS the margin product. This is where they reclaim the spread between SaaS and AI margins

## Slide 7 — Case: Klarna (energy break)
- Why here and not later: six slides of concepts is too long without real interaction. Klarna grounds everything they just learned in a real company — and the debate gets voices in the room before the next theory block
- Three beats: Bet (AI assistant handled ~⅔ of support chats, ~700 FTE equivalent), Crack (token costs scale with usage, edge cases → humans, variable COGS replaced fixed labor), Correction (tiered to copilot for hard cases, narrative shifted from headcount savings to CX quality)
- **Interactive:** 1-min debate — headline pricing ("we saved 700 jobs!") vs P&L pricing (what are actual unit economics?)
- Why Klarna matters: it's the most public story of "we automated everything" meeting "variable COGS is messy." The lesson isn't that automation failed — it's that features get automated but the business model has to match

## Slide 8 — How You Charge > How Much
- This is the big reframe from Madhavan Ramanujam (Lenny's Podcast — worked with 400+ companies, 50 unicorns, wrote Monetizing Innovation)
- His core line: "How you charge is way more important than how much you charge"
- Three models on slide: seat/access (Figma, Slack), hybrid base+usage (HubSpot, Canva AI), outcome/resolution (Intercom Fin, Harvey)
- **Intercom Fin** is the standout example — they charge per resolved conversation, not per seat. Only true pricing model innovation in AI so far. Aligns price directly to customer value
- Data from Palle Broe (Lenny's newsletter, 44 companies): 59% bundle AI into existing plan, 23% sell as add-on, 18% standalone
- Why we teach this: PMs default to seat pricing because it's what they know. But AI often delivers *work*, not access. If you price access on a product that does work, you leave massive value on the table

## Slide 9 — Activity: Access or Outcome?
- This is a standalone activity slide — don't skip it. It's here because Daria's feedback was clear: pair activities buried inside theory slides get lost. Carlos needs a clear "stop and do" moment
- **Interactive:** pair 45 sec — is your hero SKU closer to access (left) or outcome (right)? Point left or right
- Walk the room — if most point left (access), that's fine but challenge them: "Is your product doing work for them? Then why are you pricing access?"
- Punch line on slide: "If you price access on a product that does work — you leave value on the table." Let it land

## Slide 10 — Leaders, Fillers & Killers
- This is Madhavan's bundling framework from Monetizing Innovation
- **Leader** = what users come for, must-have, high willingness to pay (AI: core intelligence like GitHub Copilot autocomplete)
- **Filler** = nice addition at marginal cost, bumps ARPU (AI: summaries, translations, templates)
- **Killer** = kills the bundle if you include it — sell as add-on (AI: heavy inference like image gen, agent workflows)
- His Big Mac example: burger = leader, fries + Coke = fillers, coffee would kill the bundle → sell separately
- **70% rule** from Palle Broe: if >70% of users use the AI feature, bundle it. <70% but high-value for a few → add-on
- Gokul beat: raise price on proven value — don't only shave tokens. Do both
- Why: if you bundle wrong, you give the farm away. Most AI products put everything in one plan because they're afraid of looking "nickel-and-dime." But that means power users subsidize everyone and your best features don't get priced

## Slide 11 — Activity: Name Your Leader, Filler & Killer
- Another standalone activity — same logic as slide 9. Give the room a clear pause to apply what they just learned
- **Interactive:** pair 60 sec — name your Leader, one Filler, one Killer
- The visual on slide has fill-in blanks with emoji cues — it should feel playful, not like a test
- If they bundled the Killer into their plan: "What % of users actually use it? If <70%, it's an add-on, not a feature"
- This is the last activity before the Margin Calculator — after this, it's all hands-on tools

## Slide 12 — Margin Calculator
- **Interactive:** write your actual gross margin % on a sticky, hold it up (anonymous energy, no one needs to shout)
- Walk through live: 1k requests × $0.03 = $30 COGS; $80 price → healthy. Now 3× that cost → broke
- Stress column: always model 3× cost AND +50% usage from power users
- Note: OpenAI and peers have cut list prices repeatedly — but your stress model must survive both directions (price cuts = good, but provider lock-in risk if you assumed cheap forever)
- Why: abstract margin talk doesn't change behavior. Seeing YOUR number on a sticky note does
- **🔧 Tool:** "Open the Margin Calculator — plug in your numbers and it auto-calculates your margin, runs the 3× stress test and 2× heavy-user scenario, and tells you if you're healthy, warning, or danger. Way faster than the sticky — and you can export it."

## Slide 13 — Break
- Optional homework during break: pull your provider's pricing page on your phone
- Reset before the hands-on blocks

## Slide 14 — Build Your Cost Curve
- Solo table work, 15 minutes
- **Interactive:** 2-min checkpoint — shout your highest-volume AI feature (or round-robin)
- They map each AI feature to a complexity tier (simple/medium/complex), model tier, cost per request, and volume %
- Common trap: underestimating embeddings volume, over-assigning to frontier
- Why: this forces honest tiering. Most people say "we'll use the best model for everything" — this exercise shows that's a 3× cost difference they can't afford

## Slide 15 — Design Your Pricing
- This is where Madhavan's "Product-Market-Pricing Fit" lands — it's not enough to have product-market fit, you need to know people will pay, and HOW they want to pay
- Three steps on slide: (1) pick your strategy — Skim (Apple), Penetrate (Amazon), Maximize (Microsoft); (2) name the unit of work you'd meter; (3) set the structure (base + usage)
- **GitHub Copilot proof point:** charges $19/user = 4.75× the base SaaS price. Justified because coders complete tasks 55% faster. That's the "price = measure of value" principle in action
- Madhavan's WTP method to share: ask customers three questions — acceptable price, expensive price, prohibitively expensive price. Between expensive and prohibitive is a cliff — that's your psychological threshold
- **Labor test:** $100/hr human work vs $50/mo all-you-can-eat AI = you're giving away 99% of the value you create
- Why: most PMs price by looking at competitors. Madhavan's point is that 72% of innovations fail because they never checked willingness to pay. The exercise forces them to design around the price, not slap one on at the end
- **🔧 Tool:** "Open the Pricing Strategy Designer — it walks you through picking your strategy, naming the unit, setting the structure, and checking your bundling with the Leaders/Fillers/Killers framework. Everything auto-saves and exports to markdown."

## Slide 16 — Peer Stress-Test
- 6 minutes each, partner breaks your model
- Stress test 1: inference costs 3× — what breaks first?
- Stress test 2: heavy users 2× — they pay less than they burn
- One vulnerability written on paper per pair
- If pairs are being too polite, push them — the CFO won't be polite when they see 3× in a scenario plan
- Why: self-assessment is always generous. The peer challenge surfaces blind spots. The written vulnerability travels to Module 4

## Slide 17 — Build Moment (Board One-Pager)
- 15 minutes — the exec artifact
- Before/after comparison: current model vs AI-enhanced model
- Key reframe for the room: lower margin % can be fine if NRR and gross $ are both up. Revenue × margin = profit, and AI can expand the numerator
- Narrative line: what's the 12-month projection? What's the hedge?
- Why: execs need the STORY when margin % moves. This one-pager is what they'd actually present to a board. It's the most "real world" artifact in the module

## Slide 18 — Synthesis
- Tie back to Slide 4 — margin compression is the default. Now they have levers (cascading, routing, pricing model, bundling) and artifacts (cost curve, pricing strategy, board one-pager)
- Component 3 checklist on slide
- Quick recall: Madhavan says revisit pricing every 6-12 months, especially when you add new AI features

## Slide 19 — Bridge to M4
- Economics without trust doesn't convert — Module 4 is reliability, contracts, evaluation
- Bring: cost curve, pricing strategy, value capture, Components 1–3
- The Kill Switch from M2 feeds directly into M4's vendor evaluation framework

## Slide 20 — Survey
- 30 seconds, genuine thanks — close the loop
