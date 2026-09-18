# CLAUDE.md: prattatx.github.io

Personal site for James H. Pratt, Ph.D. Read this before changing anything.

## What this site is

A public credibility surface for **one consulting practice**, not a job-search site. James is
CEO of Fyve Health and stays there.

**The site sells the AI Effectiveness Audit**, repositioned 2026-09-15. Two questions answered
together from watching the work happen: which tasks should the machine do, and who on this team
actually produces well with AI. It is built on **PART**, an AI-readiness assessment measuring
Passion, Agency, Rigor and Taste, which James owns outright. The method is named (Widen, Score,
Defend); the offers are not, because named methods command premium while named offers
commoditize.

| Tier | What | Price |
|---|---|---|
| Front door | One workflow, observed and allocated | $5,000, published |
| Main | Full engagement across a function | Five figures, scoped |
| Ongoing | Named advisor or fractional seat | Retainer |

**ICP: organizations integrating AI into knowledge work.** Not stage-gated, not industry-gated.
Elder care, senior care and healthcare are excluded as a primary market from James's direct
operating experience.

**The A through E engagement codes are retired**, along with the seed-and-early ICP. Five ICPs
were derived and withdrawn on 2026-09-14 and 2026-09-15; the reasons each failed are in
`docs/superpowers/specs/2026-09-14-offers-redesign-DRAFT.md`. Read that before proposing a sixth.

Positioning anchors that still hold: function flag is **AI Product**, story is **AI at consumer
scale**, methods over industry, Austin / remote. Never frame James as "just a UX guy."

**Never make a PART validity claim.** PART has no criterion validity evidence. Nothing may say
or imply it predicts performance. Market the assessment; never publish the instrument (construct
defense, instrument design memo, task specs, item text).

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
8. **17 and 24 measure different things. Never swap one for the other.** `24` is years deciding
   human or machine, counting from Lockheed Martin, February 2002. `17` is years shipping AI at
   consumer and enterprise scale, which began later. The stat rail uses 24; the CV's "seventeen
   years shipping AI" is correct and must not be "updated" to 24. A find-and-replace conflated
   them on 2026-09-15 and had to be reverted.

## Clearance (approved 2026-08-13)

**Published:** the M.A. thesis and its PDF, nine peer-reviewed publications, the 358 granted patents,
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

> **`design.md` at the repo root is the authority for this system.** It codifies what actually
> ships: the full token table with computed contrast, the four macrostructure families, accent
> discipline, motion rules, CTA voice, and the section-head pattern. Read it before changing
> colour, type, spacing, motion, or component voice. Where it and this section disagree,
> `design.md` wins and this section should be updated to match. The notes below are the origin
> story and the clearance-relevant constraints, not the live spec.

**The site is light, not dark.** This changed on 2026-08-14 and the brand book has not caught up.

Current system (v2): warm off-white paper `#faf8f4`, never pure white. Every neutral sits at hue
75 to 85, the warm side. **Inter** carries structure (headings, nav, labels, controls),
**Source Serif 4** carries body copy, and **mono is for data only** (patent numbers, years, dates, axis labels,
counters, code). Accent is indigo `#4f52d4`, which is the value the old print stylesheet already
used for light surfaces, so the brand hue survived the direction change.

**Cal Sans is retired.** Do not reintroduce it.

Origin: Personal Brand System tokens v1.0 (`Cowork OS/Personal Brand System/`), 2026-05-24, which
specified Cal Sans, `#6366f1`, `#0f1117`, and dark-only. James opened the brand lock and that book
is now out of date. `design.md` is the live spec; the brand book needs reconciling to it.

The direction came from two studied references (structure only, no pixels copied): warm light paper
and serif body from maggieappleton.com, and the strategy that chrome recedes so the work carries
the colour from c82.net.

Contrast floors currently met, all computed rather than estimated: headings 14.75:1, body 9.53:1,
muted labels 5.34:1, indigo as text 7.09:1, control boundaries 3.24:1, white on accent 6.02:1.
Nothing on the site is smaller than 11px. Do not lower any of these.

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

- **Jekyll publishes any root file that has no YAML front matter**, unless `_config.yml`'s
  `exclude:` list names it. The repo is public and `robots.txt` is `Allow: /`, so an unexcluded
  working document is served at its own URL. `CLAUDE.md`, `README.md`, `PRODUCT.md`, `design.md`,
  `docs`, `_gen`, `_preview` and `build-preview.py` are all excluded. **Add anything new of that
  kind before committing it.** On 2026-09-15 this nearly published the strategy specs, PART's
  unsigned construct-defense status, and five withdrawn ICPs. When checking, inventory every root
  entry rather than spot-checking: the same defect was found three times because each pass looked
  at a narrower slice than the problem.

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

Push to `master`. GitHub Pages builds and serves.

Pages is `build_type: legacy`, source `master:/`, so `pages-build-deployment` runs Jekyll and
that is the only deployer. Verify with:

    gh api repos/prattatx/prattatx.github.io/pages --jq .build_type   # expect: legacy

**Do not add a workflow that publishes a Pages artifact.** `.github/workflows/static.yml` used to
do exactly that, uploading the repo as raw static content on every master push. Both it and Jekyll
fired and both reported success, so the site served whichever finished last. Jekyll won every time
on timing alone (roughly 47s vs 21s), never by design. Had the static job won, every page would
have served its front matter as visible text. It was deleted for that reason. If this ever reads
`workflow` instead of `legacy`, the site is being served by an artifact builder and pages will
show raw front matter.
