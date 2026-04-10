---
title: "Vercel V0 GM on Transforming Developer Workflows to Ship Faster | Zeb Hermann | E280"
guest: "Zeb Hermann"
date: "2025-12-10"
source: "buzzsprout"
episode_id: "18323592"
duration: "2794"
audio_url: "https://www.buzzsprout.com/90361/episodes/18323592-vercel-v0-gm-on-transforming-developer-workflows-to-ship-faster-zeb-hermann-e280.mp3"
---

# Vercel V0 GM on Transforming Developer Workflows to Ship Faster | Zeb Hermann | E280

> In this episode, Carlos Gonzalez de Villaumbrosia interviews Zeb Hermann, General Manager, v0 at Vercel, the AI cloud platform recently valued at $9.3 billion. Zeb oversees v0, which has grown to 3.5 million unique users by fundamentally changing how developers and PMs build software.Zeb dives into the operational shifts required to transform developer workflows and increase velocity. He explains why Vercel prioritizes a &quot;vetoe-based&quot; culture over approvals and how AI tool

## Transcript

Zeb Hermann | Vercel v0 00:00:00

I’m pretty out on 996. I think that concept is wrong because it focuses on hours spent in the office as opposed to the amount of impact you have and the work you deliver. The only thing I really care about is impact. So, the thing I had to fix was the structure. We needed very few leaders involved, more autonomy, and a team empowered to make decisions.

Carlos González | Product School 00:00:25

As we talk about vibe coding as a category, it’s exploding. As you know, there are new vibe coding or prototyping tools popping up like mushrooms. What’s crazy is that they are all raising money, and they’re all generating revenue.

Zeb Hermann | Vercel v0 00:00:37

I realized in one-on-ones, I was frequently having the same conversation with a bunch of different people. Why would I have the same conversation six separate times? As I think about leadership principles and the approach that works particularly well for v0, it’s really about solving that core problem for the team.

### Introduction

Carlos González | Product School 00:00:56

Hey, this is Carlos, CEO at Product School and your host on The Product Podcast. Today’s guest is Zeb Hermann, General Manager of v0 at Vercel, the leading AI cloud platform for building and deploying modern web applications. Since its founding in 2015, Vercel has become foundational to the modern web, powering millions of developers and serving brands like OpenAI, Anthropic, PayPal, Nike, and Walmart. In September 2025, the company raised $300 million in Series F funding at a $9.3 billion valuation.

Carlos González | Product School 00:01:40

Zeb leads v0, Vercel’s AI-powered prototyping tool with over 3.5 million unique users. v0 turns natural language prompts into production-ready interfaces, redefining how teams move from idea to code. In this episode, we dig into how AI prototyping is evolving into an end-to-end platform that lets product managers go from idea to deployment faster, how to empower PMs to deploy code without driving engineers crazy, what it takes for a product to graduate into its own business unit with a GM, and how to price AI products for sustainable growth in a market obsessed with free tokens. This episode is a masterclass in how AI-native product teams operate: fast, lean, and obsessed with impact. Let’s dive in.

### Main Conversation

Carlos González | Product School 00:02:12

Hey Zeb, welcome to the Product Podcast.

Zeb Hermann | Vercel v0 00:02:15

Thank you. I’m excited to be here.

Carlos González | Product School 00:02:17

I’m actually excited to be here because this is the Vercel office in San Francisco.

Zeb Hermann | Vercel v0 00:02:21

Yeah, we have a very small office, which will shortly be much bigger and better in about a month. But right now, the only reason we were able to get this room is that we sent three-quarters of the company to our big flagship conference. Otherwise, we’d be fighting for space.

Carlos González | Product School 00:02:36

I love it. There are so many things I want to talk about with you, but as the GM for v0, I first want to understand: what is the product you run, and how does it fit into the overall Vercel picture?

Zeb Hermann | Vercel v0 00:02:48

v0 is a vibe coding tool. I think that’s the easiest way to think about it. We see literally thousands of different use cases. The first use cases we saw were people creating components for UIs they were designing or very basic UIs, like a landing page or a single-page app.

Nowadays, people use it to build much more sophisticated projects. There are two broad categories. One category is students, folks with a startup idea, or people on their nights and weekends building interesting things that are experimental—like the first app they’ve ever created.

The other side, which is much more relevant here, includes product and design teams—especially at bigger companies—who are radically changing the way they build products. They’re using v0 or other vibe coding tools to help them prototype and express ideas for how their product will evolve with a working version, as opposed to a written document.

### Graduating to a Business Unit

Carlos González | Product School 00:03:52

v0 is one of the products that are part of Vercel. You are the GM for this product. I’m curious to know what it takes for a product to get that type of treatment and be considered a business unit, versus other products that are overseen by someone else.

Zeb Hermann | Vercel v0 00:04:11

We had many discussions about the right structure. We split v0 off into its own business unit about six months ago, and we did it for two reasons.

First, it has a different customer base and audience. When we look at the users of core Vercel, it’s engineers—especially web developers. When we look at the audience for v0, it’s PMs, designers, and founders who aren’t as technical—people who traditionally would be scared of using the Vercel CLI. We realized it’s a different audience, so we wanted a different sales team, different marketing, and a whole different motion around it.

The second reason is that Vercel is about 700 people now. We focus on moving quickly, but it’s hard to make decisions fast when you have 12 different leaders in the engineering organization weighing in. Guillermo [Rauch], the CEO of Vercel, and I thought speed was critically important for v0 to compete in such a crowded market. We wanted to optimize for speed rather than perfection of decision-making. So, we went with this General Manager structure where marketing, sales, engineering, and product all roll up independently for the v0 org.

Carlos González | Product School 00:05:47

So how do you collaborate and take advantage of the fact that you also have a platform?

Zeb Hermann | Vercel v0 00:05:54

It’s interesting figuring out the right way to do that. The way we talk about it internally is that we want v0 to be "customer zero" for Vercel. We’re an engineering-led organization with a big dogfooding ethos. When we realized v0 had a different audience, we saw it’s more of an app built on top of Vercel than a component of Vercel.

Because of that, we have this privileged opportunity. For instance, we dogfood our marketplace APIs. We’re built on top of the Vercel infrastructure for billing. For things like optimizing fluid compute, v0 has one of the largest workloads on Vercel with hundreds of thousands of users. We put a lot of strain on the fluid compute product as Vercel was building it. The relationship is basically customer-vendor, but because we’re inside the building, we can be a demanding customer that gives immediate product feedback to the teams shipping our compute, CDN, or billing systems.

### Speed as a Principle

Carlos González | Product School 00:07:14

One of the words you used is speed. San Francisco is packed with billboards that say "The website is fast. It’s on Vercel." You really double down on speed and velocity. I’m curious to know more about what that means for your principles.

Zeb Hermann | Vercel v0 00:07:37

This gets into how product development is evolving. Ten or fifteen years ago, the time it took to ship a fairly simple feature was often a quarter. Waterfall development is laughable now, but it was the standard not long ago.

On the speed side, our engineers can operate so quickly that the constraint is less about "Do we make the right decision?" and more about "How long does it take to make a decision?" Malte, our CTO, and Guillermo published content about empowering people to ship—removing an approvals-based culture and replacing it with a "vetoes-based" culture.

But even that vetoes-based culture was too slow for v0. What we’ve ended up with is an independent team where every engineer makes their own product decisions. We have two PMs, but most product decisions are made by the designer or engineer shipping the code. We automatically wire in customer feedback so they see the complaints or requests and make changes immediately. That system, which has almost no oversight or approval meetings, is designed to enable high-caliber engineers to ship as quickly as possible.

Carlos González | Product School 00:09:15

I want to double down on that. As a founder, I resonate with shipping fast and breaking things if necessary. But in this new AI-native paradigm where engineers and non-engineers can ship, how do you operationalize that at a scale of 700 people while maintaining guardrails?

Zeb Hermann | Vercel v0 00:09:52

It’s a hard problem. As we’ve gotten bigger, you sit in product review meetings with ten different executives—Aparna, myself, the CPO, the CTO—all chiming in. I can tell that’s not optimal. There are very few decisions where having the whole EPD leadership team weigh in is necessary.

We have been pushing towards clear, dedicated ownership—a bit more of the Amazon "Single Threaded Owner" model. They have an ethos that connectivity points between teams should be APIs, not documents and meetings.

For example, our relationship with the Next.js team: they build Next.js, and we ensure v0 is built using the most recent Canary version. We pass feedback back and forth, but they don’t need to ask permission for features. We use the technical incarnation of the product, not a written document, to collaborate.

### Dogfooding & AI Prototyping

Carlos González | Product School 00:11:29

Part of the advantage of your product is that it’s being used by your own team. You’re vibe coding things internally. How do you dogfood your own product so you are in a position to offer that to customers?

Zeb Hermann | Vercel v0 00:11:55

I’ll give a few examples. Juan Gabriel, the second PM ever on v0, joined a couple of months ago. He reached out with a cold email including a v0 link with about ten product enhancements we should make. One was mind-bogglingly obvious: simplifying the login page to show icons for sign-up options instead of text. Seeing a product person’s ideas not in a doc, but as a "vibe coded" working prototype with tooltips explaining the changes, was tremendously helpful.

We’ve adopted that ethos everywhere. We’re working on improving the Git sync flow—how you import from and sync back to GitHub. It’s complex. Instead of whiteboarding, Ari (our other PM) and Pablo (a designer) spent three hours prototyping the end-to-end experience in v0. They recorded a video of the prototype, which sparked a 90-message Slack thread where everyone could feel what the product would be like two weeks from now. That clarity allows us to ship the final version much faster.

Carlos González | Product School 00:14:37

What sounds crazy to me is that for a fairly big team, there are only two PMs.

Zeb Hermann | Vercel v0 00:14:43

Overall, Vercel is not a very PM-led company. When I joined, I think there were three PMs at the company. We found that product-minded engineers—especially ex-founders—can make 95% of product decisions. The velocity trade-off of having one person who sees feedback, makes decisions, and ships the product speeds up the team dramatically. We tend to hire or acquire these ex-founders and empower them, rather than having one PM for every four engineers.

### The "Full Stack" Team

Carlos González | Product School 00:16:01

Let’s talk about bottlenecks. Back in the day, teams were bottlenecked by engineering capacity. Now more people have access to the keys, but how do you handle handoffs?

Zeb Hermann | Vercel v0 00:16:15

In my perfect world, there are no handoffs. I push everyone on the team to submit their own PRs. We don’t have a single designer or PM who doesn’t actively contribute to the product.

If Pran, our designer, sees a flaw, the coordination cost of explaining it is wasted time. It’s faster for her to spend 15 minutes coding a better version and shipping the PR. We try to minimize the number of people involved and ensure the team consists of "full stack designers" and "full stack PMs" who contribute actual changes to the product.

Carlos González | Product School 00:17:11

I think that’s fascinating. Finding a designer who knew frontend used to be a unicorn. Now it feels like everyone needs to be a builder. Can you tell me more about that and the ideal pod size?

Zeb Hermann | Vercel v0 00:17:45

Ideally, competencies are a spectrum. Sahaj on our team—who built the open-source project shadcn that is widely beloved—had an amazing chart showing this. On one end you have design, on the other AI engineering. He highlighted his area: traditional frontend web dev, but with strong product sense and backend competence.

Five years ago, a designer who was also a frontend dev wasn’t common. Now, tools like v0 empower people like Pablo. He’s an incredible designer who basically taught himself to code using v0. He went from a non-technical designer to someone who makes front-end changes himself because the tools helped him deepen his technical knowledge.

### The Vibe Coding Moat

Carlos González | Product School 00:19:44

Vibe coding is exploding. New tools are popping up like mushrooms, all raising money. What is your moat?

Zeb Hermann | Vercel v0 00:20:01

We are about to enter the "trough of disillusionment" in the hype cycle. At one point, a different vibe coding startup got funded every day.

I see this market evolving like ride-sharing. You had Lyft, Uber, Sidecar, and many others. Now, it’s mostly just Uber. I think we’re at that stage for vibe coding. Right now, anyone can create a vibe coding tool using open-source templates. But in 18 months, there will be two or three real winners.

Our moat includes a few things:

Security: Being part of Vercel makes us much more secure, which matters to enterprise customers. Next.js Integration: Many competitors output "raw React" without server-side rendering, which makes the sites invisible to web crawlers and bad for SEO. v0 creates Next.js applications out of the box. Shadcn Integration: We are the best tool for outputting anything shadcn-related. Quality: We do head-to-head testing against Replit, Lovable, Bolt, etc. We pride ourselves on being first or second in quality. There is huge AI engineering work required to turn a basic template into a best-in-class tool. Carlos González | Product School 00:23:15

What is the criteria for "best in class"? Is it code quality or taste?

Zeb Hermann | Vercel v0 00:23:23

Taste is a huge piece. Theo, the streamer, recently ranked about 15 vibe coding tools, and v0 was the only one in the top tier. A lot of that is design—people want beautiful, delightful designs without purple gradients everywhere.

Then there is product quality: does the app actually run? One metric we measure is: of the code we try to run in the preview, what percentage crashes? Just having the code actually render is a major differentiator. So, it’s design quality plus functional product quality.

### From Prototype to Production

Carlos González | Product School 00:24:46

Common feedback is that these tools work well in demos but are hard to put into production. How are you thinking about expanding the product?

Zeb Hermann | Vercel v0 00:25:01

This is the number one feedback from enterprise customers. I gave a talk recently, and 95% of the audience said they had adopted prototyping in their product teams. The change happened in months. Now, they are struggling with the "prototype to production" gap.

PMs at eBay or Stripe prototype incredible experiences in v0, but getting that to production is often a full rebuild. We are betting that people will want to start from the actual code of their application. We think PMs, designers, and marketers want to open a specific repo in v0 and modify it there.

We are also excited about Design Systems. Customers like Mercado Libre have sophisticated component libraries. Competitors allow basic theming, but we are launching capabilities to take all your internal components and context, feed them to v0, and output design-correct code. This increases reusability dramatically.

Carlos González | Product School 00:27:55

This reminds me of AB testing tools like Optimizely, which allowed non-developers to tweak production sites. How do you view this convergence?

Zeb Hermann | Vercel v0 00:28:48

I’m not the biggest Optimizely fan. We refer to client-side overrides as "client-side slop." They often make applications up to twice as slow. In e-commerce, that latency costs hundreds of millions of dollars.

I think the future is broadening the universe of who is a developer. We want to move from 30 million developers to 50 million, and eventually 100 million. These people will be changing production code, not just applying client-side overrides. As they do that, they learn how applications actually work. I’m much more excited about broadening technical literacy than creating overrides that nuke performance.

### Pricing AI Products

Carlos González | Product School 00:30:20

Since you are the GM for v0, I want to talk about pricing. How do you price your product given the unclear usage costs of AI?

Zeb Hermann | Vercel v0 00:30:35

Pricing is very hard for two reasons.

First, frontier model costs are high. At Vercel, a single engineer using the Opus model for agents spent over $60,000 in one month. Your pricing model must be aware of that. We charge a seat fee for the product differentiation, which comes with included usage. Then we charge for usage on top of that—basically selling tokens at cost.

Second, there is a lot of venture funding in the space, so someone is always giving it away for free. Cursor had to roll back generous policies because they were selling tokens at a loss. You can’t build a sustainable business that way. Startups with $20M in funding might give tokens away to get users, which puts pressure on us. But we believe people will pay for higher quality, consistency, and security.

Carlos González | Product School 00:34:05

Would you consider the Amazon strategy—taking a loss to drive other business?

Zeb Hermann | Vercel v0 00:34:15

I admire Amazon, but I don’t want to emulate anti-competitive pricing. I prefer to put pressure on my team to build a product so excellent that people are willing to pay for it. I see it with our users; we have hundreds of thousands of users despite not being the free option, because the value is there.

Carlos González | Product School 00:35:55

How do you prevent bill shock, like the engineer who spent $60k?

Zeb Hermann | Vercel v0 00:36:10

In v0, you pay in advance for credits, not in arrears. You buy a top-up when you hit a limit. This prevents the "runaway bill" scenario common in serverless computing where you get a $1,200 bill because of a misconfiguration or a bot attack. With AI tokens, if a customer spends $1,000, it’s usually because they built sophisticated applications, so the value is there, unlike paying for bandwidth from a DDoS attack.

### Leadership & Culture

Carlos González | Product School 00:38:13

I want to switch gears to leadership. How many direct reports do you have?

Zeb Hermann | Vercel v0 00:38:20

I have about nine direct reports. The team is around 50 people: 18 on enterprise GTM/evangelism and about 30 in engineering, product, and design.

My leadership style is focused on speed. When I took over, the team was frustrated by meetings with too many leaders. I fixed that by establishing a structure with fewer leaders involved and more autonomy. We know that even if the team is wrong 15% of the time, if they ship twice as fast, it works out better in aggregate.

Carlos González | Product School 00:40:17

I know we aren’t fans of one-on-one meetings. What is your rationale?

Zeb Hermann | Vercel v0 00:40:25

I was taught the "manager handbook" style of weekly one-on-ones, but I noticed leaders like Doug Leone or Guillermo Rauch don’t do them. I realized I was having the same conversation with six different people. Why not have one meeting or a Slack huddle with everyone?

I spend time with people based on need. When Juan joined, I spent huge amounts of time with him. Now that he’s up to speed, I spend time with the pod working on a specific project. Let’s have a meeting to solve an issue, not a meeting about our feelings.

Carlos González | Product School 00:41:59

If I zoomed into your calendar, what would I see?

Zeb Hermann | Vercel v0 00:42:05

I try to keep my calendar as free as possible—ideally, three hours or less scheduled per day. The rest is for unplanned meetings, Slack huddles, or customer issues.

I spend a lot of time with data experts. Spending 30 minutes a few times a week with Christie (Analytics) or Kate (Finance) to drill into trends is incredibly valuable.

Carlos González | Product School 00:43:37

How about recruiting?

Zeb Hermann | Vercel v0 00:43:40

It’s up and down. Before I hired Rahul to run engineering, recruiting was 50-60% of my time. Now that I have functional leaders, it’s closer to 10%—mostly final "sell" calls.

Carlos González | Product School 00:44:40

In Silicon Valley, there is a lot of talk about the 996 culture. What is the expectation at a fast-growing company like yours?

Zeb Hermann | Vercel v0 00:44:55

I’m out on 996. It focuses on hours rather than impact. I only care about impact.

When I hire someone, I say: "In your first week, ship something. In your first month, deliver tens of thousands in business impact. In your first year, deliver millions." The people with the most impact do work a lot—I start at 7:00 AM and often work nights—but I want that to come from excitement about the work, not a requirement to sit in a chair for 12 hours. I’ve seen banking cultures where people sit around doing nothing just to be seen. I would hate for that to be our culture.

### Closing

Carlos González | Product School 00:46:00

Zeb, I loved spending this time with you and learning from you. Thank you so much for your time.

Zeb Hermann | Vercel v0 00:46:10

Awesome. Thank you, Carlos.
