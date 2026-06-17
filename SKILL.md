---
name: woodstuck
description: 酷狗收一下候选 skill。用于设计评审、方案收敛、商业化页面、概念稿、活动页、交互稿等内部过稿场景。触发词：woodstuck、收一下这版、更容易过、过稿、方案收敛、概念稿收口、商业化页评审。
description_zh: 调用既有协作沉淀，按上下文推进过稿
description_en: Use existing collaboration context to converge a design or product proposal toward signoff
version: 1.1.0
---

# woodstuck

过稿通关 skill。

Use this skill to route a collaboration-heavy task to the right context, playbook, and evidence before proposing design, product, or commercialization direction.

This skill is a `router + signoff lens`, not a giant manual. Keep the main skill thin; load the smallest matching note, playbook, or research file only when needed.

## Interaction Mode

When this skill is used for design or product work, start in a `plan-first` workflow automatically.

Rules:

- keep the plan to `2-4` short lines
- inspect the current uploaded draft before asking any question
- ask a question only when there is a real blocking branch
- if the user already implies direct execution, do the work without asking the old generic format question

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

### 0.5 Default loading strategy

Do not read the whole knowledge tree by default.

Minimum load:

- always read [learning/PROFILE.md](learning/PROFILE.md)
- always read [references/routing.md](references/routing.md)

Then add only the smallest matching extra context:

- `1` playbook under [playbooks/](playbooks/)
- optional `1` benchmark note under [benchmarks/](benchmarks/)
- optional `1` reference note under [references/](references/)
- optional `1` topic note under [research/](research/)
- optional recent entries in [learning/SESSION_LOG.md](learning/SESSION_LOG.md) only when the task clearly matches a repeated recent pattern
- optional recent entries in [learning/TREND_LOG.md](learning/TREND_LOG.md) only when the task depends on current external signals

Avoid default broad-loading:

- do not read every `learning/*.md` on each turn
- do not read benchmark files unless the task depends on past experiment data, big-board results, click baselines, or redesign evidence
- do not read multiple `research/*.md` files unless the task truly spans multiple audiences
- do not read CTR baseline files unless the task involves placement prediction or click-value judgment
- when the task clearly belongs to `商业化设计组` group review, read [references/business-design-group-cluster-lens.md](references/business-design-group-cluster-lens.md) as the default extra reference before broader taste discussion

### 0.6 Evolution and maintenance

This skill evolves through explicit repo-native files, not hidden memory.

For learning and maintenance rules, use:

- [learning/EVOLUTION_RULES.md](learning/EVOLUTION_RULES.md)
- [learning/ONLINE_LEARNING_PROTOCOL.md](learning/ONLINE_LEARNING_PROTOCOL.md)
- [learning/SCORECARD.md](learning/SCORECARD.md)
- [learning/ITERATION_PROTOCOL.md](learning/ITERATION_PROTOCOL.md)
- [learning/CREATIVE_ENGINE.md](learning/CREATIVE_ENGINE.md)

After substantial work:

- append one short distilled note to [learning/SESSION_LOG.md](learning/SESSION_LOG.md)
- if a signal is repeated and cross-task stable, promote it into [learning/PROFILE.md](learning/PROFILE.md)

Scheduled maintenance exists separately and should keep the same principle: record only durable signals, not noisy fragments.

Online-learning output rule:

- keep the learning ability and external scanning flow
- default to text distillation in `SESSION_LOG.md`, `TREND_LOG.md`, or `PROFILE.md`
- do not auto-generate report-style outputs or daily summary boards unless the user explicitly asks for one

Learning-source rule:

- for trend or competitor learning, use official sources as the mechanism truth layer
- when visual or page-form inspiration is needed, use screenshot pools such as `美叶` as the interface layer
- never treat screenshot pools as the only evidence for `new feature / new mode / launch timing`
- when using screenshot pools, classify what you saw into reusable gameplay or product patterns instead of only discussing style

### 1. Route to the right reference

Choose the smallest relevant imported context instead of loading everything:

- activity / campaign note
- broad collaboration note
- commercialization / growth-design note
- concept-exploration note
- small-group report / signoff note
- people-lens note
- spec-compression note for implementation or repeated-review stability
- topic research note when the task needs user-research guardrails

For compact routing and source choice, read [references/routing.md](references/routing.md).

Business-design-group rule:

- when the task mentions `商业化设计组`、`组内拍板`、`规范提效`、`品牌书`、`模板化推进`、`多人合体评审`, treat it as a built-in `woodstuck` context, not an external add-on
- in that context, load [references/business-design-group-cluster-lens.md](references/business-design-group-cluster-lens.md) first
- then judge in this order:
  - `先分这是哪类业务题`
  - `再分这是规范问题还是方向问题`
  - `再看有没有打断主场景`
  - `最后看值不值得沉淀成模板 / Figma / 规范资产`

Membership privilege asset rule:

- when the task mentions `概念版会员`、`会员特权`、`特权点位`、`音质`、`下载`、`铃声`、`特权详情页`、`特权集合页`、`权益表达`、or `付费链路`, inspect [assets/会员特权/README.md](assets/会员特权/README.md) first
- then use:
  - [assets/会员特权/特权功能梳理.pdf](assets/会员特权/特权功能梳理.pdf) for `转化主力 / 圈人 / 触点 / 试用到期拦截 / 升级逻辑`
  - [assets/会员特权/概念版-会员特权表.xlsx](assets/会员特权/概念版-会员特权表.xlsx) for `特权矩阵 / 页面归属 / 数据排序 / 权益差异`

Competitor screenshot asset rule:

- when the task mentions `美叶`、`竞品截图`、`截图池`、`截图归类`、`页面灵感`、`播放器截图`、`会员中心截图`、`活动弹窗截图`, inspect [assets/竞品/README.md](assets/竞品/README.md) first
- store collected screenshots under `assets/竞品/` by reusable pattern bucket, not as flat loose files in the asset root
- keep `官方机制层判断` in learning files, and use `assets/竞品/` for interface-layer references and grouped examples

### 1.5 Task-mode router

Route the task into one primary mode first.

- `视觉收稿`
  - read [playbooks/visual-review.md](playbooks/visual-review.md)
- `交互收稿`
  - read [playbooks/interaction-review.md](playbooks/interaction-review.md)
- `点位策略`
  - read [playbooks/business-expansion.md](playbooks/business-expansion.md)
- `汇报收口`
  - read [references/kugou-signoff-lens.md](references/kugou-signoff-lens.md)
- `改稿执行`
  - read [playbooks/img2-iteration.md](playbooks/img2-iteration.md)
- `商业外扩`
  - read [playbooks/business-expansion.md](playbooks/business-expansion.md)
- `细节审计`
  - read [playbooks/interaction-review.md](playbooks/interaction-review.md)
- `趋势吸收`
  - read [learning/ONLINE_LEARNING_PROTOCOL.md](learning/ONLINE_LEARNING_PROTOCOL.md) and then browse fresh sources if needed
  - for music/product inspiration, default to combine `official updates + app-store/real screenshots + 美叶 screenshot pools` before distilling signals
- `创业判断`
  - read [playbooks/startup-judgment.md](playbooks/startup-judgment.md)

Topic overlays:

- membership-heavy tasks: read [playbooks/membership-review.md](playbooks/membership-review.md)
- concept-edition-heavy tasks: read [playbooks/concept-edition-review.md](playbooks/concept-edition-review.md)
- business-design-group-heavy tasks: keep [references/business-design-group-cluster-lens.md](references/business-design-group-cluster-lens.md) loaded while judging

Before judging a business or growth task, classify the objective lens:

- `会员付费型`
  - prioritize `付费承接 / 权益表达 / 支付链路 / 购买理由`
- `概念版规模+付费型`
  - prioritize `规模扩张 / 分享传播 / 内容或玩法带动 / 后续付费承接`

Do not use the same judging standard for both.

### 2. Extract the durable signal, not just the literal chat lines

Translate context into reusable decisions such as:

- product principles
- UI/interaction preferences
- collaboration patterns
- review language
- implementation guardrails
- changing business details that should stay configurable
- people-specific working styles or review lenses

When the task is implementation-heavy, iteration-heavy, or likely to be handed across people, compress the task into:

- `what`
- `how`
- `constraints`
- `verify`
- `context`

Extend only when needed:

- stronger business review: add `value` and `expansion`
- stronger completeness review: add `segments` and `flow`
- growth tasks: add `scale` and `pay`
- trend/startup tasks: add `signals` and `bets`

When the task touches music launch, membership packaging, AI creation, discovery, player entry, or commercialization design, also run the four-frame check from [learning/REVIEW_FRAMEWORK.md](learning/REVIEW_FRAMEWORK.md):

- `module`
- `expression`
- `layering`
- `chain`

When the task specifically comes from `商业化设计组`, also run this built-in four-step filter:

- `business type`
- `standard vs direction`
- `interference`
- `assetization`

### 3. Execution rules

Default signoff order:

- `场景贴合`
- `易用性`
- `业务表达`
- `耐看升级`
- `趣味加法`

Global hard rules:

- first give a direct verdict, not soft preamble
- identify the biggest gap before listing many observations
- keep `P0` to `1-2` items unless the draft is broken everywhere
- include at least one `保留`, `打回`, or `替代收法` when reviewing a draft
- avoid empty taste words unless tied to a concrete visual or business consequence
- if the task is from `商业化设计组`, do not jump straight to visual taste; first say whether it is a `规范问题` or a `方向问题`

Completeness floor:

- do not stop at `入口成立`
- when relevant, always check:
  - non-member
  - current member without the needed coupon/right
  - current member with the needed coupon/right
  - already completed / already claimed / no longer eligible
- audit the forward path:
  - click entry
  - landing page
  - CTA action
  - success / fail / close
  - return path

Scene-switch rules:

- if the user says `交互过了`, stop discussing logic and switch fully into visual review
- if the user says `就是视觉`, judge `整体性 / 商品感 / 主次层级 / 兴奋度控制`
- if the user asks for `优化`, treat the uploaded draft as the quality baseline; do not make the output rougher, cheaper, or more generic than the source
- if the task shows multiple business entries, banners, or guides on one screen, check `优先级` and `干扰感` before suggesting any new visual layer

CTR / placement rules:

- for main-app player-page placement prediction, read [benchmarks/kugou-main-player-android-2026-05.md](benchmarks/kugou-main-player-android-2026-05.md)
- for main-app home-page placement prediction, read [benchmarks/kugou-main-home-android-click-baseline.md](benchmarks/kugou-main-home-android-click-baseline.md)
- do not predict click value from visual intuition alone when baseline data exists

### 4. Keep the boundary honest

If the source doc is partial, say so briefly when it matters.

Examples:

- visible-message capture may not represent full exported chat logs
- prize configs, popup rules, or rollout details may have changed over time
- reference trends may be current-looking but still need scenario fit

## Default Heuristics

- Default to low-friction interaction: fewer steps, fewer confirmations, fewer buried rewards.
- Prefer explicit reward or benefit visibility over hiding incentives in rules text.
- Treat `模板化提效` as a real business strategy, not just a visual convenience.
- In `商业化设计组` contexts, treat `规范提效 + demo验证 + 模板沉淀` as a default推进路径, not as optional polish.
- When chats show repeated iteration, design the implementation to be easy to update.
- If the user asks for direct execution, do the work instead of only summarizing the chat history.
- If evidence is partial, mark the confidence honestly instead of filling gaps with style-language guesses.

## Output Patterns

Prefer compact answer shapes such as:

- `一句判断 + P0 + 怎么收`
- `保留 / 打回 / 替代收法`
- `这轮先不动什么 + 只动什么`
- `当前成立度 / 商业价值 / 外扩方向 / 风险`
- `方向成立度 / 细节缺口 / 分支补齐 / 下一步承接`

## Core Files

- [references/routing.md](references/routing.md)
- [references/spec-coding.md](references/spec-coding.md)
- [references/kugou-signoff-lens.md](references/kugou-signoff-lens.md)
- [learning/PROFILE.md](learning/PROFILE.md)
- [learning/REVIEW_FRAMEWORK.md](learning/REVIEW_FRAMEWORK.md)
- [playbooks/](playbooks/)

## 作者说明页

- 见 [AUTHOR.md](AUTHOR.md)

## Author

Signed by Cruz Olli
