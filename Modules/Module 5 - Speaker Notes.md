# Module 5 — The Guardrails

### What this module is about

We're zooming out. Module 4 was about trust at the product level — evals, confidence UX, reliability contracts. Today we ask: what happens when that product scales across teams, agents start choosing their own actions, and employees are pasting company data into tools nobody approved? The tension today is different from last time. M4 was craft — can you build something trustworthy? M5 is exposure — what's already happening that you don't know about?

The assumption I want to break today: "Compliance is a one-time checklist." Here's the thing — in AI, systems either compound or degrade silently. There's no steady state. Traditional products don't get worse when you're not looking. AI products do. That's the strategy difference I want you to internalize early, and honestly it's the one that still catches experienced PMs off guard.

You'll leave with three artifacts: a compounding system architecture with loops that actually learn, a governance one-pager covering agent autonomy, data classes, and accountability, and a shadow AI audit starter you can hand to IT or Finance on Monday. That last one — the shadow AI audit — is hopefully the one you'll still be talking about after class. It's the kind of thing that makes people go "oh no" when they actually run the numbers.

### The flow and why it's structured this way

I moved the compounding system exercise before the break so it follows the lecture immediately — same learn-then-do rhythm we established in M4. Parking it after 30 minutes of governance theory would bury the concept and honestly, by that point everyone's eyes would be glazing over. So the first half is "what compounds" — concept plus build — and the second half is "what breaks" — governance cluster, a Samsung scare story, policy writing, peer audit, shadow AI build. The break sits at the natural seam between those two themes. It's a nice mental palette cleanser before we get into the heavier governance material.

---

### Slide 1 — The Guardrails

Alright, welcome to Module 5. We're making a big shift today — product to org. Three waypoints frame the session: Compound, Govern, Audit. By the time we're done, you'll have an audit you can actually hand to someone on Monday morning. And that's what separates this from abstract governance talk — you're walking out with something real. Let's get into it.

### Slide 2 — Expectations

Same ground rules — cameras on, Slack for questions. Today's session covers both product and organizational scale, so the scope is wider than previous modules. Some of the exercises might feel uncomfortably real — the shadow AI audit in particular tends to surface things people didn't expect. Thats the point.

### Slide 3 — Course Arc

Quick look at the map. Modules 1 through 4 are done — bet, moat, margin, contract. Today is Module 5 — The Guardrails. After today, the only thing left is Module 6 where you assemble everything and pitch. So this is the last building module. Make it count.

### Slide 4 — Recall from M4

OK so let me connect where we left off to where we're going. You brought your eval dashboard spec, Components 1 through 4, and your reliability contract. Great work on all of that, by the way — M4 was a heavy one and you crushed it. Today we apply the same muscle at org scale.

Quick show of hands. Does your company have a published AI use policy? Point to me: yes, no, or sort of. Yeah, look around the room — it's mostly "sort of." I love that. That shared guilt is actually the whole point. It makes the shadow AI audit we're building later feel urgent, not academic. If everyone had said "yes, fully documented, regularly updated" — well, first of all I wouldn't believe you, and second, I'd have to redesign this whole module. So thank you for your honesty.

### Slide 5 — Provocation

Same drill as the previous modules. Three claims on screen, all false. Let's go through them.

"Governance slows us down" — false. OK so here's a story. Salesforce built what they call the Einstein Trust Layer and they literally sell it as a product feature. It's in the sales pitch. Buyers ask for it by name. Governance isn't slowing them down — it's their GTM strategy. They turned a compliance cost into a revenue driver. That's the reframe I want you to hold onto.

"We can manage AI tools organically" — false. Let me tell you about Spotify. They woke up one day and realized they had over a thousand AI tools floating around the organization. A thousand. Different teams, different vendors, no coordination. They consolidated down to 15. Organic management is just chaos with a nicer name. Sound familiar?

"Agents are just automation with better UX" — false. Agents choose actions and chain tools — that's a fundamentally different animal. Here's a wild one. Air Canada had a chatbot that literally invented a refund policy on the spot. Just made it up. And the court held the company liable for what the bot said. Let that sink in. That third one is going to come back when we hit agent governance later, so keep it in your head.

### Slide 6 — Compounding Systems

This is the conceptual foundation of the first half and honestly, I think this might be the most strategically important concept in the module. I want you to see the difference between "scales" and "compounds." Scales means volume goes up, quality stays flat, costs are linear. Fine, good, normal. Compounds means each interaction makes the next one smarter. That's a completely different economic animal. Three mechanisms make that happen: recursive learning, cross-domain transfer, and network intelligence.

Let me give you two stories. Duolingo — every single learner interaction sharpens lesson difficulty for the next learner. You struggle with past tense in Spanish? That struggle makes the next person's lesson better. Beautiful, right? Then there's ServiceTitan — 32 products, one stack, each feeding context to the others. That's vertical depth compounding. The HVAC scheduling data makes the invoicing smarter which makes the dispatching smarter which makes the scheduling even smarter. It's a loop, not a line.

Here's why you should care: most AI products scale without compounding. And that means they're commodities with variable costs. If your system doesn't get smarter with use, someone else's will. And they'll eat your lunch while you're still arguing about your next feature.

Turn to the person next to you. Thirty seconds. Name one thing in your product that compounds versus one that only scales. Go.

### Slide 7 — Governance Lab

First lab of the day. You just learned about compounding versus scaling — now sketch your own system while it's fresh. Three panels: recursive learning, cross-domain transfer, network intelligence. Lets build.

### Slide 8 — Design Compounding

You just learned compounding versus volume — now sketch your own system while it's fresh. Three panels: Recursive Learning, Cross-Domain Transfer, Network Intelligence. Here's the forcing function I want you to use: freeze your product for 12 months. No updates, no improvements. Still winning? If yes, you're not compounding — you're just scaling. Good answers name specific data flows — something like "support ticket corrections feed the fine-tuning pipeline weekly."

Now, the three-panel structure is a thinking scaffold — not every product needs all three mechanisms. Adapt what actually ships and learns in your world. Don't force-fit a template just to fill boxes. I'd rather see one loop that's genuinely real than three that are aspirational. And hey, if you're struggling with this — that's a finding too. That tells you something important about where your product actually is.

### Slide 9 — Break

Amazing work so far. Seriously — you just wrestled with compounding systems and I know that's not easy to map onto your own product. You deserved a break. Take five minutes — grab some water, stretch, check your phone. When we come back it's the governance half: responsible AI ladder, how to govern agents, a Samsung scare story that's going to make some of you very nervous, and then you're writing policy while your partner audits everything. So rest up. You're going to need it.

### Slide 10 — Cameras On

Welcome back! Cameras on please. The next stretch is the governance block — responsible AI ladder, agent governance, the Samsung scare story, then you're writing policy and your partner is going to audit you. Should be intense. Lets go.

### Slide 11 — Responsible AI

OK so welcome back. I want to walk you through a three-level ladder and I think this framing is going to change how you think about compliance entirely.

Level 1 is Compliance — EU AI Act, GDPR, CCPA — that's the minimum bar. It's table stakes. You have to do it. Congratulations, you're not getting sued. Level 2 is Trust Architecture — that's what you built in M4 with evals and confidence UX and reliability contracts. You're ahead of most companies if you're here. Level 3 is where it gets interesting — that's where governance becomes your GTM. Model cards, bias posture, making your trust infrastructure a selling point. Remember Salesforce and the Einstein Trust Layer from five minutes ago? That's Level 3. They put governance in the actual sales pitch.

The point: most orgs plateau at Level 1 or 2 and completely miss the revenue opportunity. Governance done well accelerates enterprise deals because buyers are actively asking for it. "Show me your AI governance framework" is becoming a standard procurement question. If you have a good answer, you close faster.

And then there's what happens when you get it wrong. Google Gemini had an image generation incident that paused the product publicly for remediation. That's a velocity versus safety decision made on stage, in front of the whole market. Everyone watched that happen in real time. It's the kind of thing that makes you think "OK maybe Level 1 isn't enough."

### Slide 12 — Agent Governance

OK here's where things get a little spicy. Multi-agent systems are fundamentally different from chatbots. Authorization, memory, liability, tool-calling in series — it's a completely different animal. And I say this as someone who initially thought "eh, agents are just chatbots that do more stuff." I was wrong. Four governance knobs to think about.

Autonomy — draft does not equal send, read does not equal write. This sounds obvious until you realize most agent implementations don't make this distinction. Tool Calls — whitelist them, rate-limit them, log them. Every single call is a potential risk surface. Memory — what persists between sessions and who can read it. This one gets creepy fast if you don't think about it. Chain — when agent B fails on agent A's output, who owns that handoff? Who's on the hook?

Microsoft Copilot with Graph and plugins is the real-world example here. You log and whitelist like any production system. And here's the key point I want you to hold onto: design around principles, not model names. Specific models churn every six months. Your governance framework needs to survive that churn. Be tool agnostic.

Before we move on — just think about this for a second. Point to one tool call in your product that would scare Legal if it went unlogged. Just one. Let it surface. That's the kind of risk we're going to write governance policy around later, so start thinking about your scariest one now.

### Slide 13 — Agentic ROI

OK let's be honest — your execs are going to compare agent investments to Robotic Process Automation. Same budget line, same quarterly review, completely different economics. And if you don't get ahead of that conversation, you're going to lose it. Traditional automation: fixed paths, linear ROI, breaks on edge cases. Agentic automation: token costs swing, quality is fuzzy, and it eats exceptions — if governed properly.

Three decision levers to think about. Complexity — if the task is simple and predictable, use scripts. Save yourself the headache. If it's messy and full of edge cases, that's where agents earn their keep. Error Cost — if your tolerance for mistakes is low, the human review tax kills ROI fast. Learning — agents only pay off if the feedback loops from slide 6 actually ship. Not "we plan to ship them" — actually ship. Think of it as a spectrum from traditional RPA on one end to frontier LLM agents on the other. Different beast, different business case, different conversation with finance.

### Slide 14 — Samsung Case

OK let me tell you a story and this one's a doozy. Samsung. Employees started using ChatGPT for code review, meeting notes, and process optimization. Totally understandable, right? These tools are amazing, people want to use them, nobody told them not to. Within about a month — one month — three data leaks. Source code, meeting content, and fabrication data all entered vendor training pipelines. No AI use policy. No audit trail. Nobody even knew it was happening until it was too late.

Samsung's response? Ban all external AI tools. Entirely. Then rebuild internally from scratch. Imagine explaining that to your engineering org. "Hey, that tool you've been using every day that makes you 30% more productive? Yeah, you can't use it anymore. Also we leaked our source code. Happy Monday."

Here's how I think about it in three acts. Act One, The Bet: fast wins, no guardrails, everyone's excited. Act Two, The Crack: three leaks, no trail, panic sets in. Act Three, The Correction: ban everything, rebuild from scratch, massive productivity hit. The lesson isn't "don't use AI tools." The lesson is: absence of governance isn't a compliance gap — it's a strategy failure. The ban cost them more than the leaks did.

OK pair up. I want you to name one AI tool you'd ban on Monday versus one you'd standardize — with logging. Be specific. Don't say "chatbots" — give me a product name. This is the emotional fuel for the governance policy exercise that's coming next, so really feel this one. And if you're thinking "this couldn't happen at my company" — I promise you, it already is. You just don't have the audit trail to prove it yet.

### Slide 15 — Shadow AI Audit

Great. So let's turn that Samsung scare into something you can actually use. Four steps that turn fear into a repeatable exercise for your org.

Discovery — surveys, expense reports, browser extensions, API keys. You'd be amazed what shows up in expense reports. Someone's expensing a $20/month AI tool? That's shadow AI. Multiply it by however many people are on your team. Risk — map the data path for each tool, check for Data Processing Agreements (DPAs), regulatory exposure, score each tool Low, Medium, High, or Critical. Consolidate — remember Spotify's thousand tools down to 15? The goal is governed AI, not zero AI. You're not trying to ban everything like Samsung did — you're trying to bring it into the light. Policy — allow-list, data classes, review cadence. And remember Air Canada's chatbot? Customer-facing bots need explicit bounds or you're liable for whatever they make up.

Now, this is a diagnostic lens, not an exhaustive survey. A 50-person startup and a 50,000-person enterprise will run this very differently — the categories and depth shift with org size and industry. Don't try to boil the ocean. Start with what scares you most.

Quick poll. How many distinct AI tools do you think your company pays for right now? Just throw out a number. Yeah. Let that sit for a second. Most people guess way too low. The real number is almost always higher than anyone in the room thinks, and that's before you count the ones people are paying for personally.

### Slide 16 — Draft Governance

OK so you've got responsible AI maturity, agent governance knobs, Samsung's three-act tragedy, and the audit framework all fresh in your head. Now it's time to write. A one-page governance policy. Four quadrants.

Agent Autonomy — what's OK to do solo versus what needs a human gate. Where's the line between "draft" and "send"? Data — what goes external, classified by Public, Internal, Confidential, Restricted. Be honest about what's already leaving the building. Compliance — which regs apply to your product, what artifacts you need to prove it. Accountability — who owns agent outputs, what's the escalation path when something goes wrong. And something will go wrong. That's not pessimism, that's planning.

Think of this governance framework as starter vocabulary for conversations with legal, security, and compliance. You'll need to map it onto your org's existing policies and committees, not replace them wholesale. Nobody likes it when product shows up and says "we wrote a new policy, you're welcome." That's how you make enemies.

The AI Maturity Scorer tool is linked on this slide — it scores five dimensions of responsible AI practice and shows you where you fall on the compliance to sellable trust ladder we just talked about. Give it a spin.

### Slide 17 — Peer Challenge

Alright, partners — time to audit each other. And don't be nice about it. I mean it. Being polite here doesn't help anyone.

Two lenses. Loops — is there a broken handoff? Theoretical learning that never actually happens? Corrections getting trashed instead of feeding back into the model? And Governance — unapproved agent action? Missing data class? A Samsung-style paste path where sensitive data could leak? An Air Canada-style customer bot with no guardrails?

Six minutes each direction, then we debrief. I want one sticky per person: your single biggest gap, no hedging. Not "we could improve our data classification" — I want "we have no idea what data our support bot sends to the vendor." And I want you to look for both attack paths — find one Samsung-path risk and one Air Canada-path risk. If your partner only found nice things to say, you need a tougher partner. Have fun with it.

### Slide 19 — Build

This is the highest immediate org ROI exercise in the entire course. I'm not exaggerating. The other exercises build strategy. This one might save your company from a front-page incident.

Three panels. Discovery — known tools, suspected tools, expense-report tools. The ones you don't know about are the scariest ones. Risk — each tool, what data it touches, tier it Low, Medium, High, or Critical. Be ruthless with the tiers. Decide — keep, replace, or ban. Pick one villain tool right now — the one that made your stomach drop when you thought about it during the Samsung story.

The Shadow AI Audit tool is linked on the slide — it walks you through discovery, risk-scoring, and triage with exportable results. Use it. And export the results when you're done — this is the artifact you're handing to someone on Monday, remember?

### Slide 18.5 — Shadow AI Lab

This is the highest immediate ROI exercise in the entire course. You're building a shadow AI audit you can actually hand to IT or Finance on Monday. Discovery, risk scoring, and triage. Lets find out what's actually happening in your org.

### Slide 20 — Synthesis

OK take a breath. Look at what you accomplished today. You mapped compounding systems, wrote a governance policy, survived a peer audit, and built a shadow AI tool inventory. That is a lot. Seriously — this was the densest module in the course and you handled it.

Let me close the loop back to our three waypoints. You walked in with abstract concepts — you're leaving with a compounding sketch, a governance one-pager, and a shadow AI audit starter. Component 5 is done. All five components are complete heading into M6. That's a huge milestone. Take a second to appreciate that.

Here's what "good" looks like. Good loops have named data flows — not "we learn from users" but "correction signals feed the fine-tuning pipeline weekly." Good policy has named owners — not "the team" but "Sarah in Legal reviews agent outputs monthly." Good audit lists have at least one tool that made you wince. If nothing on your list scared you, you weren't looking hard enough.

### Slide 21 — Bridge to M6

Module 5 closes the building phase. Everything from M1 through M5 — vulnerability, moat, economics, trust, guardrails — it all comes together next time. Module 6 is the board simulation. You're assembling everything into one narrative and the room is going to stress-test it. Think of it as a performance. Metrics, roadmap, story — all under fire from your peers playing board members.

I'm not going to lie, it gets intense. But you've built five components now. You've got the foundation. You're ready for it. And honestly? It's the most fun module. There's something satisfying about watching people defend their strategy under pressure. Bring your A-game.

### Slide 22 — Your Repo

Five folders done. `01-the-bet/` through `05-the-guardrails/`. All five strategy components are committed. One session left and thats the pitch. Your living strategy is essentially complete — Module 6 is about assembling the narrative and pressure-testing it.

### Slide 23 — Complete

Look at what you built today. A compounding system architecture, a governance one-pager, a peer audit, and a shadow AI audit. Two shifts: you went from abstract compliance to governance as a GTM asset, and you went from unknown shadow AI risk to a concrete audit with action items. This was the densest module and you handled it.

### Slide 24 — Takeaways

Three takeaways. First — most AI products scale without compounding, which makes them commodities. If your system doesn't get smarter with use, someone else's will. Second — governance done right accelerates deals. Salesforce sells the Einstein Trust Layer as a product feature, not a compliance checkbox. Third — shadow AI is already happening in your org. The audit isn't hypothetical — it's inventory.

### Slide 25 — Extra Practice

Two optional exercises. First — run a real shadow AI survey with your team. Even five responses will surface tools you didn't know about. Second — expand your governance policy to include specific agent autonomy boundaries — what's OK to do solo versus what needs a human gate. Next session is Module 6 — The Pitch. Everything you've built becomes one story.

### Slide 26 — Survey

QR code is on screen. Fill it out before you go — it genuinely helps me make the next session better. And thank you, seriously. This was the heaviest module in the course and you stuck with it. Great job today. See you next time.

### Slide 27 — Q&A

Any final questions? This was a dense one — genuine thanks for staying with it. Drop anything in Slack that comes up later. One more session to go and then you pitch. See you next time.
