# Spec Compression For Review Work

Use this reference when the task is not just `give taste feedback`, but needs to survive repeated review, implementation handoff, or multi-round iteration without drifting.

## What To Borrow From Spec Coding

The useful idea is not a full engineering framework. It is this:

- do not let the model answer too early from incomplete signals
- turn messy review context into explicit rules before execution
- separate `what should happen` from `how it should be expressed`
- keep constraints and verification visible so later rounds do not silently drift

## Minimal Spec Shape

Before major redesign, implementation, or structured review, compress the active context into:

- `what`: what user-facing/business result must be achieved
- `how`: what layout, flow, interaction, or packaging route should carry it
- `constraints`: what cannot be weakened, hidden, distorted, or over-decorated
- `verify`: what screenshot check, logic check, review reaction, or metric would count as success
- `context`: which imported note, role lens, or scenario this came from

Keep each field short. This is a control layer, not a second full brief.

## When To Use It

Prefer this compression step when:

- the user gives long chat logs, screenshots, or recordings
- feedback is iterative and wording changes across rounds
- the task spans design review and implementation
- different reviewers may read the same output
- the request includes `为什么总改来改去`, `怎么更稳`, `怎么方便交接`, or similar concerns

It is especially useful for:

- concept-edition review loops
- commercialization and membership surface iteration
- repeated campaign/activity revisions
- turning research findings into reusable design rules

## How To Apply It In This Skill

### 1. Complete the information before judging hard

If the evidence is still partial:

- avoid pretending confidence
- mark which part is stable and which part is provisional
- prefer `当前更像是...` over final-sounding claims

The common failure mode is early over-answering: once a weak guess enters the loop, later rounds keep patching the guess instead of re-grounding from the full context.

### 2. Turn review comments into execution rules

Examples:

- `首屏不够硬` -> `what: first-screen decision clarity must increase`
- `有点土` -> `constraints: reduce sticker noise, unify texture, keep contrast but remove cheap highlights`
- `按钮不明显` -> `how: expose one primary CTA in the first focal zone`
- `不好汇报` -> `verify: proposal should show background, current tactic, and business/design reason in one screen`

### 3. Verify against the spec, not against the latest mood only

Before final output, quickly check:

- did the main `what` actually get stronger
- did the chosen `how` stay consistent with the historical route
- did any `constraints` get broken during polishing
- is there a concrete `verify` signal, not just style vocabulary

## Suggested Output Shape

When useful, expose a short spec block in the response:

- `当前任务目标`
- `建议抓手`
- `不能退让的约束`
- `怎么判断这版更顺`

Do this only when it improves stability or handoff clarity. Do not force every small answer into a template.

## Boundary

- This is a lightweight execution habit, not a requirement to build a full spec repo.
- For small one-shot visual tweaks, direct action is still better than ceremony.
- For code tasks, this reference complements reading the real codebase; it does not replace it.
