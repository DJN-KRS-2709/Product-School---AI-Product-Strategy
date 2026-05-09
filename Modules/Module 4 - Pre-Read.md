# Module 4 - The Contract (Pre-Read)

*Twenty minutes of reading and one short noticing exercise. Done before the session, this is the difference between hearing the M4 ideas for the first time in the room and walking in already chewing on them. Especially worth doing if any of the AI vocabulary still feels slippery.*

---

## 1. Why this session matters

Modules 1 to 3 gave you a bet, a moat, and the economics. Module 4 is where the strategy gets *teeth*.

Up until now the work has been about value and money. From Module 4 forward, it's about **promises**. Specifically, the kind of promises your company is legally on the hook for the moment your AI says them out loud. The "Contract" in the module title is not a metaphor.

This is also the most jargon-dense session in the course - golden datasets, eval harnesses, LLM-as-Judge, human-in-the-loop, confidence UX, reliability contracts. The pre-read closes that gap so the in-room time can be spent on your actual product instead of on definitions.

By the end of the session you'll leave with three artifacts in your repo: a **golden dataset spec**, a **confidence UX design**, and a **reliability contract** (`04-the-contract/`).

---

## 2. The one idea to walk in already chewing on

> **Trust is a function of perceived control, not accuracy percentages.**

This is the central reframe of Module 4, and it is genuinely counterintuitive. The instinct - the one most teams build their roadmap around - is "more accurate = more trusted." It's wrong.

An **85% accurate system** that shows confidence scores, cites sources, and lets the user override the answer beats a **95% accurate black box** every single time. Users don't trust what they can't see into. Even when the black box is technically right more often, the moment it's confidently wrong with no warning, trust evaporates - and there's no way to claw it back.

You already know this as a consumer. Think about the last time an AI tool gave you a confident, polished, completely wrong answer. How did that feel compared to one that said "I'm not sure - here's a source you can check"?

Sit with that idea for a minute before reading on. The whole module hinges on it.

---

## 3. A 20-minute "noticing" exercise to do before class

This is the highest-leverage thing you can do to prepare. Pick **three** of the products below, use each for one real task you actually have to do this week, and notice **how each one signals uncertainty**. You're not building anything - you're just paying attention.

| Product | What to look for |
|---|---|
| **Perplexity** | Notice the citations on every claim. What happens to your trust when you can click through to the source? |
| **Granola** | Notice the confidence indicators on transcription. Where does it hedge? Where does it stay confident? |
| **GitHub Copilot** (or Cursor) | Notice when the suggestion is more aggressive vs. softer. Does the *style* of the suggestion change with confidence? |
| **ChatGPT or Claude** | Look for moments where it says "I'm not sure" or "I'd need to verify" vs. moments where it confidently invents. What triggers each? |
| **Tesla Autopilot** (or any modern ADAS) | If you have access, notice the forced handoffs - the moments the system *makes you* take the wheel because it's not confident. That's confidence UX in physical form. |
| **Notion AI / Grammarly** | Notice how aggressively each suggests changes. Watch for moments the suggestion gets quieter or disappears entirely. |

Twenty minutes total. No notes required. The goal is to walk into Module 4 with **felt examples** of trust patterns, not just abstract ideas. When the slide goes up that says "what does your product look like at different confidence levels?", you'll have a library to draw from.

---

## 4. Vocabulary you'll keep hearing

Full definitions go in the cumulative [`Glossary.md`](./Glossary.md) after the session. One-liner each here so the words don't trip you up in the room.

- **Golden dataset** - a labeled set of test cases that defines "good" for your specific product. Versioned like code, used as a release gate.
- **Eval / Eval harness** - the automated test suite that scores whether your AI is producing good outputs against the golden dataset.
- **LLM-as-Judge** - using a model to grade other models' outputs at scale, calibrated against the golden dataset. Lets you check thousands of outputs a day without paying a human to look at each one.
- **Human-in-the-loop (HITL)** - design pattern where a human reviews AI outputs at certain thresholds. Done well, it's a product feature. Done badly, it's a crutch that makes the team broke.
- **Confidence UX** - the visible signals in your product that tell users how sure the AI is - confidence scores, citations, hedged language, "I'm not certain" messages, override buttons.
- **Drift** - when AI quality slowly degrades over time, often silently, because the model or the inputs changed. The reason you need ongoing evals, not one-time testing.
- **Hallucination** - when the model produces an answer that sounds confident and is factually wrong.
- **Reliability contract** - the explicit promise your product makes to users about quality, response time, escalation, and feedback loops. The capstone artifact of Module 4.

---

## 5. There's a real legal case coming

I won't spoil the punchline, but here's the teaser: a major airline deployed a customer service chatbot. The chatbot invented a refund policy that didn't exist. A grieving customer relied on the bot's promise. The case went to a tribunal. The airline tried to argue the chatbot was a "separate legal entity" - basically, *don't blame us, blame the robot*.

It didn't go the way they hoped.

We'll walk through it in the room. Come ready to think about what would happen if your AI confidently told a user something it shouldn't have.

---

## 6. Two questions to come ready to answer

These will become warmups in the session, so showing up with an honest answer pays off in the room.

**Question 1:** *What's the worst thing my AI could say with high confidence?*

Be specific. Domain matters.
- Healthcare: a wrong medication interaction.
- Finance: a false tax deduction.
- Legal: a made-up case citation.
- Support: a refund policy that doesn't exist.
- Sales: a discount no one authorized.

What's *your* version? Write it down. The actual sentence your AI could generate that would end up as a screenshot on social media.

**Question 2:** *What's our current eval situation, if any?*

Honest answer. The most common honest answer is "nothing." That's fine - it's true for most teams. The point is to walk in knowing where you actually stand, not where the deck claims you stand.

If you do have something - a benchmark you run, a spreadsheet of test cases, a vibes-based "we tried 20 prompts and they looked good" - bring it. We'll pressure-test it.

---

## 7. What to bring

- Your `cost-curve.md` from Module 3 (it gets referenced).
- Your three artifacts so far: `01-the-bet/`, `02-the-moat/`, `03-the-margin/`.
- Honest answers to the two questions above.
- A willingness to be pressure-tested by a partner - the red-team exercise in this session is one of the most useful and one of the most uncomfortable things in the course. The point is to find the cracks here, before your users (or a tribunal) do.

See you in the room.
