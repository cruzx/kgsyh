---
name: kgsyh
description: 酷狗收一下候选 skill。用于设计评审、方案收敛、商业化页面、概念稿、活动页、交互稿等内部过稿场景。触发词：kgsyh、收一下这版、更容易过、过稿、方案收敛、概念稿收口、商业化页评审。
description_zh: 调用既有协作沉淀，按上下文推进过稿
description_en: Use existing collaboration context to converge a design or product proposal toward signoff
version: 1.0.0
---

# kgsyh

过稿通关 skill。

Use this skill to route a collaboration-heavy task to the right imported context before proposing designs, product logic, review feedback, or implementation direction, so the output is more likely to顺着既有语境过稿。

This skill also treats review context as a lightweight spec system: before giving recommendations, convert unstable chat signals into explicit `what / how / constraints / verify / context` rules whenever the task includes implementation, repeated iteration, or cross-person handoff risk.

## Interaction Mode

When this skill is used for design or product work, start in a `plan-first` workflow automatically.

Rules:

- keep the plan to `2-4` short lines
- no long explanations
- each line should be action-first and concise
- inspect the current uploaded draft before asking any question
- ask a question only when there is a real blocking branch
- the question must be based on the current draft, not a generic repeated template

Default behavior:

- if the user's intent already implies direct execution, do the work without asking the old generic format question
- only ask `修改标注` vs `修改后的设计稿` when that format choice is truly unresolved
- if a different decision is more relevant to the current draft, ask that instead, for example which block to prioritize or whether to keep a specific interaction pattern

## When To Use

Trigger this skill when the task clearly depends on prior collaboration context such as:

- campaign or activity iteration
- concept exploration
- commercialization or growth design
- product experience feedback
- AI design exploration
- design review / signoff loops
- role-specific approval preferences
- Kugou-style internal signoff convergence where the user asks to `收一下这版`, `更容易过`, `别太飘`, `做得更耐看`, or `按内部会过的方式改`

Do not use this skill for generic product tasks when no imported collaboration context is needed; in those cases, use the repo, current files, or other more specific skills first.

## Workflow

### 0. Start with a concise plan

Before deep critique or redesign work, give a compact plan such as:

- `先对齐概念版语境`
- `再拆样式和交互`
- `最后出标注或改稿`

Do not turn this into a long outline.

Then immediately inspect the current draft and decide whether a question is needed at all.

Question rule:

- good: `先只收头部交互，还是整页一起收？`
- good: `这版先保留横滑推荐，还是改成单主卡？`
- bad: every design turn opens with the same generic format question even when the user clearly asked for execution

### 0.5 Evolution loop

This skill should evolve across repeated use through repo-native notes.

Before doing substantial work:

- read [learning/PROFILE.md](learning/PROFILE.md)
- read [learning/EVOLUTION_RULES.md](learning/EVOLUTION_RULES.md)
- read [learning/SCORECARD.md](learning/SCORECARD.md)
- read [learning/CREATIVE_ENGINE.md](learning/CREATIVE_ENGINE.md)
- read [learning/ITERATION_PROTOCOL.md](learning/ITERATION_PROTOCOL.md)
- if the task seems related to a recent repeated pattern, inspect the latest entries in [learning/SESSION_LOG.md](learning/SESSION_LOG.md)

After each substantial conversation or iteration:

- append one short distilled note to [learning/SESSION_LOG.md](learning/SESSION_LOG.md)
- prefer the standard template in [learning/SESSION_TEMPLATE.md](learning/SESSION_TEMPLATE.md)
- if a signal is repeated, explicit, and cross-task stable, promote it into [learning/PROFILE.md](learning/PROFILE.md)

Do not claim hidden automatic learning. The evolution mechanism is explicit, repo-native, and reviewable.

### 0.6 Quality and creativity bar

When the user asks for a version that should be better, more complete, more perfect, or more creative:

- do not stop at the first acceptable answer
- internally create at least 2 candidate routes when feasible: one `稳`, one `出彩`
- run a quick self-score using [learning/SCORECARD.md](learning/SCORECARD.md)
- run one self-critique pass using [learning/ITERATION_PROTOCOL.md](learning/ITERATION_PROTOCOL.md)
- prefer delivering either:
  - a strongest signoff-ready version
  - a strongest creative version
  - or a clearly judged best-balanced version

Do not promise perfection. The operational target is: more stable, more memorable, less generic, and less likely to be sent back.

### 1. Route to the right reference

Choose the smallest relevant imported context instead of loading everything:

- activity / campaign note
- broad collaboration note
- commercialization / growth-design note
- topic research note when the task needs user-research guardrails for recommendation, AI music, AI instruments, children, membership, ringtone, HiFi, fan, concept-edition, or decoration decisions
- Kugou main player Android click baseline when reviewing main-app player entries, star cards, commercial cards, reward prompts, floating buttons, lyrics overlays, or cover-area interactions
- Kugou main home Android click baseline when reviewing main-app home page, first-screen entries, Kingkong modules, information-flow cards, recommendation cards, mini-player prompts, bottom-tab ideas, or home-page commercial/growth placements
- concept-exploration note
- small-group report / signoff note
- people-lens note when the task is about a specific collaborator role
- Kugou signoff lens when the task is explicitly about making a page, player, campaign board, commercialization design, concept proposal, or interaction draft easier to pass Kugou internal review

If the task spans multiple contexts, read only the 2-3 matching notes and synthesize them.

For a compact routing summary, read [references/routing.md](references/routing.md).

### 2. Extract the durable signal, not just the literal chat lines

Translate chat context into reusable decisions such as:

- product principles
- UI/interaction preferences
- collaboration patterns
- review language
- implementation guardrails
- changing or unstable business details that should stay configurable
- people-specific working styles or review lenses

Avoid treating the earliest visible message as final truth if later messages or newer docs show iteration.

When the task is implementation-heavy, iteration-heavy, or likely to be handed across people, also normalize the context into a compact spec:

- `what`: what outcome or user-facing change must happen
- `how`: what structural route or interaction pattern should be used
- `constraints`: what cannot be weakened, hidden, or distorted
- `verify`: what evidence, screenshot check, or metric signal would prove it works
- `context`: what historical note, scenario, or role lens this came from

Do not dump the whole chain to the user every time. Use it internally to avoid early overconfident answers and to keep revisions stable across rounds.

### 3. Apply the context to the active task

Use the imported context to improve the current work:

- For design generation or review:
  emphasize existing style signals, reward visibility, low-friction interaction, and the relevant business/design constraints.
  If the task is specifically about `过稿`, `收稿`, `更稳`, `更耐看`, or `更像能上线`, switch into a Kugou signoff-convergence lens:
  - first make the scheme `成立`, then make it `出彩`
  - check whether it is easier to browse, compare, approve, and ship
  - prefer `顺场景`, `耐看`, and `低风险落地路径` over pure novelty
- For product logic:
  preserve already-agreed entry points, reporting language, and closure expectations.
- For implementation:
  prefer existing templates, shared methods, and current project structures over blank-slate invention.
  If the task has repeated review churn, rewrite the historical signals into a compact execution spec before changing code or structure.
- For reviews:
  check for regressions against the chat-derived principles before suggesting changes.
- For person-specific analysis:
  distinguish between `visual style`, `problem framing`, `evidence standard`, and `upward communication style`, instead of collapsing everything into a generic design taste summary.

For visual design tasks:

- if the task is concept-edition related, prefer the dedicated concept brand/UI rules over generic taste
- keep plans and review language concise
- when the user explicitly wants stronger creativity, use [learning/CREATIVE_ENGINE.md](learning/CREATIVE_ENGINE.md) and avoid stopping at pure safe收法
- before producing final artifacts, inspect the current draft and ask only the smallest draft-specific question that is still unresolved
- if the user already asked to `优化`, `重画`, `直接出稿`, or similar, default to execution instead of asking the old generic format question
- when the user asks for `优化`, treat the uploaded draft as the quality baseline; do not make the output rougher, cheaper, or more generic than the source
- preserve the original page aspect ratio and component proportions; never squeeze the page narrower or distort the screen shell just to fit a board or redraw
- if the user provides style references, first extract `可借鉴信号` and `禁止误用风险`, then propose edits; do not jump straight from reference mood to direct imitation

For Kugou internal signoff-convergence tasks:

- Read [references/kugou-signoff-lens.md](references/kugou-signoff-lens.md) when the user explicitly wants a design to be easier to pass internal review.
- Default priority order:
  - `场景贴合`
  - `易用性`
  - `业务表达`
  - `耐看升级`
  - `趣味加法`
- First judge whether the draft is blocked by one of these common signoff risks:
  - the idea jumps out of the current container or listening scenario
  - the page is flashy but not durable to look at
  - information is hard to browse, compare, or approve quickly
  - the proposal sounds creative but lacks a low-risk shipping path
  - it talks only about visual polish and not about business expression or implementation pace
- Prefer output in this order:
  - one-line overall judgment
  - `P0 / P1 / P2`
  - why it is hard to pass now
  - how to收成更容易过的版本
  - if needed, a lower-risk implementation fallback
- Use direct, practical review language rather than decorative critique.

For Kugou main app player-page growth/commercialization tasks:

- Read [references/kugou-main-player-android-2026-05.md](references/kugou-main-player-android-2026-05.md) before predicting CTR or recommending placement.
- Treat the data as Android 2026 May daily average click benchmarks: denominator is player page UV; numerator is each button/action click UV.
- Use nearby player-zone baselines to ground predictions instead of relying only on visual intuition.
- Compare proposed entries against relevant anchors: cover tap `6.43%`, lyrics overall `22.70%`, floating reward primary claim `2.80%`, floating reward close/ignore `8.68%`, left side bar `6.15%`, right side bar `2.54%`, play/pause `45.68%`, next song `25.66%`.
- Distinguish entry CTR from landing-page arrival, card claim, post-claim retention, playback interruption, and negative feedback.
- Prefer stable, low-interruption placements for long-term player entries; reserve cover-dominant or high-interruption patterns for fan-targeted or campaign-window pushes.

For Kugou main app home-page growth/commercialization tasks:

- Read [references/kugou-main-home-android-click-baseline.md](references/kugou-main-home-android-click-baseline.md) before predicting CTR/click penetration or recommending first-screen/feed placement.
- Treat the first-screen data as `entry click / DAU` and the feed-card data as exposure UV, click UV, UV click rate, exposure UV penetration, and click UV penetration benchmarks.
- Use home-page anchors to ground predictions: Kingkong area overall `11.62%`, Daily recommendation `7.30%`, Guess you like `2.84%`, Ranking `1.24%`, mini-player overall `46.59%`, song list main area `13.54%`, feed card area UV click rate `17.0%`, personalized music cards UV click rate `17.8%`.
- Remember that most users see only 1-3 feed cards; card placement depth strongly affects reach.
- Do not compare an unrelated commercial/growth card directly to high-intent personalized music cards unless the user intent and content value are similar.
- Distinguish first-screen click penetration from feed card UV click rate, landing arrival, downstream conversion, play/favorite behavior, and home-page interruption.

For topic-specific user-research tasks:

- Read only the smallest matching file under [research/](research/) when the task needs compressed qualitative research, audience understanding, positioning guardrails, or willingness-to-pay signals.
- Use these topic notes as qualitative decision guardrails, not as CTR baselines or precise sample reporting.
- Prefer them when the question is really about `用户为什么会接受 / 排斥 / 付费 / 留存 / 分享`, rather than purely about visual taste.
- Match topics narrowly:
  - AI songs and labeling: [research/AI歌曲专题-AI歌曲认知与平台态度-压缩版.md](research/AI歌曲专题-AI歌曲认知与平台态度-压缩版.md)
  - AI instruments and arrangement switching: [research/AI演奏家专题-AI演奏家与变乐器需求-压缩版.md](research/AI演奏家专题-AI演奏家与变乐器需求-压缩版.md)
  - children and parents: [research/儿童内容专题-儿童听歌与家长需求-压缩版.md](research/儿童内容专题-儿童听歌与家长需求-压缩版.md)
  - recommendation strategy: [research/推荐专题-汽水QQ酷狗推荐体验-压缩版.md](research/推荐专题-汽水QQ酷狗推荐体验-压缩版.md)
  - concept-edition review rules: [research/概念版专题-设计评审与过稿规律-压缩版.md](research/概念版专题-设计评审与过稿规律-压缩版.md)
  - artist fans: [research/艺粉专题-酷狗特色歌手粉丝洞察-压缩版.md](research/艺粉专题-酷狗特色歌手粉丝洞察-压缩版.md)
  - decoration and skins: [research/装扮专题-装扮用户需求-压缩版.md](research/装扮专题-装扮用户需求-压缩版.md)
  - membership and commercialization: [research/酷狗会员专题-会员触点与商业化设计规律-压缩版.md](research/酷狗会员专题-会员触点与商业化设计规律-压缩版.md)
  - ringtone: [research/铃声专题-酷狗铃声用户需求-压缩版.md](research/铃声专题-酷狗铃声用户需求-压缩版.md)
  - HiFi and sound quality: [research/音质专题-HiFi用户需求与平台选择-压缩版.md](research/音质专题-HiFi用户需求与平台选择-压缩版.md)

### 4. Keep the boundary honest

If the source doc was based on partial visible history rather than full exported chat logs, say so briefly when it matters.

Examples:

- a small-group report note may be a first-pass capture from currently visible messages
- an activity note may include partial image-message context without full OCR
- prize configs, popup rules, or rollout details may have changed over time and should remain configurable

## Default Heuristics

- Default to low-friction interaction: fewer steps, fewer confirmations, fewer buried rewards.
- Prefer explicit reward or benefit visibility over hiding incentives in rules text.
- Treat `模板化提效` as a real business strategy, not just a visual convenience.
- When chats show repeated iteration, design the implementation to be easy to update.
- When the task is really about a specific collaborator role, default to extracting their method of decision-making, validation standard, and reporting style before talking about pure visual form.
- If the user asks for direct execution, do the work instead of only summarizing the chat history.
- When the user gives long chat logs, recordings, or moving-target feedback, compress them into a short spec before acting:
  - `目标`
  - `关键动作`
  - `不能动`
  - `验证方式`
  - `来源语境`
- Prefer waiting until the core information is complete before making a strong judgment. If the evidence is partial, mark the confidence honestly instead of filling gaps with style-language guesses.

## Output Patterns

When responding after using this skill, prefer one of these shapes:

- `Context + recommendation`: brief reminder of the relevant imported context, then the recommendation.
- `Context + implementation rule`: what the historical chat implies the code or design should preserve.
- `Context + risk`: when the task conflicts with earlier agreed principles or depends on unstable historical details.
- `Context + compact spec`: for repeated review loops, implementation handoff, or tasks that need a stable `what / how / constraints / verify` frame.

## References

- [references/routing.md](references/routing.md): quick routing table and durable signals
- [references/spec-coding.md](references/spec-coding.md): lightweight spec-compression rules for turning noisy review context into stable execution constraints
- [references/kugou-signoff-lens.md](references/kugou-signoff-lens.md): Kugou internal signoff-convergence lens merged from `酷狗过稿第一人`
- [references/kugou-main-player-android-2026-05.md](references/kugou-main-player-android-2026-05.md): Android 2026 May main Kugou player-page click benchmarks and placement guardrails
- [references/kugou-main-home-android-click-baseline.md](references/kugou-main-home-android-click-baseline.md): main Kugou home-page first-screen and feed-card click benchmarks and placement guardrails
- [research/AI歌曲专题-AI歌曲认知与平台态度-压缩版.md](research/AI歌曲专题-AI歌曲认知与平台态度-压缩版.md): AI songs, labeling, and platform attitude guardrails
- [research/AI演奏家专题-AI演奏家与变乐器需求-压缩版.md](research/AI演奏家专题-AI演奏家与变乐器需求-压缩版.md): AI instrument-switching and arrangement demand guardrails
- [research/儿童内容专题-儿童听歌与家长需求-压缩版.md](research/儿童内容专题-儿童听歌与家长需求-压缩版.md): children-content, parent decision-maker, and family-value guardrails
- [research/推荐专题-汽水QQ酷狗推荐体验-压缩版.md](research/推荐专题-汽水QQ酷狗推荐体验-压缩版.md): recommendation surprise-vs-stability guardrails
- [research/概念版专题-设计评审与过稿规律-压缩版.md](research/概念版专题-设计评审与过稿规律-压缩版.md): concept-edition review heuristics in compressed research form
- [research/艺粉专题-酷狗特色歌手粉丝洞察-压缩版.md](research/艺粉专题-酷狗特色歌手粉丝洞察-压缩版.md): artist-fan segmentation and fan-operation guardrails
- [research/装扮专题-装扮用户需求-压缩版.md](research/装扮专题-装扮用户需求-压缩版.md): skins, decoration, and self-expression guardrails
- [research/酷狗会员专题-会员触点与商业化设计规律-压缩版.md](research/酷狗会员专题-会员触点与商业化设计规律-压缩版.md): membership, conversion, and commercialization guardrails
- [research/铃声专题-酷狗铃声用户需求-压缩版.md](research/铃声专题-酷狗铃声用户需求-压缩版.md): ringtone journey and willingness-to-pay guardrails
- [research/音质专题-HiFi用户需求与平台选择-压缩版.md](research/音质专题-HiFi用户需求与平台选择-压缩版.md): HiFi audience and sound-quality platform-choice guardrails
- [learning/README.md](learning/README.md): evolution-memory overview
- [learning/PROFILE.md](learning/PROFILE.md): stable learned preferences and review rules
- [learning/EVOLUTION_RULES.md](learning/EVOLUTION_RULES.md): how to distill each conversation
- [learning/SESSION_LOG.md](learning/SESSION_LOG.md): recent conversation learnings
- [learning/SESSION_TEMPLATE.md](learning/SESSION_TEMPLATE.md): standard log-entry template
- [learning/SCORECARD.md](learning/SCORECARD.md): pre-delivery quality scoring
- [learning/CREATIVE_ENGINE.md](learning/CREATIVE_ENGINE.md): structured creativity expansion and convergence
- [learning/ITERATION_PROTOCOL.md](learning/ITERATION_PROTOCOL.md): self-critique loop before delivery

## 作者说明页

- 见 [AUTHOR.md](AUTHOR.md)

## Author

Signed by Cruz Olli
