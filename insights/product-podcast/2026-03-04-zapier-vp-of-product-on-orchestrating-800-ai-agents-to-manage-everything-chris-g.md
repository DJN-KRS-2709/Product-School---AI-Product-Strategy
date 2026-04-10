---
title: "Zapier VP of Product on Orchestrating 800+ AI Agents to Manage Everything | Chris Geoghegan | E286"
guest: "Chris Geoghegan"
date: "2026-03-04"
source: "buzzsprout"
episode_id: "18780300"
duration: "2000"
audio_url: "https://www.buzzsprout.com/90361/episodes/18780300-zapier-vp-of-product-on-orchestrating-800-ai-agents-to-manage-everything-chris-geoghegan-e286.mp3"
---

# Zapier VP of Product on Orchestrating 800+ AI Agents to Manage Everything | Chris Geoghegan | E286

> In this episode, Carlos Gonzalez de Villaumbrosia interviews Chris Geoghegan, VP of Product at Zapier. As the company’s first-ever Product Manager, Chris has spent nearly a decade scaling Zapier into a $5 billion automation giant that serves over 3.4 million businesses and 69% of the Fortune 1000.Zapier is not just building AI tools; they are powering their entire company with them. Chris reveals that his team currently runs over 800 active AI agents internally to manage everything

## Transcript

Chris Geoghegan | Zapier 00:00:00

What does it mean to do that collectively across all of your agents that you're hiring? We have a new workforce, essentially, of agents who are doing work on our behalf that we're hiring to do this job. Orchestration is how all those pieces work together. We have about 800 of these agents at Zapier that are doing work on our behalf—triggering on different schedules or events that are happening in the real world, going and doing the work, and coming back and saying, "Hey, I did this work. What do you think?"

Chris Geoghegan | Zapier 00:00:26

One of the very first things we did was call a "Code Red." I mentioned that a little bit earlier, but I think it's important to do something that says, "Hey, we are in a moment, and this moment is not like any other moment, and we need to do something about it." Who is doing it? What is the data, and where are they sending it? Do we have the right policies? Are those policies enforced? And then, can I see that those policies are enforced?

### Introduction

Carlos González de Villaumbrosia | Product School 00:00:52

Hey, this is Carlos, CEO at Product School and your host on the Product Podcast. Today's guest is Chris Geoghegan, VP of Product at Zapier, the automation platform that has become the connective tissue for over 3.4 million businesses, ranging from early-stage startups to 69% of the Fortune 1000. Zapier allows anyone to connect over 7,000 different applications to automate complex workflows. Without writing a single line of code, they have scaled into a $5 billion valuation with over 400 million in ARR, all while remaining profitable since 2014.

During our conversation, we explore how they are orchestrating over 800 AI agents internally to manage everything from complex product demos to engineering triage, giving their team unprecedented leverage. We discuss how product managers can shift their mindset from designing rigid UI flows to probabilistic AI outcomes and how to build a moat to not die when LLMs like ChatGPT or Claude release a competitive feature. Let's dive in. Welcome to the Product Podcast, Chris.

Chris Geoghegan | Zapier 00:01:47

Awesome. Thanks for having me, Carlos.

### The Early Days at Zapier

Carlos González de Villaumbrosia | Product School 00:01:49

Chris, as a fun fact, I’ve been using Zapier for many, many years—way before AI was cool. It was funny when I realized that you've been there for almost 10 years and you were the first-ever PM there, right?

Chris Geoghegan | Zapier 00:02:01

Yeah, it's been quite a journey. I joined when the founders were leading the product. Mike Knoop, one of the founders, hired me and said, "Hey, what's the first feature you want to build?" The very first thing I worked on as a PM at Zapier was Zapier for Teams. Up until that point, it had just been a solo player product. So that was my first project.

Carlos González de Villaumbrosia | Product School 00:02:26

It's always so hard for a founder, especially a product-minded founder, to hire a PM and delegate the "baby" a little bit. How were you able to help with that transition while still creating space for the founder to influence the vision?

Chris Geoghegan | Zapier 00:02:40

Even now, the whole way along, the company strategy and the product strategy go hand in hand. There's no separating the two when you're a software company. I think the main thing has been that Mike did a really awesome thing when he hired me. He said, "Just go listen. Listen to our team, go listen to our customers, hear what they're telling you, and then come back and tell me what you want to work on." That was how that first project came about—just deeply understanding who our customers are. I think when founders see other people caring as much about their customers and the business as they do, then it's possible to trust and hand over the reins a little bit.

Carlos González de Villaumbrosia | Product School 00:03:25

That's the dream case scenario. The reality is that it's almost impossible to find someone who actually cares as much, but also has the ability to push back and create a space for founders to have a voice while still taking the lead on what's important. I'm glad that you definitely proved that right. It's been almost 10 years and you're now the VP of Product.

Chris Geoghegan | Zapier 00:03:47

It has been a fun journey and I deeply appreciate the founders trusting me along the way.

### The Evolution of Workflows

Carlos González de Villaumbrosia | Product School 00:03:52

So let's talk about the current times and the future. We are in the AI era. When Zapier started, it wasn't even in the AI era. It started as this key tool to connect other tools and automate workflows. It would be good to set the tone and explain more about the expansion of your product, as there are now more and more capabilities available.

Chris Geoghegan | Zapier 00:04:14

Maybe it's helpful to do a very brief history. When Zapier first started out, it wasn't even a workflow product. It was the ability to connect a trigger to an action. That's all there was. What we saw was that customers were actually going out of their way to figure out how to build more complex workflows. So the company had to evolve. At that point, around 2016, we became a workflow company. We evolved the product to support those needs.

There were a few moments along the way where that had to happen again. We realized people were building complete software solutions on Zapier. When we looked at it, they were bending the will of software to suit their needs using Google Sheets as a database, for example. We all know Google Sheets is not a database, but folks were using it that way. We leaned into that and asked, "How do we help people who are already using Zapier to create complete software solutions? What are the missing pieces we need to add?"

So we added Zapier Tables and Zapier Interfaces so that people had the missing components—not just the business logic (which Zaps are), but also the backend storage layer and the frontend experience of interfaces and forms. Fast forward a little more to the AI era, and a few years back GPT-3 comes out and we had to call a "Code Red." We saw what was happening and realized this was going to change the landscape of how software is built. Since we enable people to build software without writing code, and AI also enables people to build software without writing code, we leaned into that and asked how we were going to reinvent our business to support people in this new paradigm.

Carlos González de Villaumbrosia | Product School 00:06:34

It’s such a privilege to have passionate users who hack your product in ways you couldn't expect. That informs how to better productize those use cases. As I hear you talk about the evolution of workflows, we now hear the term "agentic workflows." Maybe it’s good to clarify: what does that really mean? What is the difference between a workflow and an agentic workflow?

Chris Geoghegan | Zapier 00:07:00

Great question. I think the lines are blurring. When we talk about agents, we talk about a few things: the ability to have access to knowledge, the ability to take action on your behalf, and the ability to reason—to loop through a problem towards an outcome until you've actually solved for it. An agent, in our internal definition, is one capable of doing all of those things. Whereas a workflow is a trigger followed by a filter, followed by an action, followed by some branching logic. It happens the same way every time. An agent is able to change course depending on what information it gets at that current step.

Carlos González de Villaumbrosia | Product School 00:07:45

In my opinion, not every workflow needs to be an agent workflow. There are still many valid use cases where the output should be deterministic. That takes me to the next phase: we're hearing the word "orchestration" a lot as an evolution of agent terminology. What does that really mean as you tackle business problems for the user and not just the automation of a workflow?

### Hiring AI: Orchestration and Specialized Agents

Chris Geoghegan | Zapier 00:08:16

The best analogy I have for this is thinking about hiring AI like it's an employee. You have to think about how you would hire any employee: you have to onboard them, give them knowledge and context to do their job, and assign them a really good job description. Orchestration is the collective. What does it mean to do that collectively across all of the agents you're hiring? We have a new workforce of agents doing work on our behalf. Orchestration is how those pieces work together and how they are connected. A big part of orchestration is how those pieces are connected to your data and the tools you use every day for work. If agents are just in a chat window, that limits what they can do. How do you think about connecting your agents into triggers and actions that allow them to work on your behalf even when you're away from the keyboard?

Carlos González de Villaumbrosia | Product School 00:09:16

This is becoming more relevant as enterprises realize it's more powerful to have a variety of highly specialized agents versus a generic one. You truly need to orchestrate a bigger number of agents.

Chris Geoghegan | Zapier 00:09:31

Every time you make a call to an agent, you're rehiring them again for the very first time. Agents don't have memory; they're like a brand new baby or a goldfish in a tank. They've forgotten everything you told them last time. Even context is fed through the agent every single time. When you're thinking about orchestration, you're also thinking about context engineering—making sure the agent has access to all the context it needs to make good decisions and the tools to take action.

Carlos González de Villaumbrosia | Product School 00:10:13

The connection between those agents can be done in different ways. I want to talk about the evolution of the API and how MCPs (Model Context Protocol) are helping. What's the difference between an API and an MCP?

Chris Geoghegan | Zapier 00:10:29

With an API, you can give an agent documentation and say, "Go query this app for data or take this action." It can write software to go and use that API. An MCP is a little different; it’s a standard way to define access to all the tools you have available. Those tools could be API calls or pieces of code. The key thing is there's a description that defines how and when the tool should be used, so an agent isn't necessarily writing an API call from scratch every time. It knows it needs to use a specific tool and the set of inputs that make it work.

### Building a Competitive Moat

Carlos González de Villaumbrosia | Product School 00:11:29

I want to address a couple of big elephants in the room. You've heard that every time OpenAI has a Dev Day, a thousand startups die. They recently announced a product that helps create chat agents or automate workflows. As the expert, what is your take on how that is impacting your position? How do you think about it as a partner versus a potential competitor?

Chris Geoghegan | Zapier 00:11:57

You're talking about the Agent Kit they released. We were definitely checking it out, and there were things on X saying, "Oh, this is the Zapier killer." Turns out, I don't think it is. What they've done is what a lot of agent builders are already doing: realizing that if we break the job down for an agent into discrete steps, it becomes more proficient or accurate. They've added a level of determinism to how you build an agent. But compared side-by-side with Zapier, there are many pieces missing. They don't have the whole trigger infrastructure; the agents are still triggered based on chats. They don't have the same level of integration with API calls that a tool like Zapier has.

Carlos González de Villaumbrosia | Product School 00:13:03

I'm seeing a movie play out across different categories—like AI prototyping products that are all raising capital. We are seeing that now with integration products. You guys have been around for a long time, but more competitors are popping up. How do you create a moat that helps you protect and grow your business?

Chris Geoghegan | Zapier 00:13:38

Generally speaking, our moat over the last decade has been the vast number of integrations we have. We are the most connected platform, whether you're connecting AI or doing automation. We're also the easiest to use. That's a recurring loop: the easier we are, the more users come; the more users come, the more partners want to build on our platform. Going forward, we've thought about our future competitive differentiation. The thing we're leaning into is that we have the most use cases for automation and AI on our platform. One of the biggest bottlenecks for enterprises or users is: "What do I automate? What is the next use case that will transform my business?" We have that data. We know what is actually shaping that, and that's a big part of what we're leaning into next.

### AI Transformation in the Enterprise

Carlos González de Villaumbrosia | Product School 00:15:01

That leads to the next elephant in the room: moving upmarket and tackling enterprise clients. I imagine when Zapier started, the ICP wasn't always a Fortune 500. Now, users are not just engineers or marketers; it's basically everyone. What is the motion for you as you evolve from a PLG product into one serving the enterprise?

Chris Geoghegan | Zapier 00:15:40

Up until a few years ago, we didn't actually have a sales team. Zapier was fully product-led growth and self-serve. But that didn't mean we didn't have enterprise customers; many had grown up using Zapier or had innovation-forward pockets of people. As we think about moving upmarket, a big part of that is attaching a sales function. You're trying to figure out how to engineer value for an organization. Self-serve is good for individual needs, but with enterprise, you're trying to understand at the highest level what is slowing the organization down and how automation can transform it. It becomes not just what the product can do, but what are the cultural and leadership changes and the org-wide tools needed to enact that change? How can Zapier help support that? That’s been the biggest mindset shift—engineering value at an org-wide level.

Carlos González de Villaumbrosia | Product School 00:17:36

I’m going to pick on that word "engineering." We see Palantir pioneering the role of the forward-deployed engineer—not just selling the product, but embedding a team to help the client implement use cases. How are you ensuring people are getting the right value so they don't think of it as just another tool that not enough people are using?

Chris Geoghegan | Zapier 00:18:18

One of our core beliefs is that the people closest to the problem should be engineering the solution, even if they're not an engineer. If you have a problem with your onboarding flow, in the old world you might hire the IT team. In this new world, there are tools that give HR leaders a whole new set of capabilities. When we go into an organization, we try to figure out how to help the people closest to the problem use the technology rather than thinking about all the traditional handoffs. You actually have the tools in your hands to solve that problem for yourself. That's why ease of use is so important—it reduces the number of handoffs.

Carlos González de Villaumbrosia | Product School 00:19:29

In our own world, the keyword is often not "training" but "transformation." When you talk to executives, they use that term to cover everything. How are you able to connect the value you create with specific business outcomes beyond just the number of workflows created?

Chris Geoghegan | Zapier 00:20:05

Adoption and transformation are buzzy words. Adoption is: "How do I use these new tools to do what I was already doing, just more efficiently?" Transformation is: "How can I do something that I've never done before that would change the way we work?" It’s not changing an existing process; it's doing something you couldn't even do before. AI and automation help us do this. There are business ideas that exist because of Zapier that just would not be fundable businesses if they couldn't automate a large portion of it.

Carlos González de Villaumbrosia | Product School 00:21:13

I love that insight. If you can break "transformation" down into steps—first automating existing workflows, and then thinking about what can be done now that couldn't be done before.

### The AI Team Paradigm

Chris Geoghegan | Zapier 00:21:44

If it's helpful, one thing that could be interesting is: how is AI transforming the way that product teams should work? You've got engineering, product, and design working the same way for the last 10 years. How is AI transforming how we get work done?

Carlos González de Villaumbrosia | Product School 00:22:11

I’m listening.

Chris Geoghegan | Zapier 00:22:13

Think about this analogy: if AI is a teammate, how are you onboarding them? The first thing is the context you need to give AI. When you use AI—like the last time you went into Claude or ChatGPT—what were you actually doing?

Carlos González de Villaumbrosia | Product School 00:22:42

Is that a question for me? Well, very timely, because as I was researching you for this conversation, I basically have a GPT that helps me get intel on my guests and put it together in a format that saves me time.

Chris Geoghegan | Zapier 00:23:01

That's a super cool example. I imagine that GPT has some core instructions that are the same every time, maybe templates for results, and then you're giving it context about me—name, role, title. You've context-engineered an agent that is doing a job for you. You've onboarded them. Now, you did that as an individual. What if that job was a team sport? What if the whole engineering team, the PM, and the designer worked in the same space, building that context together rather than in silos? That feels transformative.

Carlos González de Villaumbrosia | Product School 00:23:54

Totally. Those agents live across different applications. How does that manifest in your team in terms of the number of agents and the tools you use to make sure they are set up for success?

Chris Geoghegan | Zapier 00:24:23

At Zapier, our team has about 800 different agents running at any given time. But that leads to the second point: if you have to go into ChatGPT to fire it off every time, it's not working on your behalf. What if that agent was connected to your calendar, knew you had this recording with me, and automatically kicked off? Now it feels like an employee with agency. These 800 agents at Zapier trigger on schedules or real-world events, go and do the work, and then come back and say, "Hey, I did this. What do you think?"

Carlos González de Villaumbrosia | Product School 00:25:13

The training iteration there is much faster, too. Probably the first time you set it up, they don't have all the right context, but there are easier ways to train them with new information.

Chris Geoghegan | Zapier 00:25:43

And if you're the only one generating feedback, it gets better slowly. But if anyone in the organization can see the output and improve the agent, that agent is shared, version-controlled, and updated by the whole team.

Carlos González de Villaumbrosia | Product School 00:26:03

I'd love to hear some examples of agents working for your product team.

Chris Geoghegan | Zapier 00:26:11

I’ll share some personal examples. One goes off every day at 8:00 AM, looks at my calendar, and iterates through each event. It uses Glean to understand what documents I should read ahead of time. If it's someone external like you, Carlos, it does research and gives me a brief. Another example: leading up to September, we were working on a relaunch of our Copilot product. Copilot builds Zaps, tables, and interfaces based on text. We wanted to coordinate weekly updates, so we "hired" an agent to look at our weekly demos channel, find relevant demos, look at the transcripts, and write a summary saying, "Hey team, this is what got shipped this week."

Carlos González de Villaumbrosia | Product School 00:27:37

I love that you use the term "we hired an agent" instead of "we created an agent."

Chris Geoghegan | Zapier 00:27:42

I think that's a really good paradigm. When you think about onboarding someone, what information do they need and do they have the software tools to get it done? The prompt is the onboarding, and the tools are the actions available to it.

### Governance, Leadership, and the "Code Red"

Carlos González de Villaumbrosia | Product School 00:28:04

It must be crazy to see behind the scenes at a company like yours. Taking the conversation back to enterprise, one challenge for them is being constrained to certain suites of tools or being worried about data security. That's usually why startups can't penetrate those accounts. How are you proving your product is not just better, but safer?

Chris Geoghegan | Zapier 00:28:55

This is top of mind. What IT and security care about is: who is sending what data where? If your product can answer those questions clearly, that's observability. If your product can put controls in place, that's access control. If you have those two pieces, that’s ultimately what people are looking for with AI governance. "Do we have the right policies? Are they enforced? And can I see that they are enforced?"

Carlos González de Villaumbrosia | Product School 00:29:40

"Governance" is another huge word in the enterprise. What are the best practices for a company working across so many functions to ensure they have the right monitoring? Is it a Chief AI Officer?

Chris Geoghegan | Zapier 00:30:10

We recently announced a new role at Zapier: the Chief AI Officer, who also happens to be our Chief People Officer. We believe this is a full-time job. We have a framework for AI transformation, and the top layer is leadership. One of the first things we did was call a "Code Red." It's important to say, "We are in a moment that is not like any other, and we need to do something about it." Then you create priority by putting people behind it. At a leadership offsite last week, we spent an hour and a half doing AI "show and tell." Every executive took turns saying, "Here's what I'm doing with AI. Check this out." Execs have to be hands-on with the technology. They have to understand the boundaries—what it can and can't do—because that is evolving every day. If you're wondering where to start, start with leadership.

Carlos González de Villaumbrosia | Product School 00:31:59

I 100% agree. That applies to any transformation. You can't just support it from the top; you have to commit. Commitment means building with it. You can't delegate too early or just buy a tool and send an AI memo.

Chris Geoghegan | Zapier 00:32:38

If you're a leader saying we need AI transformation and you're not using the tools, people will see through that very quickly. To have integrity and authenticity, you have to be hands-on.

Carlos González de Villaumbrosia | Product School 00:32:54

Chris, I loved having you on the pod, geeking out on how you're actually building and drinking your own champagne in ways that help other companies. Thank you so much for your time.

Chris Geoghegan | Zapier 00:33:11

Thanks for having me, Carlos. It was great to be here.
