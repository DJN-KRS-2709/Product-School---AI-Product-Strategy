# Module 4 — The Contract
## Speaker Briefing for Carlos

### What this module is about

This is the trust module. M1 diagnosed the bet, M2 built the defense, M3 proved the economics work. Now we're asking: does any of it matter if users don't trust the output? The emotional arc here is different from M3 — M3 was about math creating discomfort, M4 is about honesty creating accountability. Most PMs have never written down what their AI promises users. That gap between "our model is 95% accurate" and "here's what happens when it's wrong" is where the learning happens.

The word "contract" is deliberate. Not in the legal sense (though Air Canada makes it legal), but in the product sense: what are you explicitly promising users about reliability, what do they see when the system isn't sure, and what's your audit trail when things go wrong? By the end of this module, they've written that contract down. It's not a trust ethics sermon — it's a spec they can hand to engineering.

They leave with three artifacts: a golden dataset spec, a confidence UX design, and a draft reliability contract. Combined with the interactive tools (Golden Dataset Builder, Confidence UX Checklist), they have tangible output they can use at work on Monday. These artifacts also feed directly into M6 — the reliability contract becomes a key part of their board pitch.

### The flow and why it's structured this way

The first half is concept-heavy but moves fast through four connected ideas — trust vs. accuracy, golden datasets, HITL design, and LLM-as-Judge. Each gets one slide. We broke this into four lean slides rather than one long theory block based on the pattern that worked in M3: give each concept its own moment with a company example and a micro-interaction, so people stay engaged. Total lecture time is only 16 minutes for all four concepts.

The Air Canada case study sits right after the lecture block as the "reality check" — it takes the abstract concept of "your AI speaks for your brand" and makes it legal, dollars-and-cents concrete. The energy in the room should shift from "interesting concept" to "this could happen to us."

After the break, everything is hands-on. Golden dataset spec, confidence UX design, partner red-team, and the reliability contract. That's 53 minutes of applied work — the heaviest applied block in any module so far. The reliability contract at the end is the capstone because it forces them to put real numbers on promises they've been making implicitly. Even wrong numbers get corrected faster than mush.

---

### Slide 1 — Title

Set the tone: M3 was spreadsheets and cost curves, M4 is trust and craft. The shift in energy is intentional — M3 felt like a finance class, M4 should feel like a product design class where the product is trust itself. The three waypoints give structure: Define (what trust actually means), Measure (golden sets, judges, eval infra), Design (confidence UX — show doubt, don't fake certainty).

The interactive moment — "point to the waypoint that's your biggest gap" — gets an immediate read on the room. If most people point at waypoint 1, they don't yet distinguish trust from accuracy and you'll want to lean harder into the provocation. If most point at 2 or 3, they get the concept but haven't operationalized it — the applied blocks will land harder.

### Slide 2 — Agenda

Just orientation. Don't linger. The key message is that today has four lecture concepts packed tight (16 minutes total), one case study, and then a heavy applied second half. Flag the red-team exercise early as "sport, not judgment" — some participants get anxious about being challenged and it helps to pre-frame it as competitive and fun. If people are scanning ahead, that's fine; the agenda reduces format anxiety so they can focus on content.

### Slide 3 — Recall from M3

The bridge between modules matters. They brought their cost curve, pricing strategy, and Components 1–3 of the living strategy. The key connection: all of that economics work only pays off if users trust the output enough to keep using it. A product with great margins but silent failures is a lawsuit waiting to happen — and they're about to meet that exact lawsuit in the Air Canada case.

The pairs exercise ("which artifact actually moved your roadmap?") serves a dual purpose — it warms the room up with low-stakes conversation, and it reveals which M3 concepts actually stuck. If nobody mentions the cost curve, you know M3's applied work didn't convert to action yet. If someone says "the stress test changed how I think about our heaviest users," that's gold — M3 landed.

### Slide 4 — Provocation

Same vote-reveal-argue format from earlier modules — the room knows the rhythm by now, which means you can push harder on the substance. This provocation is built on a specific insight from Aman Khan at Arize AI (who was Director of Product at Spotify, Cruise, and Apple), who wrote in Lenny's Newsletter that evals are "the defining skill for AI PMs in 2025 and beyond." His line: "Prompts make headlines, but evals quietly decide whether your product thrives or dies." That's the energy for this slide.

The three false claims are sequenced to escalate discomfort. Claim #1 ("higher accuracy = more trust") is the most counterintuitive — push on it. Trust is a function of perceived control, not percentages. An 85% system with confidence scores, explanations, and override ability is trusted more than a 95% black box. If anyone pushes back, that's great — the debate IS the learning.

Claim #2 ("users don't care how the AI works") is half-right and worth acknowledging. They don't care about transformer architecture, but they care intensely about reliability signals: citations, "I'm not sure" messages, the ability to correct. Legibility is a product feature, not a technical detail.

Claim #3 ("we'll add evals later") is the guilt trip. Ask the room: "How many of you have shipped AI features without a golden dataset?" Most hands won't go up because they're embarrassed, but the silence IS the answer. Let the discomfort motivate. Jeetu Patel, Cisco's EVP, said it well on Lenny's podcast: "There's a trust deficit. If people don't trust these systems, they're not going to use them. Hallucination is a feature when you're writing poetry, but when you're trying to run predictable systems, hallucination can be a bad thing." That's a quotable line you can use in the room if the energy fits.

### Slide 5 — Trust ≠ Accuracy

This is the conceptual foundation for everything that follows. The visual contrast between the black box (95%) and the legible system (85%) should hit hard. Boards love accuracy slides — they're easy to understand and easy to brag about. Users love predictability — they want to know what happens when the system is wrong, not just how often it's right.

The company examples are deliberately chosen: Tesla/ADAS represents forced handoffs in high-stakes environments (the car literally takes your hands off the wheel when it's uncertain), while Perplexity and AI Overviews represent the source-citation pattern that's becoming table stakes for AI answers. The anti-example is "chatbot with no receipts" — generic, confident, no paper trail. That's the Air Canada energy that's about to show up in the case study.

The interactive question — "what's the failure users only discover after they trusted you?" — is intentionally scary. You want people thinking about their own product's silent failure modes before you teach them how to detect them. If the room is quiet, offer an example: "A support bot that looked fine for six months until someone realized it had been quietly inventing return policies."

### Slide 6 — Golden Datasets

This is where the module gets concrete. A golden dataset is just a labeled set of test cases that defines "good" for your specific product. Not a Kaggle leaderboard, not a public benchmark — your definition of quality, versioned like code, used as a release gate.

Grammarly is the anchor example on the slide — they maintain internal benchmark suites for correctness and tone across tiers, and those benchmarks gate releases. But there's an even more practical example from OpenAI worth mentioning verbally. Karina Nguyen, a researcher at OpenAI (ex-Anthropic), described on Lenny's podcast how she has PMs create spreadsheets: different tabs for current behavior vs. ideal behavior, with notes on why. Deterministic evals — "if the user says 7:00 PM, the model should say 7:00 PM" — pass or fail. That's literally what a golden dataset looks like before it's formalized. You can tell the room: "This isn't exotic data science. OpenAI's PMs build ground truth in spreadsheets. You can start there today."

The three roles of a golden dataset — regression (catch dips before users feel them), domain anchor (your definition of "good"), and proof for buyers (the demo when someone asks "how do you test?") — map directly to what they'll build in the applied block. The pairs exercise ("one nasty input your gold set must include") primes adversarial thinking before they hit the Golden Dataset Builder.

Hamel Husain and Shreya Shankar, who teach the #1 evals course on Maven (trained 2,000+ PMs and engineers from all the major labs), warn about a common mistake worth mentioning: teams jump to measuring "hallucination" or "toxicity" as generic scores instead of grounding evals in their actual failure modes. Off-the-shelf metrics are useful for sorting traces to discover patterns — not as dashboard scores to report. This is an important nuance if anyone in the room says "we already track hallucination rate."

### Slide 7 — Human-in-the-Loop Design

The key distinction on this slide is crutch vs. feature. HITL as a crutch means reviewing everything, costs explode, and the fixes vanish — nobody captures the corrections for the model to learn from. HITL as a feature means thresholded review (low confidence → human, high confidence → auto), captured fixes that feed back into training data, and clear escalation UX where the user opts in to human help.

The company examples are deliberately from regulated stacks: clinical imaging and ambient scribes require clinician sign-off on high-risk outputs. This normalizes HITL as professional practice, not a sign of weakness. Jason Droege of Scale AI put it well on Lenny's podcast: an agent "needs to know, if there's a low accuracy of what I'm about to accomplish, how do I pop it up to a human being for feedback?" That framing — the system knowing when to ask for help — is the design challenge.

The three levers at the bottom (threshold, capture fixes, escalation UX) connect back to M2's data flywheel. Every human correction is fuel for the flywheel if captured correctly. Say this once explicitly: "This is where M2's flywheel becomes real. Every correction is a training signal." It should land hard because they spent time designing that flywheel two sessions ago.

### Slide 8 — LLM-as-a-Judge

This slide answers a scaling problem: human rubrics don't scale to every completion. If you're generating thousands of outputs a day, you can't have humans review them all. The pattern at OpenAI, Anthropic, and most frontier labs is to pair automated graders (LLM judges) with spot-check human reviews. You calibrate the judge against your golden dataset and then use it for continuous regression, drift detection, and live routing decisions (auto / human / block).

Two important caveats worth mentioning. First, from Hamel and Shreya's work in Lenny's Newsletter: a judge that always predicts "pass" on a system that succeeds 99% of the time looks 99% accurate but never catches a single failure. That's why you measure True Positive Rate and True Negative Rate separately, not just overall accuracy. Second: the tools (LangSmith, Braintrust, etc.) give you judge infrastructure, but you still own the labels. If your golden dataset is weak, no amount of tooling saves you. The gold set is sacred — the judge is just the scaling mechanism.

The poll — "thumbs up if a model already grades your outputs somewhere" — gives you a read on how far the room has already gone. Many teams are already using LLM judges without calling them that. Name it for them.

### Slide 9 — Case Study: Air Canada

This is the centerpiece moment of M4. Air Canada's chatbot invented a bereavement policy that didn't exist. A customer relied on it. When the customer asked for the promised refund, Air Canada argued the chatbot was a "separate legal entity." The tribunal ruled: the bot speaks for the brand. Air Canada was liable.

The lesson isn't just "be careful with chatbots." The lesson is that the word "contract" in this module's title isn't a metaphor. When your AI makes a promise — explicit or implied — your company is on the hook. That's why you need receipts (golden dataset), thresholds (confidence UX), and escalation paths (HITL). Everything they learned in the lecture half comes together here as the answer to "how do you avoid being the next Air Canada?"

The pairs exercise — "worst thing your AI could say with high confidence" — is intentionally dramatic. You want people to feel the Air Canada energy in their own domain. Healthcare: a wrong medication interaction. Finance: a false tax deduction suggestion. Legal: a confident but made-up case citation. Let them scare themselves a little. That's what makes the applied blocks feel urgent rather than academic.

This case is also validated by Lenny's podcast — in the Aishwarya/Kiriti episode (Arize AI), they reference it directly: "Air Canada had this thing where one of their agents hallucinated a policy for a refund, which was not part of their original playbook." It's become the canonical cautionary tale for AI product trust.

### Slide 10 — Eval Dashboard Spec

This slide bridges from "why evals matter" to "what your eval system looks like in practice." Think of it as the Datadog or Stripe status page for AI quality. Four quadrants: metrics (quality, latency, confidence spread, HITL%, overrides), judge setup (model, rubric, gold set, thresholds), drift alerts (auto-ping when trends cross the line), and UX hooks (scores visible in UI, citations, thumbs-up feedback loops).

The key challenge for Carlos: push the room with "Would you screen-share this in a sales call next Tuesday?" If the answer is no, the eval system isn't product-grade — it's an internal monitoring tool nobody looks at. Nick Turley, Head of ChatGPT at OpenAI, said on Lenny's podcast that he started "writing evals before I knew what an eval was because I was just outlining very clearly specified ideal behavior for various use cases." He realized evals might be "the lingua franca of how to communicate what good looks like." That's the energy this slide should carry — evals aren't a technical obligation, they're how you make quality visible and communicable.

### Slide 11 — Break

Reset before the heavy applied work. Frame what's coming: "After break you're building three things — golden dataset spec, confidence UX, and a reliability contract. And in between, your partner is going to try to break everything." Tease the red-team exercise as sport, not judgment. Suggest they think about their product's worst confident failure during the break — it'll prime them for the golden dataset exercise.

### Slide 12 — Golden Dataset (Applied)

This is 15 minutes of writing, and they should leave with a spec, not a feeling. The three panels (Scope, Sources, Maintenance) are structured to force specificity: domain, input/output types, target size (100–500 rows), real user data vs. expert-curated vs. adversarial, owner name, update cadence, versioning approach.

The "sales test" one-liner — "Here's how we test our AI" — is a forcing function. If they can't say it in one sentence, the spec isn't crisp enough. Teams like Notion and Linear treat eval sets like versioned product assets — you can mention that as aspiration if the room needs it.

The interactive tool link is on this slide — students can open the Golden Dataset Builder, which structures test cases by category, lets them tag adversarial rows, and exports a clean spec they can hand to engineering on Monday. Point people there, especially anyone who gets stuck staring at blank panels.

For coaching: a "good" golden dataset spec names a specific domain (not "our product" but "customer support ticket classification"), has at least one adversarial row (the input that would be most embarrassing to get wrong), and has a named owner. A "bad" spec is vague on scope, has zero adversarial cases, and lists "the team" as the owner — nobody owns it, nobody maintains it.

### Slide 13 — Confidence UX (Applied)

This is where Air Canada energy meets product design. A one-mode UI ("here's the answer") creates the exact liability problem they just studied. Three tiers — confident (>90%), uncertain (50–90%), not confident (<50%) — force them to design what the UI looks like at each level: colors, copy, user controls.

The reference companies are Grammarly (depth of rewrite varies with confidence — full rewrite when sure, lighter suggestion when less sure) and Copilot (citations appear, tone softens when the model is uncertain). These are products many people in the room use daily, so the pattern should feel familiar rather than abstract.

The four Y/N questions at the bottom (adjust threshold? see reasoning? correct & override? corrections → model?) are deliberately binary. Force the decision. The last one — "corrections feed back to the model" — connects directly to M2's flywheel. If the answer is yes, every user correction makes the product smarter. If no, they're leaving data on the table. Say it once: "That yes/no is the difference between a learning system and a static one."

The interactive tool (Confidence UX Checklist) is a 16-point audit across confidence display, fallback design, HITL triggers, and transparency. It gives them a coverage score and surfaces the gaps they haven't thought about yet.

### Slide 14 — Red-Team (Peer Challenge)

This is the cheapest place to fail — in a classroom, with a partner, not in production or in court. The four attack cards (confident hallucination, adversarial input, ground truth shifts, boundary cases) give structure to what could otherwise be unfocused poking.

Keep it timeboxed: 6 minutes each direction. The attacker uses one or more of the four lenses to stress-test the partner's eval spec and confidence UX. The defender learns where their spec has blind spots. After both rounds, each pair names one line — "the worst miss my partner found." Those one-liners should be uncomfortable. If they're not, the red-teaming was too polite. Push them.

If the room needs gravitas, reference Microsoft's internal red-team programs for Copilot — enterprise red-teaming is a formal practice at the largest AI companies, not a classroom exercise they should feel embarrassed about. Better to find the failure here than in a tribunal ruling.

### Slide 15 — Reliability Contract (Build Moment)

This is the capstone artifact of M4 and the one that feeds most directly into M6's board pitch. The four quadrants — Promise, Measurement, Escalation, Feedback Loop — form a complete accountability framework.

Push for real numbers even if they're draft numbers. "We commit to 92% accuracy on Tier 1 queries, measured weekly against our golden dataset, with automated alerts at 88%." That's a contract. "We'll try to be accurate" is mush. The analogy is cloud SLAs — AWS doesn't promise "pretty good uptime," it promises 99.99% with defined credits when they miss. That specificity creates accountability, and accountability creates trust. Even wrong numbers get corrected faster than vague aspirations — because wrong numbers force a conversation about what the right number should be.

The partner share — "one promise you'd sign today vs. one you'd redline" — surfaces which commitments feel real and which feel aspirational. The redlined ones are the honest gaps. Those gaps become the first items on their M5 roadmap.

### Slide 16 — Synthesis

Close the loop back to slide 4. They walked in thinking trust = accuracy. They're leaving with an audit trail: golden dataset spec, confidence UX design, reliability contract. Component 4 of the living strategy is tangible — it's not a feeling, it's a set of specs they can hand to engineering and show to buyers.

The clap — "if today changed what you'll demo next sprint" — is a quick energy check. If the room claps, they felt the artifacts were real. If it's quiet, ask what's missing — that feedback shapes what you emphasize in M5.

### Slide 17 — Bridge to M5

The bridge is simple: trust at the product level (M4) is different from trust at the organizational level (M5). M4 was about your product being reliable. M5 is about what breaks when you scale that product across teams, when agents start operating autonomously, when shadow AI tools proliferate across the org. The hook: governance isn't a compliance burden — it's the thing that closes the enterprise deal.

They should bring to M5: eval dashboard spec, reliability contract, confidence UX design, and all four components of the living strategy.

### Slide 17.5 — Module Tools

Just point students to the interactive tools. These are for continued work during or after class. Mention that data saves to the browser and carries forward to M5 — no work is lost.

### Slide 18 — Survey

Quick close. Thank them genuinely — this was the most writing-intensive module so far and they produced real artifacts. The feedback shapes how Carlos and Daria tune the balance between hands-on and theory in future cohorts.
