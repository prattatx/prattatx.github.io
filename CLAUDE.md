# CLAUDE.md: prattatx.github.io

Personal site for James H. Pratt, Ph.D. Read this before changing anything.

## What this site is

A public credibility surface for **advisory work**, not a job-search site. James is CEO of Fyve
Health and stays there. The site sells five engagement types, coded A through E throughout the
markup and matching the Career Management workstation's Portfolio Index:

| Code | Engagement |
|---|---|
| A | Fractional / advisory AI product lead |
| B | Expert consult |
| C | Board seat or named advisor |
| D | Modern-methods strategy sprint |
| E | Workshops, panels, speaking |

Positioning anchors, unchanged from the Portfolio workstation: function flag is **AI Product**,
story is **AI at consumer scale**, methods over industry, leans seed and early, Austin / remote.
Never frame James as "just a UX guy."

## Hard content rules

1. **Never invent experience, titles, dates, or metrics.** Every claim traces to
   `Cowork OS/00_Resources/professional-background.md` or the Career Management workstation.
2. **Patents: 358 granted, 226 in force**, verified 2026-08-07. Never the older "300+."
3. **Education: M.A. 2000**, not M.S. 1999. **AT&T end date: December 2025.**
4. **White papers: "lead author."** Not co-author, not primary author.
5. **wisely.io is not an exit.** It wound down on capital constraints. Say so plainly.
6. **No em dashes, anywhere.** Use commas, colons, periods, parentheses.
7. **Banned words:** dive into, game-changing, straightforward, leverage, synergize, circle back,
   touch base, moreover, furthermore, in conclusion, at the end of the day, needless to say.
   See `00_Resources/voice-principles.md` in Cowork OS for the full voice spec.

## Clearance (approved 2026-08-13)

**Published:** the M.A. thesis and its PDF, six peer-reviewed publications, the 358 granted patents,
three redacted Tessa case studies, five AT&T method-only case studies **as text with all images
removed**, and the patent-development workshop case study with the client unnamed.

**Do NOT publish, ever, without a fresh yes from James:**

- Any AT&T case-study image. All five carry AT&T-proprietary or IBM-confidential stamps and are
  pending permission clearance.
- The AT&T white paper PDFs. Published-vs-internal status is unconfirmed.
- PART instrument memos. Private until the venture develops.
- The Liz User Research plugin. A redacted cut was never made.
- The Trading Bot. Public framing unconfirmed.
- Tessa financials, traction, raise terms, team specifics, competitor names, or the internal
  advisor-politics material.
- James's phone number.

The `/work/` index has a short "Not published here" section that acknowledges this work exists
without naming any of it. Keep it that way.

## Design

Built on the **Personal Brand System** tokens (`Cowork OS/Personal Brand System/`), v1.0, 2026-05-24.
Cal Sans display, Inter body, indigo `#6366f1`, very dark navy `#0f1117`. Dark mode only; the
brand book says dark is the default for interactive surfaces.

Two deliberate extensions, logged here rather than invented silently:

- **`--accent-text: #8b8ef7`.** The brand indigo is 4.2:1 on the dark background, which fails WCAG
  AA for text. `--accent-text` is 6.6:1 and is used for anything indigo that is *text*. The original
  `#6366f1` stays for fills, rules, and the playhead, where the 3:1 graphical threshold applies.
- **`--text-4: #767e92`.** Decorative separators only. Never body copy.

Contrast floors currently met: body text 8.1:1, small mono labels 7.2:1, indigo text 6.6:1. Nothing
on the site is smaller than 11px. Do not lower either.

### The signal rail

A fixed-seed waveform down the left edge, drawn in `assets/js/site.js`. Scroll position is the
playhead. It is deterministic on purpose (same trace every visit) and honours
`prefers-reduced-motion`. Below 1000px it collapses to a 2px top progress bar. It is the site's one
decorative gesture, and it is grounded in the actual work: sleep EEG, edge audio, ambient sensing.
Do not add a second motif.

### Anti-slop rules

No gradient blobs, no glassmorphism, no emoji icons, no stock photography, no three-column feature
grids with generic line icons. Type carries the design. Indigo is rare enough to mean something.
Motion only where it clarifies.

Charts follow the dataviz rules: one series means one colour, thin marks not thick blocks, solid
hairline baselines with no gridlines, labels on first/peak/last only, hover enhances rather than
gates, and a table view always exists. Hero figures use proportional numerals, not `tabular-nums`.

## Architecture

Jekyll on GitHub Pages. No collections, no plugins, no npm, no Sass. Pages are plain HTML with front
matter and `layout: default`. That is deliberate: it keeps the site previewable without Ruby, which
the authoring container does not have.

- `_layouts/default.html`: shell: head, rail, masthead, footer
- `_layouts/post.html`: blog post wrapper
- `_includes/analytics.html`: renders nothing unless `site.ga4` is set
- `assets/css/main.css`: the whole design system, sectioned and numbered
- `assets/js/site.js`: signal rail, scroll reveal, mobile nav. Progressive enhancement only;
  every page is fully readable with JavaScript off.
- `assets/data/patents.json`: 358 granted patents, compact array schema
- `_gen/cases.py`: **source of truth for the case studies.** Edit here, not in `work/*/index.html`,
  then re-run it. It writes the nine pages and the index together.
- `_gen/patents.py`: rebuilds the patent JSON from the CSV export
- `build-preview.py`: single-file preview renderer for working without Jekyll

## Gotchas

- **Do not hand-edit `work/*/index.html`.** `_gen/cases.py` overwrites them.
- **`build-preview.py` is not Jekyll.** It resolves simple Liquid only. Anything looping over
  `site.posts` needs a real build to verify.
- **The patent page reads `window.__PATENTS__` first, then falls back to `fetch`.** That is how the
  preview works offline. Keep both paths.
- **The CV PDF is rendered from `/cv/` through the print stylesheet.** If you change the CV page,
  regenerate the PDF or the two will disagree. Never link the old branded `.docx`: it still says
  300+ patents.
- **The two 2016 posts are `published: false`, not deleted.** James has not authorized a delete.

## Assets

- `assets/img/james-pratt.{jpg,webp}`: 4:5 portrait, 1000x1250, used on the home contact block and
  the About page. `-square` and `og.jpg` (1200x630, the social card) are crops of the same source.
  All generated from one supplied headshot; regenerate all four together if it is ever replaced.
- The portrait is a dark image on a dark site by design. It carries a 1px border and a 12px radius
  so it reads as a deliberate object rather than a hole in the page.

## Deploy

Push to `master`. GitHub Pages builds and serves. There is a `.github/workflows` file that uploads
the repo as static content; if Pages is ever switched to that workflow as its source, **Jekyll stops
running and every page renders raw front matter**. Confirm the Pages source is "Deploy from a
branch" before touching that workflow.
