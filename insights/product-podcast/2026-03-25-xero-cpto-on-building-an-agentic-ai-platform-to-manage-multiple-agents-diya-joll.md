---
title: "Xero CPTO on Building an Agentic AI Platform to Manage Multiple Agents | Diya Jolly | E289"
guest: "Diya Jolly"
date: "2026-03-25"
source: "buzzsprout"
episode_id: "18899615"
duration: "2426"
audio_url: "https://www.buzzsprout.com/90361/episodes/18899615-xero-cpto-on-building-an-agentic-ai-platform-to-manage-multiple-agents-diya-jolly-e289.mp3"
---

# Xero CPTO on Building an Agentic AI Platform to Manage Multiple Agents | Diya Jolly | E289

> In this episode, Carlos Gonzalez de Villaumbrosia, CEO at Product School, sits down with Diya Jolly, CPTO at Xero, the global accounting platform trusted by over 4 million customers. Diya shares how Xero is redefining B2B software by building JAX, an agentic AI platform that intelligently manages specialized sub-agents to streamline business operations.What you&apos;ll learn:How Xero built an agentic AI platform that orchestrates multiple agents across payroll, pa

## Transcript

### Introduction

Diya Jolly | Xero 00:00:00

How you interact with SaaS will change in two ways. Instead of SaaS apps becoming a place where you take action, SaaS apps will move more and more to a place where you are either reviewing or getting insights. Number two, instead of clicking buttons all over the place, it's going to become a lot easier just to do things as you do in normal conversation.

Diya Jolly | Xero 00:00:21

Product management is about having customer empathy and understanding your customer and your domain deeply. If you try to hit too many different segments of customers that have different needs, your product is going to be a hodgepodge. One of the common things in pricing is you will usually start high on price and then you will bring it down because you know you can bring it down.

Diya Jolly | Xero 00:00:44

There's always an option to bring it down, but there's rarely an option to go up significantly.

Carlos Gonzalez de Villaumbrosia | Product School 00:00:49

One of my product advisors would say many years ago that it doesn't take a genius to reduce prices. The really hard thing is to raise them. So, you pretty much want to start higher and then give yourself the option.

Carlos Gonzalez de Villaumbrosia | Product School 00:01:01

Hey, this is Carlos, CEO at Product School and your host on the Product Podcast. Today's guest is Diya Jolly, Chief Product and Technology Officer at Xero. Xero is a leading accounting software serving over 4.5 million businesses across 180 countries. It has a market cap of approximately $9 billion and over 1.2 billion in annual revenue.

Carlos Gonzalez de Villaumbrosia | Product School 00:01:19

Diya has led both consumer and enterprise products, previously serving as the Head of Monetization at YouTube and CPO at Okta. In our conversation, we cover the key aspects involved in scaling complex platforms. First, bringing AI capabilities into non-AI native products without slamming AI on top of an existing UI.

Carlos Gonzalez de Villaumbrosia | Product School 00:01:36

Next, building a super agent that orchestrates specialized sub-agents who autonomously execute specific tasks. Then, finding the maximum price users are willing to pay for your product without sacrificing user delight. Also, introducing humans in the loop to ensure 100% precision and prevent LLM hallucinations.

Carlos Gonzalez de Villaumbrosia | Product School 00:01:53

And finally, enabling APIs to power a global platform while providing hyper-local flexibility across different markets. Let's get into it. Welcome to the Product Podcast.

Diya Jolly | Xero 00:02:03

Thank you for having me, Carlos. It's fantastic to be here.

Carlos Gonzalez de Villaumbrosia | Product School 00:02:07

I've been tracking you for a long time. We have hundreds of common connections on LinkedIn, so I'm glad that this is happening.

Diya Jolly | Xero 00:02:14

Yes, I'm excited to be here too. We have a lot of common friends.

### The Core Fundamentals of Product Management

Carlos Gonzalez de Villaumbrosia | Product School 00:02:18

I see that you were a product executive at YouTube—your latest role there was as Head of Monetization—then CPO at Okta, and now the Chief Product and Technology Officer at Xero. Let's start with some of the very different products. YouTube is a consumer-type of business. I can imagine Okta is more like large enterprise, and Xero is more in the SMB space. What are some of those core fundamentals that stay true across all three?

Diya Jolly | Xero 00:02:47

That's a great question. I think product management is really about having customer empathy and understanding your customer and your domain deeply. That remains true no matter where you are.

Diya Jolly | Xero 00:02:56

In YouTube, it was about understanding both the advertisers and the users. Understanding the users is easy because you yourself are a user. But understanding advertisers takes some work because you're not an advertiser. Same thing at Okta; you need to understand your customers deeply, whether it's a CSO or a CIO. And same thing at Xero. Basically, I think if you understand your customers deeply, that's one key tenet of product management.

Diya Jolly | Xero 00:03:17

The second key tenet is then being able to take that understanding and convert it into a vision for a product that is obviously technically feasible, but also something that adds value beyond what they could have imagined. Because they are not the technologists, they don't necessarily understand what technology can do and they are not looking at the product as a whole. So, you can probably find ways to give value to them—whether that's more time back, the ability to grow their business, or more revenue for them.

Diya Jolly | Xero 00:04:08

I would say the core tenet is: how do you understand your customers deeply? How do you understand the jobs that they need to get done, their goals, their daily workflows, and their challenges? Then, convert that into a software solution using your technical know-how and your ability to take pain points and convert them into a software process.

### Maintaining Customer Empathy at Scale

Carlos Gonzalez de Villaumbrosia | Product School 00:04:35

I would like to go deeper on that because when I hear you talk about understanding customers deeply, my mind goes to the fact that in a company like YouTube, I’m a huge user. I feel like I can do this better than if I were doing an accounting software product. Also, at scale, when you are at a large company with thousands of people, it's very easy for some executives to remove themselves from reality. How do you make sure that there is still a conduit for you to really understand and touch your users?

Diya Jolly | Xero 00:05:11

I think that's a fantastic question. In the consumer world, you yourself are a user of the product, so you have opinions and your friends are users. In consumer data, tons and tons of people use your product, so you can see where the drop-off is and what features they like. You can go fast, iterate, and launch a bunch of features to see if it works or doesn't work.

Diya Jolly | Xero 00:05:35

Consumer is very different. When you come into B2B, it's a bit of a different game, and enterprise is a bit different than standard B2B. At Xero, we're serving business owners. We're serving accountants and bookkeepers where we could actually go have a conversation. We have a sales team that talks to them, and we have advisory boards. We can ask them, "How are you using things? What do you like and what don't you like?"

Diya Jolly | Xero 00:06:15

You can actually go and spend time with them. I recently had my team spend a whole day with an accountant and bookkeeper, learning what they do and how they do it so that you can get empathy. When I first started in advertising, I actually went and worked for an advertiser for a week to understand their workflow and the business deeply.

Diya Jolly | Xero 00:06:33

When you are on the enterprise side, you have data in some cases, but you end up relying on conversations also to understand their daily lives. There's nothing more important than actually being able to stand in their shoes—whether it is working with them for a week or being a product person that does customer support for a week to understand where the pain points are.

Carlos Gonzalez de Villaumbrosia | Product School 00:07:24

I like that point about not using B2B as an excuse to say you're just going to rely on data because you're not the specific customer. It's really powerful to find ways to still use the product and connect with the people using it. It reminds me of a story of a CPO at Uber who made it mandatory for all of their PMs to be drivers for some time.

Diya Jolly | Xero 00:07:50

Exactly. You have to get close to the product and you have to use it. I have demo orgs I use all the time. Whenever somebody says there's a really cool startup doing something new, the first thing I do is go set myself up. We also talk to our customers through a small business advisory council and an accountant and bookkeeper council. You have to stay close to them and understand their world and pain points.

### One-Way vs. Two-Way Door Decisions

Carlos Gonzalez de Villaumbrosia | Product School 00:08:22

That leads me to the next point. I know you are big on making decisions with imperfect or incomplete data. Tell me more about that.

Diya Jolly | Xero 00:08:31

There are two types of decisions. One decision is where, if you make it, it is very hard to reverse. An example is deciding whether you want to price a new product at a certain price. If you price it too low, it's generally very hard to then go price it higher. With these "one-way doors," you want as much data as possible and you want to see if there are ways to keep optionality open. One common strategy in pricing is to start high and then bring it down if needed, because you know you can bring it down.

Diya Jolly | Xero 00:09:22

There's always an option to bring it down, but there's rarely an option to go up significantly.

Carlos Gonzalez de Villaumbrosia | Product School 00:09:28

One of my product advisors would say many years ago that it doesn't take a genius to reduce prices. The really hard thing is to raise them. So, you pretty much want to start higher and then give yourself the option.

Diya Jolly | Xero 00:09:38

Exactly. The other types of decisions are two-way door decisions, in which case you're actually better off experimenting and launching instead of sitting and debating. I'm a big fan of experiments. Where you can experiment, just do it and then course-correct. Most of the decisions you take on a daily basis—80% to 90% of them—are two-way doors if you structure the solution properly. You do iterative milestones where you experiment and get feedback.

Carlos Gonzalez de Villaumbrosia | Product School 00:10:14

You're referring to the famous two-way door leadership principle that Amazon coined. I think that's really powerful because a lot of the times, what seems like a final decision is really just a smaller step in one direction with the option to reverse or adjust.

Diya Jolly | Xero 00:10:35

Exactly. Product and tech should be developed iteratively. Any "big bang" has the risk of any one small step being wrong.

### Consensus vs. Conviction in Large Organizations

Carlos Gonzalez de Villaumbrosia | Product School 00:10:52

The challenge I see with this approach, especially in larger organizations, is that you get committees and too many other people involved. Where do you draw that line between consensus and conviction?

Diya Jolly | Xero 00:11:08

That is always a challenge in a big company. I think you have to decide for each initiative—each product or feature—who the eventual decision-makers are and how you will hold them accountable for making the right decision. Most companies are struggling with AI development today because it’s a horizontal that cuts across all product features. If you let every single person decide, you end up with tiny features boiled down to the lowest common denominator.

Diya Jolly | Xero 00:12:08

What we've done, as an example, is empowered a data science leader, an AI leader, a product leader, and an engineering leader to work across all different product areas. They talk to the customers and come back with an end-to-end workflow. Everyone has the option to give feedback, but at the end of the day, they make the decisions. Given how strategic this is, they run it by me, but eventually, it is their decision. We hold them accountable through metrics: did they drive adoption, utilization, and value?

Carlos Gonzalez de Villaumbrosia | Product School 00:13:11

I think that's an interesting dimension—how high-stakes something is determines if it requires escalation versus letting the team run with it.

Diya Jolly | Xero 00:13:19

Exactly. It comes down to clear ownership of who owns the decision and metrics to measure them by. Any one decision can be wrong, but if 60% of your decisions are wrong, then you have a problem.

Carlos Gonzalez de Villaumbrosia | Product School 00:13:33

Amazon expects a certain volume of decisions to not be right, but for the most part, leaders need to be right. It's not just about calling shots and expecting something will stick.

Diya Jolly | Xero 00:13:54

Yes, exactly.

### Organization Design and Platform Thinking

Carlos Gonzalez de Villaumbrosia | Product School 00:13:58

I'm very curious about your org design. How do you structure the team across these different functions?

Diya Jolly | Xero 00:14:05

I have it structured by function because I believe you have to have functional depth to build a craft. A stellar engineer is going to want to learn from a manager who is a stellar engineer. The virtual team that works on a given product includes PM, design, engineering, and analytics or ML. They form a dedicated pod across each product, aligned across functions with a common mission. You essentially create a mini "C-team" for each product.

Carlos Gonzalez de Villaumbrosia | Product School 00:15:09

One unique thing about your role is being Chief Product and Technology Officer. Traditionally, the CTO was a peer to the CPO. In practice, what does wearing both hats mean for the way you structure the team?

Diya Jolly | Xero 00:15:29

I still structure by function below me. I have two or three product leaders owning the top parts of the product. I have a design leader because I want someone to think about the product horizontally. And currently one engineering leader. I go between models depending on our needs. Right now, I have a singular engineering leader because we have to make a ton of trade-offs across platform changes to enable data to flow more seamlessly for AI.

Diya Jolly | Xero 00:16:25

However, if those changes were already in place, you could easily have a product leader paired with an engineering leader for specific segments. It just doesn't work for us right now. Currently, I have two key product leaders, one engineering leader, one design leader, one pricing leader, one AI leader, and one security leader.

Carlos Gonzalez de Villaumbrosia | Product School 00:16:58

I like how you're thinking about org design as a product, giving yourself the option to adjust. Your team is global, spanning New Zealand to Europe, and you have to deal with specific regulations in different countries. How do you build a product that is structured for core components but flexible across markets?

Diya Jolly | Xero 00:17:45

That requires platform thinking. First, you look at what pieces are common—like invoices. On the surface, an invoice looks the same everywhere, but the way sales tax is calculated or how payments are processed is different in every country.

Diya Jolly | Xero 00:18:36

However, the items entered or the name of a customer are common. You have to look at the product, build the common pieces together as a service, and then have regional specific efforts for the rest. You provide flexibility through a properly designed API surface across the common elements. This allows the "pay" button to connect to the right payment processor in that country. It's about designing common services with the right APIs and regional specific teams.

Carlos Gonzalez de Villaumbrosia | Product School 00:19:53

You call it basic because you've done it so much, but platform design and scaling are very hard.

Diya Jolly | Xero 00:20:01

I didn't mean to say it was simple; platform design by itself is very, very hard. Scaling product platforms is very, very hard.

Carlos Gonzalez de Villaumbrosia | Product School 00:20:11

I take it as a positive. You've been thinking about these problems long enough to see patterns that aren't obvious to others. What is the scale of the business in terms of customers and markets?

Diya Jolly | Xero 00:20:34

We have 4 million plus customers and we are global, serving most markets across the globe.

### AI Transformation and Accuracy

Carlos Gonzalez de Villaumbrosia | Product School 00:20:51

Let's talk about AI. In your industry, things need to be 100% accurate because it's a highly regulated environment. You have a moat due to scale, but smaller teams might move faster. How are you approaching AI advantageously?

Diya Jolly | Xero 00:21:28

The big advantage for us is that we have a fully functioning product. A startup has to build the ledger, invoicing, and payroll from scratch. We already have that feature set built. Second, in the world of AI, data is gold, and the more customers you have, the better your AI can be.

Diya Jolly | Xero 00:22:20

The challenge is accuracy. We handle this in two ways. One is through guardrails. If you want an LLM to tell you what your cash flow is, we put algorithms in place to ensure the answer is within specific bounds before it's surfaced. We ensure LLMs work within bounds and are not allowed to return crazy answers.

Diya Jolly | Xero 00:24:01

Second, where we automate something like bank reconciliation, we ensure there is a workflow for the accountant to review it. We make it easy for them to eyeball the matches and catch errors. The job of AI is not to replace your knowledge, but to speed up how you do work. Just like an engineer evaluates AI-written code for bugs, we automate while providing visibility to check if the automation is correct.

Carlos Gonzalez de Villaumbrosia | Product School 00:25:22

I resonate with that. How do you create these guardrails for users like bookkeepers so they don't give up on the AI experience?

Diya Jolly | Xero 00:26:02

You have to show the value. People worry if it actually helps them and if they have the control to correct things. We’re seeing that we save people about 22 hours a month in certain areas. You have to give them the control to make sure it's correct and allow them to quickly make adjustments.

### Orchestration and the Financial Super Agent

Carlos Gonzalez de Villaumbrosia | Product School 00:26:48

I want to talk about agents and the "super agent". How do you orchestrate this in a way that is manageable?

Diya Jolly | Xero 00:27:06

We believe you will need a super agent that can intelligently manage all these agents for you. We call our super agent JAX.

Diya Jolly | Xero 00:27:32

JAX essentially will manage your bank reconciliation agent, your payment agent, and your payroll agent. It will orchestrate the right actions across them and make sure that information is transferred so that they are not acting independently. It will also understand your preferences across the board. For example, if you like to do your bank reconciliation right after you've done your payroll, that is your general workflow. How do we ensure that is done every time in an automated fashion for you, versus the agents picking up their own cadences?

Diya Jolly | Xero 00:28:16

The second thing is that a lot of people are just slamming AI on top of their current UX experience. I talked about this a little bit, but with AI, the experience of SaaS is going to change. How you interact with SaaS will change in two ways. Instead of SaaS apps becoming a place where you take action, they will move more and more to a place where you are either reviewing or getting insights. How does the UI paradigm change for that? That’s number one.

Diya Jolly | Xero 00:28:52

Number two, instead of clicking buttons all over the place, it’s going to become a lot easier to do things as you do in normal conversation. For example: "Hey JAX, what's my cash flow?" In the past, you would have to click a bunch of buttons and look at a report to see your cash flow. Now, you can think about sending a text from your phone asking JAX for that information. You can connect with a SaaS app across multiple surfaces; it doesn’t have to be within the app. Even when you are connecting within the app, your interaction paradigm becomes more human.

Diya Jolly | Xero 00:29:33

When I ask JAX what my cash flow is, I'm interacting with it as a human being. If I asked you as my accountant for my cash flow, you would tell me the number, but you might also send me a slide with a presentation. JAX should be able to do the same. That is how we are thinking about a financial super agent that goes across the platform. Think of it as your junior employee that can help you run your business, both by providing insights and by automating the stuff you need to get done.

Carlos Gonzalez de Villaumbrosia | Product School 00:30:05

It also expands the type of customers who would want to use your product. I can ask questions in English without having to log in and mess something up. This moves beyond the world of static dashboards.

Diya Jolly | Xero 00:30:48

Exactly. It's moving from a system of record to systems that run independently with a more human interaction paradigm on top.

Carlos Gonzalez de Villaumbrosia | Product School 00:31:08

Data is one thing, but interpretation and action are what matter.

Diya Jolly | Xero 00:31:18

Exactly. We launched Financial Insights to put advisory in everyone's pocket. If a bakery owner wants to buy a delivery vehicle, they can ask JAX. JAX can look at historical data, see that volume might go down in summer, and suggest waiting until September or suggest leasing versus buying based on cash outlay.

Carlos Gonzalez de Villaumbrosia | Product School 00:32:39

So, the super agent becomes the new UI. What if the information lives outside your platform? How does it become a thinking partner?

Diya Jolly | Xero 00:33:07

An accounting system is the system of record for almost all business transactions. Sales from POS systems or Shopify flow in. We have a robust, open ecosystem where apps feed data into us. JAX is advantaged because we are your ERP, so we have more data across your entire business. We are also allowing other apps to connect into JAX so it becomes your one repository.

Diya Jolly | Xero 00:34:45

It goes both ways—people will want to interact with Xero data on other surfaces too. A lawyer might want to ask Xero in Microsoft Teams how much a client owes them without opening the app. We will allow other platforms like ChatGPT, Teams, or Gemini to query us as well.

Carlos Gonzalez de Villaumbrosia | Product School 00:35:47

That makes so much sense. I hope MCP servers help expedite that process.

### The Decision to Stick within the SMB Space

Carlos Gonzalez de Villaumbrosia | Product School 00:36:09

I just have one last area I want to explore with you, which is SMB. You've been in large enterprise and you've been in consumer. A lot of companies like to go up-market at some point. So why would you make the intentional decision to stick within SMB?

Diya Jolly | Xero 00:36:25

You mean why did Xero make that intentional decision? Look, I think the reality is there is so much value to add. I think the needs are very different in enterprise versus the needs of a small business. When people say small business, they define it very differently. For someone, an enterprise is like a $100 million company, and for others, a small business is a one-person shop.

Diya Jolly | Xero 00:36:56

What we do is serve customers anywhere from zero to 200 employees, but our sweet spot is one to 20 and one to 50. The reason is because there are so many problems to solve. You can't do everything for everyone. When you want to develop innovative, industry-leading products that add value, you really need to understand the needs of your customer set. If you try to hit too many different segments of customers that have different needs, your product is going to be a hodgepodge.

Diya Jolly | Xero 00:37:46

We feel like there's a whole global market of SMBs. They power the economy. There are so many problems we can solve for them, from accounting and tax to being able to get paid, paying people, payroll, and scheduling. The list could go on and on, and there’s a lot of opportunity there.

Carlos Gonzalez de Villaumbrosia | Product School 00:38:05

I'm with you. The founder of Gusto said the same thing—there is plenty of room to grow. But there is often a perception that you need to sell to the Fortune 500 or move up-market.

Diya Jolly | Xero 00:38:31

You can't build one product for the Fortune 500 and have it work for a small business. The small business customer is a hybrid of a consumer and a business user. They need the UI and concepts to be simple, but they also have all the functionality requirements of an enterprise.

Carlos Gonzalez de Villaumbrosia | Product School 00:39:25

Strategy is as important for defining what you are going to do as it is to define what not to do.

Diya Jolly | Xero 00:39:43

It's not good strategy to try to meet in the middle. The needs are different. We've decided to serve the need of our persona with multiple products.

### Closing Remarks

Carlos Gonzalez de Villaumbrosia | Product School 00:40:13

It's been a pleasure to have you here. Thank you so much for sharing how you're building.

Diya Jolly | Xero 00:40:17

Thank you so much. I appreciate it.
