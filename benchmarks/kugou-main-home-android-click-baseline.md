# Kugou Main Home Android Click Baseline

## Source And Scope

- Source asset: `assets/kugou-main-home-android-click-baseline.png`
- User-provided screenshot: Kugou main app home page data slide.
- Platform: Android main Kugou home page.
- Metric definitions shown in source:
  - First-screen click penetration: `entry click / DAU`.
  - Information-flow card data includes exposure UV, click UV, UV click rate, per-user play count, per-user favorite count, exposure UV penetration, click UV penetration.
- Data entry method: transcribed from the provided annotated screenshot. Treat as directional benchmark unless raw backend data is later provided.

## High-Level Reading

Home page traffic is concentrated in a few high-intent modules. Commercial/growth entries should benchmark against the closest home-page zone instead of using generic CTR assumptions.

Durable signals:

- The first-screen high-traffic zones are bottom tab, mini-player/current song bar, lyrics/song interactions, top tools, and the core recommendation modules.
- In the top grid, only `每日推荐`, `猜你喜欢`, and `排行榜` are meaningful high-click modules; most other grid modules are under 1%.
- Information-flow music recommendation cards have strong performance: card area overall UV click rate `17.0%`, personalized music card overall `17.8%`.
- Exposure size and click rate must be read together. Some low-exposure modules have high UV click rate but limited total contribution.
- Existing commercial/growth entries should avoid comparing themselves only to high-intent music content modules unless they share similar user intent.

## First-Screen Click Penetration

Metric: `entry click / DAU`.

### Page / Navigation / Top Tool Area

| Area / Action | Click Penetration |
|---|---:|
| Homepage monthly average exposure UV shown in source | 4220w |
| Top tab group area | 3.7% |
| Top headphone / listening tool | 8.4% |
| Top menu / more | 7.4% |
| Red-packet / reward icon | 0.26% |
| Refresh / change action | 1.37% |
| Promo strip: video yearly card / drama prompt | 26.4% |

### Kingkong / Grid Area

| Module | Click Penetration |
|---|---:|
| Kingkong area overall | 11.62% |
| Daily recommendation | 7.30% |
| Guess you like | 2.84% |
| Ranking | 1.24% |
| Listen to books | 0.29% |
| Singer | 0.16% |
| Children area | 0.05% |
| Songbook / score | 0.01% |
| Performance tickets | 0.01% |
| Music apps | 0.01% |
| Rhythm game | 0.01% |
| Music alarm | 0.01% |
| Record player | 0.01% |
| National cleaning | 0.01% |
| Playlist | 0.59% |
| Category | 0.72% |
| Scene music | 0.53% |
| Healing music | 0.12% |
| Record store | 0.01% |
| Celebrity livestream | 0.01% |
| AI singing | 0.01% |
| Circles | 0.00% |
| Ringtone / color ring | 0.03% |
| Charging animation | 0.01% |
| Singing/dancing hall | 0.01% |

Source note: except `Daily recommendation`, `Guess you like`, and `Ranking`, other grid module click rates are below 1%.

### Feed / Song List / Mini-Player / Bottom Tabs

| Area / Action | Click Penetration |
|---|---:|
| Song list personalized title / main song area | 13.54% |
| Personalized song section title | 1.41% |
| Song cover / image area | 2.77% |
| Refresh | 0.50% |
| More | 0.87% |
| Long press song | 1.63% |
| Double-tap song | 0.43% |
| Expand more | 4.42% |
| Mini-player overall | 46.59% |
| Mini-player play/pause | 14.32% |
| Bottom tab: Music | 86.5% |
| Bottom tab: Listen | 1.1% |
| Bottom tab: Live | 1.0% |
| Bottom tab: Me | 38.1% |

## Information-Flow Card Exposure Count Distribution

Excludes Kingkong area.

| Number of exposed cards | User Share |
|---|---:|
| 1 | 27.05% |
| 2 | 35.77% |
| 3 | 18.63% |
| 4 | 8.32% |
| 5 | 4.28% |
| 6-10 | 4.46% |
| 10+ | 1.49% |
| Total | 100.00% |

Implication: most users see only 1-3 feed cards. A growth/commercial card placed too deep in the feed will have sharply reduced reach.

## Information-Flow Card Module Benchmarks

| Module | Exposure UV | Click UV | UV Click Rate | Play / User | Favorite / User | Exposure UV Penetration | Click UV Penetration |
|---|---:|---:|---:|---:|---:|---:|---:|
| Card area total | 10219.3w | 1738.4w | 17.0% | 3.49 | 0.05 | / | / |
| Personalized music cards total | 6757.1w | 1206.0w | 17.8% | 2.87 | 0.06 | / | / |
| Personalized music cards share | 66.1% | 69.4% | / | / | / | / | / |
| Exclusive recommendation | 2503.3w | 474.6w | 18.9% | 6.14 | 0.05 | 50.2% | 9.5% |
| Single: personal exclusive songs | 2205.9w | 454.3w | 20.6% | 4.52 | 0.08 | 44.3% | 9.1% |
| Single: you may be interested | 863.5w | 183.0w | 21.7% | 2.51 | 0.14 | 17.3% | 3.7% |
| Single: hot good songs selected | 583.0w | 104.4w | 17.9% | 2.79 | 0.04 | 11.7% | 2.1% |
| Single: VIP exclusive recommendation | 551.1w | 99.8w | 18.1% | 2.80 | 0.04 | 11.0% | 2.0% |
| Single: recommendation by song | 540.8w | 84.6w | 15.7% | 2.30 | 0.06 | 10.8% | 1.7% |
| Single: recommendation by singer | 404.7w | 57.3w | 14.2% | 1.58 | 0.03 | 8.1% | 1.1% |
| Single: trend tasting | 385.6w | 52.5w | 13.6% | 1.27 | 0.03 | 7.7% | 1.1% |
| Single: new song recommendation | 361.6w | 47.2w | 13.1% | 1.88 | 0.03 | 7.3% | 0.9% |
| Single: niche treasure works | 302.8w | 32.5w | 10.7% | 0.60 | 0.02 | 6.1% | 0.6% |
| Single: daily theme music | 281.2w | 36.7w | 13.1% | 1.13 | 0.01 | 5.6% | 0.7% |
| Single: classic nostalgic golden songs | 276.5w | 53.6w | 19.5% | 2.52 | 0.03 | 5.5% | 1.1% |
| Ranking | 237.3w | 17.5w | 7.3% | 2.58 | 0.05 | 4.7% | 0.3% |
| New-user recommendation guide | 114.3w | 1.0w | 0.9% | 0.00 | 0.00 | 2.3% | 0.0% |
| Video | 112.3w | 8.2w | 7.2% | 0.48 | 0.00 | 2.2% | 0.2% |
| Audio / books | 107.2w | 10.0w | 9.3% | 0.79 | 0.00 | 2.1% | 0.2% |
| Music livestream | 88.9w | 6.6w | 7.5% | 0.04 | 0.00 | 1.8% | 0.1% |
| Sing chat | 76.2w | 3.5w | 4.6% | 0.02 | 0.00 | 1.5% | 0.1% |
| Fish sound | 59.4w | 3.0w | 5.1% | 0.02 | 0.00 | 1.2% | 0.1% |
| Mall | 47.3w | 1.5w | 3.2% | 0.00 | 0.00 | 0.9% | 0.0% |
| Hot programs | 46.9w | 1.5w | 3.1% | 0.00 | 0.00 | 0.9% | 0.0% |
| Followed singer new-song card | 21.9w | 2.9w | 13.2% | 0.00 | 0.00 | 0.4% | 0.1% |
| Music station | 16.9w | 0.8w | 4.7% | 19.32 | 0.13 | 0.3% | 0.0% |
| Theme playlist | 13.5w | 0.6w | 4.2% | 0.79 | 0.01 | 0.3% | 0.0% |
| Music short video | 8.6w | 0.4w | 4.1% | 0.81 | 0.00 | 0.2% | 0.0% |
| Healing music | 3.4w | 0.2w | 5.2% | 0.00 | 0.00 | 0.1% | 0.0% |
| Novel card | 2.7w | 0.1w | 2.9% | 0.00 | 0.00 | 0.1% | 0.0% |
| Livestream selected | 1.6w | 0.0w | 1.6% | 0.00 | 0.00 | 0.0% | 0.0% |
| Real-time audio recommendation / long audio | 0.4w | 0.1w | 30.5% | 0.00 | 0.00 | 0.0% | 0.0% |
| Single: revisit favorite | 0.3w | 0.0w | 7.3% | 1.78 | 0.01 | 0.0% | 0.0% |
| Other | 0.2w | 0.0w | 9.3% | 0.00 | 0.00 | 0.0% | 0.0% |

## How To Use In Review

Use this reference when reviewing Kugou main app home-page designs, first-screen entries, Kingkong modules, recommendation cards, feed cards, mini-player prompts, bottom-tab ideas, or home-page commercial/growth placements.

When predicting conversion:

- Use `entry click / DAU` for first-screen entrance predictions.
- Use `UV click rate`, `exposure UV penetration`, and `click UV penetration` together for information-flow card predictions.
- Do not overvalue a high UV click rate if exposure UV penetration is near zero.
- For feed cards, remember most users see only 1-3 cards; placement order is a major determinant of reach.
- For commercial/growth entries inside music recommendation contexts, compare against non-music modules and existing low-intent modules, not only against strong personalized music cards.

## Placement Guardrails

- First-screen Kingkong modules below the top 3 generally benchmark below `1%` click penetration.
- Mini-player is an extremely high-attention zone (`46.59%` overall), but commercial insertion there risks strong interference with listening intent.
- Music-personalized feed cards can achieve `17%-22%` UV click rate when intent is aligned; this should not be used as a default benchmark for unrelated commercial cards.
- Feed card exposure count drops sharply after the first 3 cards. If a new card needs reach, place it in the first 1-3 exposures or package it into a stronger existing module.
- For growth cards, prefer explicit benefit/reward visibility and low-friction interaction, but validate against downstream conversion rather than only entrance CTR.

Recommended guardrails:

- Primary: entry click penetration, card UV click rate, landing-page arrival, conversion/claim/play completion.
- Secondary: exposure UV penetration, click UV penetration, per-user play count, per-user favorite count, repeat exposure.
- Guardrail: feed skip, home bounce, music playback interruption, bottom-tab diversion, negative feedback.
