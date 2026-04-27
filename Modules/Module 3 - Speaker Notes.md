# Module 3 — The Margin

### What this module is about

This is the money module. Module 1 diagnosed where youre vulnerable, Module 2 built the defense. Now were asking a totally different question — does any of this actually make money? And the vibe shifts here. Modules 1 and 2 were about threat and defensibility, which gets the adrenaline going. This one is about math. And math creates a different kind of discomfort, the quiet kind where you realize you maybe should have looked at these numbers six months ago. Most of you have never calculated your AI cost per user. I know because I ask every cohort and the room always goes quiet. That gap between "I think were fine" and the actual number — thats where the learning happens today.

By the end youll walk out with three artifacts committed to your repo under `03-the-margin/cost-curve.md`: a cost curve, a pricing strategy, and a board-ready one-pager. Real math you can drop into a spreadsheet or a board deck on Monday. Not theory.

### The flow and why its structured this way

The first half is concept-heavy, but we break it up with a Klarna case study and two standalone activity slides. I pulled the activities out of the theory slides and gave them their own full-screen moments because when activities are buried inside lecture slides they get lost — people half-do them while still reading. Nope. Each one gets its own stage.

The second half is almost entirely hands-on: cost curve, pricing design, peer stress-test, and the board one-pager. Thats where the real output gets created and honestly, thats where the energy picks back up after a math-heavy morning.

On the opening Expectations and Syllabus slides, Im keeping it to quick orientation — I just want to show you that there are two big applied blocks after the break so you know the lecture portion is front-loaded and it gets hands-on from there. Nobody wants to hear "trust me, it gets interactive later" without seeing the agenda. So I show it.

---

### Slide 1 — The Margin

Alright, welcome back everyone. This session is calmer than the first two, but I'll warn you — the pain is sharper when the math actually lands. Its a different kind of uncomfortable. Not "someone could copy me" uncomfortable. More like "wait, am I losing money on every user?" uncomfortable. By the end of today, you will think differently about your products economics. Thats a promise.

### Slide 2 — Expectations

Same ground rules. Cameras on, Slack for questions, be present. Today's a math-heavy session, which I know isn't everyone's favorite. But I promise it's the kind of math that changes how you think about your product. And the tools do most of the number-crunching for you.

### Slide 3 — Syllabus

Quick orientation. Module 1 was The Bet, Module 2 was The Moat, and today is Module 3 — The Margin. We're at the halfway point. After today we move into trust, governance, and the capstone. Everything from the first two modules feeds into what we're doing today — your flywheel scores and your kill switch audit both show up in the cost model.

### Slide 4 — Recall

OK so lets connect the dots. Everything you built in Module 2 — your flywheel, your moat, your kill switch — all of that is meaningless if the economics dont work. You can have the deepest moat in the world and still go broke. So before we dive into the new stuff, quick warm-up with your partner: name one AI call path in your product that could spike costs if usage doubled. Just one. I want you thinking about money before we even start. Go.

### Slide 5 — Provocation

Alright, honest question — who in this room actually knows their inference cost per user per month? Raise your hand. Yeah, thats what I expected. Dont feel bad, its pretty much the same every cohort. And thats exactly the point. If you already feel the gap in your knowledge, every concept in the next 30 minutes is going to land harder. Thats how this works.

Heres the thing. There are three beliefs PMs carry around like security blankets. One: costs will come down. Two: seat pricing works. Three: scale fixes everything. And I get it — these feel true. They sound reasonable when your VP says them in a planning meeting. But none of these are reliably true for AI products. Lets talk about why, because once you see it, you cant unsee it.

### Slide 6 — Margin War

OK so this is the core economic argument of the whole module and I need you to really sit with this one. Traditional SaaS runs at 80%+ gross margins because your infrastructure costs are mostly fixed. You spin up a server, you add users, the marginal cost is tiny. Beautiful model. AI products flip that completely. You introduce variable costs — tokens, inference — that scale with usage. And your power users? They can blow up your unit economics entirely. One enthusiastic customer running agents all day can cost you more than a hundred casual ones.

Lets do the math together. Pull up the OpenAI and Anthropic pricing pages — look at the real dollar-per-token gap between small models and frontier models. Now look at the napkin math on screen. A thousand calls at three cents a call is thirty dollars per user per month just in AI COGS. Thats before you pay for anything else. Before engineering, before support, before the ping-pong table. When you see that number for the first time, it hits differently than just hearing someone say "AI is expensive." Sound familiar? Yeah. Lets keep going.

### Slide 7 — Model Cascading

So if the margin war from the last slide is the disease, routing is the cure. And this is good news — I didnt want to just scare you. The single highest-leverage thing most AI products can do for their margins is an 80/20 split — 80% of requests go to a cheap model, 20% go to frontier. This isnt theoretical. Cursor does this. GitHub Copilot does this. These are real products shipping real revenue with this exact architecture. When Copilot answers a simple autocomplete, it doesnt need the most powerful model on earth. It needs a fast, cheap one. Save the big guns for the hard stuff.

Theres three more levers at the bottom of the slide — quantization, caching, prompt optimization. I wont go deep on those today, but I want you to know the toolkit exists. You dont have to solve everything with routing alone.

One thing to keep in mind though: that 80/20 ratio is a starting scaffold. In practice it might be 95/5 or 60/40 depending on your domain and your quality bar. Tune the split to your context — dont treat 80/20 as a rule. I made that mistake early on, treating every ratio I learned as gospel. Its a starting point, not a destination.

### Slide 8 — Klarna Case

OK six slides of concepts without real interaction is too long, even for me. So lets ground everything in a story. And Klarna is perfect for this because its the most public example of "we automated everything" running headfirst into "variable COGS is messy."

Heres what happened. Klarna went all-in on AI customer service. The headlines were incredible — "AI handles 66% of customer chats!" "Equivalent of 700 full-time agents!" Amazing press. Investors loved it. But heres the thing nobody was writing about: what was actually happening to the cost structure underneath? Were those automated conversations actually cheaper than the humans they replaced, or were they just faster? Big difference.

So heres what I want you to debate with your partner: headline pricing versus P&L pricing. What did the press say Klarna was doing, and what was actually happening to their cost structure? The lesson isnt that Klarna failed — its that the business model has to match the automation. Take two minutes. Go.

### Slide 9 — Pricing Models

Heres the thing most teams get wrong, and I see this constantly. Most pricing failures happen because you never figured out HOW to charge, not how MUCH. Those are very different problems and people confuse them all the time. You can spend six months optimizing your price point and still lose money because the structure was wrong from the start.

The three models on screen — seat-based access, hybrid, and outcome-based — thats the spectrum. And the standout example here is Intercom Fin. Let me tell you what they did because its genuinely clever. They charge per resolved conversation. Not per seat. Not per message. Per resolution. Thats the only real pricing model innovation in AI right now, and its working because the unit of charge matches the unit of value. The customer only pays when they get what they came for.

Some market data for context: 59% of AI products bundle, 23% sell as an add-on, 18% go standalone. So thats what the market is actually doing. You might be surprised how few go standalone.

And if you want a "this literally just happened" example of access pricing failing — theres a $200/month AI subscription that let users run third-party agent harnesses. A single agent running for one day burned $1,000 to $5,000 in API-equivalent costs on a flat $200 plan. Think about that. Every AI subscription is a bet on average usage, and tools that let power users blow past that average forced the provider to shut down third-party access entirely within four months. The one-time credits and discounted usage bundles they offered to soften the cutoff are a real-time example of a company retroactively unbundling heavy usage from a flat subscription. Wild, right?

### Slide 10 — Access or Outcome?

Alright, theory is useless if you dont apply it to your own product. So heres what were doing — its simple and I want everyone to participate. Point left if your product should price on access. Point right if it should price on outcome.

Now heres the interesting part. If most of you pointed left, I want to push on that. Is your product doing work for your users? Is it completing tasks, resolving tickets, generating output? Then why are you pricing access? Lets be honest — most of you pointed left because thats what youre used to. Thats the default. But this is where people start to realize they might be leaving massive value on the table. If your AI writes a report that saves someone three hours, and youre charging $20 a month for access... you see the problem. Good stuff. Lets keep going.

### Slide 11 — Bundling

OK lets talk about the bundling framework, and Im going to use the Big Mac analogy because — I know, I know — but it sticks. Trust me on this one. The burger is the leader — thats what you come for. Nobody walks into McDonalds craving a medium Sprite. Fries and a Coke are fillers — they bump the average order. Coffee would kill the bundle — its too different in the consumption moment, sell it separately.

Applied to AI: your core intelligence is the leader, lightweight features like summaries are fillers, and heavy inference stuff like image generation or agent workflows are killers that should be priced as add-ons. The 70% rule gives you a concrete threshold — if more than 70% of users touch it, bundle it. If fewer, price it separately. Simple. Memorable. Useful.

One thing though — Leaders, Fillers, Killers is a lens for thinking about value capture, not a prescription. Pick the framing that matches how your buyer actually thinks about your product. If your buyer has never thought about your product as a bundle, maybe this framing isnt the right one for you. Use what fits.

### Slide 12 — Name Your L/F/K

OK your turn. Fill in the cards — whats your leader, whats your filler, whats your killer? The cards with the icons are intentionally playful, but the thinking is serious. Have fun with it.

Now heres the follow-up question, and this is where it gets interesting. If you bundled your "killer" into the main plan, I want you to ask yourself: what percentage of users actually use it? If its under 70%, its an add-on. You might be subsidizing your heaviest users with everyone elses subscription. That one realization has changed pricing strategies for people in previous cohorts. Just saying.

This is the last activity before the Margin Calculator, so after this its all hands-on. Hope that landed — because were about to put real numbers behind it.

### Slide 13 — Margin Calculator

This is where abstract becomes concrete and honestly, this is my favorite part of the module. Heres what I want you to do — grab a sticky note, write your gross margin percentage on it, and hold it up. Nobody has to shout a number but everyone gets to see the range. Thats the point. Last cohort, the range was something like 12% to 78%. The room got very quiet after that.

Walk them through the six-line table on screen — requests per user, cost per request, COGS per user, revenue, gross margin, gross margin %. Then run the stress column live: 3x the cost per request and watch what happens to the bottom row. Thats the whole demo. The point isnt precision, its the structure — if they can fill these six lines for their product, they know more about their AI economics than 90% of PMs.

The link at the bottom of the slide drops them straight into `03-the-margin/cost-curve.md` in their repo template. Tell them to keep that tab open — theyll be filling the same six lines for their own product in a few minutes.

### Slide 14 — Break

Amazing work. Seriously — that was a lot of math and you stayed with it. You deserved a break. Take five minutes, grab some water, stretch. Before you come back though, pull up your providers pricing page — youre going to need it for the cost curve exercise right after. See you in five.

### Slide 15 — Cameras On

Welcome back! Cameras on please. The next stretch is all hands-on — cost curves, pricing design, and a peer stress test. You're going to need a partner for the stress test so make sure you can see each other. Lets finish strong.

### Slide 16 — Cost Curve Lab

Alright, this is the applied block. Everything from the first half — margin compression, model cascading, pricing models — you're about to apply all of it to your actual product. First up: mapping your cost curve. Lets go.

### Slide 17 — Cost Curve

Alright, welcome back. Fifteen minutes of solo work here and this one matters. I want you to map every AI feature in your product to a model tier and estimate the cost. The goal here is honest tiering. Most peoples instinct is to say "we use frontier for everything" and this exercise is going to show you thats a 3x cost difference you cant sustain. I get it — frontier feels safer. "What if the cheap model gives a bad answer?" But be honest about what actually needs frontier-level intelligence and what doesnt. Your autocomplete does not need GPT-5. I promise.

Couple of traps to watch for: you will underestimate how often embeddings get called — its always more than you think — and youll default everything to the most expensive model. Resist that. Be specific. Be honest. Future-you will thank present-you when the cost curve doesnt make your CFO cry.

### Slide 18 — Pricing Design

OK this is where "Product-Market-Pricing Fit" lands and I love this framework. Were walking through three steps: pick a strategy — skim like Apple, penetrate like Amazon, maximize like Microsoft. Then name the unit of work youd meter. Then set the structure — base plus usage.

Let me tell you about GitHub Copilot for a second because its a perfect proof point. $19 per user. Thats 4.75x a typical SaaS seat. And nobody blinks. Why? Because developers complete tasks 55% faster. The price isnt justified by features — its justified by outcome. When someone saves an hour a day, $19 is a rounding error. Thats the kind of value-based pricing that works. The question is: can you make the same argument for your product?

The link at the bottom drops them back into `03-the-margin/cost-curve.md` — same file as the cost curve exercise, theyre just filling the pricing section now. And remember — hybrid strategies and archetypes are lenses, not playbooks. The right structure is the one that fits your buyers mental model and how value shows up in their world. Dont force a framework. Let the buyer tell you what makes sense.

### Slide 19 — Stress Test

Alright, time to break each others models. I love this exercise because its where the polite answers die. Your partner is about to be your worst-case scenario. Two situations: first, inference costs go 3x — what breaks first in your pricing? Second, your heavy users double — are they paying less than they burn?

Write down the vulnerability you find in each others model. This matters — it travels to Module 4, so dont lose it. And if youre being too polite with your partner, remember: the CFO wont be polite when they see 3x in a scenario plan. Push each other. Be the stress test you wish youd had before the board meeting. Some of the best insights from previous cohorts came out of partners who were willing to say "this doesnt work and heres why."

### Slide 20 — Board Lab

OK, last lab of the day and it's the most "real world" one. You're building a board one-pager — a before-and-after comparison that you could actually present to leadership. Everything from today feeds into this artifact.

### Slide 21 — Board One-Pager

OK this is the most "real world" artifact in the whole module, and I think youre going to love it. You have 15 minutes to build a before-and-after comparison — your current model versus the AI-enhanced model.

Heres the key reframe I want you to internalize, because this trips up even experienced PMs. A lower margin percentage can be totally fine if revenue and gross profit are both up. I know that sounds counterintuitive. Were all trained to panic when margin percentage drops. But AI can expand the numerator even if the percentage dips. If your margin goes from 80% to 65% but your revenue triples — you are winning. This one-pager is what youd actually present to a board. When someone asks "why is our margin lower?" — this is your answer. And the fact that you built it in this room means you wont be scrambling to build it the night before the board meeting. Youre welcome.

### Slide 22 — Synthesis

Lets tie it all back to where we started. Remember slide 5? The three security blankets — costs come down, seat pricing works, scale fixes everything? Look at what you know now. Margin compression is the default for AI products. But now you have the levers — cascading, routing, pricing model, bundling — and you have the artifacts — cost curve, pricing strategy, board one-pager — to actually do something about it. Thats not theory. Thats a toolkit.

This is the moment to lock in Component 3. `03-the-margin/cost-curve.md` should now contain your cascade map, blended COGS per user, pricing structure, margin under stress, and the board before/after. Commit it. Three folders done in your repo. Halfway through the course and your living strategy is starting to look like a real strategy.

### Slide 23 — Bridge to M4

So heres the connection going forward. Economics without trust doesnt convert. You can have perfect pricing and beautiful margins, but if customers dont trust the output, none of it matters. Module 4 is about reliability, contracts, and evaluation — the things that make customers actually adopt and keep using what youve priced and built. Everything from today — your cost curve, your pricing strategy, even the kill switch from Module 2 — feeds directly into Module 4s vendor evaluation framework. Its all connected. And honestly, Module 4 is where a lot of people have their biggest "aha" moment, so come ready.

### Slide 24 — Your Repo

Check out your repo. Three folders done now — `01-the-bet/`, `02-the-moat/`, and `03-the-margin/` with your cost curve, pricing strategy, and board one-pager. Halfway through the course and your living strategy already has three solid components. Feels good to see it building up.

### Slide 25 — Complete

Look at what you accomplished today. You mapped a cost curve, designed a pricing strategy, survived a partner stress test, and built a board one-pager. Two big shifts: you went from unknown margins to quantified cost-per-user, and you went from gut-feel pricing to a structured pricing strategy. This was a math-heavy session and you crushed it.

### Slide 26 — Takeaways

Three things to hold onto. First — AI products compress margins from 80% to 40% because inference costs scale with usage, not users. Second — model cascading is the highest-leverage margin lever most teams aren't using. Route 80% of requests to cheap models and save frontier for what actually needs it. Third — a lower margin percentage is fine if revenue and gross profit are both up. AI can expand the numerator even if the percentage dips. Thats the story your board one-pager tells.

### Slide 27 — Extra Practice

Two optional exercises that both live in `03-the-margin/cost-curve.md`. First — re-run the cascading ratio at 60/40, 70/30, 80/20 and find the split that turns your worst stress case positive. Commit the update. Second — redesign your pricing as outcome-based, Intercom Fin-style, per-resolution or per-output. Update the pricing section and commit. The more real the numbers, the more useful this artifact becomes. Next session: Module 4 — The Contract. Economics without trust doesnt convert.

### Slide 28 — Survey

Thats it for today. Thank you, seriously — this was a lot of math and you stayed with it the whole way. I know numbers arent everyones favorite thing, but look at what you built: a cost curve, a pricing strategy, a board one-pager. Thats real work. Fill out the survey before you head out — it genuinely helps me make the next session better. See you next time.

### Slide 29 — Q&A

Any questions before we wrap? Feel free to unmute or drop them in the chat. Slack is always open too. Great work today — that was a lot of math and you stayed with it. See you next time.
