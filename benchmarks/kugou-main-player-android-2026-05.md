# Kugou Main Player Android Click Baseline · 2026-05

## Source And Scope

- Source asset: `assets/kugou-main-player-android-2026-05-click-map.png`
- User-provided screenshot: Android main Kugou player page click map.
- Period: 2026 May daily average.
- Platform: Android.
- Metric definition shown in source: denominator is unified as player page UV; numerator is each button/action click UV.
- Data entry method: transcribed from the provided annotated screenshot. Treat as directional benchmark unless raw backend data is later provided.

## High-Level Reading

The player page has very uneven click distribution. Core playback and lyric actions dominate. Commercial or new growth entries should avoid fighting the highest-intent music controls unless the goal is short-term exposure.

Durable signals:

- Central playback controls are the strongest attention/action zone.
- Lyrics area has very high engagement and can distort experiments if a growth entry is placed too close to lyrics.
- Cover area has meaningful click intent, but long-press/double-tap behaviors are lower.
- Side bars and top-right tools are moderate-to-low attention zones.
- Existing floating reward entry has non-trivial visibility, but claim conversion is much lower than close/ignore behavior.

## Click Benchmarks

### Top And Side Areas

| Area / Action | Click UV / Player Page UV |
|---|---:|
| Top-right first icon | 0.86% |
| Top-right second icon | 2.29% |
| Left side bar | 6.15% |
| Right side bar | 2.54% |

### Cover Area

| Area / Action | Click UV / Player Page UV |
|---|---:|
| Tap cover | 6.43% |
| Long press cover | 2.35% |
| Double-tap favorite | 1.42% |

### Lyrics Area

| Area / Action | Click UV / Player Page UV |
|---|---:|
| Tap lyrics | 18.34% |
| Swipe lyrics | 7.18% |
| Lyrics overall | 22.70% |
| Long press lyrics | 1.10% |

### Floating Reward Entry

| Area / Action | Click UV / Player Page UV |
|---|---:|
| Floating entry close / ignore area | 8.68% |
| Floating entry primary claim button | 2.80% |

Interpretation: a floating reward element may attract attention, but the close/ignore rate can exceed the primary claim click rate. Use this as a guardrail against overestimating conversion from visibility alone.

### Artist / Tag Row

| Area / Action | Click UV / Player Page UV |
|---|---:|
| Artist name | 2.64% |
| Follow | 0.14% |
| VIP tag | 0.11% |
| High quality | 0.93% |
| Sound effect | 1.28% |
| Accompaniment | 0.43% |
| Video | 0.46% |

### Middle Action Row

| Area / Action | Click UV / Player Page UV |
|---|---:|
| Comment / discuss icon | 0.38% |
| Download / VIP download | 1.42% |
| Ringtone | 0.32% |
| Like / favorite | 13.21% |
| Comment bubble | 9.10% |
| More menu | 8.27% |

### Progress And Device Area

| Area / Action | Click UV / Player Page UV |
|---|---:|
| Progress left area | 4.88% |
| Progress right / drag area | 26.90% |
| Bluetooth device label | 0.33% |

### Playback Controls

| Area / Action | Click UV / Player Page UV |
|---|---:|
| Playback mode | 10.21% |
| Previous song | 10.25% |
| Play / pause | 45.68% |
| Next song | 25.66% |
| Playlist | 12.47% |

## How To Use In Review

Use this reference when reviewing Kugou main app player-page entries, especially star cards, commercial cards, membership/reward prompts, floating buttons, lyric overlays, or cover-area interactions.

When predicting conversion:

- Do not treat high visual exposure as equal to effective conversion.
- Compare a proposed entry with nearby baseline zones. If it sits near the cover, use cover tap `6.43%` as a rough upper-neighbor reference; if it sits near side bars, compare against `2.54%-6.15%`; if it sits as a floating reward entry, compare against primary claim `2.80%` and close/ignore `8.68%`.
- For stable long-term player-page entry, prefer moderate-attention areas that preserve playback controls and lyrics, unless the campaign intentionally accepts higher interruption.
- For short-term campaign push, higher-interruption placements may raise CTR but must be checked against player exit, playback interruption, and close/ignore rates.

## Star Card Demo Implications

For明星星光卡 / star card player entries:

- A small cover-adjacent entry can reasonably target a CTR around the low-to-mid cover/side benchmark range if the benefit is clear.
- A large card occupying the cover area may raise CTR above a small entry, but risks interfering with normal cover/lyrics attention and should be constrained to fans or campaign windows.
- A corner-peel or decorative reveal pattern needs clear affordance. If users read it as decoration, it may underperform despite a nice motion effect.
- Always distinguish `entry CTR` from `landing arrival`, `card claim`, and `post-claim retention`.

Recommended guardrails:

- Primary: entry CTR, landing-page arrival rate, card claim rate.
- Secondary: card use/show rate, repeated player visits, fan vs non-fan segment split.
- Guardrail: player exit rate, playback interruption, close/ignore rate, return rate, non-fan negative feedback.
