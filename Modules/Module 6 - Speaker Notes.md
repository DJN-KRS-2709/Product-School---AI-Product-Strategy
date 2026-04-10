# Module 6 — The Pitch
## Speaker Briefing for Carlos

### What this module is about

This is the capstone. Five components built across five sessions — now they assemble one story and pitch it under fire. The emotional arc is performance anxiety turning into confidence. They walk in nervous about presenting something they've been building in fragments; they leave having said it out loud to peers playing their board. That's the transformation: from worksheets to narrative.

The traditional assumption this module breaks: "A roadmap is a strategy." It's not — it's a delivery plan. A strategy answers why this bet, why now, and why us. The roadmap follows after the story is clear. Stripe's model is the reference: public writing plus principles → bets → then epics. Roadmap follows. Most PMs in the room will have never separated "strategy" from "roadmap" before — naming the distinction is the conceptual unlock of this module.

They leave with four artifacts: a finalized living strategy repo (all five component folders plus a board-ready README), a multi-horizon roadmap committed to their repo, a board pitch they've rehearsed out loud, and a before/after comparison of their M1 baseline to prove their own growth.

### The flow and why it's structured this way

The first half is a fast lecture block — full arc, provocation, multi-horizon roadmaps, AI metrics, board questions, GTM frictions, Duolingo case, moat scorecard. We cover a lot of ground quickly because none of these are deep-dive concepts the way golden datasets or data flywheels were in earlier modules. These are translation skills: how to take the substance from M1–M5 and package it for an executive audience. The lecture block is essentially a crash course in "how boards think about AI investments."

The break sits before the heaviest applied stretch in the entire course. After break, the session is almost entirely hands-on: finalize the living strategy (~15 min), run it through the AI evaluator (~8 min), build the roadmap (~10 min), then the board simulation capstone (~35 min). More than a third of the session is rehearsal and performance, not consumption. That ratio is deliberate — by M6, they know the frameworks. What they need is practice saying it out loud to someone who pushes back.

On the opening Expectations and Syllabus slides, keep it light. Everyone knows the drill by now. The Recall slide (slide 4) matters more — it connects M5's governance and compounding work to today's assembly task and reframes the session as "you've built it all, now sell it."

---

### Slide 1 — The Pitch

This is the last title slide of the course, so the energy should feel different from the previous five. The three waypoints on-slide — Integrate, Translate, Present — are the session's three acts. Name them explicitly: "First half, we learn how boards think about AI investments. Second half, you assemble everything and pitch it under fire."

The subtitle on the slide is "How Do You Get This Funded, Shipped, and Adopted?" — that's the question this whole module answers. The wow moment to plant early: "In about 2 hours you'll have said your strategy out loud to peers playing your board. Most of you have never done that." Let the stakes land. Performance anxiety is productive here — it focuses attention.

### Slide 5 — Course Arc

This is the closure moment where the full course clicks as one connected argument instead of six isolated sessions. The slide shows all six module nodes in a flow (M1→M6), with the first five marked as complete and M6 highlighted as the current active node. Below the arc, three bundles break down how the components group: C1–C2 (Bet + Moat = thesis and defensibility), C3–C4 (Margin + Contract = economics and trust), C5 (Guardrails = scale without blowing up).

Walk through the three bundles in about 30 seconds each. The Adobe Firefly example at the bottom of the slide is optional but powerful if you have time: bet on brand-safe generative AI → moat via Creative Cloud workflow integration → margin via bundles (Firefly is a filler inside Creative Cloud, not a standalone product) → contract via IP indemnification and opt-in training data. That's the whole course in one company story, told in about 30 seconds.

The teaching point: they didn't build a deck — they built a system. Each component feeds the next. The bet validates what to build, the moat makes it defensible, the margin makes it sustainable, the contract makes it trustworthy, the guardrails make it scalable. The pitch is the story that ties them together.

### Slide 6 — Provocation

Three claims on-slide, all FALSE. Same format as previous modules — click to reveal. The three claims are: "Our roadmap IS our strategy," "AI metrics = product metrics," and "Great product sells itself."

Claim #1 (roadmap = strategy) is the core argument of the module. Most PMs equate roadmap with strategy because that's what they present quarterly. The distinction: a roadmap shows decisions made visible — features, timelines, resources. A strategy explains why those decisions and not others. A roadmap without a thesis is a to-do list. The Stripe reference: they write the strategy document first (public memos, principles, bets), then derive the roadmap from it. Epics follow strategy, not the other way around.

Claim #2 (AI metrics = product metrics) sets up slide 8. Traditional product metrics like MAU and retention are necessary but insufficient for AI products. You also need quality signals (hallucination rate, drift velocity), cost signals (inference ROI), and trust signals (HITL rate, confidence distribution). Without these, your board defaults to "black box plus liability."

Claim #3 (great product sells itself) sets up slide 10. AI products face three GTM frictions that traditional SaaS doesn't: probabilistic outputs make demos scary, governance gates block purchase decisions, and trust needs to ramp gradually. A great AI product with no governance pack loses to a mediocre one with a compliance story.

Poll each claim — thumbs, stand/sit, or Zoom reactions. Then reveal. After all three, do a 20-second partner flash: "Which claim did you believe?" This surfaces assumptions they're still carrying into the capstone.

### Slide 7 — Three Horizons

This is the first of four lecture points that teach board-level thinking. The slide shows three horizon cards: H1 (0–3 months, quick wins that fund H2), H2 (3–12 months, where the living strategy lives), H3 (12+ months, new behavior or new market). The red line at the bottom: "One horizon only = incomplete roadmap."

The teaching point: boards fund portfolios across time, not one backlog. An AI roadmap that's 100% H1 is execution without vision. An AI roadmap that's 100% H3 is vision without credibility. Boards want to see all three horizons funded with different risk profiles — H1 builds trust through delivery, H2 is the strategic bet, H3 is the optionality play.

Shopify is the concrete example: H1 was polishing the core commerce stack (fast wins, proving the team ships). H2 was AI embedded in workflows — Sidekick, the merchant assistant — a bet on AI-as-copilot that changes how merchants manage their stores. H3 was the platform ambition — Shopify as the operating system for commerce, not just a storefront builder. Same narrative spine, three different time horizons, three different risk profiles.

Interactive moment: "Point to H1 / H2 / H3 — where does your roadmap put most of its weight right now?" Most rooms cluster at H1, which is the honest answer but also the vulnerability. If someone says they're mostly H3, push gently: "What's your H1 proof point that earns the right to fund H3?" This primes the roadmap exercise after the break.

### Slide 8 — AI Metrics

The slide shows a 3×2 grid of six AI-specific metrics that boards care about beyond standard product metrics: Hallucination Rate (liability signal), Drift Velocity (silent failure), Confidence Distribution (quality profile), HITL Rate (scalability ceiling), Inference ROI (margin health), and Eval Regression (reliability across updates). At the bottom: "Durability beats hype — retention is the quality signal."

The teaching point: without AI-quality and cost signals alongside traditional metrics, executives default to treating AI as a liability rather than an investment. These six metrics give your board a way to evaluate AI health the way they evaluate financial health — with leading indicators, not just lagging outcomes. Microsoft Copilot and Datadog are the reference patterns: pair the usage/adoption story with guardrails and degradation visibility.

Quick poll: "What's the number one AI metric you'd put on a board slide tomorrow?" Go round-robin — 3–4 people, 15 seconds each. This surfaces how few people have a clear answer, which is exactly the gap this slide fills. Most PMs can name their retention metric but can't name their drift metric. That's the problem.

### Slide 9 — Board Questions

The slide frames board communication as four questions organized into three buckets: (1) The Case — why invest, why can't this be copied (maps to Bet + Moat), (2) The Model — does the math hold (maps to Margin), (3) The Risks — trust, failure modes, scale (maps to Contract + Guardrails). The red callout at the bottom: "Don't open with the model — open with the thesis."

The teaching point: executive working memory operates in buckets, not your full stack trace. When you present to a board, they're mentally sorting everything you say into "do I believe the bet," "do the numbers work," and "what can go wrong." If you open with the tech architecture or the model details, you've lost them before they understand the thesis.

Notion is the worked example: AI as a workflow wedge (bet) plus distribution advantage through existing workspace adoption (moat) — not "we use GPT-4" first. Stripe is another one: money movement plus risk management first, not "LLM inside our fraud detection."

Sixty-second pair practice: one partner plays PM, the other plays board member. The PM frames their product using the three buckets — case, model, risks — in 60 seconds. This is a dress rehearsal for the board simulation structure they'll use after the break. If someone can't fill a bucket, that's a gap they need to fix in the finalization exercise.

### Slide 10 — GTM Frictions

This slide primes the real-world objections participants will face in the capstone simulation. Three AI-specific GTM friction patterns are shown: (1) Show + tell — probabilistic outputs mean one bad demo answer feels fatal, so you need to script demo paths and show recovery behavior. (2) Gov gate — enterprise buyers send security and legal through the door before they'll even look at the wow, so the M5 governance pack becomes actual sales collateral. (3) Trust ramp — start with high-confidence use cases and widen autonomy as proof stacks up, not "full AI from day one."

The Salesforce and Intercom reference: both built sales motions around governance-first storytelling. Salesforce sells the Einstein Trust Layer as a feature in the sales deck. Intercom leads with containment metrics ("Fin resolves X% of conversations without escalation") rather than "we use LLMs."

Pair exercise: "Which of these three frictions is scariest for your buyer? Tell your partner in 45 seconds." Naming the friction now means they can preempt it in their board pitch later. If someone says "none of these apply to us," push them: "What would your buyer's CISO say about your AI product today? That's the friction."

### Slide 11 — Duolingo Case

Standard 3-act case study format. Bet: Duolingo partnered with GPT-4 for roleplay conversations and explanations, unlocking conversational practice for 500M+ learners — moving beyond drills to real dialogue. Crack: the market asked "does AI actually improve learning outcomes?" — the story shifted from tech buzz to pedagogical scrutiny, and investor reactions were mixed. Fix: Duolingo reframed AI as extending the learning loop (practice → correction → better practice), published learning outcome data, and led investor decks with retention and learning metrics instead of "GPT-4 inside."

The teaching point and why this case is here: this is the same muscle as board Q&A — narrative repair under scrutiny. Duolingo's mistake was leading with the technology story; their fix was leading with the user impact story. That's the exact shift most people in the room need to make. When a board member asks "so what?" — you answer with what changed for the user, not what model you used.

Poll or hand-raise: "Is your current AI story mostly about the technology, or mostly about the user outcome?" Most people skew tech, which is exactly the Duolingo mistake. Let the self-awareness land before moving to the moat scorecard.

### Slide 12 — Moat Scorecard

The slide shows a table with all eight moats from M2 (Data, Workflow, Regulatory, Distribution, Ecosystem, Network, Physical, Scale), each scored 0–1 with an "evidence" column. A total score at the bottom: 4+ strong, 2–3 weak, 0–1 danger.

This gives participants vocabulary and self-defense for the inevitable board question: "Why can't someone copy this?" In the board simulation, partners playing the board will almost certainly ask some version of this question. Having a scored moat card with evidence means they can answer with specifics rather than generalities.

Snowflake vs. Nvidia is a good comparison if you need a quick example: Snowflake's moat is data + ecosystem (data sharing network effects, third-party marketplace), while Nvidia's moat is physical + scale (fabrication lead time, CUDA ecosystem lock-in). Completely different shapes, same scorecard framework.

Two minutes solo: score your eight moats with evidence. Two minutes partner compare: where did you disagree? The disagreement is where the learning happens — it forces evidence over opinion. If someone scores themselves 1/1 on a moat with no evidence sentence, that's a 0.

### Slide 13 — Break

Reset before the heaviest applied stretch in the entire course. Tease what's coming so they return focused: "When you come back — 15 minutes to finalize your strategy, 10 on the roadmap, then 35 minutes of board simulation. This is the session where everything you've built gets said out loud."

### Slide 16 — Finalize Strategy

This is a split-layout slide. The left side frames the goal: review all five component folders and update the top-level README.md with complete summaries. The right side shows the three component bundles: C1–C2 (Bet + Moat — thesis, flywheel, kill switch), C3–C4 (Margin + Contract — cost path, eval, trust UX), C5 (Guardrails — governance, agents, audit). A bottom bar links to the Strategy Repo Template for reference.

The teaching point: integration skill matters more than starting over. Some people will want to panic-rewrite from scratch because the capstone feels high-stakes. That wastes five sessions of cohort work. The exercise is curation and synthesis — review each folder, tighten the language in the README, make sure the story flows from bet to pitch. Three rows on-slide, details live in their docs.

Practical instruction: have everyone open their strategy repo. They should check each of the five component folders (01-the-bet through 05-the-guardrails) and make sure the key artifacts from each module are committed. Then update their README.md — this is the document they'll present from in the board simulation. The README should tell the full strategy story: what's the bet, why is it defensible, how do the economics work, what's the trust architecture, how does it govern at scale.

Optional warm-up: 90-second elevator pitch to a partner before going into silent work. This surfaces the gaps before they start writing. If someone can't say their strategy in 90 seconds, they're not ready to finalize — they need to cut.

What "good" looks like: a README that a colleague could read cold and understand the strategy without opening any sub-folders. What "bad" looks like: a README that's just headings with no substance, or five unconnected paragraphs that don't build on each other.

### Slide 17 — AI Evaluator

The slide shows six evaluation dimensions in a 2×3 grid: Bet Validation (evidence-backed or just conviction?), Capability Gaps (what needs to be built?), Defensibility (platform-proof or copyable?), Pricing Alignment (economics hold under stress?), Trust & Reliability (contract explicit and measurable?), and Impact & Scale (what breaks at 10×?). Below: "Paste your strategy → generate prompt → run in ChatGPT or Claude → review before your pitch."

This is the meta-move of the course — using AI to evaluate their own AI strategy. The evaluation dimensions aren't random; they're the same five lenses from M1–M5 turned into a systematic query. Bet validation is M1. Defensibility is M2. Pricing alignment is M3. Trust and reliability is M4. Impact and scale connects to M5's governance concerns. This creates a reusable workflow they take back to work — after the course, they can adapt these dimensions for any new bet.

How it works: participants open their strategy repo, copy their README or key component summaries, and construct a prompt that asks an AI to evaluate their strategy across these dimensions. They paste the prompt into ChatGPT or Claude and get a scored, specific critique. Give them about 5 minutes to construct and run the prompt, about 3 minutes to review the AI's output. The critique surfaces gaps they should address before the board simulation.

If time is tight, this can be done after the session — the evaluation framework is permanent. But if you can fit it in, the AI feedback creates a powerful moment where participants see their blind spots surfaced by a dispassionate evaluator before their peers do it in the simulation.

### Slide 18 — Build Roadmap

The slide shows three horizon cards with fill-in fields: H1 Quick Wins (initiative + metric impact), H2 Bets (the bet + kill criteria), H3 Moonshots (vision + what must be true). A link at the bottom points to the `06-the-pitch/roadmap.md` template in their repo.

The teaching point: a roadmap proves the strategy moves through time — it's not a wishlist. The roadmap has to show how H1 wins fund H2 bets, and how H2 bets earn the right to pursue H3 moonshots. The Amazon/AWS pattern is the classic: near-term commerce cash and operational improvements funded the platform bets that became AWS, the most profitable division. Near-term credibility buys long-term optionality.

Two forcing functions: (1) Every roadmap must have an H3 line. If someone's roadmap is all H1, push them: "Where's the bet that scares you? That's H3. If you don't have one, your board will wonder where the ambition is." (2) Every H2 bet needs a kill line — a falsifiable signal that tells you whether to double down or walk away. Stripe-style check: "If we don't see X by month 6, we stop." If someone can't name their kill criteria, their H2 isn't a bet — it's a hope.

### Slide 19 — Board Simulation

This is the capstone exercise and the single best bang-for-minute in the whole certification. The slide shows: 5 minutes to present, 3 minutes for Q&A, approximately 4 decks presented to the room. The left card lists what to cover in 5 minutes (Bet, Moat, Margin, Trust, Scale risk, Roadmap). The right card lists what the board may ask (Why fund this? Moat score? Margin under stress? Governance gaps? Kill plan?).

Setup: mix company sizes and archetypes in the presentation order if possible. Ask for volunteers first — there are usually 2–3 people who want to go. If the room is quiet, call on someone whose moat scorecard or roadmap was particularly interesting during the exercises. The presenting participant walks the room through their strategy repo README. Their partner (or the room) plays the board and asks the hardest questions they can think of.

What to watch for: the decks that land will lead with the thesis first and tech stack second. If someone opens with "we use GPT-4 for X," gently redirect: "The board doesn't know what GPT-4 is. What problem are you solving?" The debrief after each presentation should name one thing that worked and one thing that didn't. The most common weakness: no kill criteria, no answer to "what if this doesn't work?"

If the room's questions are too soft, seed Stripe-style questions: "What's your inference cost per user?" "What happens when your provider doubles pricing?" "If I gave this to a competitor, how long until they replicate it?" These are the questions a real board asks. Nobody on a board cares about your model architecture — they care about the bet, the moat, and the margin.

### Slide 20 — M1 vs Now

The slide shows two cards side by side: Module 1 (their original 3-sentence answer to "Your CEO asks: what's our AI strategy?") vs. Module 6 (write your new answer, 3 sentences). Below: "The delta is your growth. The living strategy is the proof."

This is the emotional proof of growth without forcing vulnerability. It's the same CEO prompt from Module 1 — the one they wrote in 3 minutes on day one, before they had any frameworks. Now they write it again with everything they've learned. Keep sharing optional, but most people will be genuinely surprised by how different their answer is. The M1 version is usually vague ("We should use AI to improve our product"), while the M6 version is specific ("We're betting on AI-powered X because of Y, with a moat in Z, priced as W"). That gap is the course working.

Don't rush this. Give them 3 minutes of quiet writing time. If someone wants to read both versions to the room, let them — it's a powerful moment. But don't force it.

### Slide 21 — What You Leave With

The slide lists all five strategy components with checkmarks (Bet + Moat, Margin + Contract, Guardrails), plus the additional artifacts from today: roadmap, AI metrics, moat scorecard, and the baseline delta.

The teaching point here is artifact over attendance. Don't read the list — they can see it. Instead, name the transformation: "You walked into M1 with a vague sense that your company needed an AI strategy. You're leaving with a version-controlled repo containing six component folders, a board-ready README, and a roadmap with kill criteria. Others at your company can open this repo, fork it, build on it. It doesn't require an annual rewrite — you update it as your product evolves. That's a living strategy."

This is the Figma/Notion energy moment — a toolkit they can reuse Monday, not a certificate they frame and forget.

### Slide 22 — Certification

Formal close after the emotional peak of slides 19–20. The slide shows: "Done means: 6 modules · living strategy · capstone delivered." Keep it brief and warm. They earned it. The certification is the formal milestone, but the real proof is the repo they built.

### Slide 27 — Survey

Product School feedback loop. About 2 minutes. High response rate if you ask in-room while the energy is still up. Genuine thank-you — this was the culmination of six sessions of hard work.
