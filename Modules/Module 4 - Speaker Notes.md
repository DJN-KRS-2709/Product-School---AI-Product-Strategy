# Module 4 — The Contract

## Slide 1 — Title
- Hardest product challenge in AI: trust
- They'll walk out with a golden dataset spec, eval dashboard, confidence UX, and a reliability contract

## Slide 2 — Agenda
- Lecture on trust psychology, eval infrastructure, confidence UX
- Applied work: golden dataset + confidence UX design
- Peer challenge: red-team each other's eval spec

## Slide 3 — Recall from M3
- They brought cost curve, board-ready comparison, Components 1-3
- The economics only work if users trust the output enough to pay

## Slide 4 — Provocation
- "Higher accuracy = more trust" — nope, trust comes from perceived control. An 85% system that shows confidence scores and lets you override beats a 95% black box every time
- "Users don't care how it works" — they don't care about transformers, but they absolutely care about confidence scores, citations, "I'm not sure" messages. Legibility drives adoption
- "We'll add evals later" — most expensive mistake in AI. Systems degrade silently. By the time users complain, trust is gone. Evals are launch infrastructure

## Slide 5 — Trust ≠ Accuracy
- Black box: 95% accurate, no explanation, no override — users find out it's wrong by consequence
- Legible system: 85% accurate, shows confidence, cites sources, lets you correct
- Users trust the second one every time. The research is clear

## Slide 6 — Golden Datasets
- Curated inputs with known-correct outputs — your ground truth
- Why it matters: regression testing (catch drops before users), domain anchoring (what "good" means in your domain), and it's a sales asset (enterprise customers ask "how do you test this?")
- Start with 100-500 real examples, include edge cases and adversarial stuff

## Slide 7 — Human-in-the-Loop Design
- HITL as crutch: human reviews everything, doesn't scale, AI never gets better
- HITL as feature: human steps in at confidence thresholds, corrections feed back into the model, HITL rate goes down over time
- This is how you make the M2 correction loop a 5

## Slide 8 — LLM-as-a-Judge
- Human eval doesn't scale — use a second model to judge the first
- Three uses: regression testing, drift detection, real-time quality gates
- Who judges the judge? The golden dataset. Ground truth all the way down

## Slide 9 — Case Study: Air Canada Chatbot
- Bet: chatbot for customer service — bookings, baggage, bereavement fares
- Crack: chatbot made up a bereavement fare policy with perfect confidence. Air Canada's lawyers said the chatbot was a "separate legal entity" — tribunal said absolutely not
- Correction: the chatbot speaks for the company, period. You need confidence thresholds, source grounding, human escalation, audit trails
- Ask: "what's the worst thing your AI could confidently say that's wrong?"

## Slide 10 — Eval Dashboard Spec
- Four pieces: metrics panel, judge configuration, drift alerts, UX integration
- Two audiences: internal (catch problems) and external (enterprise sales)
- If you can't show this in a sales meeting, it's not product-grade

## Slide 11 — Break
- 5 min

## Slide 12 — Define Your Golden Dataset
- 15 min — domain scope, input/output types, target examples, sources
- Include failure cases and adversarial inputs, not just happy path
- Who owns it, how often is it updated, how is it versioned

## Slide 13 — Design Your Confidence UX
- 10 min — three tiers: confident (>90%), uncertain (50-90%), not confident (<50%)
- What changes in the UI at each level? Colors, language, controls
- Corrections that feed back = M2 flywheel connection

## Slide 14 — Peer Challenge: Red-Team
- 6 min per person
- Four attacks: confident hallucination, adversarial input, ground truth changes, boundary cases
- Find the failure mode the defender didn't think of

## Slide 15 — Build Moment: Reliability Contract
- 15 min — the promise (accuracy, response time, uptime), the measurement (what you track), the escalation (what happens when quality drops), the feedback loop (how corrections improve the system)
- This is what they show customers and the board in M6

## Slide 16 — Synthesis
- Fill in Component 4 — golden dataset, eval dashboard, confidence UX, reliability contract, top failure mode, HITL architecture

## Slide 17 — Bridge to M5
- M5 is about what breaks at scale — compounding systems, agent governance, shadow AI audits
- Governance as a sales asset, not compliance overhead

## Slide 18 — Survey
- QR code / link
