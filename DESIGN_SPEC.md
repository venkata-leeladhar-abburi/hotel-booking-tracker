# StayWatch deck — design spec (v2)

Revision after review: one palette for the whole deck, real photography, no decorative
fake UI, larger type throughout.

## Canvas
Fixed 1280 x 720 design space (16:9), CSS-scaled to any viewport. Margins 72 / 60 / 56.
Print: one slide per landscape page.

## Colour — ONE system, no second palette
| Token | Value | Used for |
|---|---|---|
| `--page` | #FAFAF8 | every light slide |
| `--card` | #F1F1EE | bento cards, strips |
| `--ink` | #14151A | headlines, card titles |
| `--ink-2` | #3C3F46 | body copy |
| `--muted` | #7A7E87 | captions, labels, descriptions |
| `--line` | #E4E4E1 | hairlines |
| `--accent` | #1F5FD8 | **only** live product data: prices, drops, key figures |
| `--accent-soft` | #9DC2FF | the same blue on dark/photo backgrounds |
| `--dark` | #111216 | legal section — same ink family, not a new world |
| `--dark-card` | #191A1F | legal cards |

No orange, no gradients, no glass. Photographs carry all other colour, and are graded to
one tonal family (saturation 0.90, contrast 1.03) so they sit together.

## Type — unchanged, sizes raised for readability
- Display: **Instrument Serif**. Hero 78px, slide title 52px.
- UI: **Geist** (fallback Inter Tight).
- Raised from v1: card title 19 → 21px, card body 13.5 → 15.5px, list text 12.5 → 15px,
  footnotes 11.5 → 12.5px, lede 17 → 18px. Body never below 15px.
- Stats use tabular figures.

## Photography
Full-bleed on the hero; a 176px band at the top of each persona card. Always `object-fit:
cover`, never stretched. Credits in `images/CREDITS.md` and on the Sources slide.

## Cards
Radius 20px, flat `--card` fill, no shadow on light slides, 1px hairline on dark.
No floating chips, no blur, no 3D.

## Rules
One idea per slide · ≤40 words of body · every number footnoted with a link · no emoji.

---

## Deck structure (30 slides)

| # | Slide | Visual |
|---|---|---|
| 1 | Title | Full-bleed photograph |
| 2 | The problem | Line chart, price after booking |
| 3 | Who faces it | 4-card photo bento |
| 4 | Solution in one line | 4-step flow |
| 5 | App + WhatsApp | Phone mock + chat mock |
| 6 | User journey | Horizontal timeline |
| 7 | Market size | Stat bento |
| 8 | Existing solutions | 6-card bento |
| 9 | Competitor deep dive | Comparison table |
| 10 | Positioning map | 2×2 plot |
| 11 | Drawbacks and risks | 6-card bento with mitigations |
| 12 | How we stand out | 6-card bento |
| 13 | MVP features | 10-card grid |
| 14 | App screens | 3 phone mock-ups |
| 15 | Admin dashboard | Desktop mock-up |
| 16 | Support playbook | Cards + case table |
| 17 | Version 2 and later | 3 tiers of tiles |
| 18 | Architecture | 5-column flow diagram |
| 19 | Where prices come from | 4-step flow + two cards |
| 20 | Data source options | 4 cards + warning strip |
| 21 | Tech stack | Wordmark tiles |
| 22 | Legal and compliance | **Dark** — checklist cards |
| 23 | Case law and our rules | **Dark** — cases + allowed/not-allowed table |
| 24 | Business model | 3 cards + 2 |
| 25 | Costs and unit economics | Price table + derivation |
| 26 | Go-to-market | 6-card bento |
| 27 | Roadmap | Timeline with gates |
| 28 | Scaling features | 6-card bento |
| 29 | Metrics | 8 stat cards |
| 30 | Sources | Grouped link index |

Dark treatment is used **only** on slides 22–23.

## Renaming the product
`src/tail.html` holds one constant (run `python3 build.py` after changing it):

```js
const PRODUCT_NAME = "StayWatch";
```

It fills every `[data-name]` element, derives the forwarding domain for `[data-domain]`,
and sets `<title>`. Changing that one string renames the product across the whole deck —
verified with zero leftovers.

## Navigation
Arrow keys, space, Page Up/Down, Home/End; click right third forward, left third back;
`#n` in the URL deep-links to a slide. Print to PDF gives one landscape page per slide.

## Delivery
`index.html` is one self-contained file (~1.2 MB): the 5 photographs are re-encoded at
display size (hero 1920 px, persona bands 640 px) and inlined as base64, and the two fonts
(Instrument Serif, Geist — latin + latin-ext) are inlined as woff2. It makes no network
requests; it renders the same offline. It is built by `build.py` from `src/` (slides, shell,
fonts) and `images/` (source photos and credits) — edit those, never `index.html` directly.
The slide-nav pill hides while the mouse is still and reappears on movement.

## Verified
All 30 slides measured at the 1280×720 canvas: every slide with a footer clears the rule
by 21–39 px (25–26 px on 24 of them), nothing clipped inside cards or phone screens, no
element past a margin, all 5 photographs decode from the file, 85 external source links,
all `rel="noopener"`.
