---
title: "Walmart CPO on Scaling AI-Powered Localization Across Hundreds of Stores Worldwide | Tim Simmons | E285"
guest: "Tim Simmons"
date: "2026-02-18"
source: "buzzsprout"
episode_id: "18691272"
duration: "1685"
audio_url: "https://www.buzzsprout.com/90361/episodes/18691272-walmart-cpo-on-scaling-ai-powered-localization-across-hundreds-of-stores-worldwide-tim-simmons-e285.mp3"
---

# Walmart CPO on Scaling AI-Powered Localization Across Hundreds of Stores Worldwide | Tim Simmons | E285

> In this episode, Carlos Gonzalez de Villaumbrosia, Founder &amp; CEO at Product School, interviews Tim Simmons, Chief Product Officer at Walmart International, the retail giant serving 255 million customers weekly across 18 countries. Tim is leading a massive transformation to move from decentralized tech stacks to global platforms that empower local innovation.Tim explains why complexity is actually a competitive advantage when training AI. He dives deep into Agentic AI and the con

## Transcript

Tim Simmons | Walmart 00:00:00

I think it’s the new battle for who customers will really trust. Are they going to trust an LLM to basically be their shopper agent? Or are they going to trust Walmart? 71% of customers will tell you they lose trust in the experience—whether it’s a website or an app—if it’s not translated correctly. We’re translating intent, not just literal, word-for-word text.

We are doing this across 22 languages, translating millions of catalog items per month. Every single translation is done within 20 milliseconds. What I’m learning is that the more we can expose AI to our complexity, the smarter and more resilient it gets. That is actually starting to show up as a competitive advantage.

### Introduction

Carlos Gonzalez de Villaumbrosia | Product School 00:01:00

Hey everyone, it’s Carlos, CEO at Product School and your host on The Product Podcast. Today’s guest is Tim Simmons, Chief Product Officer at Walmart International. Walmart is the largest retailer in the world, with over $650 billion in annual revenue and over 255 million customers every single week. Tim manages a massive international portfolio across 18 countries outside the U.S.

What makes this episode essential for senior product leaders is how he’s executing a full-stack platform strategy and leveraging agentic AI to turn complexity into a competitive advantage. During our conversation, Tim shares the advanced frameworks driving that strategy: the "Orchestrator Strategy," how they build AI agents that automate user stories with an 88% acceptance rate from human PMs, and the ROI of AI—a look at their internal translation engine that cuts costs by 99%.

Carlos Gonzalez de Villaumbrosia | Product School 00:01:49

We also discuss the playbook for building one core platform that scales to 30 brands without losing critical hyperlocal nuance. Let’s dive in. Welcome to the Product Podcast, Tim. We’ve been trying to catch you for some time!

Tim Simmons | Walmart 00:01:58

Thank you, it’s great to be here. I’m thrilled to be a part of this.

Carlos Gonzalez de Villaumbrosia | Product School 00:02:05

One of our common friends and mentors recommended that we have you on. We tried to bring you for ProductCon New York, and I’m glad we’re finally here in San Francisco. You are the Chief Product Officer at Walmart International. What does "international" mean for Walmart?

### Defining Walmart International

Tim Simmons | Walmart 00:02:23

It’s a great question because it’s not commonly known that Walmart has such a broad global footprint. People think about Walmart U.S. and Sam’s Club, but the reality is that we have a robust portfolio of retail businesses globally. We work in seven markets consisting of about 18 countries.

We have over 30 banners or brands. For example, in Mexico, we have Walmart, which looks like a traditional Supercenter, but we also have the Bodega brand, which is a deep-discount brand. We have Sam’s Club Mexico, and in Central America, we have multiple different brands. We also have Flipkart and PhonePe in India. It’s a broad portfolio that spans many different retail models.

### Structuring for Global Scale

Carlos Gonzalez de Villaumbrosia | Product School 00:03:15

As you think about the different dimensions—countries, retail versus online, different brands—how do you put it all together?

Tim Simmons | Walmart 00:03:30

I’ve been in International for about a year and a half. Our CEO is Kath McLay; I worked with her previously at Sam’s Club when I was the CPO there. I knew very well what she expected, but when I joined International, she added one specific priority: build a global product organization and uplift the capability.

I structured the team so that I have product leaders for all seven markets. Any time we interact with a market, I interact directly with that leader. I also have central platform leads who focus on taking Walmart U.S. systems and adapting them into global platforms. We all meet once a week, and it creates a great dynamic: it brings the market voice to the center, and the markets stay appraised of everything happening with the core platforms.

### The Shift to Global Platforms

Carlos Gonzalez de Villaumbrosia | Product School 00:05:15

You mentioned platforms. There is baseline infrastructure that can be repurposed, but you also need flexibility for different brands. How do you balance that?

Tim Simmons | Walmart 00:05:30

We’re on a journey there. Previously, we had a very decentralized strategy where markets were building bespoke technology stacks. We learned that wasn't a great idea. If you spread investment over seven markets to build bespoke tools, that investment doesn't go very far. Our markets struggled to compete on technology.

Now, we are working toward global platforms where we build once at the center, largely leveraging the massive investment already made in Walmart U.S. technology. We are turning those into multi-tenant codebases. The goal is a future where markets are on sophisticated core platforms but retain the ability to innovate locally by building extensions. We’ve made a lot of progress in our largest markets, like Mexico and Canada, with high-priority platforms like e-commerce, marketplace, and supply chain.

### Complexity as a Competitive Advantage

Carlos Gonzalez de Villaumbrosia | Product School 00:08:05

Hyper-localization is key to staying relevant. I can only imagine the complexity behind the scenes. You’ve talked about complexity as a competitive advantage—could you elaborate on that?

Tim Simmons | Walmart 00:08:30

It’s hard to articulate the sheer scale. We service 255 million customers a week and have billions of items in our catalogs. Six months ago, I would have thought of this complexity as something that slowed us down. But with agentic AI, we’re learning something different.

You can build agent systems that actually get smarter because of the complexity. For example, there are different words for "t-shirt" in Spanish depending on whether you are in Mexico, Chile, or the U.S. Normally, a translation would get that wrong or slow you down. With agentic systems, you train them on these nuances as they arise so they don’t repeat the error. The more we expose AI to our complexity, the more resilient it becomes.

### The Orchestrator Strategy

Carlos Gonzalez de Villaumbrosia | Product School 00:11:25

How does this work in practice? Are you keeping humans in the loop?

Tim Simmons | Walmart 00:11:35

Absolutely. Everything we do today still has a human in the loop, but we’re being strategic about it. If you build task-based agents, it’s efficient, but if a PM has to interact with dozens of different agents for every small task, you haven't actually given them much freedom.

We are building "Orchestrators." Think of them like Project Manager agents that know how to take the output of one agent and feed it into the next, following an end-to-end workflow. They only alert the human product manager when an anomaly is detected or a decision is needed. This is proving to be incredibly effective because the orchestrator sees across the entire process and learns from what the human does at every phase.

### The AI-Powered Product Lifecycle

Carlos Gonzalez de Villaumbrosia | Product School 00:14:00

What are some specific use cases, and how are you measuring the value?

Tim Simmons | Walmart 00:14:15

We refer to this as the Product Development Lifecycle. We have about 10 agents—and growing—that orchestrate discovery, estimation, and user story writing. At Walmart’s scale, a PM usually manages multiple products at different stages.

The PM just has to kick the process off. They don’t need a massive prompt because these agents are already trained on our "Walmart Brain"—systems like Confluence and Jira. The PM provides a simple prompt about the feature, and the orchestrator takes over. Sometimes we are ready to hand off to developers within minutes.

Regarding success metrics, we look at adoption and accuracy. We have 3,100 product managers using our "PM Assist" agent. 88% of the time, the agent’s output is accepted on the first pass with no revisions. We’re seeing a 75% gain in efficiency.

### The ROI of Translation: 99% Cost Reduction

Carlos Gonzalez de Villaumbrosia | Product School 00:17:30

Translation seems like a massive external use case for you. How does that look from a value perspective?

Tim Simmons | Walmart 00:18:14

We were spending roughly $25 million a year on translations in International. We built the Walmart Translation Platform (WTP), which uses three layers of orchestration.

First, we have human cultural experts who write rules—not just fixing a word, but teaching the machine the context so it's smarter next time. Second, we have the models—neural machine translators for the first pass and LLMs for quality review. Third, we have the data pipes ensuring the right signals are fed back in.

We now translate millions of catalog items per month across 22 languages, and it’s costing us only 1% of the original cost. More importantly, it builds trust. 71% of customers lose trust if a site isn't translated correctly. This AI orchestration actually makes us feel more human because we are translating intent and meaning, not just words.

### The Future of Discovery and Search

Carlos Gonzalez de Villaumbrosia | Product School 00:24:30

E-commerce discovery is changing. We’re moving away from the traditional navigation bar. What are you seeing regarding the "time to value" for a customer?

Tim Simmons | Walmart 00:25:00

We have entire teams focused on this "battle for the search box." I think it’s actually a battle for trust. Will customers trust an LLM to be their shopper agent, or will they trust a brand like Walmart?

It’s early days, but we are looking at how to bridge the online experience with the in-store experience. We want to be hyper-personalized across both. We’re focusing on how to make the transition seamless so that the second you walk into a store, you pull out your app because you know it will provide an amazing, tailored experience.

### Closing

Carlos Gonzalez de Villaumbrosia | Product School 00:27:25

Tim, it’s been a pleasure to have you on the show. I admire that despite the scale of your team, you stay so close to the details.

Tim Simmons | Walmart 00:27:44

Thank you, I appreciate that. It’s been great to share what we’re learning. It’s so important that we share these insights as a community, especially with how fast things are moving.
