---
title: "OpenAI & Figma Product Builders on Killing the Design-to-Code Handoff and Vice Versa | Ed Bayes & Matt Colyer | E290"
guest: "Ed Bayes & Matt Colyer"
date: "2026-04-01"
source: "buzzsprout"
episode_id: "18944348"
duration: "1987"
audio_url: "https://www.buzzsprout.com/90361/episodes/18944348-openai-figma-product-builders-on-killing-the-design-to-code-handoff-and-vice-versa-ed-bayes-matt-colyer-e290.mp3"
---

# OpenAI & Figma Product Builders on Killing the Design-to-Code Handoff and Vice Versa | Ed Bayes & Matt Colyer | E290

> AI is collapsing the silos between design and engineering. In this episode, Carlos Gonzalez de Villaumbrosia, CEO at Product School, sits down with Ed Bayes (Design Lead, OpenAI) and Matt Colyer (Product Director, Figma) to discuss their groundbreaking integration that enables a seamless round-trip workflow from code to canvas.Matt Colyer walks us through a step-by-step demo of the new code to canvas and right to Figma capabilities. You’ll see exactly how OpenAI’s Codex and Figma’s

## Transcript

### Introduction

Carlos González de Villaumbrosia | Product School 00:01:01

Hey, this is Carlos, CEO at Product School and your host on The Product Podcast. Today's guests are Ed Bayes, Design Lead at OpenAI, and Matt Colyer, Product Director at Figma. OpenAI and Figma just announced a new integration that creates a true round-trip workflow between Codex and Figma. Product builders can now start a design in code on Codex and then iterate on Figma's Design Canvas. Similarly, it's also possible to start a design on Figma and then push it to Codex in order to generate the code. Regardless of where you start, the main benefits are faster iteration and a cleaner handoff between what you design and what you ship. In this episode, Matt walks us through a step-by-step demo. Let's get into it.

Hey everyone. Today I have two guests — probably the first time I'm hosting two builders at the same time. I have Ed Bayes from OpenAI and Matt Colyer from Figma. Ed, welcome to The Product Podcast.

Ed Bayes | OpenAI 00:02:01

Thanks.

Carlos González de Villaumbrosia | Product School 00:02:03

Tell us a little bit more about what you're up to at OpenAI.

Ed Bayes | OpenAI 00:02:07

I'm on the design team and work on Codex, our suite of coding products. I've been at OpenAI for about 18 months, always working on research and coding products. Excited to chat today.

Carlos González de Villaumbrosia | Product School 00:02:21

I think you're also the first designer on The Product Podcast — even though, as you know, all the lines are blurring, so I consider you all builders. Matt, what about you?

Matt Colyer | Figma 00:02:32

My name's Matt. I just joined the product team at Figma in January and have worked with several teams here. The first was Code to Canvas, and then just yesterday we had our second follow-up launch — Write to Figma. Pretty excited. It's all in the space of AI, development, design, and how it all goes together.

Carlos González de Villaumbrosia | Product School 00:02:54

That's exactly why I wanted you both together — so we can actually demo this new launch and show how it's now easier than ever for any builder to go from code to design and vice versa. In previous conversations you called this the round-trip workflow.

Matt Colyer | Figma 00:03:13

Yeah, definitely.

### The Collapse of Design and Engineering Silos

Carlos González de Villaumbrosia | Product School 00:03:14

Matt, can you tell us a little more about what this is all about?

Matt Colyer | Figma 00:03:20

The world is changing. AI has unlocked incredible capability that we didn't have before — for builders and for everyone else. It's really democratized who can create software and expanded who does design. My personal take is that we now have a lot more people doing design who might not even realize it. Ed, what's your take?

Ed Bayes | OpenAI 00:03:46

For a while, individual roles have been collapsing and historic silos have been breaking down. More and more designers are in code, and because the velocity of engineering has sped up so much, more and more engineers are also designing — designing in prod, building new components.

The old way of working was two separate groups: designers in their tools, handing off to engineering, who would finish things in their own stack. Now what you're seeing is a hybrid. Engineers are jumping into Figma, iterating on design systems, tweaking the underlying design system. And designers are hopping into code more — jumping into last-mile polish, upleveling the craft, and closing the fidelity gap between the initial design and the final product. Or even earlier in the process, prototyping in code themselves to test interaction design.

It's less that everyone is moving to code, and more that engineers are coming into design and designers are going into engineering. The tools are all becoming way more flexible and interoperable. That's why I'm super excited about some of these recent Figma launches — because it's no longer a one-directional process from design to code. Now it goes back and forth. You can update design system files from production, and you can move designs into production from Figma.

### The Round-Trip Workflow: Starting in Figma

Carlos González de Villaumbrosia | Product School 00:05:35

I want to unpack both workflows so it's crystal clear — and I know we're going to do an actual demo after. Traditionally, if a designer started designing, they'd go to Figma and the handoff to engineering was just "here's the design" — and the reality is the implementation was never 100% as expected. Matt, can you start with that initial workflow? For people who start with a design in Figma, how is this new workflow different?

Matt Colyer | Figma 00:06:13

One of the things we've been really pushing on is how we enable agents to leverage the tooling inside of Figma. Companies and individuals who've invested in design libraries inside Figma have representations they use to prototype and explore ideas. That's really where the value of Figma is — this ability to riff quickly, with other people, in real time.

What we're now bringing is the ability for agents to use that same set of tooling. With the Write to Figma capability, we allow agents to use the plugin API — just like plugins inside of Figma — and that unlocks a whole new set of capabilities.

To give an example: previously, designers who worked in design systems would spend a fair bit of their time taking a design library and updating it with the latest changes from code. Say they have a dropdown and want to add multi-select to the component in their design library — they'd have to add all those states in design, then go back to code and re-implement the states there. That's the design translation process — and Ed's shaking his head because all of us in the industry have lived that pain. It's not a fun process, because at the end of the day you're trying to deliver value to customers. The interesting part isn't adding all those different states. The opportunity is that with agents, we have an immensely leveraged tool. Design taste and direction still matters just as much as it did before — but now we don't have to spend our time moving layers around and implementing slots and props inside Figma. We can ask agents to help us do that.

### Handoff Quality and the Role of Human Judgment

Carlos González de Villaumbrosia | Product School 00:08:03

So how do you ensure the handoff is actually correct — that what you're designing on a visual interface is going to be accurately implemented in code?

Matt Colyer | Figma 00:08:16

That was true before agents too. Lots of designers and engineers would pull up chairs next to each other and sit in front of one monitor. The engineer would implement the multi-select, but in a certain case the mouse would hover and the menu would disappear — and they'd say, "Well, that interaction's not quite right." So that verification work still needs to be done. Human judgment is still an irreplaceable part of the process.

Agents continue to improve, and as they get better, they can do some of that themselves — like hooking up open-source tooling that drives a browser and takes a screenshot. But it is not a substitute for human judgment.

Carlos González de Villaumbrosia | Product School 00:09:00

Ed, from your perspective as the designer in the room — what's your experience of how this new integration helps you stay satisfied with the actual code implementation when you hand off a design?

Ed Bayes | OpenAI 00:09:14

It's all about how close the designer can get to the final product. There was always this translation process — you'd spec things out, pixel-perfect, with your perfect design system. Then you hand it off, and the engineer has to hop into the file, click into developer mode, figure out the exact pixel padding or width, figure out the CSS behind something like a shadow. It's complex, and there are a lot of places where lossiness can appear and deviations can creep in. A lot of that work was this messy translation piece.

With some of these new tools, that just goes away. In the new world, designers and engineers have a broader range of tools that all speak to each other and work super fluidly across them. The TLDR on these new tools is it's basically new plumbing that connects different tools and services together. So a lot of your time is no longer spent on things that used to take a long time and, frankly, weren't the most exciting part of a designer's job. Removing that frees up time to think at a high level about the big-picture stuff — the super interesting interaction, the really smooth new system. It's about automating low-level work so you can focus on the high-level primitives.

### Making Code Accessible to Non-Technical Builders

Carlos González de Villaumbrosia | Product School 00:11:15

We talked about the handoff challenge and how it's now possible to go from design to code implementation in a much more accurate way. But I want to talk about the reverse — because the interface is also a real challenge, especially for non-technical people. Non-technical people are comfortable on a document or a canvas, but you're sending them to a CLI. That's not their natural habitat. Ed, even as a designer working at OpenAI — how does that work for a non-technical person to open a terminal and get comfortable enough to use code in order to design?

Ed Bayes | OpenAI 00:12:00

Where we started with Codex — and where a lot of these tools started — was building for developers. If you build a tool for a developer, it looks a little different to a consumer tool. Maybe it lives in your CLI, or maybe even if it lives in an app, there's a bunch of stuff in the interface that, to a non-developer, might feel intimidating or scary.

But the very cool thing that has happened — and you can see it in the information architecture of these products — is that we've moved from a side chat on the right to putting chat front and center on the left. The primary focus becomes the conversation. And it turns out anyone can have a conversation. Maybe you render some things in there that are a little technical — terminal outputs, files being edited — but at its core it's just a conversation, and that's accessible to anyone.

We do have CLI products, and we also released a Codex app a few months ago — a standalone desktop app, both on Mac and Windows. If you open it up, even if you're not a developer, it's not as scary as traditional developer products. It has a familiar chat interface. You can just ask a question, and under the hood it's super powerful. If you connect the Figma plugin — which we're releasing this week — it can work with your Figma. Connect your email plugin and it can read your emails and help draft responses. Connect Slack.

As we move up the level of abstraction and build interfaces that are more universal for getting work done, a lot of the scariness of code for non-developers goes away. You can scale up and down in complexity, and on first look these products are not as scary as a CLI.

Carlos González de Villaumbrosia | Product School 00:14:28

Speaking from experience — I'm a former engineer, I can't claim to be one anymore, but I'm now using the terminal again, which is crazy. Many years later, I'm back at it. One of the things that helped me was just making an instruction and it works. I could say "connect to Figma MCP," and boom — connection made. And now with skills, codifying a set of instructions and importing skills that weren't even created by me suddenly gives me those superpowers, ensures I'm working within certain guidelines and guardrails, and lets me just focus on getting stuff done. Matt, can you tell us more about how you're making those MCP connectors and skills work for non-technical folks?

Matt Colyer | Figma 00:15:17

For the longest time in this information technology revolution, we humans worked like computers. Sixty or seventy years ago it was punch cards — very inhumane, very binary. Then we got to programming languages, which were a little more human, kind of like language but not really. What's really cool about skills and multimodal models is that you can legitimately have a conversation with them — even with voice. That always seemed like sci-fi, like Star Trek — you talk to the computer and it answers. But we can all do that with the phones in our pockets now.

Skills are a natural extension of that. What's so powerful about them is that they're accessible. If you can speak or write, you can use a skill.

That's actually one of the critical parts of how we designed Write to Figma — we exposed the underlying plugin API and made sure the model had access to all the important bits of information to use it correctly. But then we also shipped what we're calling foundational skills, which give it the pattern. Think of skills like recipes: we provided all the ingredients, which is the complicated engineering part. But anyone in the Figma community can totally write a skill, because it's about taking the domain knowledge and expertise the community has. Knowing, for example, that when you build a design system component, you should use tokens so you can support light mode and dark mode in the future — that's expertise from the design profession that a layperson might not have. Their first pass at a skill might just be "make me a button," without thinking about whether that button ends up on a phone or on the web and how it should look differently.

So we've built foundational skills, and one of the other exciting things we've done is build community skills. Ed and the Codex team have been great partners — they've got a plugin marketplace and we're in there too. The world is building toward these composable Lego blocks of skills. It's an exciting time to be a design developer. The next billion software developers can now code using language. Good ideas can come from anywhere, and the more people we have using these tools, the better ideas we'll all have.

### Live Demo: Write to Figma

Carlos González de Villaumbrosia | Product School 00:17:52

I think we're ready for action.

Matt Colyer | Figma 00:17:54

We'll do a live demo — with the caveat that this is live and agents sometimes do different things. So here's how Write to Figma works. I've got the Figma canvas open. I'm calling it the badge component. I've got Codex open on the left and I've loaded it with the skills we just talked about from the Codex repo — all the ones that are included now. And for example purposes, I've pulled in Daisy UI, which is an open-source framework that implements a button component in React.

I've got this prompt ready to send. It's asking: "Use the Figma tool to draw the branch component in the Figma file and use proper variables and structure with good layer composition so that I can manipulate the design."

The first thing it does is read in the skill, as we just showed. Then it creates a plan — and before doing so, it checks the documentation for how the Figma API works. We'll allow this for the session. The first thing it does is take a screenshot of the canvas and see if there's anything there. It realizes it's empty, which is what we expect.

Now it's going to read the source code for the badge component — it's looking for Python, it'll try again. Now it's looking for variables and how they work within the Figma API. Now it's going to go ahead and add the token collection and the variables, then follow up with the actual component.

It's written the script, connected to the file, and it's adding those variables. It's got all the variable collections in place. Now it's going to draw the elements on the canvas, take a screenshot, and confirm it matches what it expects. And it's finished.

Carlos González de Villaumbrosia | Product School 00:20:14

That's a really good example of the workflow going in one direction. I'd love to talk about the reverse — the round-trip workflow. If I were to start on the other side of the spectrum, how would that work?

Matt Colyer | Figma 00:20:30

The opposite version is: instead of going from code where you've got a component defined and want to bring it into a design library — say you've been working with coworkers in a Figma canvas and you've decided on a new signup flow for your dog-walking app. You could take one of those frames — say you're changing the order of the fields — and then go to Codex, pull up your local app repository, and start Codex in there. It's able to see the implementation of the current signup page. You can then ask it, using the Figma URL we just showed, to pull in the new frame and make the changes you've specified.

What it does behind the scenes is go into Figma and pull a screenshot of what it should look like. The model is then able to compare that to a screenshot of what the current page looks like. It also has access to a code representation — some of the tooling we've built at Figma can take our design canvas and present it as code. The Codex agent's job is to take both screenshots — the before and the after — as well as the code, and make the change.

### Business Impact: Velocity, Bottlenecks, and What Changes

Carlos González de Villaumbrosia | Product School 00:21:47

I'm curious how this new workflow is improving velocity and other business outcomes in your own product teams — with design and engineering together. You're already living in this future. What does it really mean for a business in terms of headcount, velocity, and expectations?

Ed Bayes | OpenAI 00:22:18

It basically just helps teams work faster. If you're a designer and you've built out a design, with some of these new MCPs you can literally do one prompt turn and your full design can appear in the product. What might have taken a few hours to a day previously happens really fast. It speeds up team velocity, means teams can work on more things, and the handoff is way quicker.

But interestingly, it also means design can feel like the bottleneck now. Engineering might have been accelerated 10x by coding agents. Designers have been accelerated too — but there's a lot of slow, careful thought that needs to go into designing a product, specking things out, designing systems. The real challenge for designers right now is choosing when to go slow — when to take more time and consideration around what to build. When you can build anything, what's the right thing to build?

And designers can now hop into the codebase themselves and take things across the finish line. Practical example: across our team we have folks working on content design — people who mainly do writing, UX copy. They're submitting PRs now. I was chatting with someone the other day who's a real Codex power user — she's been submitting PRs in the ChatGPT codebase to improve UX copy across the product. At both ends of the spectrum, it speeds folks up. But the main challenge becomes deciding what to build.

Carlos González de Villaumbrosia | Product School 00:24:08

As a non-technical person, how much coding skill did you have to develop to feel comfortable in this new workflow?

Ed Bayes | OpenAI 00:24:21

My background is actually half design, half engineering, so I'm maybe slightly different in that respect. But another really powerful and underrated thing about these tools is that they're like a tutor. Everyone now has access to a tutor who's incredible at coding and a bunch of other things.

More and more, we have internal Slack groups where designers post works in progress. Over the past six months I've seen a shift — more and more people are posting interactive demos. They might send a Figma Make demo or a link to a prototype. I'll often DM them because I didn't know they usually coded, and they'll say, "I just gave it a go and I was able to build it."

People on the really non-technical side who've never coded — maybe they don't even have a GitHub account or have never submitted a PR — are finding this on-ramp really accessible. And for folks who skew more technical, it accelerates you even more and you can work across more of the stack.

One thing I'd encourage anyone listening: if you've always thought coding wasn't for you or it's scary, just give it a go. My wife is non-technical and she's been enjoying building little fun websites for herself. And once you start building, it's not just prompt-and-ignore — if you're curious, you start asking what's going on. It's like a tutoring approach: "Okay, I built this React app — what is React? What's the difference between these different pages?" It's also an amazing on-ramp for folks who previously would have had to go to a bootcamp. Now you can hop in directly. And the key is how you continuously learn and improve so you're not just vibe coding but becoming genuinely proficient in proper engineering work — and that requires having a teacher along the way.

Carlos González de Villaumbrosia | Product School 00:26:43

Matt, how is this new way of working impacting expectations at Figma as a product team?

Matt Colyer | Figma 00:26:51

Design is now different. The way I think about these tools is like 100x leverage or 1000x leverage — things that used to be hard are not hard anymore. That changes the traditional product development process. One of the sayings here right now is: use staging flags, don't make a demo. Even the design folks here are getting in on that now.

There's this feeling that it's almost like you're playing a game. I have kids, and one of the things I love to do with them is solve problems they have together with AI — it's a way to have fun, but it's also kind of a game in itself.

Ultimately, that's what design is at the end of the day — this iterative polish of human perspective into fashioning a tool. Humans have been tool makers almost as long as we've been human. The modern version is software. What's exciting is that it used to be a very small set of people could do this because it was very complicated — not because it needed to be, but because we just didn't have the right tools yet.

Where this falls into modern business practices is it allows us to try more things faster. Another saying here: don't have a meeting, just make a prototype. The number of people in a meeting and the time spent debating ideas — some of those ideas could just be tried. Was it A or B? Let's do both, try it, and then decide.

### Advice for Product Leaders: Stay Curious, Start Building

Carlos González de Villaumbrosia | Product School 00:28:38

Any closing thoughts for product managers who are half scared, half excited after this demo? Especially product leaders thinking, "This is not just for the junior folks — I need to catch up. Some people are already getting more productivity gains than me." How do they get on board in a way that honors the role and value they bring — while also recognizing there's a window, and it's really up or out?

Matt Colyer | Figma 00:29:22

There is a lot of change. I was fortunate to start this journey early — about three years ago when GPT-4 was around — and it was incredible to see the progress we've made in that short time.

Going forward, it doesn't matter what role you have in a business. These tools can affect almost anything you do. Specifically for product, not even getting close to development — I remember as an early PM doing customer calls, getting feedback from sales teams, and spending hours trying to collate notes from the field about specific accounts and the features they were requesting. My idealized backlog would have been prioritized by account size times frequency of requests divided by whatever — and I never built that because it would have taken too many hours. It's not that hard to build now, which is crazy.

As a leader, these tools also let you magnify what you can see. You can look at data trails — if you work in source management systems, you can understand what branches or changes are getting merged and write your own personal release notes. You can ask questions. People think AI is only good for writing, but it's actually really good for answering technical questions. As a PM you might say, "I need to understand exactly how this event is triggered in order to understand the business implications." Previously you had to find someone on your team. Now you can just use these tools.

To anyone on the product side, whether early or late in your career: I'd encourage curiosity and play. We haven't even tapped the full potential. Someone once described it to me as alien technology — like an LLM crashed on Earth and we don't quite know how it works, so we just poke at it until we find what it can do. After working with these things for four years, that's kind of how it goes. It's more art than science — and eventually the science will catch up, but for now it's about play and curiosity.

Carlos González de Villaumbrosia | Product School 00:31:35

Love it. Ed?

Ed Bayes | OpenAI 00:31:38

Pretty similar — stay curious and just get involved. With the Codex app, you can download it as part of your account. You don't need to open the terminal. It just appears on your computer. You can open a folder and start going.

Give it a go — maybe on weeknights or weekends. Maybe there's an idea you've been thinking about for a while, something you've been chatting about with your family and wondering, "Could I build that now?" Just explore a bit, feel it out, and pretty soon you'll get to know the edges of what's possible and keep pushing. You'll find you can do way, way more than you thought.

Carlos González de Villaumbrosia | Product School 00:32:28

A little bit less reading and watching about AI — a little bit more just prompting it and going from there.

Ed Bayes | OpenAI 00:32:36

You can just build things.

### Closing Remarks

Carlos González de Villaumbrosia | Product School 00:32:39

Thank you both so much for being here today — for really showing what's possible now and demystifying that you can genuinely reduce your time from idea all the way to production.

Ed Bayes | OpenAI 00:32:58

Thank you.

Matt Colyer | Figma 00:33:00

Thanks.
