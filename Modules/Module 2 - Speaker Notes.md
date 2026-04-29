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

### Slide 2 — Expectations

Same ground rules as Module 1. Cameras on, be present, use Slack for questions. One thing I'll add for today: the exercises are more intense than M1. When I say "be honest with your scores," I really mean it. Generous scores only hurt you when your partner tries to attack your flywheel later. Trust the process.

### Slide 3 — Course Arc

Quick look at where we are in the course. Module 1 was The Bet — you diagnosed your vulnerability. Today is Module 2 — The Moat. Can anyone copy what you're building? After today we move into economics, trust, governance, and the final pitch. Each module adds a component to your living strategy. Todays the one where you find out if your strategy has staying power.

### Slide 4 — Recall from M1

Quick reconnect before we jump in. You brought your Module 1 scorecard and your prototype. All that work from last session feeds directly into what we're doing today. The vulnerability you diagnosed? Thats the crack we're going to try to defend. So pull up your repo and have your scores handy — you'll need them now.

### Slide 5 — Moat Stress Test

OK so pull out your Module 1 scorecard. Find the lowest score — thats your crack, your weak spot. Now I want you to name one specific company that could exploit it. And I don't mean "Big Tech" — give me a real name. A company with a face and a product page. You've got two minutes to write it down. 

We're doing this first because it anchors everything that follows in something personal. Every concept I'm about to teach you is going to land harder because you already feel the threat. I know it's a little uncomfortable to start here But trust me generous answers don't help anybody. I learned that one the hard way.

### Slide 6 — 8 Moats

Lets look at the grid. I want you to read each card and think about *why* each one is hard to copy — not just who does it.

Bloomberg sits on proprietary data that compounds with every terminal session. The more people use it, the richer the dataset gets. Salesforce is so deeply embedded in how companies run their sales process that ripping it out would take years — switching cost is the moat. Palantir holds compliance certifications and government clearances that competitors have to earn from scratch — you can't shortcut that. Apple owns the channel — they decide how a billion people discover and adopt software. Shopify has thousands of third-party apps and integrations creating interdependence — leave Shopify and you leave the ecosystem. LinkedIn gets more valuable with every new user — classic network effects. Tesla has gigafactories, charging infrastructure, hardware that takes years and billions to replicate. AWS runs at a scale where unit economics keep improving — the bigger they get, the cheaper each unit becomes.

Now heres the thing — you don't need all eight. You need ONE that's actually real. Strategy is being excellent at the minimum number of things, not average at many. And for AI products specifically, Data and Workflow are the two that matter most. I spent way too long early in my career trying to be defensible on five dimensions at once. Spoiler: I wasn't defensible on any of them. Learned that lesson the expensive way.

So which moat is yours? Name it in one word. And then — what other company masters one of these? I want to hear it from you. Either raise your hand and unmute, or post it in the chat. If you can't name your moat in one word, by the way, thats a finding. Thats not a failure — thats actually one of the most useful things you could discover today. Because you can't defend what you can't name.

The way to think about this: most products need only one or two genuine moats, not all eight. This grid gives you vocabulary for naming what's defensible. It's not a checklist to complete — it's a mirror.

### Slide 7 — $1.5B Wrapper

OK so you just named your moat. Heres what happens when it isn't real. Let me tell you a story.

Jasper. $125 million raised, $1.5 billion valuation, 70,000 customers. In 2022, they were THE AI startup. I mean THE one. Fastest growing, most hyped, investors literally fighting to get in. Every conference, every blog post, every "future of AI" list — Jasper was on it. They were the darling. And then ChatGPT launched. OpenAI added plugins. Google shipped Gemini into Workspace. And overnight — and I mean literally overnight — AI writing went from premium product to free feature baked into tools everyone already used. Jasper had to pivot to enterprise marketing workflows. The trajectory: from 1 to 100 and then 100 to 40. Thats not a dip. Thats an identity crisis. Sound familiar? It should, because this pattern is everywhere right now.

I'm showing you this right after the 8 Moats because the typology is abstract until you see a $1.5 billion company get eaten in real time. Jasper thought they had a moat — 70,000 customers, fastest growth in AI. They didn't. So now I want to ask you: what is YOUR product — wrapper (A thin UI layer on top of someone else's AI model that dies the moment the model provider ships the same feature natively.)  or workflow (A product that orchestrates a process around the model — accumulating proprietary data, embedding into user operations, and surviving any model swap because the value is in the orchestration, not the API call.) ? 

### Slide 8 — Depth Spectrum

OK heres a spectrum that I think makes this really concrete. On the left: Chatbot — you can switch in a day. On the right: Operating System — switching means rebuilding everything. Four examples along the way: Zendesk AI handles tickets, Notion AI sits inside docs, GitHub Copilot touches your editor plus PRs plus CI, and NetSuite runs the entire business. See the chatbot end? Jasper sat right there. The OS end? That's NetSuite. And you can kinda feel the difference, right? 

Where does your product sit? Point to a spot on this spectrum. Lets hear two or three. And here's the uncomfortable question: could your users switch in a weekend? If yes, you're Jasper. I don't say that to be mean — I say it because I've watched it happen to products I cared about. Now if someone's thinking "we're early stage, we have no depth yet" — that's totally fine. Cold-start is temporary. Every product starts shallow. The real question is whether your architecture is designed to escape it. Thats what separates intentional from accidental. And thats what the rest of today is about.

### Slide 9 — Loops, Not Data

I think this might be the most important reframe of the day. 

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

### Slide 12 — Lab: Data Flywheel

Alright, this is where the real building happens. Everything from the first half — the 8 moats, the Jasper story, the flywheel concept — now you apply it to your own product. We're going straight into the flywheel exercise before the break so that you can sit with your scores during the break and let them sink in. Lets get into it.

### Slide 13 — Map Your Flywheel

You've got fifteen minutes on your own now and this is the big one. Score the four loops and write what you actually capture today. And I mean today — "we plan to build this" is a 1, not a 3. I know that feels harsh but I promise generous scores only hurt you later. I've watched people give themselves 4s on loops they haven't even started building yet. Don't be that person. If you score generously and the peer challenge coming up next won't bite. So be honest.

I'll be walking around So please shout if you need any help.

Go to your repo and select the Flywheel Scorer tool — scores each loop, and flags the weakest one. It also pulls in your Module 1 vulnerability data if you saved it. 

### Slide 14 — Encroachment Threats

There are three vectors I want you to think about: platform encroachment, vertical competitor, and adjacent expansion. For each one, name the attacker, identify the vector, estimate the time-to-threat, and the percentage of your value at risk. Go to your repo, open `02-the-moat/data-flywheel.md`, and scroll down to the Encroachment Threat Assessment section — fill in all three vectors there. We use three vectors because most people only think about direct competitors. Platform and adjacent are the two that blindside you — and honestly, they're the ones that actually kill products. Direct competition is a slow burn. Platform encroachment is a house fire.

Heres a live example of adjacent expansion that still blows my mind. When Anthropic cracked down on third-party agent harnesses using Claude subscriptions early this year (2026), OpenAI treated it as a customer acquisition channel. They hired OpenClaw's creator in February, publicly endorsed third-party harness use with Codex subscriptions, and positioned openness as a differentiator while Anthropic was locking down. One provider's governance decision became another provider's growth lever — thats encroachment through policy, not features. Wild, right? Nobody saw that coming.

### Slide 15 — Break

Amazing work so far. You scored your flywheel and mapped your encroachment threats. You deserved a break. Take five minutes — grab some water, stretch. Let those scores and threats sit with you. When you come back: your partner is going to attack your moat for real with a 90-day plan. The fun stuff. 

### Slide 16 — Cameras On

Welcome back everyone! Quick reminder — cameras on please. The applied work coming up is partner-heavy and its way better when you can see each others faces. Plus some of the exercises involve pointing at your screen, which is hard to do with cameras off. Lets stay engaged for this home stretch.

### Slide 17 — 90-Day Encroachment

OK this is one of my favorite exercises.
I'm going to pair you up with someone. Six minutes per person. The defender presents their flywheel plus threats. The encroacher builds a concrete 90-day plan: weeks 1 through 4, what do you ship? Weeks 5 through 8, how do you poach users? Weeks 9 through 12, why don't users come back? Target the weakest flywheel loop — thats your entry point.

Here is why it is important to be challenged: self-assessment is always generous. Always. I don't care how honest you think you are — when it's your own product, you soften the edges. A partner's attack plan surfaces blind spots you literally cannot see yourself. And the week-by-week structure forces specificity — no hiding behind "eventually someone might." If your partner is being too polite, tell them: you're not being helpful by being nice. The market won't be nice.  Have fun with it  — some of the best insights I've seen come out of exercisesb like this. People surprise themselves with how creative they can be when they're playing offense.

### Slide 18 — Kill Switch

Three layers. First, abstraction — no direct provider calls in your code. Second, multi-model routing — tasks get routed by cost, quality, and latency. Third, an eval harness — an automated quality check. So let me ask: how many of you could swap providers in 48 hours? Yeah, almost nobody. I get it. Thats the normal answer. Don't feel bad about it.

That 48 hours is deliberately aggressive — it should make you uncomfortable. Most products are hard-wired to one provider and nobody thinks about it until that provider changes their pricing or their terms. And by then its a fire drill. The Kill Switch turns dependency into optionality. Its the difference between "we chose this provider" and "we're trapped with this provider."

Now, vendor portability looks different in every domain. Think of the 48-hour bar as a way to reason about dependency and swap readiness, not as a literal SLA you need to hit tomorrow. It's a thought experiment that reveals how trapped you actually are. And for some of you, the answer to that thought experiment is going to be uncomfortable. Thats OK. Thats why we're here.

### Slide 19 — Lab: Kill Switch

OK time to build your escape plan. This is the Kill Switch lab — the exercise where you audit your actual vendor dependencies and build a portability plan. Three layers, three timelines, one very uncomfortable question: how fast could you swap?

### Slide 20 — Portability Audit

Fifteen minutes — audit your vendor dependency. Here are the stress tests: what if your provider doubles pricing? What if they restrict your use case? Walk out of this exercise with three concrete action items: this week, this month, this quarter. And I want specifics — not "build abstraction layer" but "abstract the embedding call in search by Friday." Specific enough that you could hand it to an engineer and they'd know exactly what to do. This checklist travels to Module 3 because portability directly affects your cost model.

And if anyone thinks "restricts your use case" feels hypothetical — oh, let me tell you. January This year (2026) — Anthropic quietly blocked subscription OAuth tokens from working outside Claude Code. February — rewrote the legal terms. March — shipped Claude Code Channels to replace the core reason people used third-party harnesses. April — cut the cord entirely. Four months from passive enforcement to full cutoff. If your product depends on a provider's subscription tier for cost arbitrage, that timeline is your portability risk made real. Four months. Thats not a lot of runway. Thats barely enough time to get alignment on a new vendor.

The Kill Switch Audit tool is linked on the slide — it walks through each dependency layer, stress-tests swap time, and gives you a concrete this-week, this-month, this-quarter action plan. Export it — you'll need it in Module 3.

### Slide 21 — Synthesis

OK so take a breath and Look at what you accomplished today. You stress-tested your moat, scored a flywheel, survived a 90-day attack from a partner who was actively trying to destroy your business, and built a portability plan. Thats a lot. Hope you enjoyed it — I know some of it was intense but you handled it really well.

Now its time to tie it together. Fill in Component 2 of your living strategy: flywheel scores, weakest loop, top threat, portability plan, swap readiness, and your three actions. The living strategy compounds across all six modules — if you skip Component 2, Module 3's cost model won't have the right inputs. So don't skip this. Future-you will thank present-you. I promise.

### Slide 22 — Bridge to M3

So here's what's coming next. Module 3 is the economics reality check — inference costs are compressing margins from 80% to 30%. Bring everything you built today. We've had two sessions on strategy and defensibility — Module 3 is the cold shower: does any of this make money? I'm not going to lie, it gets a little intense. But after what you did today — stress tests, encroachment attacks, kill switches — you've got the foundation. You'll be ready.

### Slide 23 — Your Repo

Take a look at your repo now. `01-the-bet/` is done from last session. And now `02-the-moat/` has your flywheel scores, your kill switch audit, and your encroachment analysis. Two folders down, four to go. The living strategy is starting to take real shape. Every module adds a layer and by M6 this thing tells your complete strategy story.

### Slide 24 — Takeaways

This is the storytelling close — same three-act structure we used for the Notion case in Module 1 and the Jasper case earlier today. Bet → Crack → Correction. I lean on the visuals and tell the story out loud, because by this point in the session people are tired and a list of bullets just bounces off them. A story lands.

Walk it left to right. Act one — "our data is our moat" — say it the way a PM would say it in a pitch meeting, slightly proud, slightly defensive. Thats where most of the room walked in this morning. Then act two — flip the energy. Jasper. $1.5 billion. 70,000 customers. Eaten in months. And they didnt see it coming because they were grading their own homework. Pause there. Let it sit. Then act three — heres what you actually built today. Compounding loops, not stockpiles. Peer-tested honesty, not self-assessment. Forty-eight hour swap readiness, not vendor dependency. Three real shifts, three real artifacts.

Land on the closing line — "most AI products live in Act 1. Today, you wrote your Act 3." Thats the whole module in one sentence. If you want to add one personal thing, this is the slide for it — a moment when you watched a team you cared about live in Act 1 and pay for it. Makes the lesson stickier than any framework.

This slide also replaces the old "What You Accomplished Today" closer — Synthesis already does that work, no need to repeat it. The Takeaways slide is now the emotional close, not the recap.

### Slide 25 — Extra Practice

Two optional exercises if you want to go deeper. First — run the 90-day encroachment plan again, but this time YOU play the encroacher against a different product in your industry. What would you do? Second — review your kill switch audit and add technical detail to each action item. Make them specific enough that an engineer could pick them up. Next session is Module 3 — The Margin. Does any of this make money?

### Slide 26 — Survey

QR code is on screen. Hope you enjoyed today — I know it was a lot. Like, genuinely a lot. But you handled it and you've got real artifacts to show for it. Fill out the survey before you go, it genuinely helps me make the next session better for you. Thanks everyone, amazing work today. See you next time.

### Slide 27 — Q&A

Alright, any final questions before we close? Feel free to unmute or drop them in the chat. And as always, Slack is open if something comes to you later. Great work today everyone. See you next time.
