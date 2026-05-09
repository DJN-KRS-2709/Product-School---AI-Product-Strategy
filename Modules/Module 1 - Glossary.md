# Module 1 Glossary

*The terms introduced in Module 1 - The Bet. For the full course-wide reference (every module's terms in one place), see [`Glossary.md`](./Glossary.md).*

Two sections:

1. **AI/ML Foundations** - the technical vocabulary the rest of the course assumes.
2. **Strategy Concepts** - the frameworks and ideas Module 1 introduces.

---

## 1. AI/ML Foundations

### Drift

When model behavior shifts over time - either because the provider updates the underlying model, or because the data the model sees in production changes. A real product needs evals to catch drift before users do.
*Seen in: M1, Slide 6 (the probabilistic outputs row of Traditional vs. AI).*

### Hallucination

When the model produces an answer that sounds confident but is factually wrong. The reason AI products need eval harnesses, golden datasets (Module 4), and human review for high-stakes outputs.
*Seen in: M1, Slide 6.*

### Model

The trained AI system that takes input and produces output. Models come in tiers (small / cheap / frontier) and from different providers. Your product is almost always making choices about which model to call for which task.
*Seen in: M1, Slide 6; foundational throughout.*

### Prompt

The instruction (and any context) you send to the model. Prompt design directly affects cost (longer prompts = more tokens) and quality.
*Seen in: foundational throughout, first relevant in M1.*

---

## 2. Strategy Concepts

### AI Value Archetypes (the 5)

Five categories that capture what an AI product fundamentally does, each with a different margin profile and governance burden: **Automator** (replaces tasks - UiPath), **Copilot** (augments people - GitHub Copilot), **Oracle** (surfaces hidden signals - Palantir), **Creator** (generates new assets - Midjourney), **Orchestrator** (chains agents and tools - Zapier AI). Most products blend two or three; what matters is which one dominates your economics.
*Seen in: M1, Slide 14.*

### Contextual Moat

How embedded your product is in the way people actually work. The first axis of the Three-Axis Diagnostic. Workflow depth multiplied by switching cost.
*Seen in: M1, Slide 18.*

### Data Advantage

The second axis of the Three-Axis Diagnostic. Not "we have data" - it's specifically about whether your product gets smarter every time someone uses it. A stockpile is not an advantage; a flywheel is.
*Seen in: M1, Slide 18.*

### Kill criteria

The conditions under which you stop a bet, written down before the bet starts. The thing that turns "we'll see how it goes" into an actual learning loop.
*Seen in: M1, Slide 12 (the OLD vs. NEW reframe: "70% this hits Y - here's how we'll know, and when we stop").*

### Platform Exposure

The third axis of the Three-Axis Diagnostic. The risk that a platform (OpenAI, Google, Apple, Microsoft) ships your wedge as a free native feature tomorrow.
*Seen in: M1, Slide 18.*

### Probabilistic vs. Deterministic

The core reframe of Module 1. Traditional software is deterministic - it does the same thing every time. AI is probabilistic - outputs are distributions, not point estimates. Strategy has to shift from "ship X by Q3 → Y result" to "70% this hits Y - here's how we'll know, and when we stop."
*Seen in: M1, Slide 12.*

### Three-Axis Diagnostic

The Module 1 framework for scoring your AI vulnerability across **Contextual Moat, Data Advantage, and Platform Exposure**, each on a 1-5 scale. Calibration: Figma is a deep moat, a thin ChatGPT wrapper is shallow.
*Seen in: M1, Slide 18.*
