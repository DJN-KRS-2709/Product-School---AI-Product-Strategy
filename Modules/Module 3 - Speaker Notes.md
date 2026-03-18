# Module 3 — The Margin

## Slide 1 — Title
- The "will this actually make money?" session
- They'll build a cost model, a pricing strategy, and a board-ready P&L comparison

## Slide 2 — Agenda
- Two applied work blocks (cost model + pricing), peer stress-test, then a board-ready comparison as the build moment

## Slide 3 — Recall from M2
- They brought their flywheel map, Kill Switch audit, Components 1-2
- The flywheel is great — but if every spin costs more than it earns, it's a liability

## Slide 4 — Provocation
- "AI will lower our costs" — eventually, but not yet. Margins drop from 80% to 40-60% and most leaders don't see it until the P&L lands
- "We should price per seat" — nope, seat-based works for tools humans use. AI does work. Pricing per seat for a system that does the work is like a flat taxi fare regardless of distance
- "Scale will fix the economics" — nope, Gokul killed this one. Scaling a money-losing AI product just scales the losses. The fix is architectural (cascading, caching) and strategic (pricing)

## Slide 5 — The Margin War
- Traditional SaaS: 80% margins, ~$5-8/seat COGS
- Add AI: 1,000 calls/user/month at GPT-4 rates = $15-60/user/month in COGS. 80% margin becomes 40%
- The trap: leaders plan AI features with SaaS margin assumptions and ignore the cost side

## Slide 6 — Model Cascading
- A classifier routes requests: 80% go to cheap models, 20% go to frontier
- Blended cost drops ~70% — that's the difference between 40% margin and 65%
- Other levers: quantization, semantic caching, prompt optimization
- The classifier has to be accurate or UX breaks

## Slide 7 — Access Products vs. Work Products
- Access product = tool humans use (Figma, Notion). Per-seat makes sense
- Work product = AI does the work (Klarna tickets, Harvey legal docs). Price per outcome
- Most heading toward hybrid: base fee + usage tiers
- Gokul's big insight: labor budget is the new TAM, not software budget. If your AI replaces $150K/year in labor and you charge $50/month, that's a 99% discount

## Slide 8 — Commoditize the Complement
- Where does the profit pool live — data or workflow?
- Option 1: own the data, commoditize the workflow
- Option 2: own the workflow, commoditize the data
- Gokul's margin advice: price increases beat cost decreases. And not every AI feature needs to be a profit center — some exist for retention (Square model)

## Slide 9 — Case Study: Klarna
- Bet: AI support handled 2/3 of chats in month one, equivalent to 700 agents
- Crack: inference costs scaled with volume, complex cases still needed humans, P&L got less predictable
- Correction: moved to cascading, shifted narrative from cost-cutting to value (speed, 24/7, multilingual)
- Ask: "pricing for the headline or the P&L?"

## Slide 10 — The Margin Calculator
- Six inputs: requests/user/month, cost/request, COGS/user, revenue/user, margin/user, margin %
- Stress tests: costs 3x, heaviest segment doubles usage, provider raises prices 50%
- Below 40% in the stress test = needs architectural intervention

## Slide 11 — Break
- 5 min

## Slide 12 — Build Your Cost Curve
- 15 min — map every AI feature by complexity, assign model tiers, estimate volume, get blended cost
- Don't forget embedding calls. Don't assign everything to GPT-4

## Slide 13 — Design Your Pricing Strategy
- 10 min — base fee + what AI work gets charged separately
- The labor test: if AI replaces $100/hour human work and you charge $50/month, you're leaving 95%+ on the table

## Slide 14 — Peer Challenge: Stress-Test
- 6 min per person
- Triple the inference costs — does the model still work?
- Double the heaviest user segment — power users now cost 5x what they pay
- Write down the biggest economic vulnerability

## Slide 15 — Build Moment: Value Capture Comparison
- 15 min — one-page before/after their board can read in 2 minutes
- Before: SaaS model. After: AI model. Revenue, COGS, margin, narrative
- The hard part is the narrative: lower margins on higher value capture
- This goes to M6 for the board presentation

## Slide 16 — Synthesis
- Fill in Component 3 — cost curve, blended COGS, pricing model, margin % (current + stressed), board comparison, top vulnerability

## Slide 17 — Bridge to M4
- M4 is about trust — 95% accuracy with no audit trail loses to 85% with one
- Bring everything

## Slide 18 — Survey
- QR code / link
