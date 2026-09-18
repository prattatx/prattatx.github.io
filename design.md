# Design: prattatx.github.io

The locked design system for this site. Every page reads this file before any
visual change. Do not regenerate it per page: extend or amend it when the system
needs to grow.

**Status: v2, shipped.** v1 codified the dark system. v2 is a direction change
derived from two studied references, and is implemented in
`assets/css/main.css`. Every contrast figure below is computed from the shipped
hex, not estimated.

Where this file and the design notes in `CLAUDE.md` disagree, this file wins and
`CLAUDE.md` should be updated to match.

### Token name mapping

v2 kept v1's token *names* rather than renaming to `--paper` / `--ink`, because
renaming would have touched every rule in a 1,500-line stylesheet for no
functional gain. The doc vocabulary maps to the shipped names as:

| This doc | Shipped token |
|---|---|
| `--paper` / `--paper-2` / `--paper-3` | `--bg` / `--bg-subtle` / `--bg-muted` |
| `--rule` / `--rule-strong` | `--border` / `--border-strong` |
| `--ink` / `--ink-2` / `--ink-3` | `--text` / `--text-2` / `--text-3` |

`--font-ui` is new in v2 and carries the sans structure voice; `--font-body` is
now the serif.

## Provenance

v1 derived from Personal Brand System tokens v1.0 (2026-05-24). The brand book is
the origin, not the ongoing authority: this file is.

v2 is a **studied-DNA** direction. Two public reference sites were read via
`hallmark study` in URL mode, structure only, no pixels copied and no signature
work reproduced:

- **maggieappleton.com** — warm light paper, serif body, multi-hue accent system,
  Utopia fluid scale, footer-as-nav. Source of the *temperature*.
- **c82.net** — achromatic chrome, sans structure over serif body, dense
  auto-fill grids, work-carries-the-colour. Source of the *strategy*.

Neither site's content, imagery, or licensed fonts are used. Canela (Appleton) is
a paid retail family and is not adopted.

## Direction

The problem v2 solves, measured on the v1 build:

1. **One flat plane.** All four v1 surfaces sat inside 10.6% lightness, so
   nothing read as in front of anything.
2. **No warmth.** 19 palette hues, 2 outside the cool range, both status dots.
   Every neutral sat at hue 264–275.
3. **Over-signalled engineer.** One display weight plus 23 uppercase-mono
   treatments read as a monitoring dashboard, not 26 years of judgment.
4. **The record was invisible.** 358 patents and 9 publications rendered as a
   filterable table and a list.

v2's answer, in one line: **the chrome recedes and the record carries the
page.** Warm off-white paper, sans structure over serif body, one quiet accent
for wayfinding, and the patent and publication data promoted from table to
rendered artifact.

On light paper the surface steps are necessarily close together (1.07:1 and
1.31:1 below). That is not a repeat of problem 1: on light, depth comes from
rules and type weight rather than lightness, and the content is now what carries
visual interest. Problem 1 was flat chrome *plus* nothing else to look at.

## Genre

**Editorial.** The site is a document, not a product surface. Type carries the
design, rules carry the structure, and the single accent is rare enough to mean
something.

## Macrostructure families

Four families. A page picks the family its content belongs to and varies only
the archetypes that family allows.

- **Landing** (`/`): Stat-Led. Hero, then a stat rail, then labelled sections on
  a varied rhythm. One page only.
- **Index** (`/work/`, `/research/`, `/speaking/`, `/writing/`, `/about/`):
  Long Document. Page head, then labelled sections carrying rows, lists or cards.
- **Document** (9 case studies, `/cv/`, `/presentations/*/`): Long Document,
  dense variant. Page head, optional meta grid, then prose under mono section
  rules.
- **Tool** (`/patents/`): Workbench. Page head, figure, filter row, then a table.
  The only family where interactive state is a first-class concern.

## Theme: "Signal"

Light only. Warm off-white paper, never pure white: `#ffffff` reads flat and
synthetic, and the reference that uses it gets away with it only because
saturated artwork supplies the warmth.

The neutrals are not grey. Every one sits at hue 75 to 85, the warm side, with
chroma ramping 0.006 at the lightest to 0.023 at the darkest. That warmth is
the point of v2 and is the single most important thing to preserve if the
palette is ever regenerated.

All values verified by computation, not estimated.

| Token | Hex | OKLCH | On `--paper` |
|---|---|---|---|
| `--paper` | `#faf8f4` | `oklch(98.0% 0.006 85)` | paper |
| `--paper-2` | `#f3f0ea` | `oklch(95.6% 0.009 85)` | 1.07:1 |
| `--paper-3` | `#e1dace` | `oklch(89.2% 0.017 82)` | 1.31:1 |
| `--rule` | `#e0dad0` | `oklch(89.0% 0.015 81)` | 1.31:1 |
| `--rule-strong` | `#948977` | `oklch(62.4% 0.024 84)` | 3.24:1 |
| `--ink` | `#26231f` | `oklch(25.8% 0.009 75)` | 14.75:1 |
| `--ink-2` | `#46413a` | `oklch(37.8% 0.013 76)` | 9.53:1 |
| `--ink-3` | `#6d665c` | `oklch(51.4% 0.018 77)` | 5.34:1 |
| `--accent` | `#4f52d4` | `oklch(51.5% 0.195 276)` | 5.67:1 |
| `--accent-text` | `#4341c4` | `oklch(46.5% 0.197 276)` | 7.09:1 |
| `--on-accent` | `#ffffff` | `oklch(100% 0 0)` | 6.02:1 on accent |

The indigo is deliberate continuity: `#4f52d4` is the value the v1 **print**
stylesheet already used for light surfaces, so the brand hue survives the
direction change rather than being discarded.

### Accent discipline

One accent, three jobs. The chrome recedes so the record can carry the page, so
accent coverage stays under roughly 3% of any viewport, tighter than v1's 5%.

- `--accent`: fills, rules, list markers, the playhead. 5.67:1, so unlike v1 it
  is legible as text too, but reserve it for graphical use.
- `--accent-text`: indigo that is text. 7.09:1.
- `--on-accent`: white on a filled accent. 6.02:1.

Status hues (`--ok`, `--info`) carry over from v1 and are re-derived for light
paper at implementation time. v1's four-indigo split is retired: on light paper
one accent clears every floor, so the extra tokens were solving a dark-only
problem.

### v1 accent discipline *(still shipping until v2 lands)*

Four indigos, each with one job:

- `--accent`: fills, rules, the playhead, list markers. Graphical only, where
  the 3:1 threshold applies. **Never carries text.**
- `--accent-solid`: filled controls only. White on it is 4.99:1. White on
  `--accent` is 4.47:1 and fails AA, which is the entire reason this token
  exists.
- `--accent-text`: any indigo that *is* text. 6.57:1.
- `--accent-hover`: hover and active text states.

Accent coverage stays under roughly 5% of any viewport.

### Contrast floors

Not to be lowered:

| Role | Floor | v2 value |
|---|---|---|
| Headings | 12:1 | 14.75:1 (`--ink`) |
| Body copy | 8:1 | 9.53:1 (`--ink-2`) |
| Muted labels | 4.5:1 | 5.34:1 (`--ink-3`) |
| Indigo as text | 6.5:1 | 7.09:1 (`--accent-text`) |
| Control boundaries | 3:1 | 3.24:1 (`--rule-strong`) |
| Graphical marks | 3:1 | 5.67:1 (`--accent`) |

`--rule` (1.31:1) is a **decorative hairline only** and may never bound a
control; that is what `--rule-strong` is for. Nothing renders below 11px.

v2 has no equivalent of `--text-4`. The tier existed to squeeze a fourth step
out of a dark ramp and was the source of a documented floor violation.

## Typography

A 2+1 pairing, inverted from v1: **sans carries structure, serif carries
reading.** That inversion is the main fix for "reads like a dashboard."

- **Structure and display**: Inter 500/600/700. Already self-hosted, four
  weights present, so no new font files are needed for this role. Tracking
  -0.02em to -0.035em at display sizes. Roman always; no italic headings.
- **Body**: **Source Serif 4** (OFL), self-hosted and variable across 200 to 900,
  so body at 400 and `strong` at 600 come from one roman file. Stack:
  `'Source Serif 4', 'Iowan Old Style', 'Palatino Linotype', Palatino, Georgia,
  serif`. Georgia is the universal floor and is genuinely good at body sizes.
- **Mono** (outlier): unchanged stack, but **scope reduced**. Mono is now for
  data only: patent numbers, dates, figures, axis labels, tabular columns. It
  is no longer the voice of section labels, nav links, tags or the footer.

**Cal Sans is retired in v2.** It was the display face at a single weight, and
its job moves to Inter. This is the largest single call in the proposal and the
easiest to reverse: it is one token.

Numerals: `tabular-nums` on any column of figures. Hero and stat figures stay
proportional on purpose.

### The mono budget

v1 shipped 23 uppercase-mono treatments and that is most of why the site
over-signalled engineer. v2 caps mono at **data contexts only**. Section labels
become real headings in Inter at a real size, not 12px mono caps.

### Type scale

Every size resolves to a token. There are no raw `font-size` values in the
screen stylesheet, so the whole site retunes from the token block.

Fixed steps: `--text-2xs` 11px (the floor), `--text-xs` 12, `--text-sm` 13,
`--text-md` 14, `--text-base` 15, `--text-lg` 16, `--text-xl` 17, `--text-2xl`
18, `--text-3xl` 20, `--text-4xl` 22, `--text-5xl` 24.

Fluid steps, named by role: `--text-lede`, `--text-lede-hero`, `--text-quote`,
`--text-post-h2`, `--text-stat`, `--text-page-h1`, `--text-display-s`,
`--text-display`, `--text-display-sm`.

**11px is a hard floor.** Nothing renders smaller.

## Spacing

A 4pt scale named by multiple: `--s1` is 0.25rem, `--s4` is 1rem, `--s24` is
6rem. Steps: 1, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 24, 32.

Use named tokens. Raw rem values in markup are drift.

Widths: `--content` 1080px, `--narrow` 720px, `--rail` 88px. Measure caps at
68ch for prose, 42 to 62ch for ledes, 84ch for dense CV lists.

Radii: `--r-sm` 4px, `--r-md` 8px, `--r-lg` 12px, `--r-xl` 16px, `--r-full`.

## Motion

Two easing curves, and only two:

- `cubic-bezier(.4, 0, .2, 1)` for all state transitions, at `--t-fast` 100ms,
  `--t-base` 180ms, `--t-slow` 320ms.
- `cubic-bezier(.16, 1, .3, 1)` at 520ms for the single scroll reveal.

Rules:

- Animate `transform` and `opacity` only. Never layout properties. A `height`
  or `width` transition is drift, however small.
- **One orchestrated entrance per page.** The stat rail on `/` is it. Sections
  do not fade in as you scroll; the page settles once and stays settled.
- Focus rings appear instantly. Never transition `outline`.
- `prefers-reduced-motion: reduce` collapses everything.

### The signal rail

A fixed-seed waveform down the left edge, drawn in `assets/js/site.js`, with
scroll position as the playhead. Deterministic by design: the same trace every
visit. Below 1000px it collapses to a 2px top progress bar.

It is grounded in the actual work (sleep EEG, edge audio, ambient sensing) and
it is **the site's only decorative gesture. Do not add a second motif.**

**The hero field (2026-09-18).** The rail runs as a 1px thread in a gutter
nobody reads, while the landing hero carries roughly 480px of empty paper to
the right of a 42ch lede. The same signal now opens into that column as an
11-channel montage: same seed, same generator, so it is the first motif given
room rather than a second one. Active and overlapping beside the name, with
burst packets, settling to a flat line by the buttons, the way a recording
winds down. `--border-strong`, the rail's own resting trace, so no accent is
spent. Static: no entrance, no scroll response, because the stat rail is the
page's one orchestrated entrance. Hidden below 1100px, where the lede closes
the gap it lives in. Renders nothing with JavaScript off, which is correct,
since it carries no information the page needs.

The bar for a future addition here is unchanged and high: it must be the same
signal, generated by the same seeded function, or it is a second motif and the
answer is no.

## Microinteraction stance

- Silent success. No toasts, no celebratory confirmation, no modals.
- Hover and `:focus-visible` always ship together. Any affordance that appears
  only on hover is invisible to touch and keyboard, and is drift.
- Hover treatments belong only to elements that are actually links. Rows are
  read, not clicked, and carry none.
- Filters use `aria-pressed`; search filters live with a visible result count.
- Hover backgrounds are solid, never gradients: `transition: background` cannot
  interpolate a gradient and will snap.

## CTA voice

- **Primary**: filled `--accent-solid`, `--on-accent` label, `--r-md`, padding
  `--s3` by `--s5`, trailing arrow that translates 3px on hover and focus.
- **Secondary**: 1px `--border-strong`, `--text` label, identical geometry.
- **Inline**: `--accent-text`, trailing arrow, no box. For "read on" links.
- Labels are short enough never to wrap. Clickable text is a one-line object.

## The record as artifact

The v2 move that matters most, and the one neither v1 nor either reference's
chrome supplies. 358 granted patents across two decades and 9 peer-reviewed
publications are the strongest assets on this site and v1 rendered them as a
filterable table and a bulleted list.

The rule: **the record is drawn, not tabulated.** The patents page leads with a
rendered view of the whole portfolio, and the table is the accessible companion
beneath it rather than the main event.

### The field (shipped)

`/patents/` opens with 358 marks, one per grant, stacked into 16 year columns.
Column height is still the year count, so it remains a histogram, but the unit
is the patent: the whole portfolio is physically present on the page.

- **Encoding**: one accent hue, three weights. In force is a filled mark and
  sits on the baseline; too-recent is outlined; expired is a neutral fill and
  stacks on top. Marks are sorted within each column so the statuses band
  instead of speckling.
- **What it reveals**: the older years are largely lapsed and the recent years
  almost entirely in force. That is ordinary maintenance-fee pruning, and the
  bar chart it replaced could not show it at all. The chart now carries an
  argument, not just a count.
- **Interaction**: sixteen keyboard stops, one per year column, each announcing
  its year, grant count and in-force count. Per-patent detail rides a `title`
  for pointer users. Marks dim rather than disappear when a filter narrows the
  set, so the whole is always legible against the part.
- **Accessibility**: the table below remains the complete data view, and a
  visually-hidden summary tracks the filter state.

This is where the site's colour and visual interest come from. It is why the
chrome is allowed to be quiet: something else is carrying the page.

Constraints that still bind: one series means one colour, thin marks over thick
blocks, hairline baselines, no gridlines, labels on first/peak/last, hover
enhances rather than gates, and a table view always exists. Real counts only,
never an invented figure.

### The homepage curve (shipped 2026-09-18)

The third drawn record, and it took the new positional encoding the rule above
demands: a continuous cumulative line, where `/patents/` owns discrete year
columns and `/research/` owns lanes across time. It carries the accumulation
rate, which a per-year histogram cannot show, and it lands on exactly 358. The
two definition lists stay beneath it as the accessible companion, which is the
point: the record section used to be only those lists, on the one page that has
to convert.

Generated by `_gen/record_curve.py`, never hand-drawn, and the generator
refuses to emit anything if the cumulative total does not equal the published
grant count. The chart may not state a figure the record does not.

Two mechanics worth keeping if this encoding is reused. Every label is HTML
rather than SVG text, because text inside a viewBox scales with the graphic and
an 11px label would render near 4px once the curve is 350px wide, straight
through the type floor. And the final year is dashed and labelled "to date",
because a part-year count flattens the curve and reads as decline when the data
only says the year is not over.

## Section heads

A mono-caps label on a hairline, with an optional right-aligned count. The
label **is** the section heading and ships as `<h2>`.

- No ordinal numbers. These sections are a set, not a sequence.
- Never place a label directly above another heading. That is an eyebrow.
- The tag-left / heading-right two-column head is banned outright.

## Per-page allowances

- Landing may vary section rhythm via `.section--tight` and `.section--open`.
- Index and Document families keep an even rhythm: they are lists and documents,
  and varying their spacing is decoration rather than structure.
- Tool may introduce interactive state, and only Tool may.
- Typography carries every page. No family gets decorative hero enrichment:
  no stock imagery, no gradient field, no abstract ornament bought in to fill
  space. **Amended 2026-09-18.** The Landing hero may carry the signal rail's
  own trace in its empty column (see The signal rail). The rule this replaces
  read "no family gets hero enrichment" flatly, which the hero field would have
  broken; the line it is actually defending is that nothing arrives in a hero
  that is not already the site's own material.

## What pages MUST share

- The wordmark, the mono chrome voice, and the nav.
- The accent tokens and their four separate jobs.
- Cal Sans and Inter, and the mono outlier for labels.
- The CTA voice: shape, radius, padding rhythm, arrow behaviour.
- The section-head pattern.
- One entrance, two easings, `transform` and `opacity` only.

## What pages MAY differ on

- Macrostructure, within the family the page belongs to.
- Row versus card versus table for listing content.
- Section rhythm, on the Landing family only.
- Meta grids and prev/next, on the Document family only.

## Charts

One series means one colour. Thin marks, not thick blocks. Solid hairline
baseline, no gridlines. Labels on first, peak and last only. Hover enhances and
never gates. A table view always exists.

## Print

Print is the light surface, and the CV PDF is rendered from `/cv/` through it.
The print palette is tokenized (`--p-ink`, `--p-body`, `--p-accent`, three rule
weights) and declared inside the first `@media print` block. A raw hex in a
print rule is a value that will not follow a brand change into the PDF.

## Resolved

All six questions raised when this file was first written are closed.

1. **`--border-strong` raised to 3.06:1** (was `#3d4761`, 2.04:1). It bounds six
   interactive controls (nav toggle, ghost buttons, filter buttons, patent
   search, load-more, co-inventor chips), so WCAG 1.4.11 asks 3:1. The new value
   stays in the same hue family, so the neutral ramp is undisturbed.
2. **`::selection` moved to `--accent-solid`**, 4.99:1. It was the only place
   white sat on `--accent` (4.47:1, failing AA) and the only violation of the
   accent-discipline rule above.
3. **A named type scale exists.** Every screen `font-size` resolves to a token;
   there are no raw values left. This also closed a floor violation: three
   selectors (`.contact-links .k`, `.meta-grid dt`, `.case-nav .k`) rendered at
   10px against a documented 11px floor, and now sit at `--text-2xs`.
4. **Reduced motion narrowed.** It collapses spatial motion and keeps colour,
   instead of zeroing every transition and taking hover and focus feedback with
   it.
5. **`css/main.css` deleted.** A pre-rebuild stylesheet (Work Sans, `width:70%`)
   nothing referenced. Recoverable from git history if it is ever wanted.

## Open questions

1. **`about` and `cv` use `<p class="mono dl-head">` where `index` uses `<h3>`**
   for the identical pattern. The `<p>` version is arguably wrong: it labels the
   list below it and should be a heading. Fixing it changes the heading outline
   on both pages, so it wants a deliberate call.
2. **`--accent-solid` is now identical to `--accent`.** On light paper one value
   clears both the graphical and the on-white floors, so the split that v1
   needed is redundant. Kept as a distinct token so call sites did not have to
   change; collapse it if the palette is ever regenerated.

## Resolved after v2 shipped

Kept here because the reasoning constrains future work, not just the outcome.

- **Source Serif 4 is self-hosted.** Two files, roman and italic, each variable
  across 200 to 900, so body at 400 and `strong` at 600 both come from the roman
  with no synthetic bolding. The italic is the full variable range rather than a
  pinned 400 instance, so emphasis inside `strong` is not synthesised either.
  The roman is preloaded next to inter-400. `assets/fonts/LICENSE-OFL.md` now
  carries the OFL text for both bundled families.
- **`CLAUDE.md` corrected** to the light system, and the deploy race documented.
- **`/research/` is drawn, as three lanes across time.** The deliberate call the
  old question asked for: nine items do **not** warrant a unit chart, because
  nine is already legible as a list and the column heights would top out at two.
  What the list genuinely hid was the shape. Three research lines that ran in
  sequence, and the years between them. One lane per line, one mark per
  publication, placed in its year. Marks stay a single accent on purpose:
  `/patents/` already spends fill, muted and outline on grant status, and
  reusing those three treatments for a different variable would put the two
  pages in conflict. **If a third drawn record is ever added, give it a new
  positional encoding rather than a fourth mark treatment.**
- **The portrait is mounted.** Measured, its edges meet the paper at 16 to 18:1,
  which made it the highest-contrast element on the site, above headings at
  14.75:1. The inherited 1px `--border` cannot resolve against a black edge. The
  system has no shadows, so depth was not available; the photo is matted instead,
  paper then `--bg-muted` then image, with concentric radii of 8px inside an 8px
  mount inside 16px. **The rule this sets: mediate a hard tonal meeting with a
  surface tone, never by introducing elevation.**
- **`.github/workflows/static.yml` deleted.** Pages is `build_type: legacy` on
  `master:/`, so Jekyll is the intended builder. The workflow uploaded the raw
  repository as a competing Pages artifact on every push to master; had it won
  the race, every page would have served its front matter as visible text.

## On changing the look

This file codifies what shipped. If the visual direction changes, this file is
what gets amended first, and then the pages follow. The parts most likely to
move, in the order they would move:

- **Type.** Cal Sans is doing all the display work at one weight. It is the most
  replaceable decision here and the one with the largest effect.
- **The accent.** A single indigo carries every emphasis on the site, which is
  disciplined but also the reason the page reads as one flat temperature.
- **Surface depth.** The paper and its four elevations sit inside 11% lightness.
  That is very close together, so the page reads as one plane.
- **The rhythm.** Section spacing now varies on the landing page only.

What would survive any redesign: the mono label voice, the hairline structure,
one accent used rarely, tabular figures, the contrast floors, and the signal
rail as the only motif.

## Exports

Portability formats. `tokens.css` mirrors what ships; the rest are conversions
for reuse elsewhere.

### tokens.css

```css
:root {
  --bg:            #0f1117;
  --bg-subtle:     #151820;
  --bg-muted:      #1c2030;
  --bg-overlay:    #232840;

  --border:        #2e3547;
  --border-muted:  #232a3a;
  --border-strong: #3d4761;

  --text:          #f0f1f3;
  --text-2:        #a3aabb;
  --text-3:        #98a0b2;
  --text-4:        #767e92;
  --text-inv:      #0f1117;

  --accent:        #6366f1;
  --accent-solid:  #5b5ee8;
  --accent-text:   #8b8ef7;
  --accent-hover:  #a5a7fa;
  --accent-subtle: rgba(99, 102, 241, 0.12);
  --accent-border: rgba(99, 102, 241, 0.35);

  --ok:            #22c55e;
  --ok-soft:       rgba(34, 197, 94, 0.16);
  --info:          #38bdf8;
  --on-accent:     #ffffff;

  --font-display: 'Cal Sans', 'SF Pro Display', system-ui, sans-serif;
  --font-body:    'Inter', 'SF Pro Text', system-ui, sans-serif;
  --font-mono:    ui-monospace, 'SF Mono', 'JetBrains Mono', Menlo, monospace;

  --s1: .25rem;  --s2: .5rem;   --s3: .75rem;  --s4: 1rem;
  --s5: 1.25rem; --s6: 1.5rem;  --s8: 2rem;    --s10: 2.5rem;
  --s12: 3rem;   --s16: 4rem;   --s20: 5rem;   --s24: 6rem;
  --s32: 8rem;

  --r-sm: 4px; --r-md: 8px; --r-lg: 12px; --r-xl: 16px; --r-full: 9999px;

  --content: 1080px;
  --narrow:  720px;
  --rail:    88px;

  --t-fast: 100ms cubic-bezier(.4, 0, .2, 1);
  --t-base: 180ms cubic-bezier(.4, 0, .2, 1);
  --t-slow: 320ms cubic-bezier(.4, 0, .2, 1);
  --t-reveal: 520ms cubic-bezier(.16, 1, .3, 1);
}
```

### Tailwind v4 `@theme`

```css
@theme {
  --color-bg:           oklch(17.8% 0.013 271);
  --color-bg-subtle:    oklch(21.0% 0.017 269);
  --color-border:       oklch(33.0% 0.033 268);
  --color-text:         oklch(95.8% 0.003 265);
  --color-text-2:       oklch(73.8% 0.026 268);
  --color-accent:       oklch(58.5% 0.204 277);
  --color-accent-text:  oklch(69.0% 0.152 280);

  --font-display: 'Cal Sans', system-ui, sans-serif;
  --font-body:    'Inter', system-ui, sans-serif;
  --font-mono:    ui-monospace, 'SF Mono', Menlo, monospace;

  --spacing-4:  1rem;
  --spacing-6:  1.5rem;
  --spacing-12: 3rem;
  --spacing-24: 6rem;

  --radius-md: 8px;
  --radius-lg: 12px;

  --ease-standard: cubic-bezier(.4, 0, .2, 1);
  --ease-reveal:   cubic-bezier(.16, 1, .3, 1);
}
```

### DTCG `tokens.json`

```json
{
  "color": {
    "bg":          { "$value": "oklch(17.8% 0.013 271)", "$type": "color" },
    "bg-subtle":   { "$value": "oklch(21.0% 0.017 269)", "$type": "color" },
    "border":      { "$value": "oklch(33.0% 0.033 268)", "$type": "color" },
    "text":        { "$value": "oklch(95.8% 0.003 265)", "$type": "color" },
    "text-2":      { "$value": "oklch(73.8% 0.026 268)", "$type": "color" },
    "accent":      { "$value": "oklch(58.5% 0.204 277)", "$type": "color" },
    "accent-text": { "$value": "oklch(69.0% 0.152 280)", "$type": "color" }
  },
  "font": {
    "display": { "$value": "Cal Sans", "$type": "fontFamily" },
    "body":    { "$value": "Inter",    "$type": "fontFamily" }
  },
  "space": {
    "sm": { "$value": "1rem",   "$type": "dimension" },
    "md": { "$value": "1.5rem", "$type": "dimension" },
    "lg": { "$value": "3rem",   "$type": "dimension" }
  }
}
```

### shadcn/ui CSS variables

```css
:root {
  --background:         17.8% 0.013 271;
  --foreground:         95.8% 0.003 265;
  --primary:            55.9% 0.204 277;
  --primary-foreground: 100%  0     0;
  --muted:              28.6% 0.031 266;
  --muted-foreground:   73.8% 0.026 268;
  --border:             33.0% 0.033 268;
  --input:              33.0% 0.033 268;
  --ring:               58.5% 0.204 277;
  --radius:             8px;
}
```
