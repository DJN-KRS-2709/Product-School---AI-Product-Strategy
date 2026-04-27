# Module 1 — The Bet

### What this module is about

This is the opening module and it sets the tone for everything that comes after. Heres the big move: traditional product strategy assumes you can predict outcomes, lock in costs, and plan in annual cycles. AI breaks all of that. So today I'm introducing probabilistic thinking — the idea that AI products are bets, not plans. The emotional arc is about controlled discomfort. They're going to walk in expecting a framework deck and leave having diagnosed their own vulnerability, written a killer memo against themselves, and built a working prototype. That shift from passive to active is the whole point of Module 1.

The assumption I'm breaking today: "We can plan AI products the way we plan everything else." We can't. Outputs are probabilistic, costs are variable, competitive moats evaporate when platforms ship your feature for free, and discovery cycles that used to take 6 weeks now take 4 days. That's what slide 5 is about — five assumptions that AI shatters. Every module that follows maps to one of those rows.

They're leaving today with a GitHub repo containing three artifacts: a vulnerability scorecard with honest scores across three axes, a killer memo where they write three sentences attacking their own product from a platform's perspective, and a working prototype they built in 15 minutes. The repo IS the living strategy — they fork a template today and push real work to it in every module that follows. By M6, that repo is their board-ready strategy. It's a lot for one session but honestly the pace is what makes it land.

### The flow

The first half is concept-heavy but I keep it punchy — provocation, thesis, case study, framework. I never let theory run more than two slides without getting them doing something. The break sits after the framework slides so they've had time to absorb the diagnostic model before they have to apply it. Right after break, they fork their strategy repo — the living strategy that anchors the whole course. The second half is almost entirely hands-on: set up the repo, score yourself, get challenged by a partner, write the killer memo, build a prototype, push everything to the repo. The prototype is the emotional peak — seeing something exist in 15 minutes makes the whole "probabilistic bets" argument feel real instead of academic. And committing it to a real repo makes it permanent.

I want to reduce anxiety early — show them it's applied-heavy and they'll be doing stuff, not memorizing. Two hours: provocation, short theory, case, framework, break, diagnose, pair, build, synthesize. I don't need to read every line of these notes — just hit the beats: three exercises, one case, one prototype.

---

### Slide 1 — The Bet
Alright, welcome everybody. I'm really glad you're here. This is a working session, not a passive lecture. You're going to leave today with real artifacts, not just notes. By the end of this session you'll have code committed to a repo.

So heres the big shift we're wrestling with in this course. The way you've been trained to do product strategy — deterministic planning, annual roadmaps, fixed outcomes — that doesn't work for AI products. AI products are bets. And today we're going to figure out what your bet actually looks like.

By the end of this session you'll have what I call Component 1 of your living strategy, plus a working prototype. And it doesn't matter whether you're bolting AI onto an existing product or building something AI-native from scratch — the strategic questions are the same.

Quick thing before we go further — look at the slide. Diagnose, Discover, Decide. Which one of those feels hardest for you right now? Just write it in the chat.

### Slide 2 — Expectations
Before we dive in, lets set our ground rules. Cameras on — I know, I know, but it genuinely makes a huge difference in how we connect and learn from each other. Be present, arrive on time, and I really encourage you to participate actively during exercises. Use Slack for all communication so nothing gets lost. And save deeper questions for after class or post them in Slack so we dont interrupt the flow — but dont worry, there will be plenty of time for everything.

### Slide 3 — Introductions
I think by now, a lot of you folks could do the introduction for me. So I will keep it short. Im Dejan. Im a father of two boys — seven and eight. I like to say I buy Lego for them… but lets be honest, Im really buying it for myself. I am a coffee nerd tracking beans, extraction times, and grinder settings in spreadsheets. Ive been in product for more than 16 years. Back in the day, product management meant writing huge specifications and then praying for six months that the features would be delivered as expected. What should I say? They never did and we had to change our approach.

Before Spotify, I worked at SoundCloud, where we built an insights and analytics platform from scratch. I also launched Fan-Powered Royalties — a completely new way of paying artists on a streaming service. Ive been at Spotify for 4.5 years now. To help with the mission to unlock human creativity by giving a million artists the opportunity to live off the art and a billion fans to be inspired by it. But enough about me — Id love to get to know you. Drop your name, role, and at least one fun fact in Slack or the chat. The more we know about each other, the better we can learn together.

### Slide 4 — Syllabus
Heres the full outline. Six modules, each one building on the last. Module 1 is today — The Bet. You'll diagnose where strategy breaks and build your first prototype. Module 2 is The Moat — can anyone copy you? Module 3 is The Margin — does this make money? Module 4 is The Contract — trust and reliability. Module 5 is The Guardrails — what breaks at scale? And Module 6 is The Pitch — you assemble everything and present it. Each session adds a component to your living strategy repo. By the end, you dont have a deck — you have a version-controlled strategy you can actually use at work.

### Slide 5 — Final Project

Before we get into the content, let me show you where all of this is going. Your final deliverable for this course is a Living Strategy Repo — a GitHub repository that you'll build one component at a time across all six sessions. Today you'll add the vulnerability diagnostic and a working prototype. Next session you'll add your data flywheel and kill switch. And so on — every module adds a layer.

In Module 6, you assemble everything into one cohesive story and pitch it to the room. The class plays your board of directors. No slides, no deck — you present directly from your repo. Five minutes to pitch, three minutes of Q&A where your classmates ask the hardest questions they can think of.

The repo is yours to keep after the course. It's version-controlled, shareable, and portable. You can hand it to a colleague, open it in a board meeting, or use it as a template for future strategy work. This isn't homework — it's the most useful thing you'll build all year. And the best part? You don't have to cram at the end. If you do the work each session, by M6 you're just polishing, not building from scratch. Alright, lets get into it.

### Slide 6 — The Premise
OK so this is the opening thesis for the entire course, and I want you to really sit with this table because we're going to keep coming back to it. Like, constantly.

Traditional product strategy makes five assumptions that AI just completely breaks. Deterministic outputs — you can predict what the product will do. Fixed costs — you know what it'll cost to run. Clear competitive boundaries — you can see who you're competing with. Trust by default — users believe your product works. And annual planning cycles — you plan once a year and execute. Sound familiar? Yeah, because most of us were trained on exactly this playbook.

OK so heres my question for you: which of these shifts have you felt most in your own product?  who's felt the probabilistic outputs problem? Who's dealt with platform encroachment? Cost surprises? Trust issues? Planning chaos?... And by the way — each of these rows maps to a module in this course. But I'm not going to tell you which is which. You'll figure that out as we go. This slide is the one you'll pull up when someone at work asks "why can't we just use our normal strategy process for AI?"

### Slide 6 — Which Are You?
Alright, lets see who's in the room. There are really two paths here — you're either bolting AI onto an existing product, or you're building something AI-native from the ground up. The good news is, the frameworks we're using work for both. I've been on both sides of this and honestly, the bolt-on path is harder in some ways because you're fighting existing assumptions the whole time.

please post in the chate who's bolting on, who's building native? Great, good mix. One ground rule though: I need you working on a real product at your company for the exercises today. Not a startup fantasy, not a side project — the thing you actually go to work and deal with every day. I know that feels a little exposing but that's what makes this useful. Trust me on this one.

### Slide 7 — CEO Question
OK heres what I want you to do. Imagine your CEO/CPO or VP or Product stops you in the hallway tomorrow and says, "What's our AI strategy?" I want you to write your answer. Three sentences, no polish, just what you'd actually say. You've got three minutes. This is private — nobody's reading it.

Don't overthink it. Seriously, I just want to capture where your head is right now before we give you any tools or frameworks. And I promise you this — you'll look back at this answer in Module 6 and you'll cringe at it, in a really good way. I always do when I find old strategy docs from six months ago. That's the whole point. The means you grew.

### Slide 8 — True/False
Alright, lets have some fun. I'm going to throw some claims at you and I want you to vote on each one before I give you the answer. Ready?

"The best product wins." True or false? Hands up for true. Hands up for false. Interesting.

"AI product outcomes are predictable with enough data." True or false?

"Traditional discovery timelines still apply." True or false?

Heres the thing — all three are false. The best product doesn't win if a platform copies you overnight. Moats matter, and we'll dig deep into that in Module 2. Outcomes are distributions, not fixed points — some of the biggest AI wins came from entirely new behaviors that nobody predicted. And discovery that used to take six to eight weeks can now run in days with AI-assisted research loops. Your competitors are not going to wait for your research timeline.

I know some of that is uncomfortable. Good. Thats the point. Better to feel it here than in a quarterly review.

### Slide 9 — Course Arc
Let me show you the full journey. There are six modules, six big questions. Today is just the first one — "The Bet." Let me trace the arc real quick so you know where we're headed.

Module 1 is about diagnosing your bet. Module 2 asks whether anyone can copy you. Module 3 is the economics reality check. Module 4 is about trust and evaluation. Module 5 is the planning cadence. And Module 6 is where you put it all together and present.

But the thing I really want you to hold onto is this: across all six sessions, you're building a living strategy in a GitHub repo. Not a browser tool, not a worksheet — a real version-controlled repo. I chose GitHub deliberately because strategy docs that live in Google Docs get forgotten. Strategy in a repo gets versioned, diffed, and evolved. By Module 6, your repo IS your strategy. That's the artifact you could walk into a board meeting with. Pretty cool, right?best thing is you can create an output of your strategy for individual audiences.
- You want to pitch it to the board? Extract.
- You want to pitch it to the team? Extract.
Use the right language for the right audience

### Slide 10 — Annual Cycles
How many of you still have a frozen annual roadmap for your AI bets? and I get it — your org plans that way. Everyone's org plans that way. But heres the reality: you cannot commit to Q3 deliverables when the underlying model might change three times between now and then.

There's a great quote on this slide about variability and probabilistic models. it is "With AI, outcomes are influenced by data variability, algorithm behavior, and probabilistic models.". This isn't about "bad execution" — it's about the fact that AI products are fundamentally variable. The planning horizon has to match the uncertainty of the domain. And right now, most planning processes don't. I've sat in so many annual planning meetings where people are basically making up numbers for AI initiatives and everyone in the room knows it but nobody wants to say it.

This slide is me giving you permission to stop pretending. Feels good, right?

### Slide 11 — Discovery
OK let me show you something concrete because "AI makes things faster" is way too abstract. Nobody changes their behavior based on a vague claim. So let me tell you a story about Notion. They had a standard discovery process — user interviews, synthesis, prioritization, the whole shabang. Roughly six weeks, start to finish. Then they started using AI editor insights for clustering and synthesis and compressed that entire loop down to about four days. Four days. You can see Intercom and Sprig-class stacks on this slide as other examples of how teams are compressing research today.  please post in the chat  — I want to know where you all are. Your discovery cycle right now: under two weeks, two to six weeks, or six-plus weeks?

Thats not a judgment — thats just the reality. And it's exactly why the rest of this module matters — because your competitors might be running at Notion speed while you're still in week three of your research plan.

### Slide 12 — Probabilistic
OK so this is the core reframe for today and honestly for the whole course. As leaders, we've been trained to promise outcomes. "We'll ship X by Q3, it'll move Y metric by Z percent." I've done this. You've done this. We've all done this. But AI doesn't work that way. AI rewards a different operating model: place a bet, define your kill criteria, set a learning cadence, and iterate.

Look at the old versus new cards on the slide. Look at Bard becoming Gemini — same product, completely different positioning, because the underlying model is inherently variable. Google had to rebrand an entire product line because the technology moved faster than the strategy. And then think about non-consumption plays: Shopify started enabling merchants who never could have afforded custom AI before. Gamma replaced slide decks nobody wanted to make. Granola captured meeting notes nobody was taking. These are behaviors that didn't exist before AI. The Total adressable market looks tiny until suddenly it doesn't.

Alright, quick  exercise. think for thirty seconds — and then post in the chat: what's one outcome your leadership still asks you to "guarantee"? Because I bet most of you have at least one. And that gap between what they expect and what's actually possible? That's what we're here to close. 

### Slide 13 — Notion Case
Let me walk you through the Notion case.
Heres the arc: the Bet, the Crack, the Correction. Notion saw AI coming, placed the bet early, moved fast. Then they found the crack — the first approach wasn't working the way they expected. And instead of doubling down or pretending everything was fine, they corrected quickly. The weapon here was time — speed of learning, not perfection of planning. They didn't have a better plan than anyone else. They just learned faster. And honestly, thats the whole thesis of this course in one case study.

So heres my question: which pace matches you right now? Are you moving at Notion speed, or are you still in research-first mode? Lets be honest. I'd love to hear from two or three of you. What does your pace actually look like? Don't tell me what you wish it was — tell me what it is  right now.

### Slide 14 — Archetypes
OK so this is one of my favorite frameworks. I genuinely get excited about this one. Your AI product's archetype drives everything — your margins, your governance model, what "good" even looks like. And I see teams skip this step all the time and then wonder why their economics don't work or their eval metrics feel meaningless.

Look at the five archetypes on the slide. UiPath is Automation — it does the work for you, full stop. GitHub Copilot is the Copilot archetype — it works alongside you, pair programming style. Palantir is Insight — it shows you what you couldn't see. Midjourney is Creation — it makes entirely new things that didn't exist before. Zapier AI is Orchestration — it connects and coordinates across systems.

Now heres the important thing: these five are a thinking tool, not a taxonomy. Most products blend two or three. I spent way too long trying to force one of my own products into a single archetype before I realized it was legitimately two. The point is knowing which archetype's economics and trust profile dominates your product, because that shapes everything from your pricing model in Module 3 to your eval design in Module 4. So figure out your primary, maybe your secondary, and be honest about what doesn't fit.

so please reflect: which archetype is your product? Automation? Copilot? Insight? Creation? Orchestration? 

### Slide 15 — Break
Amazing work so far. Seriously — you've covered a lot of ground and I can tell the energy is high. You deserved a break. Take five minutes. Grab some water, stretch, check your phone a no don't check your phone. See you in five.

### Slide 16 — Cameras On
Welcome back! Quick reminder — cameras on, please. I know it feels like a small thing but it makes a real difference.

### Slide 17 — Fork Repo
Alright, first thing — lets get your workspace set up. I'm dropping the template repo link in the chat https://djn-krs-2709.github.io/Product-School---AI-Product-Strategy/Modules/Strategy%20Repo%20Template.html 

Heres what you're going to do: click "Use this template" on GitHub, give it a name, and open it up in Cursor, VS Code, or even GitHub's web editor if you prefer. This should take about five minutes.

If you don't have a GitHub account, no stress — pair up with someone who does. You can set up your own account after class. But heres the important thing I want you to understand: this repo is the anchor artifact for the entire course. Everything you build from today forward goes here. It travels with you after the course ends. By Module 6, you're presenting from this repo. So it's not homework — it's your living strategy. Think of it like a product you're building for yourself.

### Slide 18 — Diagnostic
OK now lets talk about the diagnostic framework. We're going to score ourselves on three axes: moat strength, data advantage, and platform risk. One means you're in pain, five means you're strong. And don't worry if your numbers feel low — a partner is going to challenge your scores in a few minutes anyway, so there's no point in being generous with yourself.

Let me be clear about something. These three axes are a lens, not a final score. The numbers force honesty — and if you score yourself all fives, come find me because we need to talk. Seriously. I've never seen a product that's a five on all three and I've looked at a lot of products. But the axes are deliberately broad. If you're in healthcare AI, your "platform risk" looks completely different from someone building a consumer app. Adapt the criteria to your world.

Let me calibrate with some companies you know. Figma built such deep workflow integration that switching costs are enormous — strong on workflow moat. Slack has network effects that grow with every team that joins — deep on that dimension. A thin ChatGPT wrapper UI? Lets be honest — basically no moat at all. One API change and you're done. Zapier built an entire ecosystem of integrations — strong on orchestration. See how different the profiles are? That's what your scores should reflect.

### Slide 19 — Live Diagnosis

Before you score yourselves, let me demystify this rubric by doing it live on a product we all know. Shout one out what should be the product — Notion, Figma, Linear, or Slack? Heres the scenario: Apple, Google, or OpenAI ships a native version of this product's core feature tomorrow. Then what?

We're going to score it together on all three axes from the previous slide — Contextual Moat, Data Advantage, and Platform Exposure — 1 to 5 on each. Shout out a number for Moat. Then Data Advantage. Then Platform Exposure. Don't worry if we disagree — messy is good. The argument IS the learning.

Use the cheat sheet below as your fallback if the room goes quiet — it has my own rough scores across all three axes for each of the four products, so you can prime the discussion or check your gut against it.

**If the room picks Notion:**
Moat — I'd say 3, maybe 4. Deep workflow gravity once teams build their whole wiki there. But the editor itself? Google Docs and Microsoft Loop are closing fast, and AI writing assistants are commoditizing the core. Switching cost is real but not impossible — people do migrate. Data Advantage — solid 4. They see how teams organize knowledge, what gets linked, what gets searched. That's proprietary signal that OpenAI doesn't have. Platform Risk — 3. Apple Intelligence in Notes, Google Gemini in Docs, Microsoft Copilot in OneNote — all of them are gunning for "AI-powered workspace." Notion's bet is that depth of integration and the knowledge graph keep people locked in. The risk is that "good enough AI" in a tool you already pay for wins.

**If the room picks Figma:**
Moat — 4 to 5, genuinely strong. Design files, component libraries, design systems — the switching cost is enormous. Teams have years of work embedded in Figma. That's workflow gravity you can't replicate in a weekend. Data Advantage — 3. They see design patterns and component usage at scale, but it's not the kind of compounding data loop that makes the product smarter every use. Platform Risk — 2 to 3. Apple and Google aren't building Figma competitors. The real threat is AI-native design tools that skip the canvas entirely — prompt-to-UI tools that make the manual design step optional. That's the existential question for Figma.

**If the room picks Linear:**
Moat — 2 to 3. Issue trackers are notoriously easy to switch. The data is structured, exportable, and the workflows transfer. Linear is fast and opinionated, but Jira exists and AI-powered project management is coming from everywhere. Data Advantage — 2. They see sprint data and velocity, but so does every other project management tool. It's not proprietary signal that compounds. Platform Risk — 4, meaning high risk. GitHub is building project management natively. Notion is expanding into project tracking. If AI can auto-generate and manage tasks from conversations and code commits, the standalone issue tracker is the first thing that gets absorbed.

**If the room picks Slack:**
Moat — 4. Network effects are real — every person who joins makes it stickier for everyone else. Your company's institutional memory lives in Slack channels. That's powerful gravity. Data Advantage — 4 to 5. They see every conversation, every workflow, every integration. That's an extraordinary signal about how teams actually work. If they can make AI that surfaces the right context at the right time, nobody else has that data. Platform Risk — 3. Microsoft Teams is the obvious threat and it's bundled free with Office 365. But the deeper risk is that AI assistants start to replace the chat paradigm entirely — why search Slack when an agent can just answer your question directly?

and you might disagree on scores? That's exactly what happens when you score your own product. Now imagine your partner poking holes in your reasoning — that's the next exercise."

### Slide 20 — Your Scores

Alright, your turn. This is where the abstract framework meets your actual product. You've got ten minutes. I want you to score yourself on all three axes and write down at least one specific vulnerability.

Be ruthlessly honest. If everything is a five, that's a red flag — seriously, come find me. Open up `01-the-bet/diagnostic.md` in your repo. The template has the structure ready — just fill in your scores, your rationale, and we'll add the killer memo in a few minutes. When you're done, commit it. That file travels with you to Module 2.

I'm going to set you into breakout rooms for yourself. and again, don't overthink it whether the score is a 3 or a 4. Just pick one and move. You can always revise later — that's literally what version control is for.

### Slide 21 — Pair Challenge

OK time's up on solo work. Hope you were honest with yourselves. I will now assign a partner to you. You've got five minutes each.

Heres the deal: your partner has to lower at least one of your scores. Not to be mean — because self-assessment is always generous. Always. I've never met a PM who underscored themselves. A partner's pushback surfaces things you can't see yourself. And then they have to name a real attacker on that axis. Not "Big Tech" — a specific company or product that could exploit that weakness today. Give me a name and a URL.

Take sixty seconds by yourself first to think about who that competitor might be. Specificity matters. If you can't name the attacker, you haven't looked hard enough. And if your partner is being too polite, tell them — being nice isn't being helpful. The market won't be nice.

### Slide 22 — Killer Memo

Now the fun part. I love this exercise. I want you to write a killer memo. Three sentences. You are the head of AI at a major platform — Google, Apple, Microsoft, OpenAI, whoever makes sense for your space. And you're writing the internal memo about why you're going to kill this product. Put yourself in their shoes. What do they see when they look at your product? Opportunity, that's what.

Three minutes, silent. Write it as if you're that person. Outside-in perspective catches blind spots that your own self-scores miss every time.  When you're done — and if we have time — I'd love to hear a sentence or two from a couple of volunteers.

Who wants to read their attack? Don't be shy — the best ones are always a little painful to read out loud.

### Slide 23 — Prototype Lab
Alright, heres where it gets real. This is the hands-on lab section — The Prototype Bet. Everything weve talked about today — probabilistic thinking, vulnerability, speed — it all comes together right now. 

### Slide 24 — Build

Alright, this is my favorite part of the session. Everything we've talked about — probabilistic bets, vulnerability, speed — it all becomes real right now. Theory is done. We build.

You have fifteen minutes. I want you to build a working prototype of your AI product concept using v0, Cursor, or Lovable. The bar is a shareable link. That's it. It doesn't have to be pretty, it doesn't have to be complete — it has to exist. Fifteen minutes ago you were scoring yourself on a rubric. Now you're going to have a working thing. Thats the whole philosophy of this course in one exercise.

Now — I know staring at a blank prompt is the hardest part, so I'm dropping a starter template in Slack right now. Fill in the blanks and paste it into your tool. Here it is:

**Prompt template to drop in Slack:**

> Build me a web app prototype for an AI [your archetype: copilot / automator / oracle / creator / orchestrator] product called [name].
>
> **Who it's for:** [target user and their role]
> **The one thing it does:** [one core task the AI handles — be specific]
> **First screen:** When the user opens the app, they see [describe what's on screen — a dashboard, an input field, a list, etc.]
> **The AI moment:** When the user [trigger action], the AI [what it generates / surfaces / automates]
> **Show me:** [the key output — a recommendation, a report, a generated asset, a completed task]
>
> Use a clean, modern UI. Dark theme. One page, no login screen.

Three tips before you start. First — don't build your whole product. Build the one screen that shows why AI makes this valuable. The "aha moment." If your product is a copilot, show the moment the AI suggests something smart. If it's an automator, show the before-and-after of a task that used to take 30 minutes.

Second — don't over-specify the prompt. Write what the user experiences, not implementation details. "The AI analyzes their sales data and highlights the three riskiest deals" is better than "use a transformer model with RAG to process CSV uploads." Let the tool figure out the how.

Third — iterate, don't restart. If the first result is 60% right, steer it. "Make the dashboard cards clickable" or "add a confidence score next to each recommendation." One follow-up prompt beats starting over every time.

If you don't have an account on any of those tools, pair up with someone who does. When you have your link, paste it into `01-the-bet/prototype.md` in your repo and commit. The prototype now lives in your strategy repo — it's not a browser tab you're going to lose tomorrow.

This is what separates builders from deck-builders. Fifteen minutes. Go. I'll be walking around if anyone gets stuck.

### Slide 25 — Synthesis

OK lets bring it together. Look at what you accomplished today. Seriously, take a second to appreciate this. Look at your `01-the-bet/` folder in your repo. You should have `diagnostic.md` with your scores, your vulnerability, and your killer memo. And you should have `prototype.md` with your prototype link. Both committed.

That right there? That's Component 1 of your living strategy. It's real, it's in version control, and it grows every session. This repo is yours — it's not a class exercise that disappears when the course ends. By Module 6, you'll be presenting from it. And it'll look completely different from what it looks like right now, in the best way.

 Two hours ago most of you walked in not sure what to expect, and now you've got a vulnerability scorecard, a killer memo, and a working prototype — all committed to a repo. 

### Slide 26 — Bridge to M2

For next time — make sure your repo has `01-the-bet/` committed with everything from today. That's your carry-forward. Don't skip this part — Module 2 builds directly on what you did today.

And heres the question that's going to keep you up at night until Module 2: can anyone copy what you just built in six months? Because Module 2 is all about data flywheels, vendor risk, and what happens when someone decides to eat your lunch. If the killer memo exercise made you a little nervous, good — Module 2 is where we figure out what to do about it. One session down, five to go. 


### Slide 27 — Takeaways

Let me tell you a story that ties together everything we did today. Gamma — the AI presentation tool. A year and a half ago, Gamma was a small team with a simple bet: nobody actually wants to make slides. People want to communicate ideas, and the slide-making part is just friction. So they built an AI that turns a plain-text prompt into a full presentation. Ship fast, learn fast.

Heres where it gets interesting. Their first version was rough. The outputs were decent but not great. A traditional product team would have spent six months polishing before launch. Gamma didn't. They shipped it, watched what users actually did with it, and learned something nobody predicted — people weren't using it for work presentations. They were using it for school projects, church announcements, community events. Entirely new behaviors that no amount of upfront research would have surfaced. Thats takeaway one: **AI strategy is probabilistic.** You can't predict which use case wins. You place the bet, set your kill criteria, and let the data tell you where the value actually is.

Now — did Gamma have a moat? Honestly, not much. The core technology is the same LLM everyone else has access to. Any team could build "AI slides" in a weekend. And they knew it. They scored themselves honestly on that axis and instead of pretending they had a defensible position, they leaned into speed. They iterated on templates, user patterns, and distribution faster than anyone else could copy them. Thats takeaway two: **score your vulnerability honestly.** Gamma didn't lie to themselves about their moat score. They used that honesty to pick the right strategy — speed over defensibility. The teams that get in trouble are the ones who give themselves all fives and then get blindsided.

And heres the part I love most. Gamma's first prototype took days, not months. It wasn't a strategy deck about AI presentations — it was an actual AI presentation tool. Rough, imperfect, but real. And because it existed, they could put it in front of users immediately and learn. Every insight they got came from the prototype, not from a research report. Thats takeaway three: **build to think, commit to learn.** You just did the same thing in fifteen minutes. A working prototype beats a strategy deck every time. And now yours lives in a repo — version-controlled, shareable, alive. Thats what separates builders from deck-builders.

### Slide 30 — Extra Practice
If you want to go deeper, two optional exercises. First — rewrite your killer memo with a different platform attacker. If you wrote it from Google's perspective, try Apple. Does the attack vector change? That tells you something important about where your vulnerability actually is. Second — flesh out your repo. Review your `01-the-bet/` files, fill in any placeholders you skipped in class, update the top-level README with your bet summary, and commit. Next session is Module 2 — The Moat. You can build fast. Now — can anyone copy it?

### Slide 31 — Survey

Last thing — there's a quick survey, takes about sixty seconds. QR code is on the screen, I'll also drop the link in Slack. Your feedback really does help me make the next session better. I read every single response, I'm not just saying that.

And if you want to share — what's one thing that surprised you today? Drop it in the survey or tell me on the way out. 

### Slide 32 — Q&A

Alright, before we close — any final questions? This is your time to ask anything about what we covered today. Feel free to unmute or drop your question in the chat. And if something pops up later, share it in Slack — Im always around. Thanks everybody. See you next time!
