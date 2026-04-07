# Module 5 — The Guardrails
## Speaker Briefing for Carlos

### What this module is about

This is where we zoom out from "my product" to "my org." M4 was about trust at the product level — evals, confidence UX, reliability contracts. M5 asks: what happens when that product scales across teams, agents start choosing their own actions, and employees are pasting company data into tools nobody approved? The emotional arc is different from M4. M4's tension was craft — can you build something trustworthy? M5's tension is exposure — what's already happening that you don't know about?

The traditional assumption this module breaks: "Compliance is a one-time checklist." In AI, systems either compound or degrade silently — there's no steady state. That's the AI strategy difference you should name early: traditional products don't get worse when you're not looking. AI products do.

They leave with three artifacts: a compounding system architecture (loops that actually learn), a governance one-pager (agent autonomy, data classes, accountability), and a shadow AI audit starter they can hand to IT/Finance. The shadow AI audit is hopefully the one people talk about after class.

### The flow and why it's structured this way

We moved the compounding system exercise before the break so it follows its lecture immediately — same learn-then-do rhythm we established in M4. Parking it after 30 minutes of governance theory would bury the concept. So the first half is "what compounds" (concept + build), and the second half is "what breaks" (governance cluster + Samsung scare story + policy writing + peer audit + shadow AI build). The break sits at the natural seam between those two themes.

---

### Slide 1 — Title

The shift from M4 to M5 is product → org. Three waypoints frame the session: Compound, Govern, Audit. We tease the output: "You'll leave with an audit you can actually hand to someone." That's what separates this from abstract governance talk.

### Slide 2 — Agenda

Just orientation. The agenda shows the interleaved flow so people know they won't sit through 40 minutes of lecture. Name the Shadow AI Audit early — it's the "holy crap" moment and people stay more engaged through governance theory if they know the payoff is coming.

### Slide 3 — Recall from M4

Connecting M4 to M5. They brought their eval dashboard spec, Components 1–4, and their reliability contract. The bridge: M4 was product-level trust — today we apply the same muscle at org scale. Ask the room: "does Published AI use policy at your company? Point: yes / no / sort of." Most folks will be heavy on "sort of." That shared guilt sets up the provocation and makes the shadow AI audit feel urgent, not academic.

### Slide 4 — Provocation

Similar to the previous modules. Three claims, all FALSE. "Governance slows us down" — false because Salesforce literally sells the Einstein Trust Layer as a product feature. "We can manage AI tools organically" — false because Spotify used over ~1,000 AI tools and consolidated to 15. "Agents are just automation with better UX" — false because agents choose actions and chain tools — Air Canada's chatbot invented policy and the court held the company liable. That third claim plants the seed for agent governance later.

### Slide 5 — Systems That Compound

This is the conceptual foundation of the first half. The slide contrasts "scales" (volume up, quality flat, linear cost) against "compounds" (each interaction makes the next one smarter). We use three mechanisms: recursive learning, cross-domain transfer, network intelligence. Duolingo is the anchor — every learner interaction sharpens lesson difficulty for the next learner. ServiceTitan is the vertical depth example from Gokul Rajaram's thread — 32 products, one stack, each feeding context to the others.

Why should they care: most AI products scale without compounding, which means they're commodities with variable costs. If your system doesn't get smarter with use, someone else's will.

And we close with a 30-second pair prompt: "One thing in your product that compounds vs. one that only scales." This primes the design exercise that follows immediately.

### Slide 6 — Design Your Compounding System

They just learned compounding vs. volume — now they sketch their own system while it's fresh. Three panels: Recursive Learning, Cross-Domain Transfer, Network Intelligence. The forcing function is the freeze test: "Freeze 12 months — still win? If yes, you're not compounding." Good answers name specific data flows ("support ticket corrections feed the fine-tuning pipeline weekly").

**Mental model:** The three-panel structure is a thinking scaffold — not every product needs all three mechanisms. They should adapt what actually ships and learns, not force-fit a template.

### Slide 7 — Break

Reset after the compounding sprint. Tease what's coming: "After break — responsible AI ladder, how to govern agents, a Samsung scare story, then you're writing policy and your partner is going to audit everything."

### Slide 8 — Responsible AI Maturity

A three-level ladder. Level 1: Compliance — EU AI Act, GDPR/CCPA — minimum bar. Level 2: Trust Architecture — what they built in M4. Level 3: Governance equals GTM — model cards, bias posture, Salesforce's Einstein Trust Layer in the actual sales pitch. The point: most orgs plateau at Level 1 or 2 and miss the revenue opportunity. Governance done well accelerates enterprise deals because buyers ask for it.

We mention Google Gemini as the anchor — the image generation incident paused the product publicly for remediation, a velocity vs. safety decision made onstage.

### Slide 9 — Agent Governance

Multi-agent systems are fundamentally different from chatbots — authorization, memory, liability, and tool-calling in series. Four governance knobs: Autonomy (draft ≠ send, read ≠ write), Tool Calls (whitelist, rate-limit, log — each call is a potential risk), Memory (what persists, who reads), Chain (when agent B fails on agent A's output — named owner per handoff). Microsoft Copilot + Graph/plugins is the real-world example — log and whitelist like any production system. Gokul's point: design around principles, not model names, because specific models churn every ~6 months. We need to be tool agnostic.

Close with: "Point to one tool call that would scare Legal if unlogged." This surfaces the real risks before they write governance policy later.

### Slide 10 — Agentic vs. Traditional ROI

Execs will compare agent investments to Robotic Process Automation — same budget conversation, completely different economics. Traditional automation: fixed paths, linear ROI, breaks on edge cases. Agentic automation: token costs swing, quality is fuzzy, eats exceptions — if governed. Three decision levers: Complexity (simple → scripts, messy → agents), Error Cost (low tolerance → review tax kills ROI), Learning (agents pay off if feedback loops from slide 5 actually ship). UiPath-style RPA vs. frontier LLM agents.

### Slide 11 — Case: Samsung

We're going to jump into the Samsung case, where employees used ChatGPT for code review, meeting notes, and process optimization. Within about a month, three data leaks — source code, meeting content, fab data entered vendor training pipelines. No AI use policy, no audit trail. Samsung banned external AI tools entirely, then rebuilt internally. So the lesson: absence of governance isn't a compliance gap — it's a strategy failure. Standard 3-act format: Bet (fast wins, no guardrails), Crack (3 leaks, no trail), Correction (ban + rebuild).

Pair exercise: "One AI tool you'd ban Monday vs. one you'd standardize — with logging." Push for specifics. This is the emotional fuel for the governance policy exercise that follows.

### Slide 12 — The Shadow AI Audit

Four steps that turn the Samsung scare into a repeatable org exercise: Discovery (surveys, expenses, extensions, API keys), Risk (data path, Data Processing Agreement (DPA), regulatory exposure — score L/M/H/Critical), Consolidate (Spotify's 1,000 → 15 — the goal is governed AI, not zero AI), Policy (allow-list, data classes, review cadence — Air Canada's lesson: customer-facing bots need explicit bounds).

**Mental model:** This is a diagnostic lens, not an exhaustive survey. A 50-person startup and a 50,000-person enterprise will run this differently — the categories and depth shift with org size and industry.

Quick poll: "How many distinct AI tools do you think your company pays for?" Reflection moment for them.

### Slide 13 — Draft Your Governance Policy

With responsible AI maturity, agent governance knobs, Samsung, and the audit framework all fresh, they write a one-page governance policy. Four quadrants: Agent Autonomy (OK solo vs. needs human gate), Data (what goes external, classification — Public/Internal/Confidential/Restricted), Compliance (which regs, what artifacts), Accountability (who owns agent outputs, escalation path).

**Mental model:** This governance framework is starter vocabulary for conversations with legal, security, and compliance — they'll need to map it onto their org's existing policies and committees, not replace them wholesale.

The AI Maturity Scorer tool is linked on this slide — it scores five dimensions of responsible AI practice and shows where they fall on the compliance → sellable trust ladder.

### Slide 14 — Peer Challenge

Partners audit each other across two lenses: Loops (broken handoff? theoretical learning? corrections trashed?) and Governance (unapproved agent action? missing data class? Samsung-style paste path? Air Canada-style customer bot?). Six minutes each direction, then debrief. Insist on one sticky: single biggest gap, no hedging. Name both attack paths explicitly — "Find one Samsung-path risk and one Air Canada-path risk."

### Slide 15 — Shadow AI Audit (Build Moment)

Highest immediate org ROI exercise in the course. Three panels: Discovery (known tools, suspected tools, expense-report tools), Risk (tool, data it touches, tier L/M/H/C), Decide (keep, replace, ban — pick one villain tool now).

The Shadow AI Audit tool is linked on-slide — walks through discovery, risk-scoring, and triage with exportable results.

### Slide 16 — Synthesis

Close the loop to the three waypoints. They walked in with abstract concepts — they're leaving with a compounding sketch, a governance one-pager, and a shadow AI audit starter. Component 5 is done. All five components are complete heading into M6. Add what "good" looks like verbally: "Good loops have named data flows. Good policy has named owners. Good audit lists have at least one tool that made you wince."

### Slide 17 — Bridge to M6

M5 closes the building phase. M6 is about selling it — the board simulation. Everything from M1–M5 gets assembled into one narrative and stress-tested by the room. Frame it as performance: "Next session, the room is the board. Metrics, roadmap, story — under fire."

### Slide 17.5 — Module Tools

Three interactive tools: AI Maturity Scorer, Shadow AI Audit, and Living Strategy Builder (to add Component 5). Quick pointer — data saves to the browser and carries forward to M6.

### Slide 18 — Survey

Quick close. Genuine thanks — this was the densest module in the course.
