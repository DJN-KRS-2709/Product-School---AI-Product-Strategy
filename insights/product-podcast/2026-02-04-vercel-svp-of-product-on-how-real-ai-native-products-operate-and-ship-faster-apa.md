---
title: "Vercel SVP of Product on How Real AI-Native Products Operate and Ship Faster | Aparna Sinha | E284"
guest: "Aparna Sinha"
date: "2026-02-04"
source: "buzzsprout"
episode_id: "18609045"
duration: "2294"
audio_url: "https://www.buzzsprout.com/90361/episodes/18609045-vercel-svp-of-product-on-how-real-ai-native-products-operate-and-ship-faster-aparna-sinha-e284.mp3"
---

# Vercel SVP of Product on How Real AI-Native Products Operate and Ship Faster | Aparna Sinha | E284

> In this episode, Carlos Gonzalez de Villaumbrosia, CEO &amp; Founder at Product School, interviews Aparna Sinha, SVP of Product at Vercel, the cloud platform recently valued at $9.3 billion following a $300 million Series F. Aparna joins us to discuss how Vercel is powering the next generation of AI-native applications.Drawing from her experience at Google Kubernetes and Pear VC, Aparna reveals how Vercel empowers Teams of One to ship faster than ever. She explores the cultural shif

## Transcript

Aparna Sinha | Vercel 00:00:00

There's a principle at Vercel: iterate to greatness. You take a step toward that today. If you have an idea, by the evening you should have something developed that is ready for testing. Products don't really die; they evolve and we iterate. This is why we prioritize smaller teams of even two to three people. With AI, fewer people can get more done. Product managers can create more than just working prototypes—they can build actual products and test them with users. Underlying this is our compute platform, which we call Fluid Compute. It is highly optimized for AI, ensuring you only pay for the compute when it is being used. Generally, pricing wisdom suggests pricing for value. You want to understand the value the customer receives and ensure your model reflects that.

### Introduction

Carlos González | Product School 00:00:59

Hey, this is Carlos, CEO at Product School and your host on The Product Podcast. Today’s guest is Aparna Sinha, SVP of Product at Vercel. Vercel is a cloud platform for building, deploying, and scaling web applications. The company recently hit a massive $9.3 billion valuation after raising $300 million in their Series F. Aparna is one of the top cloud executives, bringing ten years of experience leading cloud products at Google and three years as a partner at Pear VC, where she invested in the next generation of AI companies. Now, she is building the AI-native cloud at Vercel.

Carlos González | Product School 00:01:46

In this episode, we dive deep into her playbook for building AI-native teams that ship 10x faster. We discuss the philosophy of the "team of one," how AI enables individual builders to achieve the output of entire squads, and a new organizational design for maximum leverage. We also explore why shipping imperfect products early is the only viable strategy in a market changing weekly, and how to successfully balance cost recovery with value-based monetization in an AI-first world. Let's dive in.

### Main Conversation

Carlos González | Product School 00:02:11

Welcome to the podcast, Aparna.

Aparna Sinha | Vercel 00:02:12

Thank you, Carlos. Great to be here.

Carlos González | Product School 00:02:14

We need to start with the news of the week. Vercel announced a Series F: $300 million at a $9.3 billion valuation.

Aparna Sinha | Vercel 00:02:22

That's right. We're very fortunate and happy. Our lead investors reinvested, and we welcomed two new investors, GIC and Accel. Many of our institutional investors also joined the round. We're excited about the valuation, but it also means we have a lot of work to do to continue growing.

Carlos González | Product School 00:02:48

Vercel has built a massive reputation in a relatively short time. When was the company actually born?

Aparna Sinha | Vercel 00:02:55

The company is about ten years old. It started as a company called ZEIT. About five years ago, it rebranded to Vercel and became the premier developer experience for high-performing sites on the web. This year, right around the time I joined, we introduced the AI Cloud. We already had our v0 coding solution and the AI SDK, which is a popular open-source tool. The company really found its core product-market fit five years ago and has had an incredible growth journey since.

### Defining the AI-Native Cloud

Carlos González | Product School 00:03:41

With so many AI products hitting the market, how do you specifically position Vercel?

Aparna Sinha | Vercel 00:03:48

First and foremost, Vercel is a developer company focused on an excellent experience—fast, ergonomic, and highly performant. When you deploy on Vercel, you are on a globally available, secure, and reliable cloud. On top of that, we provide the ability to build AI-native applications. Whether it's a chatbot, a website with embedded AI, or autonomous agents helping customers, they all benefit from our globally aware infrastructure. We’ve created a set of primitives specifically for AI applications to make them more efficient and flexible.

Carlos González | Product School 00:05:29

Beyond the platform, you also have your own applications like V0.

Aparna Sinha | Vercel 00:05:35

Exactly. Our philosophy is to build things we know will be useful. We often build internally first to understand what capabilities are needed. That’s how the AI Cloud started; we were building agents for ourselves. V0 is an agentic application that empowers everyone to ship products. By using AI models to create applications from a mockup or a simple description, we drastically speed up the development process. This allows anyone—product managers or analysts—to create a prototype, get feedback, and iterate quickly before moving to production.

### Shipping in an Earthquake

Carlos González | Product School 00:07:10

Speed is the keyword in the AI world. You've mentioned that shipping fast is the primary differentiator for AI-native companies. How do you maintain that pace?

Aparna Sinha | Vercel 00:07:22

At Vercel, the mantra is "If it's fast, it's on Vercel." Building in AI right now feels like building during an earthquake; the ground is constantly shifting. New models come out every week, sometimes every day. To take advantage of that innovation without falling behind, you need a platform that lets you experiment and release with high quality and security.

Carlos González | Product School 00:08:45

You spent ten years at Google before this. How has your mindset as a product leader changed in this new environment?

Aparna Sinha | Vercel 00:08:58

I love early-stage products. Even at Google, I worked on Kubernetes when the team was only 30 people. There are many parallels because both Vercel and Kubernetes are rooted in open source. I prefer working with game-changer technologies that are still finding their exact business path. In this hyper-growth phase, you have to make fast calls and iterate constantly.

### The Team of One and Founder Mode

Carlos González | Product School 00:10:45

You mentioned that AI allows for much smaller teams. Can you elaborate on that?

Aparna Sinha | Vercel 00:10:55

AI has significantly increased engineering productivity. You no longer need a huge squad for prototyping. At Vercel, sometimes a "team" is just one person. We have a "mobile development team" that is literally one individual.

Carlos González | Product School 00:11:19

What are the essential skill sets for these tiny teams?

Aparna Sinha | Vercel 00:11:23

Skill sets are becoming more fungible. With AI tools, PMs can create working products, and engineers can handle design and product requirements. An ideal small team usually has two or three engineers and someone focused on the customer or business side—handling pricing, experimentation, and growth. We look for "founder mode" in our PMs; constraints actually help them because they have more agency and can move faster.

### Organizational Design for Flexibility

Carlos González | Product School 00:13:08

How do you structure the broader team as the SVP of Product?

Aparna Sinha | Vercel 00:13:16

I avoid rigid structures. In the early stages of a technical product, I align PMs closely with engineering. As a product matures, I introduce specialized roles: solution-focused PMs who stitch features together for customers, and horizontal teams for pricing, strategy, and growth. Growth PMs focus on self-serve cross-selling, while enterprise teams focus on sales collateral.

Carlos González | Product School 00:15:35

How do you balance these priorities across the platform and specific apps like V0?

Aparna Sinha | Vercel 00:15:52

V0 is essentially "Customer Zero" for our AI Cloud. We built primitives like the Gateway and the Sandbox because V0 needed them. The Gateway allows us to switch to the latest models instantly, and the Sandbox lets us execute AI-generated code safely. Our underlying Fluid Compute platform is also a differentiator; it's cost-effective because you only pay when the application is active. This is crucial for AI, where apps often spend time waiting for model reasoning or human feedback.

### Iterate to Greatness

Carlos González | Product School 00:20:33

Google was famous for launching many experiments, some of which ended up in a "cemetery." Does Vercel have a graveyard for products that don't make the cut?

Aparna Sinha | Vercel 00:20:58

We don't really "kill" products; they evolve. Our principle is "iterate to greatness." You might have a 10x ambitious goal, but you take a small step today. We have Demo Days every Friday where anyone can show what they’ve built. It’s not a contest—everyone is encouraged. We work in the open using public Slack channels. People provide organic feedback, and if a project is doing well, it graduates to a private beta or a full release.

Carlos González | Product School 00:26:54

As the leader, how do you decide where to allocate your own time?

Aparna Sinha | Vercel 00:27:10

I prioritize being responsive and staying at the forefront of the industry. We are in the middle of the AI revolution in San Francisco, constantly talking to startups and customers. Our founder, Guillermo Rauch, lives several years in the future, so we all try to live there too. We stay nimble; if a new innovation emerges, we lean into it immediately.

### Pricing for the AI Era

Carlos González | Product School 00:33:53

AI pricing is a challenge. Some companies give away too many credits, while others struggle with high costs. How do you handle this?

Aparna Sinha | Vercel 00:34:10

The goal is to price for value, not just cost-plus. However, because AI compute and token costs are high and variable, a hybrid model is best. Part of the metric should be value-aligned (like seats or specific outcomes), and part should be cost-aligned (like token consumption). This prevents "power users" from making the system unprofitable while still keeping the entry point accessible.

### Closing

Carlos González | Product School 00:36:47

Aparna, thank you for sharing these principles—from "founder mode" to "iterating to greatness." It's been a pleasure learning how an AI-native company actually ships.

Aparna Sinha | Vercel 00:37:05

Thanks for having me, Carlos.
