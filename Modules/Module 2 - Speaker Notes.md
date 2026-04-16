# Module 2 — The Moat

### What this module is about

Module 1 diagnosed vulnerability. This one is where you build the defense. The emotional arc today is competitive anxiety — and honestly, thats a good thing. I know that sounds a little sadistic, but hear me out. Most AI products look differentiated right up until a platform ships the same feature for free. Happens all the time. By the end of this session, we're going to find out if anyone can copy what you're building in six months. Sounds scary? Good. Thats the whole point.

Heres the assumption I want to break today: "Our data is our moat." I hear this constantly. Every pitch deck, every strategy review, every PM who's trying to sound smart in a meeting. But lets be honest — data sitting in a database isn't a moat. It's a cost center. The real moat is whether your product gets smarter every time someone uses it. Thats a loop, not a stockpile. The flywheel concept is the engine of everything we do today, and once you see it, you genuinely cannot unsee it. I wish someone had shown me this framing about five years earlier than they did.

You'll leave with three artifacts: a scored flywheel with four loops rated honestly, a vendor portability plan — that's the Kill Switch audit with this-week, this-month, and this-quarter actions — and a competitive positioning map. Component 2 of your living strategy gets locked in at synthesis. So yeah, busy day. But after what you did in Module 1, you're more than ready for it.

### The flow and why it's structured this way

I'm opening with a stress test activity instead of a lecture because Module 1 already warmed everyone up — no need for another provocation. Getting you into your scorecard right away raises the stakes and honestly, I just think you learn faster when something's on the line. I'll spend about two minutes at the top on housekeeping — cameras, tools, ground rules. The first half covers moat theory: the 8 moats, the Jasper story, the depth spectrum, and the flywheel concept, broken up with the case study for energy. After the break its all applied work: map the flywheel, face an attacker in the 90-Day Encroachment Plan, build the Kill Switch, then position yourself on the competitive map. The 90-Day Encroachment Plan is a different framing from Module 1's pair challenge so it won't feel repetitive. The Kill Switch and positioning map at the end are the wow moments — practical artifacts you'll actually talk about after class. I genuinely think this is the session where things start clicking for people.

---

### Slide 1 — The Moat

Alright, welcome back everyone. Hope Module 1 didn't keep you up at night — or maybe I secretly hope it did, just a little. If you're feeling slightly more paranoid about your product than you were last week, that means it worked.

OK so today we're going to find out if anyone can copy what you're building in six months. By the time we're done, you'll have a scored flywheel, a vendor portability plan, and Component 2 of your living strategy filled in. We're starting here because most AI products look differentiated right up until a platform ships the same feature for free. Module 1 diagnosed vulnerability — today we build the defense. Lets get into it.

### Slide 5 — Moat Stress Test

OK so pull out your Module 1 scorecard. Find the lowest score — thats your crack, your weak spot. Now I want you to name one specific company that could exploit it. And I don't mean "Big Tech" — give me a real name. A company with a face and a product page. You've got two minutes to write it down, then three minutes to share with the room.

We're doing this first because it anchors everything that follows in something personal. Every concept I'm about to teach you is going to land harder because you already feel the threat. I know it's a little uncomfortable to start here — nobody loves staring at their weakest point first thing in the morning. But trust me, be honest with yourselves. The generous answers don't help anybody. I learned that one the hard way.

### Slide 6 — 8 Moats

Lets look at the grid. One real company per moat: Bloomberg for Data, Salesforce for Workflow, Palantir for Regulatory, Apple for Distribution, Shopify for Ecosystem, LinkedIn for Network, Tesla for Physical, AWS for Scale. Heres the thing — you don't need all eight. You need ONE that's actually real. Strategy is being excellent at the minimum number of things, not average at many. And for AI products specifically, Data and Workflow are the two that matter most. I spent way too long early in my career trying to be defensible on five dimensions at once. Spoiler: I wasn't defensible on any of them. Learned that lesson the expensive way.

So which moat is yours? Name it in one word. Go ahead, just say it out loud — don't overthink it. And then — what other company masters one of these? I want to hear two or three of you. If you can't name your moat in one word, by the way, thats a finding. Thats not a failure — thats actually one of the most useful things you could discover today. Because you can't defend what you can't name.

The way to think about this: most products need only one or two genuine moats, not all eight. This grid gives you vocabulary for naming what's defensible. It's not a checklist to complete — it's a mirror.

### Slide 7 — $1.5B Wrapper

OK so you just named your moat. Heres what happens when it isn't real. Let me tell you a story.

Jasper. $125 million raised, $1.5 billion valuation, 70,000 customers. In 2022, they were THE AI startup. I mean THE one. Fastest growing, most hyped, investors literally fighting to get in. Every conference, every blog post, every "future of AI" list — Jasper was on it. They were the darling. And then ChatGPT launched. OpenAI added plugins. Google shipped Gemini into Workspace. And overnight — and I mean practically overnight — AI writing went from premium product to free feature baked into tools everyone already used. Jasper had to pivot to enterprise marketing workflows. The trajectory: from 1 to 100 and then 100 to 40. Thats not a dip. Thats an identity crisis. Sound familiar? It should, because this pattern is everywhere right now.

I'm showing you this right after the 8 Moats because the typology is abstract until you see a $1.5 billion company get eaten in real time. Jasper thought they had a moat — 70,000 customers, fastest growth in AI. They didn't. So now I want to ask you: where is YOUR product — wrapper or workflow? Lets hear two or three of you. And yeah, this should sting a little. Better to feel it in this room than in a board meeting.

### Slide 8 — Depth Spectrum

OK heres a spectrum that I think makes this really concrete. On the left: Chatbot — you can switch in a day. On the right: Operating System — switching means rebuilding everything. Four examples along the way: Zendesk AI handles tickets, Notion AI sits inside docs, GitHub Copilot touches your editor plus PRs plus CI, and NetSuite runs the entire business. See the chatbot end? Jasper sat right there. The OS end? That's NetSuite. And you can kinda feel the difference, right? It's almost physical.

Where does your product sit? Point to a spot on this spectrum. Lets hear two or three. And here's the uncomfortable question: could your users switch in a weekend? If yes, you're Jasper. I don't say that to be mean — I say it because I've watched it happen to products I cared about. Now if someone's thinking "we're early stage, we have no depth yet" — that's totally fine. Cold-start is temporary. Every product starts shallow. The real question is whether your architecture is designed to escape it. Thats what separates intentional from accidental. And thats what the rest of today is about.

### Slide 9 — Loops, Not Data

Quick pivot here and I think this might be the most important reframe of the day. So pay attention to this one.

Everyone claims a data advantage. Every pitch deck I've ever read says "proprietary data moat" somewhere around slide 7. Its like a law of nature at this point. But lets be honest — data in a database isn't a moat. It's a cost center. The moat is whether your product gets smarter every time someone uses it. Thats a loop, not a stockpile. Look at the red question on screen: "When your users correct your AI, does that signal disappear — or compound?"

This matters because "data moat" is the thing every senior PM defaults to. It sounds smart. It slides easily into a strategy deck. But almost nobody actually has compounding loops. That distinction sets up the flywheel as a real mechanism, not just a concept. So keep that question in your head as we go into the next slide. Seriously, write it down if you need to. It's the kind of question that changes how you see your product.

### Slide 10 — Data Flywheel

This is the engine that turns depth into distance. And this is why Jasper's story ended the way it did — they never built it. Look at the circular diagram: users interact, you capture the signal, the model improves, you get better outputs, usage goes up, and the cycle starts again. Beautiful in theory. Hard in practice. Really hard, actually.

There are three data types that actually compound. First, corrections — when a user fixes your AI, that's proprietary training data. Nobody else has it. Think about that. Every time a user goes "no, thats wrong, it should be THIS," thats gold. Second, preferences — every edit builds a taste profile. Third, domain context — industry-specific knowledge that generic models will never have because they'll never see the inside of your customers' workflows.

The question is: does your product capture these or throw them away? And most products throw away their best signal. A correction is proprietary training data nobody else has. If you don't capture it, you're literally burning your own moat. And I get it — capturing signal is unglamorous infrastructure work. Nobody gets promoted for building a feedback loop pipeline. But it's the work that matters. It's the work that separates the products that survive from the ones that end up on a "whatever happened to" blog post.

### Slide 11 — Flywheel Scoring

Four loops: Correction, Preference, Domain Context, Network. Score each one from 1 to 5. Your weakest loop is where competitors attack first.

Now, scoring forces specificity, but the loop set is yours to adapt — your flywheel might have two loops or six. This isn't a fixed template, it's a starting point. Make it yours.

Heres the thing: abstract concepts don't change behavior. Numbers do. Once you see a 1 or 2 staring back at you, the priority becomes obvious. You stop debating philosophy and start fixing plumbing. I've seen this happen in every cohort — the moment someone writes down a number, the conversation changes completely. And this is the last thing before the break, so let it sit with you. Don't rush through it. Give yourself permission to be honest here.

### Slide 12 — Break

Amazing work so far. Seriously — look at what you just did. You stress-tested your moat, named your weakest point out loud, watched a $1.5 billion company get eaten alive, and scored your own flywheel with actual numbers. Thats not a small thing. You deserved a break. Take five minutes — grab some water, stretch, check your phone, do whatever you need. When you come back its all applied work. You're going to map your flywheel, face an attacker, and build your escape plan. The fun stuff. I promise.

### Slide 15 — Map Your Flywheel

OK welcome back. Hope you enjoyed that breather because we're going right back in.

You've got fifteen minutes on your own now and this is the big one. Score the four loops and write what you actually capture today. And I mean today — "we plan to build this" is a 1, not a 3. I know that feels harsh but I promise generous scores only hurt you later. I've watched people give themselves 4s on loops they haven't even started building yet. Don't be that person. Fifteen minutes instead of ten because this is the core artifact of the module. If you rush it, you'll score generously and the peer challenge coming up next won't bite. So be honest.

I'll be walking around — and fair warning, if you say you're capturing preferences but your product doesn't actually personalize model behavior, I'm going to push back. Thats a 1. I'm not trying to be mean, I'm trying to be useful. There's a difference. And you'll thank me when your partner tries to attack your flywheel in about twenty minutes.

The Flywheel Scorer tool is linked right on the slide — it gives you a visual flywheel, scores each loop, and flags the weakest one. It also pulls in your Module 1 vulnerability data if you saved it. Open it up and let it do the heavy lifting on the visualization.

### Slide 16 — Encroachment Threats

There are three vectors I want you to think about: platform encroachment, vertical competitor, and adjacent expansion. For each one, name the attacker, identify the vector, estimate the time-to-threat, and the percentage of your value at risk. We use three vectors because most people only think about direct competitors. Platform and adjacent are the two that blindside you — and honestly, they're the ones that actually kill products. Direct competition is a slow burn. Platform encroachment is a house fire. Big difference.

Heres a live example of adjacent expansion that still blows my mind. When Anthropic cracked down on third-party agent harnesses using Claude subscriptions in early 2026, OpenAI treated it as a customer acquisition channel. They hired OpenClaw's creator in February, publicly endorsed third-party harness use with Codex subscriptions, and positioned openness as a differentiator while Anthropic was locking down. One provider's governance decision became another provider's growth lever — thats encroachment through policy, not features. Wild, right? Nobody saw that coming.

### Slide 17 — 90-Day Encroachment

OK this is one of my favorite exercises in the whole course. Seriously, I look forward to this one every cohort.

Pair up with someone — ideally not the same partner from Module 1, mix it up a little. Six minutes per person. The defender presents their flywheel plus threats. The encroacher builds a concrete 90-day plan: weeks 1 through 4, what do you ship? Weeks 5 through 8, how do you poach users? Weeks 9 through 12, why don't users come back? Target the weakest flywheel loop — thats your entry point.

Heres why this works: self-assessment is always generous. Always. I don't care how honest you think you are — when it's your own product, you soften the edges. A partner's attack plan surfaces blind spots you literally cannot see yourself. And the week-by-week structure forces specificity — no hiding behind "eventually someone might." If your partner is being too polite, tell them: you're not being helpful by being nice. The market won't be nice. I'd rather you feel the punch here than in a quarterly review. Have fun with it though — some of the best insights I've seen in this course come out of this exercise. People surprise themselves with how creative they can be when they're playing offense.

### Slide 18 — Kill Switch

Three layers. First, abstraction — no direct provider calls in your code. Second, multi-model routing — tasks get routed by cost, quality, and latency. Third, an eval harness — an automated quality check. So let me ask: how many of you could swap providers in 48 hours? Show of hands. Yeah, almost nobody. I get it. Thats the normal answer. Don't feel bad about it.

That 48 hours is deliberately aggressive — it should make you uncomfortable. Most products are hard-wired to one provider and nobody thinks about it until that provider changes their pricing or their terms. And by then its a fire drill. The Kill Switch turns dependency into optionality. Its the difference between "we chose this provider" and "we're trapped with this provider."

Now, vendor portability looks different in every domain. Think of the 48-hour bar as a way to reason about dependency and swap readiness, not as a literal SLA you need to hit tomorrow. It's a thought experiment that reveals how trapped you actually are. And for some of you, the answer to that thought experiment is going to be uncomfortable. Thats OK. Thats why we're here.

### Slide 20 — Portability Audit

Fifteen minutes — audit your vendor dependency. Here are the stress tests: what if your provider doubles pricing? What if they restrict your use case? Walk out of this exercise with three concrete action items: this week, this month, this quarter. And I want specifics — not "build abstraction layer" but "abstract the embedding call in search by Friday." Specific enough that you could hand it to an engineer and they'd know exactly what to do. This checklist travels to Module 3 because portability directly affects your cost model.

And if anyone thinks "restricts your use case" feels hypothetical — oh, let me tell you. January 2026 — Anthropic quietly blocked subscription OAuth tokens from working outside Claude Code. February — rewrote the legal terms. March — shipped Claude Code Channels to replace the core reason people used third-party harnesses. April — cut the cord entirely. Four months from passive enforcement to full cutoff. If your product depends on a provider's subscription tier for cost arbitrage, that timeline is your portability risk made real. Four months. Thats not a lot of runway. Thats barely enough time to get alignment on a new vendor, let alone migrate.

The Kill Switch Audit tool is linked on the slide — it walks through each dependency layer, stress-tests swap time, and gives you a concrete this-week, this-month, this-quarter action plan. Export it — you'll need it in Module 3.

### Slide 21 — Synthesis

OK so take a breath. Seriously, take an actual breath. Look at what you accomplished today. You stress-tested your moat, scored a flywheel, survived a 90-day attack from a partner who was actively trying to destroy your business, and built a portability plan. Thats a lot. Hope you enjoyed it — I know some of it was intense but you handled it really well.

Now its time to tie it together. Fill in Component 2 of your living strategy: flywheel scores, weakest loop, top threat, portability plan, swap readiness, and your three actions. The living strategy compounds across all six modules — if you skip Component 2, Module 3's cost model won't have the right inputs. So don't skip this, even if you're tired. Future-you will thank present-you. I promise.

Once you've filled it in, pull it into the Living Strategy Builder and watch your flywheel scores and kill switch status show up in the dashboard. This is the first real visual you'll see in there: a flywheel radar chart that color-codes the strength of each loop. It's pretty satisfying to see it come together. Like, genuinely satisfying. You've earned that little dopamine hit.

### Slide 22 — Bridge to M3

So here's what's coming next. Module 3 is the economics reality check — inference costs are compressing margins from 80% to 40%. Bring everything you built today. We've had two sessions on strategy and defensibility — Module 3 is the cold shower: does any of this make money? I'm not going to lie, it gets a little intense. But after what you did today — stress tests, encroachment attacks, kill switches — you've got the foundation. You'll be ready.

### Slide 27 — Survey

QR code is on screen. Hope you enjoyed today — I know it was a lot. Like, genuinely a lot. But you handled it and you've got real artifacts to show for it. Fill out the survey before you go, it genuinely helps me make the next session better for you. Thanks everyone, amazing work today. See you next time.
