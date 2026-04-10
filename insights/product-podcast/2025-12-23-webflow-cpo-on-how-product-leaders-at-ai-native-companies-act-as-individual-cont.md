---
title: "Webflow CPO on How Product Leaders at AI-Native Companies Act as Individual Contributors | Rachel Wolan | E281"
guest: "Rachel Wolan"
date: "2025-12-23"
source: "buzzsprout"
episode_id: "18397742"
duration: "2701"
audio_url: "https://www.buzzsprout.com/90361/episodes/18397742-webflow-cpo-on-how-product-leaders-at-ai-native-companies-act-as-individual-contributors-rachel-wolan-e281.mp3"
---

# Webflow CPO on How Product Leaders at AI-Native Companies Act as Individual Contributors | Rachel Wolan | E281

> In this episode, Carlos Gonzalez de Villaumbrosia speaks with Rachel Wolan, CPO at Webflow, the visual development platform valued at $4 billion that empowers over 3.5 million designers worldwide. Rachel discusses Webflow’s bold strategy to evolve into an AI-native experience platform with the launch of AppGen, a tool bridging the critical gap between AI prototyping and true production for enterprises like The New York Times and Spotify.What you&apos;ll learn:

## Transcript

Rachel Wolan | Webflow 00:00

AI-native means that you are using the toolkit available at that moment, and that is your product. If you don’t know that toolkit, you are not going to be able to lead and say, “Hey, this is where we need to place a bet.” The hardest thing to displace is how somebody behaves inside a company, and this platform shift is driving new behaviors. AI cannot be the only hammer in the toolkit, but you definitely need to understand it. Today, there’s a new toolkit. In this next wave, you’re really going to have to think about Answer Engine Optimization (AEO) as well as experimentation around new ways to get people into your brand and app. Webflow is an AI-native digital experience platform. I don't think we would have said that a year ago, but this past year has been an explosion for us in terms of what is possible.

### Introduction

Carlos González de Villaumbrosia | Product School 00:56

Hey everyone, it’s Carlos, CEO at Product School and your host on The Product Podcast. Today’s guest is Rachel Wolan, CPO at Webflow—the visual development platform valued at $4 billion that empowers over 3.5 million designers and teams worldwide. Webflow is the engine behind the digital front door for major enterprises like The New York Times, Dropbox, and Spotify. Webflow is currently executing a bold strategy to evolve from a website builder into a complete AI-native experience platform. They are redefining how products are built with the recent launch of AppGen, a tool that allows users to generate full-stack, on-brand web apps directly from prompts, bridging the critical gap between prototyping and true production.

Carlos González de Villaumbrosia | Product School 01:38

During our conversation, Rachel shares insights on the concept of the IC CPO (Individual Contributor Chief Product Officer) and why modern leaders must remain "patient zero" for their own tools. We discuss the shift from SEO to AEO (Answer Engine Optimization), why product managers now own this new distribution channel, and how she built her own Chief of Staff AI agents to automate research and give her team massive leverage. Let's dive in.

### Main Conversation

Carlos González de Villaumbrosia | Product School 02:05

Welcome to The Product Podcast, Rachel.

Rachel Wolan | Webflow 02:07

Thank you, Carlos. It's amazing to be here.

Carlos González de Villaumbrosia | Product School 02:10

I've been chasing you for months, so I'm glad we finally made it happen.

Rachel Wolan | Webflow 02:16

I am so glad we made this happen. I'm really grateful for the community you've built here. It's amazing to get to learn from you and your community as well as share a bit. So, thank you.

### The Rise of the IC CPO

Carlos González de Villaumbrosia | Product School 02:36

I appreciate it. One of the reasons I've been so interested in having you here is because you've been talking a lot about the concept of the IC CPO—Individual Contributor Chief Product Officer. You are the CPO at Webflow, and I would love for you to elaborate on what that really means today.

Rachel Wolan | Webflow 02:55

I love this question because I don't know that I've always been an IC CPO. I think it's really been in this era where I've been able to satisfy my curiosity, and that's really what it means. It doesn't mean you are doing all the work. I have an incredible team of builders talking to customers, designing our product, and answering questions through our data. But being an IC CPO means you can run down an answer quickly. I can ask, "How many visitors and signups did we get yesterday?" and go dissect it by segments to really understand the detail.

Rachel Wolan | Webflow 03:48

You have to think about it as a system where you need to be "patient zero." You are the one wrestling through answers, realizing, "Oh, I didn't get the answer I wanted," or "I'm missing this context." For example, I started using the Snowflake MCP (Model Context Protocol) about six months ago. As soon as these models came out, I wanted to build a Chief of Staff. I knew I wouldn't get budget for a human Chief of Staff, so I wanted to try building one using these models.

Rachel Wolan | Webflow 04:38

I realized there is a lot of context we need to build up to get credible answers from models. About a year ago, I asked the data science team, "Why can't we use these models right now to let anyone on the product team answer questions in natural language?" They told me the models couldn't spend enough time answering or lacked context. So, I asked, "What would it take?" You need a vision for how you want your AI org to operate and then work backward. In our case, we needed to use DBT to document our models, hire specific people, and acquire platforms to manage and certify questions. You start to unpack it when you put a vision out, but you also have to model it. Being an IC CPO is about modeling the work, having someone say, "That's not right," and then being curious about your own process to get to the answer yourself.

Carlos González de Villaumbrosia | Product School 06:13

Just to be clear, it's not that you don't have a team. You are the Chief Product Officer who also happens to be leading from the trenches and building with your own hands when necessary.

Rachel Wolan | Webflow 06:23

I have a team of 100 people. For me, the question is: can I turn that team of 100 into a team of 1,000 or 10,000 without actually expanding the headcount? That is one of the principles that comes with being AI-native.

### Defining AI-Native

Carlos González de Villaumbrosia | Product School 06:43

I see your LinkedIn headline says, "I'm building AI-native products and teams." What does that really mean for you?

Rachel Wolan | Webflow 06:54

An AI-native product starts from an AI experience. We all think of a prompt box as the quintessential AI experience—you put in natural language and get out something structured. Whether it is an answer in ChatGPT, an app built on AppGen, or an agent that runs a workflow completely agentically, AI-native means you are using the toolkit available at that moment from the model companies, and that is your product. That is fundamental to people getting value.

Carlos González de Villaumbrosia | Product School 08:06

I would add that you need to know that toolkit. Otherwise, how are people going to even know what the options are?

Rachel Wolan | Webflow 08:13

100%. If you don't know the toolkit because you aren't spending time experimenting with it, you won't be able to lead and place the right bets. For example, I went to the OpenAI Dev Day a couple of weeks ago. We were interested in what they would release around rich experiences inside their platform. They released an SDK, and the next day I said, "Okay, we need to start prototyping on this." You need to be in the weeds understanding the implications, have a North Star of where the world is going, and as new things come out, map them to your vision.

### Building an AI Chief of Staff

Carlos González de Villaumbrosia | Product School 11:14

I would love for you to showcase some of the specific AI use cases you've created for yourself to give you more leverage.

Rachel Wolan | Webflow 11:24

One of the first use cases I tried was building an agentic Chief of Staff. I failed at this ten times. Then, about a month and a half ago, when the new versions of Sonnet and Opus came out, something clicked. The models became very good at not getting lost on long tasks. At the same time, our DBT models were ready in our repo. I had cleared the path by accessing our model repo on GitHub and building out mini-apps.

Rachel Wolan | Webflow 13:49

I can show you a bit. I use Cursor as an IDE to build out a host of different agents. You generate an agent, describe it, select the model, and draft the task list so it doesn't get lost. I have an email triage terminal, an analytics terminal, a calendar terminal, and I've started connecting to our monorepo and Jira. For podcast prep, I have a "Podcast Prep Researcher" agent. I give it the topic, and it generates markdown files with research. It even calls a different agent—a YouTube transcriber—to process videos. It compiles everything into a readable format in my Chief of Staff app. What used to take hours now takes minutes in the background.

Carlos González de Villaumbrosia | Product School 18:02

I love that you showcased this live. As a podcast host, I can vouch for this. I save tons of hours on prep compared to when I had a producer doing this manually. I think I can get to 80% much faster.

### Prompt to Production

Carlos González de Villaumbrosia | Product School 18:37

This is a good segue to the value of a tool on top of a model. What is the value when you move beyond raw output?

Rachel Wolan | Webflow 19:15

The value most tools provide on top of a model is helping a customer go from that 80% to 100%. We call it "Prompt to Production." There are many amazing prototyping tools like Lovable, v0, and Bolt, but the gap from prototype to production is still wide. That is the market we live in.

Carlos González de Villaumbrosia | Product School 20:35

Let me add one thing. Webflow started as a product helping non-developers put something into production. I built my wedding website on Webflow. But in this AI era, the concept of putting something into production is different. How are you positioning the product now?

Rachel Wolan | Webflow 21:10

Webflow is an AI-native digital experience platform. A year ago, we would have called ourselves a website experience platform. Our mission has always been to bring developer superpowers to everyone. What has changed is the definition of "developer superpowers" and "everyone." Everybody is a developer now, and nobody is a developer.

Rachel Wolan | Webflow 23:47

Our customers are often large enterprises like The New York Times, Dropbox, and Spotify. Their website is the front door of their business. Recently, the website and the web app have become intertwined. We see a desire to move faster and build content for Answer Engine Optimization (AEO). Think of AEO as optimizing for ChatGPT—if someone asks, "What is the best enterprise CMS?", you want Webflow to show up. We are building products to help customers adapt to this new way people discover companies.

### The Strategy: Integrations and MCP

Carlos González de Villaumbrosia | Product School 29:22

I’m curious about integrations and specifically MCP (Model Context Protocol). How do you collaborate with other tools when you are not the only platform a client uses?

Rachel Wolan | Webflow 29:53

MCP has been amazing for us. We have so many developers, agencies, and freelancers building on our platform. By plugging into ecosystems through our MCP server—like Zapier or Cloudflare—we expose our APIs to be digestible by LLMs. Developers can use code-gen tools to interact with our platform. We get to see where people fail and provide more context. For example, customers use our MCP server for migrations, like moving from WordPress to Webflow. That’s not the fun part of building a website; if we can make that go away quickly, they can spend more budget on creative strategy.

Carlos González de Villaumbrosia | Product School 32:04

I never liked switching costs as a strategy—it keeps customers captive. AI-native companies have less legacy and can start from a clean slate. I see MCP as a way to put users on a "happy path."

### Defensibility and The Moat

Carlos González de Villaumbrosia | Product School 33:50

Eventually, features like MCP or prompting UIs will be commoditized. What is the real moat that helps you grow in enterprise?

Rachel Wolan | Webflow 34:22

The more you can align your business with the growth of your customer's business, the stickier you will be. Data is a weaker moat than before because migration is easier. However, the hardest thing to displace is behavior. This platform shift is driving new behaviors. The opportunity lies in those new workflows. I don't think AI will always unseat everything, but right now, it feels like everything is up for grabs.

### Mindset Shift for Product Managers

Carlos González de Villaumbrosia | Product School 36:01

What is the shift in mindset you are seeing from PMs to drive ROI for their clients in this new era?

Rachel Wolan | Webflow 36:19

There is a lot of teaching that has to happen, which means you have to be a "learn-it-all." You have to teach your customer, so you must learn faster than they do. It creates psychological safety when we are all trying things out together. In the past, a PM was expected to have the answer. Now, as a leader, I’ve learned I don’t have the answer, so I have to keep relearning.

### Distribution: From SEO to AEO

Carlos González de Villaumbrosia | Product School 37:34

Distribution is critical. As product becomes more strategic, how can teams be more ROI-focused regarding distribution?

Rachel Wolan | Webflow 38:09

All the distribution mechanisms we used to hold dear are changing. First, it was SEO and search. Then came mobile and the App Store. The third wave was social. In this next wave, you have to think about Answer Engine Optimization (AEO) and experimentation.

Rachel Wolan | Webflow 39:35

That’s why we focused on AppGen. I can generate apps that look just like my brand in a few prompts. I built a party planning app and a budget planner in minutes. Webflow is excellent at manifesting your Brand OS—your design system and CMS. We handle the hosting, security, and reliability. This allows you to pick the right platforms for distribution. Do you want to rank in ChatGPT or Gemini? There will be different ways that AI moats show up versus AEO.

Carlos González de Villaumbrosia | Product School 43:19

One key takeaway is that distribution is definitely a PM's responsibility now. It's not just about conversion; it's about tapping into new channels like AEO or creating independent app experiences.

Rachel Wolan | Webflow 44:05

That's exactly right. The more you can create experimentation mechanisms tightly coupled with your product experience, the more likely your product is to be successful. The customer pain hasn't changed, but the solution and discovery mechanisms have.

### Closing

Carlos González de Villaumbrosia | Product School 44:33

Rachel, it's been a pleasure to get a sneak peek into how you build from the trenches as an AI leader. Thank you so much for your time.

Rachel Wolan | Webflow 44:47

Thank you so much, Carlos. It was a wonderful conversation.
