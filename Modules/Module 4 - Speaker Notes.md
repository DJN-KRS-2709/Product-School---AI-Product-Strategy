# Module 4 — The Contract

## Slide 1 — Title
- **Why:** Shift energy from M3 spreadsheets to trust + craft — this is where “will they rely on it?” lives
- Hardest AI PM job: believable uncertainty, not model hype
- Out: Component 4, eval dashboard spec, reliability contract (your quality / trust contract in writing)
- **Interactive:** Point to waypoint 1/2/3 — which is the biggest gap today?

## Slide 2 — Agenda
- **Why:** Front-load that this block is hands-on (red-team, contract) — not another trust ethics sermon
- Lecture = fast concepts + company anchors; applied = where the “fireworks” land

## Slide 3 — Recall from M3
- **Why:** Margin only matters if people keep using the output — habit beats peak accuracy
- They brought cost curve, Components 1–3, value capture story
- **Interactive:** Pairs 30s — which artifact actually moved their roadmap?

## Slide 4 — Provocation
- **Why:** Reframe before definitions — audit trail > bragging rights on accuracy
- Three FALSE claims: control beats naked %; users want signals (Perplexity-style citations); evals are launch infra
- Optional 10s story: support bots that looked fine until silent drift
- **Interactive:** Hands vote each claim, then hands — versioned golden set in prod?

## Slide 5 — Trust ≠ Accuracy
- **Why:** Boards love %; users love predictability and escape hatches
- Black box vs legible — short contrast, not a paragraph
- **Companies:** ADAS / driver-assistance UIs (Tesla-style handoff pressure) vs “chatbot with no receipts”; Perplexity / AI Overviews = sources first
- **Interactive:** Quick — what’s the failure they only discover after they trusted you?

## Slide 6 — Golden Datasets
- **Why:** Without labels you’re flying blind — gold set is the root of all eval truth
- Regression · domain anchor · buyer proof
- **Company:** Grammarly — internal benchmarks for correctness/tone tiers (not a public leaderboard)
- **Interactive:** Pairs 45s — one nasty row the gold set must include

## Slide 7 — Human-in-the-Loop
- **Why:** HITL is either a tax forever or a funnel that shrinks — product choice
- Crutch vs feature — threshold, capture fixes, escalation UX (ties to M2 flywheel)
- **Companies:** Clinical imaging + ambient scribes — clinician sign-off on high-risk outputs; regulated paths normalize this
- **Interactive:** Point — where does a human catch a catastrophic miss first?

## Slide 8 — LLM-as-a-Judge
- **Why:** Human rubrics don’t scale; judges buy you coverage if calibrated to gold
- Regression · drift · live routing (auto / human / block)
- **Companies / pattern:** OpenAI/Anthropic-style auto-graders + spot humans; LangSmith / Braintrust = tooling — you still own labels
- **Interactive:** Thumbs — already using a model to grade outputs somewhere?

## Slide 9 — Case: Air Canada
- **Why:** Legal reality = the bot is the brand — “contract” isn’t academic
- Bet / crack / ruling — tight story; liable, need receipts + thresholds + HITL
- **Interactive:** Pairs 60s — worst confident-wrong answer in their domain?

## Slide 10 — Eval Dashboard Spec
- **Why:** Makes quality visible — internal SRE loop + external proof for buyers
- Four tiles: metrics · judge setup · drift · UX hooks
- **Analogy:** Datadog / Stripe status-page energy — would you screen-share this?
- **Interactive:** Thumbs — ready to show a buyer next week?

## Slide 11 — Break
- **Why:** Reset before writing-heavy work; red-team is coming — frame as sport

## Slide 12 — Golden Dataset (applied)
- **Why:** They leave with a spec, not a vibe — failures-first beats happy-path only
- Scope / sources / maintenance + sales-test one-liner
- Optional: teams like Notion/Linear treat eval sets like versioned product assets
- **Interactive:** Stand if at least one adversarial row is in (or planned)
- **🔧 Tool:** "Open the Golden Dataset Builder — it structures your test cases by category, lets you tag adversarial rows, and exports a clean spec you can hand to your eng team Monday."

## Slide 13 — Confidence UX (applied)
- **Why:** One-mode UI = Air Canada energy; three modes = legible system
- Tiers >90 / 50–90 / <50 — force color + copy
- **Companies:** Grammarly depth of rewrite; Copilot citations + softer tone when unsure
- **Interactive:** Point at screen — which tier is live product closest to?
- **🔧 Tool:** "Open the Confidence UX Checklist — it's a 16-point checklist across confidence display, fallback design, HITL triggers, and transparency. Check off what you have, see your coverage score, and spot the gaps."

## Slide 14 — Red-team
- **Why:** Cheapest place to fail; builds shared language on risk
- Four lenses — keep timeboxed (6 min each side)
- Optional: enterprise red-team / safety programs (e.g. Microsoft Copilot narrative) if room needs weight
- **Interactive:** Point at the attack card that scares them most; one-line worst miss after

## Slide 15 — Reliability Contract
- **Why:** Execs fund explicit promises; mush doesn’t survive QBRs — this is M6-ready
- Four quadrants — push for real numbers even if draft
- **Analogy:** Cloud SLAs — specificity creates accountability
- **Interactive:** Partner share — one promise they’d sign vs one they’d redline

## Slide 16 — Synthesis
- **Why:** Close the loop from slide 4 — they built the audit trail today
- Component 4 checklist — short bullets only on slide
- **Interactive:** Clap once if something changes what they demo next sprint

## Slide 17 — Bridge to M5
- **Why:** Trust at product level ≠ trust at org scale — M5 is where shadow AI and agents appear
- Bring eval spec, contract, confidence UX, Components 1–4

## Slide 18 — Survey
- **Why:** Instructor iteration — Carlos/Daria use this to tune hands-on vs theory
- QR / link; keep energy positive on the way out
