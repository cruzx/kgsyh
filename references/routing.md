# Collaboration Context Routing

## Source Types

- imported activity/project note
- imported concept-exploration note
- imported commercialization / growth-design note
- imported UX feedback note
- imported design-ops / team-learning note
- imported small-group report / signoff note
- imported people-lens note
- spec-compression note for implementation or repeated-review stability
- topic research note for user-understanding, willingness-to-pay, and positioning guardrails

## Which Context To Read

### 1. Activity / Campaign Context

Read the imported activity note when the task mentions:

- a time-bounded campaign
- rewards, sharing, invite flow, prize configuration
- meme-style or themed interaction
- iterative activity rules

Durable signals:

- reward visibility matters
- entry points should stay complete
- low-barrier play beats heavy gating
- style consistency matters across copy, motion, and visuals
- unstable prize or rule details should stay configurable

### 2. Broad Collaboration Context

Read the broad collaboration note when the task mentions:

- concept exploration
- commercialization design
- product experience feedback
- AI design exploration
- engineering handoff or debugging support

Durable signals:

- some notes capture organization-level AI learning and design-ops infrastructure
- some notes capture a high-value pool of concrete UX defects and confusion points
- some notes capture AI-design validation and reporting-confidence concerns
- some notes capture practical local-debugging and troubleshooting collaboration
- when the task mixes design judgment with execution or handoff risk, turn the context into a compact `what / how / constraints / verify / context` spec before acting

### 3. Commercialization / Growth Context

Read the commercialization note when the task mentions:

- member touchpoints
- payment conversion
- cancel-recovery
- benefit perception
- card-based AI entry
- category-specific commercialization design
- Kugou main-app player page entries, star cards, commercial cards, floating rewards, lyrics/cover overlays, or player-page placement decisions
- Kugou main-app home page first-screen entries, Kingkong modules, information-flow cards, recommendation cards, mini-player prompts, bottom-tab ideas, or home-page commercial/growth placements

Durable signals:

- designs are evaluated through business value, conversion, retention, and extensibility
- repeated-play potential, randomness, and low-friction mechanics matter in activity design
- AI entry flows should be card-based or preset-driven to lower startup cost
- strong solutions are expected to become reusable strategy assets, not just one-off pages
- for main-app player placement decisions, read `benchmarks/kugou-main-player-android-2026-05.md` and ground CTR predictions in the 2026 May Android player-page click benchmarks
- for main-app home-page placement decisions, read `benchmarks/kugou-main-home-android-click-baseline.md` and ground CTR/click-penetration predictions in first-screen and feed-card benchmarks
- when the task explicitly mentions `商业化设计组`, day-to-day group review, template/brand-book buildup, repeated popup/card normalization, or a need to borrow the merged judgment style of multiple internal reviewers, also read `references/business-design-group-cluster-lens.md`

### 4. Small-Group Report / Signoff Context

Read the small-group report note when the task mentions:

- quick design signoff
- template-first execution
- popup guideline refinement
- blended or lighter-weight guidance patterns
- category template expansion

Durable signals:

- this is a small-group report-and-signoff context
- template-building is used to stabilize quality when source materials are inconsistent
- popup design often gets normalized toward lighter color use, clearer layout, less flashy titles, and more refined imagery
- blended guidance patterns can be preferred over hard popup dependence

### 4.5 Business-Design Group Cluster Context

Read `references/business-design-group-cluster-lens.md` when the task mentions:

- `商业化设计组`
- 多人合体评审
- 组内拍板口径
- 规范提效
- 品牌书 / 模版 / Figma 资产沉淀
- “这更像规范问题还是方向问题”
- 一个页面上多个业务入口一起抢位

Durable signals:

- common optimization should be normalized into standards when possible
- the first split is often `business type`, then `direction issue vs standard issue`
- interference control matters as much as visual polish
- promising ideas still need demo, data, or a reuse path before being over-sold
- this context often tries to turn one review outcome into a reusable asset

### 5. Concept Exploration Context

Read the concept-exploration note when the task mentions:

- first-screen conversion clarity
- seasonal operation packaging
- playful activity mechanics
- content listening/book-listening packaging
- decorative or thematic skin exploration
- concept-edition operational posters, membership festival visuals, brand-book checks, or concept operations design drafts
- concept-edition UI pages, cards, popups, member surfaces, or design-system style checks

Durable signals:

- proposals should lead with background, core idea, and review ask
- first-screen clarity and stronger key-entry emphasis matter a lot
- fun ideas are welcome, but structural clarity and texture consistency are still strict
- good concept designs often become reusable operational templates
- when the task is specifically about concept operations visual style, read the dedicated concept operations brand-book skill/reference first before giving taste-level feedback
- when the task is specifically about concept UI, also read the concept UI guidelines so the review does not confuse page UI with poster-style operation branding

### 6. Spec Compression Context

Read `references/spec-coding.md` together with the smallest matching note when the task mentions:

- repeated revisions or review churn
- implementation handoff
- long chat logs, recordings, or research dumps
- uncertainty around what is stable vs provisional
- a need to make the advice easier to reuse or report upward

Durable signals:

- do not answer too early from incomplete evidence
- compress noisy context into explicit execution rules
- preserve `what / how / constraints / verify / context` across rounds
- use verification language, not style confidence alone

### 7. Topic Research Context

Read the smallest matching file under `research/` when the task mentions:

- recommendation strategy, surprise vs stability, or cross-platform recommendation comparison
- AI songs, AI covers, AI labeling, or AI music-zone rules
- AI instruments, arrangement switching, or scenario-based alternate versions
- children content, parent decision-making, child membership, or family listening
- decoration, skins, badges, pendants, or self-expression commerce
- membership touchpoints, membership value expression, or payment-conversion rationale
- ringtone, clipping, ringtone tools, setting flow, or ringtone monetization
- HiFi, lossless, mastering, source trust, or sound-quality positioning
- artist fans, fan identities, rankings, support tasks, or fan monetization
- concept-edition review heuristics when the ask is closer to qualitative user/review规律 than to live collaboration routing

Durable signals:

- these files are compressed qualitative research notes, useful for `why users accept / reject / pay / stay / share`
- use them as decision guardrails, not as precise sample-size reporting or CTR baselines
- read only one topic note unless the task clearly spans multiple audiences or value systems
- when both collaboration context and research context apply, use collaboration notes for approval language and research notes for user-behavior guardrails

## Role Mapping

- `strategic reviewer`: checks whether the business or design logic is convincing
- `top-level approver`: focuses on shape accuracy, color comfort, realism, and avoiding misleading transitions or semantics
- `direction amplifier`: pushes immersion, motion, upgrade potential, and showcase value
- `system builder`: frames design as reusable method, validation process, or scalable asset

## Synthesis Rules

- Read only the smallest relevant source set.
- If the task is about a specific person-like role, read `references/people.md` together with the smallest matching source note.
- If two notes conflict, prefer the more specific and more recent one.
- If imported context conflicts with the current user instruction, obey the current user.
- If the task is implementation-heavy, use imported context as guardrails, not as a substitute for reading the current code.
- If the task is both collaboration-heavy and iteration-heavy, read `references/spec-coding.md` as the control layer before finalizing recommendations or edits.
- If the task is both review-heavy and research-heavy, combine one collaboration note with one `research/` topic note instead of broad-loading multiple research files.
