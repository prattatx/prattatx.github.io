# CLAUDE.md: prattatx.github.io

Personal site for James H. Pratt, Ph.D. Read this before changing anything.

## What this site is

A public record of one person, with nothing for sale. Repositioned 2026-11-12, after James
started a full-time role as Director, AI and Data Science at Charles Schwab on 2026-11-09 and
could no longer solicit paid work. The earlier positioning (a consulting practice selling the AI
Effectiveness Audit) is retired; its specs under `docs/superpowers/` are history, not guidance.

**The site sells nothing.** No offer, price, tier, engagement, retainer, "advisory", "taking on
work" or "available for" language anywhere. Removed and not to be reintroduced without a fresh
yes from James: the AI Effectiveness Audit, the PART name and its four factors, the Widen, Score,
Defend method names, the capabilities page, and the A to E engagement codes. Case studies are
tagged by kind of work (Research, Product design, Workshop, Strategy, Writing).

**The idea behind the old offer survives as `/method/`,** "How we decide who does what": an
explanation of function allocation with no offer attached.

**The visitor** has looked James up (a new colleague, an event organizer, someone from his old
network) and is verifying him. They read the record, maybe the writing, maybe say hello.

**The employer is named as one plain title line** ("Director, AI and Data Science at Charles
Schwab"): in the home hero, the About page and the CV. Nothing about the work there, ever. The
footer carries "Views here are my own, not my employer's." Nothing on the site comments on the
brokerage industry, securities markets or investing, and nothing mentions a trading bot.

**Booking is an open door and appears twice:** the masthead button and the home page's closing
block, which says in words that James does not take paid work. No other page carries a booking
button.

**Contact is `site.email` in `_config.yml`.** `james@fyve.dev` is closing; never publish it.

**Fyve Health is past tense:** co-founder, CEO 2025 to 2026. It has a featured "Founder" section
on the home page because Tessa is the most recent thing James built. The Tessa clearance rules
below are unchanged.

Positioning anchors that still hold: function flag is **AI Product**, story is **AI at consumer
scale**, methods over industry, Austin. Never frame James as "just a UX guy."

## Hard content rules

1. **Never invent experience, titles, dates, or metrics.** Every claim traces to
   `Cowork OS/00_Resources/professional-background.md` or the Career Management workstation.
2. **Patents: 358 granted, 226 in force**, verified 2026-08-07. Never the older "300+."
3. **Education: M.A. 2000**, not M.S. 1999. **AT&T end date: December 2024.**
4. **White papers: "lead author."** Not co-author, not primary author.
5. **wisely.io is not an exit.** It wound down on capital constraints. Say so plainly.
6. **No em dashes, anywhere.** Use commas, colons, periods, parentheses.
7. **Banned words:** dive into, game-changing, straightforward, leverage, synergize, circle back,
   touch base, moreover, furthermore, in conclusion, at the end of the day, needless to say.
   See `00_Resources/voice-principles.md` in Cowork OS for the full voice spec.
8. **12 and 24 measure different things. Never swap one for the other, and never put both in
   one document.** `12` is years building AI products and platforms, counting from 2014. `24` is
   years deciding human or machine, counting from Lockheed Martin, February 2002. The stat rail
   uses 24; the CV uses 12. **17 is retired** (career record, 2026-09-23): it reconciles with no
   real starting point, so never reintroduce it.

## Clearance (approved 2026-08-13)

**Published:** the M.A. thesis and its PDF, the doctoral dissertation PDF (added 2026-11-14 on
James's request; public academic work), nine peer-reviewed publications, the 358 granted patents,
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
- Any Tessa traction, buyer, acquisition, or wind-down language, anywhere on the site.
- The Lockheed 44 and 17 crew figures. Say "cut mission center crew by more than half."
- Internal AT&T figures: team sizes, the $2.9M budget, or the name of the executive who approved
  the $110M.

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

**v3 (2026-11-12): editorial with motion.** The warm paper, the serif and the indigo stay. What
changed: the left-edge signal rail is gone, the landing page sits on one shared grid, cards carry
a soft shadow, and the page moves (a hero figure that sorts tasks between a person and a machine,
numbers that count up, a patent curve and a waveform that draw themselves). `design.md` > v3 has
the rules.

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

### Alignment

James reads deliberate asymmetry as a defect. Every multi-column block on the landing page is
`.g4` or `.g2` on the `--gutter` token, so the four numbers and whatever sits under them share
column edges. Before adding a block, check its edges against the numbers row. The 2026-11-12
rework started from exactly this complaint: a four-part list that did not line up with the four
numbers above it.

### Motion

Every animated figure ships in its finished state in the HTML and is animated from there, so the
page is complete with JavaScript off and under `prefers-reduced-motion`. Keep that property.
The 2px scroll-progress line at the top is what remains of the old left-edge signal rail; the
waveform now lives in the home page's founder section, where it describes Tessa.

### Copy

James flagged four habits in the old copy as machine-sounding. None of them goes back in:

1. Punchline fragments ("Psychologist first. Everything else came after.").
2. Not-this-but-that framing ("Sessions that end in a decision, not a deck.").
3. Long paragraphs that argue a case at the reader.
4. Lines addressed to a buyer ("Your team has AI.", "Tell me what you are building.").

Write in his first person: state the fact, give the evidence, stop.

### Leader voice (2026-11-14)

James wants to read as someone who leads teams, not as an individual contributor.

- **Case studies:** keep "I" rare. James read a page full of "I" as unnatural (2026-11-14). Role
  lines and leadership bullets start with a verb ("Set the research plan..."), the team is named
  wherever it did the work, and "we" carries the execution. Each case has a "Leading the team"
  card; never title it "How I led it". Never state a team size or a reporting line: the career
  record does not settle when his direct team started.
- **Case study layout reads across, then down** (James, 2026-11-14: "people read left to right
  then top to bottom"). The problem runs full width; under it the approach is on the left and
  the outcome, then the leadership card, on the right. Whatever the layout, reading across and
  then down must give the sections in their order: problem, approach, outcome, leadership.
- **`/method/` and its film:** "we" throughout ("How we decide who does what"). "I" only for his
  own history, such as first leading the work at Lockheed Martin in 2002.
- **Patents:** co-inventors are not shown in the table. The table has a Category column and a
  category filter instead.

### Figures on the case studies

Each case study carries one drawn figure of its method, generated by `_gen/cases.py` and styled
in section 29 of `main.css`. A figure may show a sequence, a count, or what was brought together.
It may never state a fact the case text does not, and never reproduce employer or client
material. The clearance rules above are unchanged: no AT&T images.

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
- `assets/js/site.js`: scroll progress, the hero sorting figure, count-up numbers, the drawn
  curve and waveform, scroll reveal, mobile nav. Progressive enhancement only; every page is fully
  readable with JavaScript off.
- `assets/data/patents.json`: 358 granted patents, compact array schema. The seventh field of
  each row is a category index into the top-level `categories` list.
- `_gen/patent_categories.py`: sorts every patent into one of ten subject categories by title,
  and stops if a title matches no rule. Run it alone to refresh the categories in the JSON.
- `_gen/cases.py`: **source of truth for the case studies.** Edit here, not in `work/*/index.html`,
  then re-run it. It writes the nine pages and the index together.
- `_gen/patents.py`: rebuilds the patent JSON from the CSV export
- `build-preview.py`: single-file preview renderer for working without Jekyll
- `_gen/site_preview.py`: builds every page into `_preview/site` so the whole site can be served
  and clicked through locally. Use this, not a pile of single-file previews, before showing James
  anything.

## Gotchas

- **Jekyll publishes any root file that has no YAML front matter**, unless `_config.yml`'s
  `exclude:` list names it. The repo is public and `robots.txt` is `Allow: /`, so an unexcluded
  working document is served at its own URL. `CLAUDE.md`, `README.md`, `PRODUCT.md`, `design.md`,
  `docs`, `_gen`, `_preview` and `build-preview.py` are all excluded. **Add anything new of that
  kind before committing it.** On 2026-09-15 this nearly published the strategy specs, PART's
  unsigned construct-defense status, and five withdrawn ICPs. When checking, inventory every root
  entry rather than spot-checking: the same defect was found three times because each pass looked
  at a narrower slice than the problem.

- **A local preview must match what Jekyll publishes before James sees it.** On 2026-11-14 he
  reported two posts as broken when only the preview was: it passed Markdown through raw and
  dropped the preview text of posts with no `summary`. `_gen/site_preview.py` converts Markdown
  posts and stops if any page still holds Liquid. Give every post a `summary` in its front
  matter so its preview never depends on a fallback.
- **Do not hand-edit `work/*/index.html`.** `_gen/cases.py` overwrites them.
- **`_gen/site_preview.py` takes its first argument as the output folder.** It has no `--help`:
  running it with one built the whole site into a folder named `--help` in the repo root
  (2026-11-15). Run it with no arguments to build into `_preview/site`.
- **A link inside a sentence needs a real underline to pass axe.** axe's `link-in-text-block`
  rule does not count an inset box-shadow as a non-colour cue. The hero figure's caption link
  failed it until it got `text-decoration: underline` (PR 12, 2026-11-15). `.prose` and
  `.post-body` links pass because they keep the body text colour. `a.inline` uses the accent
  colour with the box-shadow underline, so it may fail the same rule wherever it is used: run
  axe on the page before relying on it.
- **`build-preview.py` is not Jekyll.** It resolves simple Liquid only. Anything looping over
  `site.posts` needs a real build to verify.
- **The patent page reads `window.__PATENTS__` first, then falls back to `fetch`.** That is how the
  preview works offline. Keep both paths.
- **The CV PDF is rendered from `/cv/` through the print stylesheet.** If you change the CV page,
  regenerate the PDF or the two will disagree. Never link the old branded `.docx`: it still says
  300+ patents.
- **The two 2016 posts were deleted on 2026-09-23**, on James's instruction.
- **Republished posts set `canonical_url` and `medium_url`.** `canonical_url` overrides the
  self-canonical in `default.html`; `medium_url` renders the "Originally published on Medium"
  credit in `post.html`. The three 2025 Medium essays carry both.

## Assets

- `assets/img/james-pratt.{jpg,webp}`: 4:5 portrait, 1000x1250, used on the home closing block and
  the About page. `-square` and `og.jpg` (1200x630, the social card) are crops of the same source.
  All generated from one supplied headshot; regenerate all four together if it is ever replaced.
- The portrait is a dark image on the light paper background. It carries a 1px border and a 12px
  radius so it reads as a deliberate object rather than a hole in the page.

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
