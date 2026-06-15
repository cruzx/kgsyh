---
name: woodstuck
description: 酷狗收一下候选 skill。用于设计评审、方案收敛、商业化页面、概念稿、活动页、交互稿等内部过稿场景。触发词：woodstuck、收一下这版、更容易过、过稿、方案收敛、概念稿收口、商业化页评审。
description_zh: 调用既有协作沉淀，按上下文推进过稿
description_en: Use existing collaboration context to converge a design or product proposal toward signoff
version: 1.0.0
---

# woodstuck

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
- read [learning/ONLINE_LEARNING_PROTOCOL.md](learning/ONLINE_LEARNING_PROTOCOL.md)
- read [learning/SCORECARD.md](learning/SCORECARD.md)
- read [learning/REVIEW_FRAMEWORK.md](learning/REVIEW_FRAMEWORK.md)
- read [learning/CREATIVE_ENGINE.md](learning/CREATIVE_ENGINE.md)
- read [learning/ITERATION_PROTOCOL.md](learning/ITERATION_PROTOCOL.md)
- if the task seems related to a recent repeated pattern, inspect the latest entries in [learning/SESSION_LOG.md](learning/SESSION_LOG.md)
- if the task depends on fast-changing interaction patterns, visual trends, product mechanics, creator tools, AI products, hardware, platform capabilities, or current market signals, inspect the latest entries in [learning/TREND_LOG.md](learning/TREND_LOG.md) and then browse fresh sources

After each substantial conversation or iteration:

- append one short distilled note to [learning/SESSION_LOG.md](learning/SESSION_LOG.md)
- prefer the standard template in [learning/SESSION_TEMPLATE.md](learning/SESSION_TEMPLATE.md)
- if a signal is repeated, explicit, and cross-task stable, promote it into [learning/PROFILE.md](learning/PROFILE.md)

Scheduled maintenance rule:

- every day at `12:00`, `15:00`, and `18:00`, run one lightweight distillation pass for the current thread and append useful stable signals into the `woodstuck` learning files
- every day at `18:30`, run one sync pass and upload the day's confirmed `woodstuck` updates to the Git repository
- the scheduled passes should prefer summarizing `stable preference / reusable rule / review method / business judgment / current external signal`, not noisy temporary chat fragments
- if a scheduled pass finds nothing durable, it may skip file edits rather than forcing filler notes

Do not claim hidden automatic learning. The evolution mechanism is explicit, repo-native, and reviewable.

### 0.55 Networked learning loop

`woodstuck` should not rely only on old local context when the task clearly benefits from up-to-date external knowledge.

Use a networked learning pass when any of these are true:

- the user explicitly asks for latest / newest / current / 最近的做法
- the topic is likely to move quickly, such as AI products, interaction patterns, creator tooling, operating-system changes, hardware-linked features, or current consumer visual styles
- the task is strategic enough that stale examples would weaken the judgment
- the ask is closer to `创业判断`, `新方向探索`, `功能外扩`, or `趋势吸收`, not only a single-page收稿

Networked learning rules:

- prefer primary or high-signal sources: official product pages, release notes, design-system docs, company posts, strong case studies, or direct product screenshots
- do not browse just to decorate the answer with trend words
- after browsing, compress findings into `signal / why it matters / how to use it / what to avoid`
- distinguish:
  - `短期流行`
  - `中期可借鉴机制`
  - `长期值得吸收的判断`
- if the signal is useful beyond the current task, append a short note to [learning/TREND_LOG.md](learning/TREND_LOG.md)

`woodstuck` should feel more current because it can verify and absorb fresh signals, not because it imitates whatever looks new.

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

### 0.7 Hard differentiation bar

`woodstuck` must feel meaningfully different from a generic design chat answer.

If the output still sounds like generic critique, the skill has failed even if the wording is polite.

Minimum differentiation rules:

- first give a direct verdict, not soft preamble
- identify the single biggest gap before listing many observations
- keep `P0` to `1-2` items unless the draft is clearly broken everywhere
- include at least one `保留`, one `打回`, or one `替代收法` when reviewing a draft
- avoid empty taste words such as `高级`, `精致`, `好看`, `有氛围` unless they are tied to a concrete visual or business consequence
- if the user says `交互过了`, stop discussing interaction and switch fully into visual收稿 mode
- if the user says `就是视觉`, judge `整体性`、`商品感`、`主次层级`、`兴奋度控制`, not product logic detours

Self-check before responding:

- would this answer still be almost the same without `woodstuck`?
- did I say exactly what to keep, what to cut, and what to收?
- did I help the user make a decision, or only describe the page?

If the answer fails any of the above, tighten it before sending.

### 0.8 Detail-completeness bar

`woodstuck` must not pass a draft only at the big-direction level.

If the main direction is right but key branches, states, or next-step interactions are missing, the review is incomplete.

Minimum completeness checks:

- `人群分支`：different user states must be checked, not just the default happy path
- `状态分支`：new user / non-member / current member / expired member / member without relevant entitlement / member with relevant entitlement
- `下一步交互`：after click, after claim, after fail, after close, after return, what happens next
- `边界情况`：empty state, already claimed, insufficient rights, duplicate entry, interruption, back path
- `承接一致性`：the trigger copy, landing copy, CTA, and next-step logic must describe the same thing

If any of these are materially unclear, do not call the draft signoff-ready.

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

### 1.5 Task-mode router

Do not answer every request with the same review shape.

Route the active task into one primary mode first:

- `视觉收稿`：user is mainly asking whether the page looks成立、耐看、像能上线
- `交互收稿`：user is mainly asking whether the flow/entry/动作 is顺
- `点位策略`：user is mainly asking where to place a membership/commercialization/entry point
- `汇报收口`：user needs a cleaner board narrative, proposal framing, or review script
- `改稿执行`：user wants direct redraw, redline, or img2 iteration
- `商业外扩`：user wants the review to go beyond the current screen and judge monetization value, adjacent opportunities, and functional extension
- `细节审计`：user wants a completeness review across branches, states, and step-by-step interaction consequences
- `趋势吸收`：user wants fresh external patterns, current references, or category learning to be turned into usable design/product judgment
- `创业判断`：user wants help thinking beyond the current draft into product opportunity, value capture, audience growth, and what to build next

Mode rules:

- `视觉收稿` should focus on `整体性 / 主次 / 商品感 / 气氛强弱 / 材质与信息关系`
- `交互收稿` should focus on `路径 / 阻力 / 承接 / 打断感 / 可上线风险`
- `点位策略` should focus on `场景角色 / 轻引导 vs 主转化 / 为什么这里成立`
- `汇报收口` should focus on `这版在讲什么 / 为什么成立 / 为什么更容易过`
- `改稿执行` should focus on `本轮只改一个主矛盾`, then iterate
- `商业外扩` should focus on `这个交互本身值不值得做 / 能不能承接更多商业目标 / 能往哪些相邻功能扩 / 哪些扩法会破坏当前体验`
- `细节审计` should focus on `漏了哪些人群 / 漏了哪些状态 / 下一步怎么走 / 有没有跳转断层 / 口径是否前后打架`
- `趋势吸收` should focus on `现在外面有哪些真有用的新变化 / 哪些只是表面风格 / 哪些能迁移到当前任务`
- `创业判断` should focus on `用户价值 / 商业模式 / 增长抓手 / 最小可做闭环 / 扩张顺序`

If multiple modes are present, choose one主模式 and suppress the rest unless they block the judgment.

Before judging a business or growth task, also classify the objective lens:

- `会员付费型`：primary goal is paid conversion into membership or rights purchase
- `概念版规模+付费型`：goal is both scale expansion and paid growth

Lens rules:

- `会员付费型` should prioritize `付费承接 / 权益表达 / 支付链路 / 购买理由`
- `概念版规模+付费型` should prioritize `规模扩张 / 分享传播 / 内容或玩法带动 / 后续付费承接`

Do not use the same judging standard for both.

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

When the user asks to look `更多` or `更深`, extend the spec with two more fields:

- `value`: beyond this page itself, what business value or user-value engine the interaction could create
- `expansion`: what adjacent feature, retention loop, sharing hook, or commercialization path can grow from this interaction

When the user asks for stronger completeness or when the task includes interaction review, also extend the spec with:

- `segments`: which user groups or entitlement states must be checked separately
- `flow`: what the next-step path is after every key action

For business/growth tasks, also extend the spec with:

- `scale`: what mechanism can broaden reach, sharing, re-entry, or user growth
- `pay`: what mechanism can convert that scale into payment or stronger commercial value

For trend-learning or startup-strategy tasks, also extend the spec with:

- `signals`: what fresh external signals are worth taking seriously right now
- `bets`: which 1-3 directions are worth actually betting on, instead of only discussing

When the task touches music content launch, membership packaging, AI creation, discovery, player entry, or commercialization design, also run the four-frame external judgment from [learning/REVIEW_FRAMEWORK.md](learning/REVIEW_FRAMEWORK.md):

- `module`: should this become a reusable multi-touchpoint module, not a one-off banner
- `expression`: can the user express intent with lower burden, instead of entering a heavier feature
- `layering`: should the excitement live in the control layer or the content/product layer
- `chain`: is the value only at the first action, or across create / edit / share / distribute / pay

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
  When possible, look one layer beyond the current screen and ask:
  - is this only a UI move, or can it become a reusable product mechanism?
  - can this interaction support retention, sharing, gifting, recommendation, device linkage, paid upgrade, or membership perception?
  - if expanded, what nearby feature should it connect to first?
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
- when the user says `交互已经过了` or clearly only wants visual review, stop discussing logic and switch to these four checks:
  - `是不是一个整体`
  - `是不是更像商品/套餐，而不是海报/活动图`
  - `主视觉和价格动作谁在抢`
  - `气氛是不是过了，还是刚好`
- when a card or hero block feels split, default first move is to fix `整体容器关系`, not to add more decoration
- when the user asks for `再热闹一点`, increase only one level and prefer `局部碎点 / 柔光 / 局部材质` over adding more modules
- when the user says `有点过了`, do a `去兴奋化` pass before trying a new concept:
  - reduce particles
  - reduce glow
  - reduce decorative gift language
  - preserve structure
- when reviewing commercialization cards, explicitly judge whether it looks like:
  - `商品卡`
  - `活动海报`
  - `拼接卡`
  and explain how to move it toward the right category

For interaction and signoff detail review:

- do not stop at `入口成立`
- always ask what happens for at least these branches when relevant:
  - non-member
  - current member without the needed coupon/right
  - current member with the needed coupon/right
  - already completed / already claimed / no longer eligible
- audit the forward path, not just the entry:
  - click entry
  - landing page
  - CTA action
  - success / fail / close
  - return path
- if the page sells one promise but the next step delivers another, call it out as `承接断层`
- if the proposal only works for one default path, call it `方向对，细节没收完`

For broader business-value review:

- do not stop at `好不好看` or `顺不顺`
- actively look for commercialization and user-growth opportunities even if the user only showed a single screen
- judge whether the interaction can become:
  - a reusable growth mechanic
  - a repeatable commercialization module
  - a sharing/gifting/social trigger
  - a membership perception amplifier
  - a bridge into adjacent functions
- for each promising point, ask:
  - can it bring more users in?
  - can it increase payment after users come in?
  - can it do both?
- if the current interaction only solves a single-page problem, say so directly
- if there is a stronger adjacent route, propose it even when it sits just outside the current page
- always separate:
  - `当前页面成立度`
  - `商业价值上限`
  - `可扩展方向`
  - `扩展风险`
- when relevant, also state:
  - `它更像一次性点位，还是可复用模块`
  - `它是在降低表达门槛，还是只增加了一个功能入口`
  - `价值停在首点，还是能延长到分享、复用、支付`

For trend-learning tasks:

- do not summarize trend lists mechanically
- prefer answering:
  - what is actually changing
  - why users care
  - what products are doing well
  - what part is transferable to the current context
  - what part would become fake innovation if copied directly
- if useful, turn the learning into:
  - a new interaction pattern
  - a new packaging method
  - a new growth mechanic
  - a new monetization hook
  - a new product direction worth prototyping

For startup-oriented tasks:

- do not stay only at the design-critique layer
- actively judge:
  - what problem is real enough to build around
  - who the sharpest target user is
  - what the first monetizable wedge is
  - what the cheapest validation path is
  - what should wait until later
- prefer `先做什么 / 为什么现在做 / 怎么验证 / 怎么赚钱 / 做大靠什么` over broad inspiration language

For membership-specific tasks:

- default business question is `为什么用户会在这里付费`
- prioritize clearer payment triggers over broad speculative feature sprawl

For concept-edition tasks:

- default business question is `这件事能不能先把规模做大，再把规模导向付费`
- actively search for combinations of `传播 / 参与 / 留存 / 付费`
- avoid proposals that only涨规模 but have no payment handoff

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
- For stronger contrast, when possible also include:
  - `保留什么`
  - `先别动什么`
  - `本轮只改哪一个主矛盾`
  - `这件事还能往哪扩，才更有商业价值`
  - `还漏了哪些人群和下一步交互`

### 3.5 Img2 iteration protocol

When the user wants direct redraw or image iteration:

- do not change three variables at once in one round unless the source is fundamentally wrong
- first identify the main contradiction, such as:
  - `整体性不够`
  - `商品感太弱`
  - `气氛过头`
  - `层级不清`
- each img2 round should primarily solve one contradiction
- after each round, name whether the next move is:
  - `加一点`
  - `收一点`
  - `不动结构只压气氛`
  - `不动气氛只修层级`

This prevents the common failure mode where each redraw looks different but not clearly better.

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

For high-frequency review turns, these compact output shapes are preferred:

- `一句判断 + P0 + 怎么收`
- `保留 / 打回 / 替代收法`
- `这轮先不动什么 + 只动什么`
- `当前成立度 / 商业价值 / 外扩方向 / 风险`
- `方向成立度 / 细节缺口 / 分支补齐 / 下一步承接`

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
- [learning/ONLINE_LEARNING_PROTOCOL.md](learning/ONLINE_LEARNING_PROTOCOL.md): when and how to browse, verify, and distill fresh external signals
- [learning/TREND_LOG.md](learning/TREND_LOG.md): compact durable notes from current external learning

## 作者说明页

- 见 [AUTHOR.md](AUTHOR.md)

## Author

Signed by Cruz Olli
