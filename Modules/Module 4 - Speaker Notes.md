# Module 4 — The Contract
## Speaker Briefing for Carlos

### What this module is about

This module teaches participants how to make reliability a visible product feature — not a backend metric. The core argument: trust is a function of perceived control, not accuracy percentages. We cover four concepts (trust vs. accuracy, golden datasets, human-in-the-loop design, LLM-as-Judge), ground them in a real legal case (Air Canada), then build three artifacts: a golden dataset spec, a confidence UX design, and a reliability contract.

### The flow and why it's structured this way

Three learn-then-do cycles instead of front-loading all theory. Cycle 1 (pre-break): two concept slides on trust and golden datasets, then 15 minutes building a golden dataset spec while the concepts are fresh. After a 5-minute break, Cycle 2: HITL design lecture + Air Canada case study as the scare story, then 10 minutes designing confidence UX while the motivation is hot. Cycle 3: LLM-as-Judge + Eval Dashboard framework, then red-team peer challenge + reliability contract capstone. Every concept gets applied within minutes of learning it. Early on, use the agenda slide for structural orientation only — it shows the interleaved flow (concept → build → break → concept + case → build → concept → challenge → build); signal that today alternates between learning and doing with no long lecture stretches. Presentation, quick scan, under one minute. Pre-frame the red-team exercise as "sport, not judgment" so nobody gets anxious about it.

---

### Slide 1 — The Contract

**Teaching:** We're framing the module around three waypoints — Define (what trust actually means), Measure (golden datasets, judges, eval infra), and Design (confidence UX). The key shift from M3: economics only matter if users trust the output enough to keep paying. The three deliverables are listed on-slide: Component 4 of the living strategy, an eval dashboard spec, and a reliability contract.

**Doing:** Presentation only. Walk through the three waypoints briefly to orient the room, then move to the agenda.

### Slide 4 — Recall from M3

**Teaching:** Connecting M3 to M4. They brought their cost curve, Components 1–3, and their value capture comparison. The bridge: all that economics work only pays off if users trust the output. A product with great margins but silent failures is a lawsuit waiting to happen.

**Doing:** Presentation + 30-second pair warm-up. Show the three artifact cards, then ask pairs: "Which of these artifacts actually moved your roadmap since last session?" This warms the room and reveals which M3 concepts stuck.

### Slide 5 — Provocation

**Teaching:** Three claims the room votes on, all revealed as FALSE. Claim #1: "Higher accuracy = more trust" — false because trust is about perceived control, not percentages (an 85% system with scores and overrides beats a 95% black box). Claim #2: "Users don't care how the AI works" — false because they care about reliability signals like citations and "I'm not sure" messages. Claim #3: "We'll add evals later" — false because AI degrades silently and evals are launch infrastructure. Context: Aman Khan (Arize AI, ex-Spotify/Cruise/Apple) wrote in Lenny's Newsletter that evals are "the defining skill for AI PMs" and "prompts make headlines, but evals quietly decide whether your product thrives or dies."

**Doing:** Interactive poll — vote, reveal, argue. For each claim, ask for a show of hands (true or false?), then reveal the answer and spend a minute on the argument. For claim #3, ask the room directly: "How many of you have shipped AI without a golden dataset?" Let the silence land. Total: 8 minutes.

### Slide 6 — Trust ≠ Accuracy

**Teaching:** The conceptual foundation for the module. The slide contrasts a 95% black box (no scores, no override, surprises in production) against an 85% legible system (confidence scores, sources, user can correct). Company examples: Tesla/ADAS forces handoffs when the system is uncertain; Perplexity and AI Overviews lead with source citations. These are patterns the room already uses as consumers.

**Doing:** Lecture, ~4 minutes. Present the two-card comparison, name the company examples, then pose the open question on-slide: "What's the failure users only discover after they trusted you?" If the room is quiet, offer an example: "A support bot that looked fine for six months until it was quietly inventing return policies."

### Slide 7 — Golden Datasets

**Teaching:** A golden dataset is a labeled set of test cases that defines "good" for your specific product — versioned like code, used as a release gate. Three roles: regression (catch dips before users feel them), domain anchor (your definition of quality, not a public leaderboard), and proof for buyers ("Show me how you test" — this is the demo). Company examples on-slide: Grammarly gates releases against correctness + tone benchmarks; OpenAI's PMs build ground truth in spreadsheets (current behavior vs. ideal behavior, pass/fail). Context from Lenny's: Karina Nguyen at OpenAI described this practice — tell the room "This isn't exotic data science. You can start there today."

**Doing:** Lecture, ~4 minutes, ending with a 45-second pair exercise. Present the three roles, then pairs share: "One nasty input your gold set absolutely must include." This primes adversarial thinking for the applied block that's coming immediately next.

### Slide 9 — Golden Dataset

**Teaching:** They just learned what golden datasets are — now they build one while the concept is fresh. They're writing an actual golden dataset spec for their own product across three panels: Scope (domain, input/output types, target 100–500 rows), Sources (real user data, expert-curated, adversarial/edge cases — Y/N each), and Maintenance (owner, update frequency, versioning). The forcing function is the "sales test": can you say "Here's how we test our AI" in one sentence? Good spec = specific domain, at least one adversarial row, named owner. Bad spec = vague scope, no edge cases, "the team" owns it. **Mental model:** That three-part structure (scope / sources / maintenance) is a thinking scaffold — their real spec may need different categories depending on domain and buyer expectations; adapt the headings, don't treat them as a form to fill.

**Doing:** 15 minutes of solo writing on their own product. The Golden Dataset Builder tool is linked on-slide — point stuck participants there. At the end, a stand-up check: "Stand up if your set includes at least one adversarial row." This creates light social accountability. Then break.

### Slide 10 — Break

**Teaching:** Nothing — reset after intensive writing.

**Doing:** 5-minute break. Tease what's coming: "After break we start with a scare story about what happens when AI makes promises without guardrails. Then you're building confidence UX, and your partner is going to try to break everything you've built."

### Slide 12 — Human-in-the-Loop

**Teaching:** The distinction between HITL as a crutch (review everything, costs explode, corrections vanish) vs. HITL as a product feature (thresholded review, captured fixes that feed back to training, clear escalation UX). Company examples: clinical imaging and ambient scribes in healthcare — clinician sign-off on high-risk outputs is normal practice, not a sign of weakness. The three levers on-slide (threshold, capture fixes, escalation UX) connect back to M2's data flywheel: every human correction is a training signal if captured.

**Doing:** Lecture, ~4 minutes. Present the crutch vs. feature comparison and the three levers, then the on-slide prompt: "Point to your answer — where would a human catch a catastrophic miss first?" Participants physically point at a part of the slide. Make the M2 flywheel connection explicit once: "This is where the flywheel becomes real."

### Slide 13 — Air Canada Case

**Teaching:** Air Canada deployed a customer service chatbot that invented a bereavement refund policy that didn't exist. A customer relied on it. When the customer asked for the refund, Air Canada argued the chatbot was a "separate legal entity." The tribunal ruled: the bot speaks for the brand, you're liable. The lesson: "contract" in this module's title isn't a metaphor — when your AI makes a promise, your company is on the hook. That's why you need the golden dataset (receipts), confidence UX (thresholds), and HITL (escalation paths). The slide uses the standard 3-act format: Bet, Crack, Correction.

**Doing:** Case study presentation (3-act walkthrough, ~3 minutes), then a 60-second pair exercise. Walk through the three cards, then pairs discuss: "Worst thing your AI could say with high confidence?" Push for domain-specific answers — healthcare: wrong med interaction; finance: false tax deduction; legal: made-up case citation. Debrief 1-2 answers from the room. Total: 7 minutes. This is the emotional fuel for the confidence UX exercise immediately following.

### Slide 14 — Confidence UX

**Teaching:** With HITL and Air Canada fresh in their minds, they're designing what their product's UI looks like at three confidence levels: >90% (confident — full answer), 50–90% (uncertain — what visibly softens?), <50% (not confident — block, escalate, or human queue). Reference patterns: Grammarly adjusts rewrite depth based on confidence; Copilot adds citations and softens tone when unsure. Four binary Y/N decisions at the bottom: can users adjust the threshold, see AI reasoning, correct & override, and do corrections feed back to the model? The last one is the M2 flywheel connection.

**Doing:** 10 minutes of solo fill-in on their own product. The Confidence UX Checklist tool (16-point audit) is linked on-slide. Closes with: "Point to your screen — which tier is your live product closest to?"

### Slide 15 — LLM-as-Judge

**Teaching:** Human rubrics don't scale to thousands of outputs per day. The pattern at frontier labs (OpenAI, Anthropic): pair automated LLM judges with spot-check human reviews, calibrated against the golden dataset. Three use cases on-slide: regression (judge vs. golden rows, continuous), drift detection (trend alerts before NPS drops), and quality gates (live routing: auto / human / block). Key nuance: the tools (LangSmith, Braintrust) provide infrastructure, but you still own the labels — the gold set is sacred, the judge is the scaling mechanism.

**Doing:** Lecture, ~4 minutes. Present the three use cases, then a quick thumbs-up poll: "Thumbs up if a model already grades your outputs somewhere." Many teams are doing this without calling it "LLM-as-Judge" — name it for them.

### Slide 16 — Eval Dashboard

**Teaching:** This bridges from "why evals matter" to "what your eval system looks like." Four quadrants on a 2x2 grid: metrics (quality, latency, confidence spread, HITL%, overrides), judge setup (model, rubric, gold set, thresholds), drift alerts (auto-ping when trends cross the line), and UX hooks (scores in UI, citations, thumbs-up loops). Analogy: think Datadog or Stripe status-page energy for AI quality. Context from Lenny's: Nick Turley (Head of ChatGPT) said he started "writing evals before I knew what an eval was — just outlining clearly specified ideal behavior."

**Doing:** Framework presentation, ~4 minutes. Walk through the four quadrants, then pose the challenge on-slide: "Thumbs up if you could screen-share this to a buyer next week." If most thumbs are down, that's the gap — the red-team coming next will pressure-test everything. Total: 5 minutes.

### Slide 17 — Red-Team

**Teaching:** Partners stress-test each other's eval spec and confidence UX using four attack lenses: confident hallucination (95% confident and wrong — then what?), adversarial input (injection, messy real text), ground truth shifts (policy changed, gold set is stale), and boundary cases (never-seen inputs — what breaks?). This is the cheapest place to find failures — better here than in production or a tribunal.

**Doing:** 13 minutes total — 6 minutes each direction (one attacks, one defends), then a 1-minute debrief. After both rounds, each pair states one line: "Worst miss my partner found." If the one-liners aren't uncomfortable, the red-teaming was too polite — push them.

### Slide 19 — Build

**Teaching:** The capstone artifact of M4 — what they promise users, how they measure it, what happens when it breaks, and how corrections feed back. Four quadrants: The Promise (accuracy %, response time, uptime), The Measurement (metrics, method, reporting cadence), The Escalation (below threshold actions, who's notified, what users see), The Feedback Loop (corrections to model, dataset updates, cadence). Analogy: cloud SLAs — AWS doesn't promise "pretty good uptime," it promises 99.99%. Push for real draft numbers — even wrong numbers get corrected faster than mush. **Mental model:** The four-quadrant layout is a thinking framework for promise / measurement / escalation / feedback — they should add, merge, or drop quadrants to match their product's trust surface, not force-fit a 2×2.

**Doing:** 15 minutes of solo writing, then a partner share: "One promise you'd sign today vs. one you'd redline." The redlined ones surface the honest gaps — those become M5 roadmap items.

### Slide 20 — Synthesis

**Teaching:** Close the loop to slide 5. They walked in thinking trust = accuracy; they're leaving with an audit trail — golden dataset spec, confidence UX, reliability contract. Component 4 of the living strategy is now tangible specs, not feelings.

**Doing:** Presentation, ~2 minutes. Quick energy check: "Clap once if today changed what you'll demo next sprint."

### Slide 21 — Bridge to M5

**Teaching:** M4 was product-level trust. M5 is what breaks at organizational scale — agents operating autonomously, shadow AI tools across the org, governance as a sales asset (not a compliance burden). They bring to M5: eval dashboard spec, reliability contract, confidence UX, Components 1–4.

**Doing:** Presentation, ~2 minutes. Show the module arc visual with M5 highlighted.

### Slide 26 — Survey

**Teaching:** None — this is feedback collection.

**Doing:** Show QR/link. Quick genuine thank-you — this was the heaviest writing module so far.
