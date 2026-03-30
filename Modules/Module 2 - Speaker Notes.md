# Module 2 — The Moat

## Slide 1 — Title
- Today we find out if anyone can copy what they're building in 6 months
- They'll walk out with a scored flywheel, a vendor portability plan, and Component 2
- Why we start here: most AI products look differentiated until a platform ships the same feature for free. M1 diagnosed vulnerability — M2 forces them to build the defense

## Slide 2 — Agenda
- Starts with a hands-on activity — they're working before we even lecture
- We do this because M1 already warmed them up. No need for another provocation — getting them into their scorecard immediately raises the stakes
- "The 90-Day Encroachment Plan" — partner builds a week-by-week plan to steal users. Different framing from M1 so it doesn't feel repetitive
- Kill Switch at the end is the wow moment — the thing they'll talk about after class
- 2 min housekeeping buffer at the top for cameras, tools, ground rules

## Slide 3 — Moat Stress Test (Opening Activity)
- Pull out M1 scorecard, find lowest score — that's their crack
- Name one specific company that could exploit it. Not "Big Tech" — a real name
- 2 min to write, 3 min to share
- Why first: anchors the entire lecture in something personal. Every concept lands harder because they already feel the threat

## Slide 4 — 8 Moats: Which One Is Yours?
- Show the grid — one real company per moat (Bloomberg = Data, Salesforce = Workflow, Palantir = Regulatory, Apple = Distribution, Shopify = Ecosystem, LinkedIn = Network, Tesla = Physical, AWS = Scale)
- Key reframe: you don't need all eight. You need ONE that's actually real. Strategy = be excellent at the minimum number of things, not average at many
- For AI products specifically, Data and Workflow are the two that matter most
- Interactive moment: "Which moat is yours? Name it in one word." Then: "What other company masters one of these?" — get 2-3 from the room
- Why the reframe: Carlos's point is right — telling people they need 4+ moats is overwhelming and unrealistic. Most startups have one, maybe two. The goal is to be excellent at that one, then build a second as you scale
- If someone can't name their moat in one word, that's a finding
- **Mental model:** Most products need only one or two genuine moats, not all eight. The grid is vocabulary for naming what's defensible — not a checklist to complete.

## Slide 5 — Case Study: Jasper vs. ChatGPT
- "You just named your moat. Here's what happens when it isn't real."
- Bet: $125M raised, $1.5B valuation, 70K customers, fastest AI startup 2022
- Crack: ChatGPT launched, OpenAI added plugins, Google shipped Gemini into Workspace. AI writing became free and native
- Fall: pivoted to enterprise marketing workflows. Gokul said "from 1 to 100 and 100 to 40"
- Why here, right after 8 Moats: the typology is abstract until you see a $1.5B company get eaten in real time. Jasper thought they had a moat — 70K customers, fastest growth in AI. They didn't. This raises the stakes for everything that follows
- Ask the room: "Where is YOUR product — wrapper or workflow?" Get 2-3 answers. This should sting

## Slide 6 — How Deep Is Your Workflow? (Depth Spectrum)
- Visual spectrum from Chatbot (switch in a day) to Operating System (switch = rebuild)
- Four examples on the spectrum: Zendesk AI (handles tickets) → Notion AI (sits inside docs) → GitHub Copilot (editor + PRs + CI) → NetSuite (runs the business)
- Jasper connection: "Jasper sat here" — point at the chatbot end. "NetSuite sits here" — point at the OS end
- Interactive: "Where does your product sit? Point to a spot." Get 2-3 answers. "Could your users switch in a weekend? If yes, you're Jasper."
- Why after Jasper: the case study proved shallow = dead. The spectrum gives them a diagnostic — where do THEY sit? If they're on the left, this is urgent
- Cold-start: if someone says "we're early stage, we have no depth yet" — that's fine. Cold-start is temporary. The question is whether your architecture is designed to escape it

## Slide 7 — Building the Defense (Transition)
- 30-second pivot slide — don't linger
- "Everyone claims a data advantage. But data in a database isn't a moat — it's a cost center. The moat is whether your product gets smarter every time someone uses it. That's a loop, not a stockpile."
- Pause on the red question: "When your users correct your AI, does that signal disappear — or compound?"
- Why this earns its place: it reframes "data moat" (which every senior PM defaults to) into "compounding loops" (which almost nobody actually has). Sets up the flywheel as the mechanism, not just a concept

## Slide 8 — The Data Flywheel
- "This is the engine that turns depth into distance. Jasper never built it."
- Circular diagram: interact → capture → improve → better outputs → more usage → back to interact
- Three data types that compound: corrections (user fixes AI = proprietary training data), preferences (every edit builds a taste profile), domain context (industry-specific knowledge generic models lack)
- Key question: does your product capture these or throw them away?
- Why this lands harder now: they've seen Jasper die (no loops), located their depth on the spectrum, and heard the "loops not stockpiles" reframe. When you say "most products throw away their best signal" — they already feel the threat. A correction is proprietary training data nobody else has. If you don't capture it, you're burning your own moat

## Slide 9 — Data Flywheel Scoring
- Four loops: Correction, Preference, Domain Context, Network
- Score each 1-5. Weakest loop = where competitors attack first
- **Mental model:** Scoring forces specificity, but the loop set is theirs to adapt — their flywheel might have two loops or six; the framework isn't a fixed template.
- Why a scoring tool: abstract concepts don't change behavior, numbers do. Once they see a 1 or 2 staring back at them, the priority becomes obvious. This is the last thing before the break — it should leave them uncomfortable

## Slide 10 — Break
- 5 min. When they come back: all applied work. They'll map their flywheel, face an attacker, and build their escape plan

## Slide 11 — Map Your Data Flywheel
- 15 min individual — score four loops, write what they actually capture today
- "We plan to build this" is a 1, not a 3
- Why 15 min not 10: this is the core artifact. If they rush, they'll score generously and the peer challenge won't bite. Walk the room and push back — analytics ≠ preferences. Do they personalize model behavior? If not, it's a 1
- **🔧 Tool:** "Open the Flywheel Scorer — it gives you a visual flywheel, scores each loop, and flags the weakest one. It also pulls in your M1 vulnerability data if you saved it."

## Slide 12 — Encroachment Threat Assessment
- Three vectors: platform encroachment, vertical competitor, adjacent expansion
- Name the attacker, vector, time-to-threat, % of value at risk
- Why three vectors: most people only think about direct competitors. Platform and adjacent are the two that blindside you — and they're the ones that actually kill products

## Slide 13 — The 90-Day Encroachment Plan (Peer Challenge)
- 6 min per person. Defender presents flywheel + threats. Encroacher builds a concrete 90-day plan
- Weeks 1-4: what they ship. Weeks 5-8: how they poach users. Weeks 9-12: why users don't come back
- Target the weakest flywheel loop — that's the entry point
- Why this works: self-assessment is always generous. A partner's attack plan surfaces blind spots you can't see yourself. Week-by-week forces specificity — no hiding behind "eventually someone might"
- If too polite: "you're not being helpful by being nice. The market won't be nice"

## Slide 14 — The Kill Switch
- Three layers: abstraction (no direct provider calls), multi-model routing (tasks go by cost/quality/latency), eval harness (automated quality check)
- Ask: "How many of you could swap providers in 48 hours?" Almost nobody raises their hand
- Why this is the wow moment: most products are hard-wired to one provider. The Kill Switch turns dependency into optionality. 48 hours is deliberately aggressive — it should make them uncomfortable
- **Mental model:** Vendor portability looks different in every domain. Treat the 48-hour bar as a way to think about dependency and swap readiness, not a literal SLA.

## Slide 15 — Your Portability Audit
- 15 min build moment — audit vendor dependency
- Stress tests: provider doubles pricing, provider restricts your use case
- Walk out with three action items: this week, this month, this quarter
- Why concrete actions: the Kill Switch is useless without a plan. Push for specifics — not "build abstraction layer" but "abstract the embedding call in search by Friday." This checklist travels to M3 — portability affects costs
- **🔧 Tool:** "Open the Kill Switch Audit — it walks you through each dependency layer, stress-tests swap time, and gives you a concrete this-week / this-month / this-quarter action plan. Export it — you'll need it in M3."

## Slide 16 — Synthesis
- Fill in Component 2: flywheel scores, weakest loop, top threat, portability plan, swap readiness, three actions
- Why we formalize: the living strategy compounds across all six modules. If they skip Component 2, M3's cost model won't have the right inputs

## Slide 17 — Bridge to M3
- M3 is the economics reality check — inference costs are compressing margins from 80% to 40%
- Bring everything
- Why this bridge: two sessions on strategy and defensibility. M3 is the cold shower — does any of this make money?

## Slide 18 — Survey
- QR code / link
