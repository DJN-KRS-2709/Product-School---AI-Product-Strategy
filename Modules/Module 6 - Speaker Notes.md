# Module 6 — The Pitch

### What this module is about

This is the capstone. Five components built across five sessions -- now you assemble one story and pitch it. The emotional arc today is performance anxiety turning into confidence. You've been filling in worksheets and scoring flywheels and auditing contracts -- now all of that becomes a narrative you say out loud. And honestly? I think a lot of you are going to surprise yourselves with how ready you already are.

The assumption I want to break today: "A roadmap is a strategy." It's not -- it's a delivery plan. A strategy answers why this bet, why now, and why us. The roadmap follows after the story is clear. Stripe is the reference here -- they write public memos, articulate principles, name the bets, then derive epics from those bets. The roadmap comes last, not first. Most of you have probably never separated "strategy" from "roadmap" before -- naming that distinction is the big conceptual unlock of this module, and once you see it you really can't unsee it.

You'll leave with four artifacts: a finalized living strategy repo with all five component folders plus a board-ready README, a multi-horizon roadmap committed to your repo, a board pitch you've rehearsed out loud, and a before/after comparison of your M1 baseline to prove your own growth. That last one is my favorite. You're going to feel the difference.

### The flow and why it's structured this way

We open with the course arc to give everyone the closure moment -- seeing all six modules as one connected argument instead of six isolated sessions. Then the provocation knocks down three myths about roadmaps, metrics, and GTM. The lecture block covers horizons, AI metrics, board framing, and GTM frictions -- four concepts that all feed the capstone simulation. The Duolingo case and moat scorecard bridge the lecture into applied work. After the break it's all hands-on: finalize the strategy, build the roadmap with AI, then the board simulation. We close with the M1-vs-now reflection and the certification. The simulation is the main event -- everything before it is setup, everything after it is emotional payoff. I genuinely think this is the session people remember most.

---

### Slide 1 -- The Pitch

Alright, welcome to Module 6. Look at you. You made it. Five sessions of building components -- the bet, the moat, the margin, the contract, the guardrails -- and today you assemble them into one story and pitch it to the room.

OK so I know some of you are already nervous about the simulation. Thats totally fine. Honestly, I'd be worried if you weren't at least a little nervous -- it means you care. But here's what I want you to hear: by the time we get there, you'll have your repo polished, your roadmap built, and the frameworks in your head. The nerves turn into confidence once you realize you've already done the hard work. You've BEEN doing the hard work for five sessions.

Heres the big idea for today: a roadmap is not a strategy. I know that sounds obvious when I say it, but think about what you actually present in your quarterly reviews. Its a roadmap. Features, timelines, resources. Thats a delivery plan. A strategy explains why those decisions and not others. Let me tell you how Stripe thinks about this. They don't start with epics. They write the strategy document first -- the public memos, the principles, the bets. Then the roadmap gets derived from that. Epics follow strategy, not the other way around. Most PMs have never made that separation, and once you see it, you can't unsee it. Sound familiar? Thats by design -- this course has been building that muscle.

### Slide 2 -- Expectations

We're on Module 6, you know the drill by now. Quick housekeeping and we're in. Lets make this last one count.

### Slide 3 -- Syllabus

Quick overview of where we are. The capstone simulation is the main event today -- everything else builds toward that moment. Think of the first half as loading the cannon and the simulation as firing it.

### Slide 4 -- Recall

So last session we covered governance and compounding -- guardrails at scale. Think of today as the natural next step: you've built it all, now sell it. Everything from M5 about responsible scaling and governance? That becomes part of the story you tell a board. You're not just pitching a product anymore, you're pitching a system that can grow without blowing up. Thats a fundamentally different conversation than "here's our feature roadmap," and boards notice the difference immediately.

### Slide 5 -- Course Arc

OK take a look at this. All six modules in a flow, M1 through M6, with the first five marked complete and M6 highlighted. This is the closure moment. Six sessions that were actually one connected argument the entire time.

See the three bundles below the arc? C1 and C2 -- your Bet plus Moat -- thats your thesis and defensibility. C3 and C4 -- Margin plus Contract -- thats economics and trust. C5 -- Guardrails -- thats scale without blowing up. And today, the pitch ties them all together.

Heres what I want you to internalize, and I mean really sit with this for a second. You didn't build a deck. You built a system. Each component feeds the next. The bet validates what to build, the moat makes it defensible, the margin makes it sustainable, the contract makes it trustworthy, the guardrails make it scalable. The pitch is just the story that connects them. Thats it. Thats all a pitch is -- a story about a system.

### Slide 6 -- Provocation

Three claims on screen, all false -- same format as always. Lets click through them.

Claim number one: "A roadmap is a strategy." This is the core argument of the entire module. Most PMs equate roadmap with strategy because thats what they present quarterly. But heres the distinction: a roadmap shows decisions made visible -- features, timelines, resources. A strategy explains why those decisions and not others. A roadmap without a thesis is a to-do list. Lets be honest, how many of you have presented a roadmap and called it strategy? Yeah. Me too, earlier in my career. Stripe figured this out -- they write the strategy document first, public memos, principles, bets, then derive the roadmap from it. Epics follow strategy, not the other way around.

Claim number two: "AI metrics are just product metrics." This sets up what we'll cover on slide 8. Traditional product metrics like MAU and retention are necessary but insufficient for AI products. You also need quality signals -- hallucination rate, drift velocity. Cost signals -- inference ROI. Trust signals -- HITL rate, confidence distribution. Without those, your board defaults to "black box plus liability." You need to give them a way to evaluate AI health the way they evaluate financial health. And most teams just... don't. They show the same dashboard they've always shown and wonder why the board is nervous.

Claim number three: "A great product sells itself." This sets up slide 10. Heres the thing -- AI products face three GTM frictions that traditional SaaS just doesn't. Probabilistic outputs make demos scary -- one bad generation and you're done. Governance gates block purchase decisions -- enterprise buyers send security and legal through the door before they'll even look at the wow. And trust needs to ramp gradually. A great AI product with no governance pack loses to a mediocre one with a compliance story. Every single time. I've seen it happen.

### Slide 7 -- Three Horizons

This is the first of four lecture points that teach board-level thinking. Look at the three horizon cards on screen. AI-compressed timeframes: H1 is "Ship" -- zero to four weeks, high confidence, execute. This earns you the credibility for H2. H2 is "Validate" -- one to three months, medium confidence, each bet has a named kill criteria. This is where your living strategy lives. H3 is "Explore" -- three to six months, low confidence, small investment, experiments. See the red line at the bottom: "One horizon only equals incomplete roadmap. AI-native cadence equals monthly, not quarterly."

OK so heres the big shift I want to name explicitly. Traditional roadmaps ran on quarterly or annual cadence -- H1 was zero to three months, H2 was three to twelve months, H3 was twelve-plus months. In an AI-native world, those timeframes compress dramatically. Amplitude went from four-month roadmaps to four-week roadmaps. And before you think "thats just one company" -- no, thats where the industry is heading. Nobody can credibly predict what happens twelve months from now in AI. If your H3 still says "twelve-plus months," you're planning in a world that no longer exists. Wild, right?

And the approach to each horizon should be completely different. H1 is execution -- you know what to build, you have the capabilities, ship it and earn trust. H2 is validation -- you're running strategic bets, each with a hypothesis and a named kill criteria. If the signal doesn't appear within the window, you stop. H3 is experimentation -- small investment, low confidence, you're exploring whether a behavior shift or new market is real. The level of investment, the team structure, and the decision-making framework should all differ across horizons.

Boards fund portfolios across time, not one backlog. An AI roadmap thats 100% H1 is execution without vision. An AI roadmap thats 100% H3 is vision without credibility. Boards want to see all three horizons funded with different risk profiles -- H1 builds trust through delivery, H2 is the strategic bet, H3 is the optionality play.

Let me tell you the Shopify story because I think it makes this really concrete. H1 was polishing the core commerce stack -- fast wins, proving the team ships. Nothing flashy, just earning trust through delivery. H2 was AI embedded in workflows -- Sidekick, the merchant assistant. Thats a real bet on AI-as-copilot that changes how merchants actually manage their stores day to day. H3 was the platform ambition -- Shopify as the operating system for commerce, not just a storefront builder. Same narrative spine, three different horizons, three different approaches. And heres the key: this isn't a document you write once a year. You revisit monthly, not annually. The living strategy is the mechanism -- push an update to your repo, not a slide refresh to a deck.

### Slide 8 -- AI Metrics

On screen you've got a three-by-two grid of six AI-specific metrics that boards care about beyond standard product metrics. Hallucination Rate -- thats your liability signal. Drift Velocity -- silent failure, the kind that scares boards most because nobody sees it coming. Confidence Distribution -- your quality profile. HITL Rate -- scalability ceiling. Inference ROI -- margin health. And Eval Regression -- reliability across updates.

Heres why this matters. Without AI-quality and cost signals alongside your traditional metrics, executives default to treating AI as a liability rather than an investment. These six metrics give your board a way to evaluate AI health the way they evaluate financial health -- with leading indicators, not just lagging outcomes. Think about how Microsoft paired Copilot adoption metrics with guardrails and degradation visibility. Or how Datadog gives you the usage story alongside the reliability story. Thats the pattern. You need both.

OK quick poll for the room: whats the number one AI metric you'd put on a board slide tomorrow? Lets go round-robin -- three or four of you, fifteen seconds each. Don't overthink it. Go.

### Slide 9 -- Board Questions

This slide frames board communication as four questions organized into three buckets. First, The Case: why invest, why can't this be copied? That maps to your Bet plus Moat. Second, The Model: does the math hold? That maps to Margin. Third, The Risks: trust, failure modes, scale. That maps to Contract plus Guardrails. See the red callout at the bottom: "Don't open with the model -- open with the thesis."

Heres the thing about executive working memory. It operates in buckets, not your full stack trace. When you present to a board, they're mentally sorting everything you say into "do I believe the bet," "do the numbers work," and "what can go wrong." If you open with the tech architecture or the model details, you've lost them before they understand the thesis. I've seen it happen so many times. Smart PMs with great products who lose the room in the first ninety seconds because they lead with the how instead of the why.

Let me tell you the Notion story because it's a perfect example. Their pitch was AI as a workflow wedge -- thats the bet -- plus distribution advantage through existing workspace adoption -- thats the moat. Not "we use GPT-4" first. Thesis first, tech stack second. Always. You'll thank me for drilling this in when you're standing in front of your actual board.

### Slide 10 -- GTM Frictions

This is going to prime the real-world objections you'll face in the board simulation coming up. Three AI-specific GTM friction patterns, and I want you to really internalize these because they're going to show up in the Q&A.

First, show plus tell. Probabilistic outputs mean one bad demo and you're done. So you need to script demo paths and show recovery behavior. Don't just show the happy path -- show what happens when the AI gets it wrong and how the product handles it. Thats actually more impressive than a perfect demo, because it shows you've thought about failure.

Second, gov gate. Enterprise buyers send security and legal through the door before they'll even look at the wow. Remember the governance pack from M5? That becomes actual sales collateral. It's not a compliance checkbox -- it's a GTM asset. I cannot stress this enough. The governance pack sells.

Third, trust ramp. Start with high-confidence use cases and widen autonomy as proof stacks up. Not "full AI from day one." You earn the right to automate more by proving you handle less. This is patience as a strategy, and it works.

### Slide 11 -- Duolingo Case

OK so let me tell you the Duolingo story because I think its one of the best cautionary tales in AI product strategy. They partnered with GPT-4 for roleplay conversations and explanations, unlocking conversational practice for 500 million-plus learners -- moving beyond drills to real dialogue. Amazing, right? Huge moment. Everyone was excited.

Then came the crack. The market asked "does AI actually improve learning outcomes?" Suddenly the story shifted from tech buzz to pedagogical scrutiny, and investor reactions were... mixed. Thats a polite way of saying the stock took a hit.

Heres what they did to fix it. They reframed AI as extending the learning loop -- practice, correction, better practice. They published actual learning outcome data and led investor decks with retention and learning metrics instead of "GPT-4 inside." The technology became invisible. The user impact became the headline.

This is the same muscle as board Q&A -- narrative repair under scrutiny. Duolingo's mistake was leading with the technology story. Their fix was leading with the user impact story. Thats the exact shift most of you need to make. If someone asks "why should I fund this?" and your first instinct is to talk about model architecture, catch yourself. Lead with the problem, lead with the user, lead with the outcome. We're going to practice this in about thirty minutes.

### Slide 12 -- Moat Scorecard

OK on screen we've got a table with all eight moats from Module 2 -- Data, Workflow, Regulatory, Distribution, Ecosystem, Network, Physical, Scale -- each scored zero to one with an evidence column.

Quick reminder on the philosophy here, consistent with what we covered in M2: you need one or two moats that are genuinely strong, not high scores across all eight. The eight moats are vocabulary for naming whats defensible, not a checklist to complete. Most great AI products have one dominant moat and maybe a secondary one. If you're trying to be strong on all eight, thats a sign you haven't made a strategic choice. Score honestly. You're going to present this in the simulation and the room will push back if the evidence doesn't match the number. Trust me, you'd rather catch that here than in front of your actual leadership team.

### Slide 13 -- Break

Amazing work so far. Seriously. You just covered horizons, AI metrics, board framing, GTM frictions, and a full case study -- thats a LOT. You deserved this break. Take five minutes -- grab some water, stretch, let your brain breathe for a second.

When you come back, cameras on. Fifteen minutes to finalize your strategy, ten on the roadmap, then 35 minutes of board simulation. This is the session where everything you've built gets said out loud. Im genuinely excited for this part.

### Slide 14 -- Cameras On

Welcome back everyone! Cameras on — this is the most important stretch of the entire course. You're about to finalize your strategy, build your roadmap, and then pitch to the room. The next 60 minutes are all applied work and performance. Stay locked in.

### Slide 15 -- Strategy Assembly

Alright, this is it. Strategy assembly time. Everything you've built across five modules — bet, moat, margin, contract, guardrails — now you pull it all together into one coherent narrative. Your repo becomes your pitch deck. Lets finalize.

### Slide 16 -- Finalize Strategy

OK everyone open your strategy repo. Heres the goal: review all five component folders and update your top-level README.md with complete summaries.

Check each of the five component folders -- 01-the-bet through 05-the-guardrails -- and make sure the key artifacts from each module are committed. Then update your README. This is the document you'll present from in the board simulation. The README should tell the full strategy story: whats the bet, why is it defensible, how do the economics work, whats the trust architecture, how does it govern at scale.

What "good" looks like: a README that a colleague could read cold and understand the strategy without opening any sub-folders. What "bad" looks like: a README thats just headings with no substance, or five unconnected paragraphs that don't build on each other. The README is your board deck. Make it read like one. And honestly, if you've been keeping up with the living strategy across modules, this should feel more like polishing than building from scratch. Thats the whole point of the system.

### Slide 17 -- AI Evaluator

On screen you've got six evaluation dimensions: Bet Validation -- is it evidence-backed or just conviction? Capability Gaps -- what needs to be built? Defensibility -- platform-proof or copyable? Pricing Alignment -- do the economics hold under stress? Trust and Reliability -- is the contract explicit and measurable? Impact and Scale -- what breaks at 10x?

OK heres the twist -- you're using AI to evaluate your own AI strategy. And I love this part because the evaluation dimensions aren't random. They're the same five lenses from M1 through M5 turned into a systematic query. Bet validation is M1. Defensibility is M2. Pricing alignment is M3. Trust and reliability is M4. Impact and scale connects to M5's governance concerns. See how it all loops back?

This creates a reusable workflow you take back to work. After this course, you can adapt these dimensions for any new bet. Run your strategy through the evaluator, see where its weak, fix it, run it again. Thats the loop. Thats something you can use on Monday morning, not just today.

### Slide 18 -- Build Roadmap (AI-Powered)

This is where the course frameworks connect to your real work. Instead of filling in blank roadmap boxes, I want you to dump your actual backlog -- Jira items, feature requests, stakeholder asks, whatever you have -- and let the AI map each initiative to your strategy components and place it in a horizon.

Heres the teaching point: a roadmap proves the strategy moves through time -- it's not a wishlist. The roadmap has to show how H1 wins fund H2 bets, and how H2 bets earn the right to pursue H3 experiments. But lets be honest, most PMs build roadmaps completely disconnected from strategy. This exercise forces the connection: every initiative has to link to a strategy component -- Bet, Moat, Margin, Contract, Guardrails -- or it's noise. Remember the compressed horizons from slide 7: H1 is zero to four weeks, ship. H2 is one to three months, validate. H3 is three to six months, explore. This isn't annual planning -- it's a living document you revisit monthly.

Heres the prompt to paste into Claude or ChatGPT:

> You are an AI Product Strategy advisor. I will give you two things: (1) my strategy summary and (2) a list of initiatives from my backlog.
>
> MY STRATEGY SUMMARY:
> [Paste your README strategy summary here -- bet, moat, margin, contract, guardrails]
>
> MY BACKLOG / INITIATIVES:
> [List 8-15 initiatives, features, or requests. Can be rough -- titles and one-line descriptions are enough]
>
> YOUR TASK:
> 1. Map each initiative to the strategy component it most directly supports
> 2. Classify each initiative into a horizon (AI-compressed cadence)
> 3. For each H2 initiative, suggest a kill criteria
> 4. Flag any initiatives that don't connect to any strategy component -- these are candidates to cut or rethink.
>
> OUTPUT FORMAT:
> Create a markdown table grouped by horizon, with columns: Initiative | Strategy Component | Hypothesis | Kill Criteria (H2 only) | Confidence (H/M/L)

Once you get the output back, review it. Does the AI's classification match your instinct? Move items that feel wrong. Pay special attention to unmapped items -- those are either noise or they're exposing a gap in your strategy. Both are valuable findings.

Two forcing functions. First, every roadmap must have an H3 line. If your roadmap is all H1, I'm going to push you: "Where's the experiment that scares you? Thats H3." Second, every H2 bet needs a kill line. Stripe-style check: "If we don't see X by week 6, we stop." If the AI didn't generate a good kill criteria, thats your job to add. Don't skip this -- kill criteria is what separates a strategy from a hope.

And remember -- this roadmap isn't a one-time artifact. You should be re-running this prompt monthly as your backlog evolves and your strategy sharpens. The output goes directly into `06-the-pitch/roadmap.md` in your repo.

### Slide 18.5 -- Roadmap Output

Take a look at what the AI generated. Does the classification match your instinct? Move items that feel wrong. Pay special attention to initiatives that didn't map to any strategy component — those are either noise you should cut, or they're exposing a gap in your strategy. Both are valuable findings. Make sure you've got at least one H3 line — if your roadmap is all H1, I'm going to push you.

### Slide 19 -- Board Simulation

OK. This is it. The capstone. The single best bang-for-minute in the whole certification, and honestly one of my favorite moments to watch. Heres how it works: five minutes to present, three minutes for Q&A. We'll get about four of you presenting to the room. No slides, no decks -- you present directly from your strategy repo.

On the left card you can see what to cover in your five minutes: Bet, Moat, Margin, Trust, Scale risk, Roadmap. On the right, what the board may ask: Why fund this? Moat score? Margin under stress? Governance gaps? Kill plan?

Lets get some volunteers. Who wants to go first? And look, I know this is scary. But you've been building toward this for five sessions. You're more ready than you think. If you're quiet, I'll call on someone whose moat scorecard or roadmap caught my eye during the exercises. The format is simple: open your strategy repo, walk us through your README and key artifacts. No Google Slides, no deck. The repo is the artifact. Everyone else plays the board and asks the hardest questions you can think of. Don't go easy on each other -- being tough here is being kind.

Heres what I'm going to watch for. The presentations that land will lead with the thesis first and tech stack second. If someone opens with "we use GPT-4 for X," I'm going to stop you: "The board doesn't know what GPT-4 is. What problem are you solving?" Remember Duolingo? Same lesson. After each presentation, we debrief -- one thing that worked, one thing that didn't. The most common weakness I see: no kill criteria, no answer to "what if this doesn't work?"

And if the room's questions are too soft, I'll seed some real board-style questions. "Whats your inference cost per user?" "What happens when your provider doubles pricing?" "If I gave this to a competitor, how long until they replicate it?" These are the questions a real board asks. Nobody on a board cares about your model architecture -- they care about the bet, the moat, and the margin.

### Slide 20 -- M1 vs Now

OK this is my favorite part of the whole course. I want everyone to do this. Remember Module 1? Your CEO asks: "Whats our AI strategy?" You wrote a three-sentence answer in about three minutes, before you had any frameworks. No structure, no vocabulary, just vibes. I want you to write that answer again. Right now. Three sentences. Same prompt, but with everything you've learned.

Take three minutes. Quiet writing time.

The M1 version is usually something vague like "We should use AI to improve our product." The M6 version is specific: "We're betting on AI-powered X because of Y, with a moat in Z, priced as W." That gap between the two? Thats the course working. Thats YOUR growth, and the living strategy is the proof. Im genuinely proud of this group for getting here.

If someone wants to read both versions to the room, please do -- it's a powerful moment. But I'm not going to force anyone. Just notice the difference for yourself. Let it sink in. You earned that delta.

### Slide 21 -- What You Leave With

You can see the list on screen -- all five strategy components checked off, plus the artifacts from today: roadmap, AI metrics, moat scorecard, and the baseline delta. I'm not going to read the list to you; you can see it.

Instead I want to name the transformation. You walked into M1 with a vague sense that your company needed an AI strategy. You're leaving with a version-controlled repo containing six component folders, a board-ready README, and a roadmap with kill criteria. Others at your company can open this repo, fork it, build on it. It doesn't require an annual rewrite -- you update it as your product evolves. Thats a living strategy.

Look at what you built. Seriously, look at it. This isn't a certificate you frame and forget. It's a toolkit you can use Monday morning. Open the repo, update a component, push a commit. Thats the whole workflow. And every time you push an update, the strategy gets sharper. Thats the flywheel from M2 applied to your own strategic thinking. How cool is that?

### Slide 22 -- Certification

Done means: six modules, a living strategy, and a capstone delivered. You earned it. Im not going to give a big speech here because honestly, the work speaks for itself. The certification is the formal milestone, but the real proof is the repo you built. Congratulations. I mean that.

### Slide 23 -- Complete Repo

Take one last look at your repo. All six folders, all components committed. The README tells your complete strategy story. This is a version-controlled, shareable, forkable strategy document. Others at your company can open it, read it, build on it. Thats the power of putting strategy in a repo instead of a slide deck.

### Slide 24 -- Complete

Look at what you accomplished across this entire course. Six modules, six components, one living strategy. You went from a vague three-sentence answer about AI strategy to a specific, evidence-backed, board-ready pitch. You built a prototype, scored a flywheel, mapped a cost curve, designed trust architecture, audited governance, and pitched it live. Thats a transformation.

### Slide 25 -- Takeaways

Three final takeaways for the whole course. First — a roadmap is not a strategy. A strategy explains why these decisions and not others. The roadmap follows. Second — boards fund portfolios across time. Show them all three horizons with different risk profiles. Third — the living strategy is a practice, not a deliverable. Open your repo monthly, update a component, push a commit. The strategy gets sharper every time you revisit it.

### Slide 26 -- Extra Practice

Two optional exercises. First — re-run the AI roadmap prompt with your real backlog from work — not the simplified version from class. See what it maps and what it flags. Second — schedule a monthly strategy review using your repo. Set a calendar reminder, open the README, update one component. Thats the living strategy workflow.

### Slide 27 -- Survey

Last thing -- QR code is on screen. Two minutes, fill it out before you go while the energy is still up. Your insights genuinely help me make each class better than the last, and I take every response seriously.

Thank you. Genuinely. This was six sessions of hard work, real thinking, and a lot of honesty about your products. You showed up every time and you did the work. Im proud of what this group built. Now go use it. See you out there.

### Slide 28 -- Q&A

Alright, last Q&A of the course. Any final questions? Anything from today or from the whole journey? Feel free to unmute. And Slack stays open — Im always around if something comes up. Thank you so much for this experience. Six sessions, real work, real growth. Im proud of what you built. Now go use it.
