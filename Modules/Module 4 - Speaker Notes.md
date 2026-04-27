# Module 4 — The Contract

### What this module is about

Modules 2 and 3 gave you a moat and an economics engine. Today we find out if any of it matters — because none of it does if users don't trust the output enough to keep using it. This is the session where reliability stops being a backend concern and becomes a visible product feature. The core idea I want stuck in your heads by the time we're done: trust is a function of perceived control, not accuracy percentages. That's counterintuitive, and it's the whole game.

We're covering four concepts today — trust vs. accuracy, golden datasets, human-in-the-loop design, and LLM-as-Judge — and we're grounding all of it in a real legal case that should genuinely scare you. By the end, you'll have built three artifacts: a golden dataset spec, a confidence UX design, and a reliability contract. This is where the strategy doc gets teeth. Up until now it's been about value and money. Today it's about promises — the kind your company is legally on the hook for. Lets get into it.

### The flow and why it's structured this way

We're doing three learn-then-do cycles instead of front-loading all the theory. I've found that if you lecture for 40 minutes and then say "OK now build something," half the room has mentally checked out. So we're interleaving. Cycle 1, before break: two concept slides on trust and golden datasets, then 15 minutes where you build a golden dataset spec while the ideas are still fresh. After a five-minute break, Cycle 2: human-in-the-loop design plus the Air Canada case study as our scare story, then 10 minutes designing confidence UX while the motivation is hot. Cycle 3: LLM-as-Judge and the Eval Dashboard framework, then a red-team peer challenge and the reliability contract as the capstone. Every concept gets applied within minutes of learning it — no long lecture stretches. I'll walk through the agenda slide quickly just so you can see the interleaved flow, but we won't dwell on it. One heads-up: later today you're going to red-team each other's work. Think of it as sport, not judgment — we're trying to find the cracks before your users do.

---

### Slide 1 — The Contract

Alright, welcome back everyone. Today has three waypoints — Define, Measure, and Design. Define: what trust actually means. Measure: golden datasets, judges, eval infrastructure. Design: confidence UX. Heres the thing — all those economics we worked through in Module 3 only matter if users trust the output enough to keep paying. You can have beautiful margins and still be one silent failure away from a disaster. And I mean a real disaster, not a bad review — we're talking legal liability. Three deliverables by end of day: Component 4 of your living strategy, an eval dashboard spec, and a reliability contract. Busy day, but honestly? This is the module where everything starts feeling real. Lets get into it.

### Slide 2 — Expectations

Same ground rules. Cameras on, Slack for questions. Today we're doing three learn-then-do cycles instead of front-loading theory. So the pace is different — you'll build something within minutes of learning a concept. Stay sharp, it moves fast.

### Slide 3 — Course Arc

Quick look at where we are. Modules 1 through 3 covered your bet, your moat, and your margins. Today is Module 4 — The Contract. Trust and reliability. After today we have governance and the capstone pitch. Were in the back half now and the artifacts are getting more specific.

### Slide 4 — Recall from M3

Quick reconnect. You brought your cost curve, Components 1 through 3, and your value capture comparison from last time. All that economics work — the margins, the pricing, the cost optimization — it only pays off if users trust the output. A product with great margins but silent failures is a lawsuit waiting to happen. Literally, as we'll see later today. I'm not being dramatic. We have a case study coming up that will prove it.

OK so turn to your partner for 30 seconds. Look at these three artifact cards on screen — which of them actually moved your roadmap since last session? Be honest with each other. I genuinely want to know what stuck and what didn't. If nothing stuck, that's a finding too.

### Slide 5 — Provocation

Alright, three claims on screen. I want a show of hands for each — true or false? And don't just go with the crowd, I can see you.

Claim one: "Higher accuracy equals more trust." Hands up if you think that's true. OK — it's false, and this is the big one for today. Trust is about perceived control, not percentages. An 85% system with confidence scores and override buttons beats a 95% black box every single time. Users don't trust what they can't see into. I know that feels backwards, but sit with it — it's going to keep coming up.

Claim two: "Users don't care how the AI works." True or false? Also false. They absolutely care about reliability signals — citations, "I'm not sure" messages, sources. They may not want a technical explanation, but they want to know the system knows its own limits. Sound familiar? Think about the last time you used an AI tool and it gave you a confident wrong answer. How did that feel?

Claim three: "We'll add evals later." Show of hands. False — and this one matters more than most people realize. AI degrades silently. Not like a server crash where you get a page at 3 AM. It just slowly gets worse and nobody notices until the damage is done. Evals aren't a nice-to-have, they're launch infrastructure. I'd go so far as to say evals are the defining skill for AI PMs. Prompts make headlines, but evals quietly decide whether your product thrives or dies.

Quick reality check — how many of you have shipped AI without a golden dataset? Yeah. Let that sit for a second. No judgment, but that changes today.

### Slide 6 — Trust ≠ Accuracy

OK so this is the conceptual foundation for everything today. Look at these two cards on screen. On the left: a 95% accurate system — no scores, no override, surprises in production. On the right: an 85% accurate system — confidence scores visible, sources cited, user can correct the output. Which one do you actually trust more as a user?

You already know the answer because you live it every day. Heres a story. Tesla's ADAS — their driver assist — forces handoffs when the system is uncertain. It literally tells you "take the wheel." It doesn't pretend to be confident when it's not. That's a design choice, and it's brilliant. Perplexity and AI Overviews lead with source citations. Not because they have to, but because it makes you trust the answer more. These aren't exotic design patterns. You use them as consumers every day without thinking about it.

So here's the question I want you sitting with: what's the failure users only discover after they've already trusted you? If the room is quiet, I'll give you one — imagine a support bot that looked fine for six months. Customers were happy, metrics were green. Then someone realized it was quietly inventing return policies. Just making them up. The policies sounded so reasonable that nobody questioned them until a customer tried to actually use one. We'll come back to that exact scenario later, and yeah, it really happened.

### Slide 7 — Golden Datasets

A golden dataset is a labeled set of test cases that defines "good" for your specific product. Versioned like code, used as a release gate. Think of it as your product's definition of quality, written down and testable.

Three roles to think about. First, regression — catching quality dips before users feel them. You push a model update on Tuesday and your golden set tells you Wednesday morning whether anything broke. Second, domain anchor — this is YOUR definition of quality, not some public leaderboard that has nothing to do with your use case. I can't tell you how many teams I've seen bragging about benchmark scores that have zero correlation with what their users actually care about. Third, proof for buyers. When an enterprise customer says "show me how you test," this is the demo. This is the receipts.

Heres the thing — this isn't exotic data science. Grammarly gates every release against correctness and tone benchmarks. PMs at frontier labs build ground truth in spreadsheets — current behavior vs. ideal behavior, pass/fail. You can start one in a spreadsheet today. Seriously, a Google Sheet with 50 rows is better than nothing.

Turn to your partner. 45 seconds. Share one nasty input your gold set absolutely must include. Think about the worst thing a user could throw at your product. The offensive content, the edge case, the thing that would embarrass you on Twitter. This primes us for the build exercise coming right after.

### Slide 8 — Trust Infrastructure

Alright, first lab of the day. You just learned about golden datasets — now you're building one while it's fresh. This is the Trust Infrastructure lab. Scope, sources, maintenance — three panels, fifteen minutes. Lets go.

### Slide 9 — Golden Dataset

Great stuff. You just learned what golden datasets are. Now you're building one while it's fresh. You've got three panels to fill in for your own product. Scope — your domain, input and output types, target 100 to 500 rows. Sources — real user data, expert-curated, adversarial edge cases, yes or no for each. And Maintenance — who owns it, how often it gets updated, how you version it.

Here's the forcing function, and I love this one. Can you say "Here's how we test our AI" in one sentence? If you can't, your spec isn't tight enough. A good spec has a specific domain, at least one adversarial row, and a named owner. A bad spec has vague scope, no edge cases, and "the team" owns it — which means nobody owns it. Lets be honest, we've all written that spec before. Today we fix it.

The three-part structure — scope, sources, maintenance — is a thinking scaffold to get you started. Your real spec might need different categories depending on your domain and your buyers. Adapt the headings, don't treat them as a form to fill.

You've got 15 minutes. The Golden Dataset Builder tool is linked on-slide if you get stuck — open it up, it'll walk you through it. When time's up, I'm going to ask you to stand up if your set includes at least one adversarial row. Lets see who's being honest with themselves. And if you're not standing — no shame, but we're going to talk about why.

### Slide 10 — Break

Amazing work so far. Seriously — you just built a golden dataset spec from scratch. That alone is more than most AI teams have. You deserved a break. Take five minutes — grab some water, stretch, clear your head. When we come back, I promised you a scare story, and I'm going to deliver. It's about what happens when AI makes promises without guardrails. Then you're building confidence UX, and after that, your partner is going to try to break everything you've built. Fair warning — it's going to get fun.

### Slide 11 — Cameras On

Welcome back! Cameras on for this next stretch. We've got a scare story coming up that I think will get your attention, then you're designing confidence UX, and after that your partner is going to try to break everything you've built. Should be fun. Stay engaged.

### Slide 12 — Human-in-the-Loop

OK, lets talk about human-in-the-loop — HITL. There are two versions of this and I'll tell you right now, most teams are running the wrong one.

HITL as a crutch: review everything, costs explode, corrections vanish into the void. Nobody learns from them. It's like having a spell-checker that you never actually teach — you just keep fixing the same mistakes over and over. Then there's HITL as a product feature: thresholded review where humans only see the cases that matter, captured fixes that feed back into training, clear escalation UX so the user knows what's happening. Totally different animal.

Look at healthcare — clinical imaging, ambient scribes. Clinician sign-off on high-risk outputs is normal practice. Nobody thinks the AI is broken because a doctor reviews the output. It's the product working as designed. That's the mindset shift. The three levers on screen — threshold, capture fixes, escalation UX — connect directly back to the data flywheel from Module 2. Every human correction is a training signal if you capture it. If you don't capture it, you're burning your own moat. Remember the flywheel scores? This is where the flywheel becomes real.

Quick — point to your answer on screen. Where in your product would a human catch a catastrophic miss first? Just point. I want to see where your instincts go. Don't overthink it.

### Slide 13 — Air Canada Case

Alright, the scare story I promised. Let me tell you what happened. Air Canada deployed a customer service chatbot. Standard stuff, right? Help customers with tickets, answer FAQs, save money on support. The chatbot invented a bereavement refund policy that didn't exist. Just made it up. Whole cloth. A grieving customer relied on it, booked flights based on the bot's promise, then came back asking for the refund the bot had guaranteed.

Heres where it gets really interesting. Air Canada's legal defense? They argued the chatbot was a "separate legal entity." Basically — don't blame us, blame the robot. The tribunal ruled — and I'm paraphrasing here — no, absolutely not, the bot speaks for the brand, and you're liable for what it says. Game over.

The word "contract" in today's title is not a metaphor. When your AI makes a promise, your company is on the hook. Legally. That's why you need the golden dataset — your receipts. The confidence UX — your thresholds. And HITL — your escalation paths. Without all three, you're one creative hallucination away from a tribunal. I know that sounds dramatic but the case is right there. It happened.

Turn to your partner. 60 seconds. What's the worst thing your AI could say with high confidence? I want domain-specific answers. Healthcare: wrong medication interaction. Finance: false tax deduction. Legal: a made-up case citation. What's yours? Go specific — not "something bad" but the actual sentence your AI could generate that would end up in a screenshot on social media.

Lets hear one or two. Yeah, sit with the discomfort — that's the fuel for what you're building next.

### Slide 14 — Confidence UX

Good. With HITL and Air Canada fresh in your heads, lets design what your product actually looks like at different confidence levels. This is where theory becomes interface. Three tiers. Above 90% — confident, full answer, go ahead and deliver. Between 50 and 90% — uncertain. What visibly softens? What changes in the UI? What does the user see that tells them "hey, double-check this"? Below 50% — not confident. Do you block, escalate, or put it in a human queue? Each of those is a different product decision with different tradeoffs.

Heres some real patterns you can steal. Grammarly adjusts rewrite depth based on confidence — when it's less sure, it suggests less aggressively. Copilot adds citations and softens its tone when it's uncertain. These aren't theoretical — these are shipping products making these choices right now.

Four yes-or-no decisions at the bottom of the slide, and these are the ones that separate thoughtful AI products from everything else. Can users adjust the threshold? Can they see AI reasoning? Can they correct and override? And — this is the Module 2 flywheel connection — do those corrections feed back to the model? If your answer to that last one is no, go back and reread your flywheel scores.

You've got 10 minutes. Fill this in for your own product. The Confidence UX Checklist tool is linked on-slide — it's a 16-point audit, really useful for pressure-testing your design. When you're done, point to your screen — which tier is your live product closest to right now? I bet it's going to be eye-opening.

### Slide 15 — LLM-as-Judge

OK so here's the scaling problem. Human rubrics don't scale. If you're producing thousands of outputs a day, you can't have a human grade every one. You'd go broke. The pattern at frontier labs is to pair automated LLM judges with spot-check human reviews, calibrated against the golden dataset you just built. See how it all connects?

Three use cases. Regression: judge vs. golden rows, running continuously — your overnight quality check. Drift detection: trend alerts that fire before your NPS drops. Think of it as a canary in the coal mine. And quality gates: live routing where outputs go auto, human, or block depending on the score. That's real-time quality control.

Quick nuance — tools like LangSmith and Braintrust give you the infrastructure, but you still own the labels. The gold set is sacred. The judge is the scaling mechanism. Don't confuse the two.

Thumbs up if a model already grades your outputs somewhere in your pipeline. See? A lot of you are already doing this — you just might not be calling it "LLM-as-Judge." Now you have the name for it, and more importantly, you know how to make it rigorous.

### Slide 16 — Eval Dashboard

This bridges from "why evals matter" to "what your eval system actually looks like." Four quadrants on screen. Metrics: quality, latency, confidence spread, HITL percentage, override rates. Judge setup: which model, what rubric, which gold set, what thresholds. Drift alerts: auto-ping when trends cross the line. And UX hooks: scores visible in the UI, citations, thumbs-up feedback loops.

Think Datadog or Stripe status-page energy, but for AI quality. You know those beautiful green-check dashboards that make you feel like everything's fine? That, but for whether your AI is actually working. The mindset I want you to adopt — you can write evals before you fully know what an eval is. Just outline clearly specified ideal behavior. That's it. Don't let the jargon intimidate you.

Thumbs up if you could screen-share this eval dashboard to a buyer next week. If most thumbs are down — and they usually are, no judgment — that's the gap. The red-team exercise coming next is going to pressure-test everything. Consider yourself warned.

### Slide 17 — Red-Team

Alright, partner time. This is one of my favorite exercises. You're going to stress-test each other's eval spec and confidence UX using four attack lenses. Confident hallucination: your system is 95% confident and completely wrong — then what? Adversarial input: injection attacks, messy real-world text, the stuff actual users send at 2 AM. Ground truth shifts: the policy changed last week but your gold set is stale — does anything catch it? Boundary cases: inputs the system has never seen — what breaks?

This is the cheapest place to find failures. Way cheaper here in this room than in production. And infinitely cheaper than in a tribunal — we just talked about that, right?

You've got 13 minutes — six minutes each direction. One person attacks, the other defends, then swap. After both rounds, each pair states one line: "Worst miss my partner found." If those one-liners aren't at least a little uncomfortable, the red-teaming was too polite. Push each other. I mean it — be the competitor, not the friend. You can buy them coffee afterwards.

### Slide 18 — Reliability Contract

This is the capstone lab for today. Everything you've built — golden dataset spec, confidence UX, red-team findings — feeds into this reliability contract. Four quadrants: the promise, the measurement, the escalation, and the feedback loop. This is the artifact with the most teeth.

### Slide 19 — Build

OK so look at what you've built today. A golden dataset spec, a confidence UX design, you survived a red-team attack. Now we tie it all together. This is the capstone artifact — the reliability contract. What you promise users, how you measure it, what happens when it breaks, and how corrections feed back. Four quadrants. The Promise: accuracy percentage, response time, uptime. The Measurement: metrics, method, reporting cadence. The Escalation: what happens when you drop below threshold — who's notified, what do users see? The Feedback Loop: how corrections get back to the model, how the dataset gets updated, on what cadence.

Think about cloud SLAs for a second. AWS doesn't promise "pretty good uptime." They promise 99.99%. I want you to push for real draft numbers. Even wrong numbers get corrected faster than mush. "We aim for high quality" means nothing. Nobody has ever been held accountable for "aiming for high quality." But "We target 92% accuracy on case summarization, measured weekly against 300 golden rows" — that means something. That's a contract. See the difference?

The four-quadrant layout is a thinking framework — promise, measurement, escalation, feedback. Add, merge, or drop quadrants to match your product's trust surface. Don't force-fit a 2x2 if your product needs something different. The structure serves you, not the other way around.

You've got 15 minutes. When you're done, share with your partner: one promise you'd sign today vs. one you'd redline. The redlined ones are the gold — they surface the honest gaps. Those become your Module 5 roadmap items. So don't be embarrassed about redlines. They're the most valuable thing on the page.

### Slide 20 — Synthesis

Lets close the loop. Remember slide 5? You walked in thinking trust equals accuracy. Look at what you're leaving with — a golden dataset spec, confidence UX, a reliability contract. Component 4 of your living strategy is now tangible specs, not feelings. That's a real shift, and I want you to feel good about it. You did the hard work today.

Clap once if today changed what you'll demo next sprint. Come on, I want to hear it. Yeah. Thats what I thought.

### Slide 21 — Bridge to M5

Today was product-level trust. Next time we go bigger — and honestly, it gets a little wild. We're talking about what breaks at organizational scale. Agents operating autonomously. Shadow AI tools popping up across your org that nobody sanctioned. Governance as a sales asset, not a compliance burden. If that sounds like a lot, it is — but you've got the foundation now. You're bringing your eval dashboard spec, reliability contract, confidence UX, and Components 1 through 4 with you.

Take a look at the module arc on screen — see where M5 sits. That's where we're heading. It builds directly on everything you did today.

### Slide 22 — Your Repo

Four folders done. `01-the-bet/`, `02-the-moat/`, `03-the-margin/`, and now `04-the-contract/` with your golden dataset spec, confidence UX design, and reliability contract. One more module of building, then we pitch. The living strategy is getting serious.

### Slide 23 — Complete

Look at what you accomplished. A golden dataset spec, a confidence UX design, a red-team stress test, and a reliability contract. Two shifts today: you went from trusting accuracy to designing for perceived control, and you went from no eval infrastructure to a spec you could hand to an engineer. This was the heaviest writing module so far and you nailed it.

### Slide 24 — Takeaways

Three takeaways. First — trust is a function of perceived control, not accuracy. An 85% system with confidence scores beats a 95% black box. Second — golden datasets are your receipts. When a buyer asks "how do you test this?", your golden dataset is the answer. Third — your AI's promises are your company's promises. Air Canada learned that the hard way. Specify them, measure them, enforce them.

### Slide 25 — Extra Practice

Two optional exercises. First — add five more adversarial rows to your golden dataset. Think about the worst inputs your users could throw at your product. Second — map your confidence UX tiers to actual UI elements in your product. Where exactly do confidence scores show up? What changes between the tiers? Next session: Module 5 — The Guardrails.

### Slide 26 — Survey

Alright, QR code is on screen, link is there too. Take two minutes and fill this out — I genuinely read every one. This was the heaviest writing module so far, and honestly you crushed it. The amount of artifacts you built today is no joke. I appreciate you staying with it. Thank you, and I'll see you next time.

### Slide 27 — Q&A

Any final questions? Feel free to unmute or chat them. As always, Slack is open for anything that comes up later. This was a heavy one — appreciate you staying with it. See you next time.
