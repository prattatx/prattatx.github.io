# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

**Primary: organizations integrating AI into knowledge work.** Not stage-gated, not
industry-gated. The buyer has AI in the building and has not decided which parts of the
work it should be doing.

Retired 2026-09-15: the previous ICP (seed and early-stage founders) and the medtech and
biotech ICP proposed on 2026-09-14. The audit trail for five ICP candidates derived and
withdrawn is in `docs/superpowers/specs/2026-09-14-offers-redesign-DRAFT.md`.

**Excluded, from James's direct operating experience:** elder care and senior care, and
healthcare as a primary market. This is practitioner evidence and it outranks the
research lanes.

**The visit is almost always a referral check.** Confirmed 2026-09-09 and unchanged. Warm
intro and referral verification is the real arrival path. The visitor arrives with context
already: someone told them about James, and they are verifying before a first conversation.

Design consequence, unchanged: the site does not have to win attention or explain who James
is from zero. It has to confirm what the visitor was already told, fast, and then let them
act.

## Product Purpose

A public credibility surface for advisory work. Not a job-search site, not a portfolio in the
seeking-work sense. James is CEO of Fyve Health and stays there.

**Success is a booked call on cal.com** (`https://www.cal.com/james-pratt`). Confirmed
2026-09-09. Passive credibility is not the goal: the booking is. Everything else on the site
exists to get a verifying buyer confident enough to take that step.

The site sells one practice, the AI Effectiveness Audit, on a three-tier ladder:

| Tier | What | Price |
|---|---|---|
| Front door | One workflow, observed and allocated | $5,000, published |
| Main | Full engagement across a function | Five figures, scoped |
| Ongoing | Named advisor or fractional seat | Retainer |

The A through E engagement codes are retired. They were internal Career Management
workstation taxonomy.

## Positioning

Function flag is **AI Product**. Story is **AI at consumer scale**. Methods over industry.
Not stage-gated. Austin or remote.

The mechanism a neighboring advisor could not truthfully copy: 358 granted patents across two
decades of shipping consumer-scale AI inside a carrier, paired with a cognitive psychology and
human factors research record. Not a design consultant with an AI interest, and not a
researcher without shipping scars.

**Never frame James as "just a UX guy."** This is a standing constraint, not a preference.

## Operating Context

- The visitor is mid-diligence on a person, not shopping a category. They usually have a name,
  a recommendation, and a specific problem already in mind.
- Reading is often quick and often on the way to a decision that involves someone else: a
  co-founder, a partner, a program director.
- The record (patents, publications, case studies) is what a referral check actually goes
  looking for, which is why it is promoted to a drawn artifact rather than a table.
- `/patents/` is the one interactive surface. Everything else is a document.

## Capabilities and Constraints

**Stack (existing, not a new decision):** Jekyll on GitHub Pages. No collections, no plugins,
no npm, no Sass. Pages are plain HTML with front matter and `layout: default`. Deliberate: it
keeps the site previewable without Ruby, which the authoring container does not have.

- Deploy is push to `master`. Pages is `build_type: legacy`, source `master:/`, so Jekyll is
  the only deployer. Never add a workflow that publishes a competing Pages artifact.
- Progressive enhancement is required. Every page is fully readable with JavaScript off.
- `_gen/cases.py` is the source of truth for the nine case studies and the `/work/` index.
  Never hand-edit `work/*/index.html`.
- `_gen/patents.py` rebuilds `assets/data/patents.json` from a CSV export.
- The patent page reads `window.__PATENTS__` first and falls back to `fetch`. Both paths must
  survive, because offline preview depends on the first.
- The CV PDF renders from `/cv/` through the print stylesheet, so the two can never contradict
  each other. Regenerate the PDF whenever the CV page changes.
- `build-preview.py` resolves only simple Liquid. Anything looping `site.posts` needs a real
  Jekyll build to verify.
- Two config switches wire themselves in when set and vanish when blank: `calendar_url` and
  `ga4` (`G-LPYRNPZYB1`, with `anonymize_ip`).

**Undecided, do not invent:** whether the site should carry any conversion instrumentation
beyond GA4 pageviews. Nothing currently measures whether a visit produced a booking, so the
stated success condition is not yet observable.

## Brand Commitments

- Voice spec is `00_Resources/voice-principles.md` in Cowork OS. Direct, authentic, no
  corporate filler.
- **No em dashes anywhere.** Commas, colons, periods, parentheses.
- **Banned words:** dive into, game-changing, straightforward, leverage, synergize, circle
  back, touch base, moreover, furthermore, in conclusion, at the end of the day, needless to
  say.
- Every factual claim traces to `Cowork OS/00_Resources/professional-background.md` or the
  Career Management workstation. Never invent experience, titles, dates, or metrics.
- Fixed facts: **358 granted patents, 226 in force**, verified 2026-08-07 (never the older
  "300+"). Education is **M.A. 2000**, not M.S. 1999. AT&T end date is **December 2025**. White
  papers are **"lead author."** wisely.io **is not an exit**: it wound down on capital
  constraints and should be said plainly.
- Visual authority is `design.md` at the repo root, which supersedes the Personal Brand System
  book (2026-05-24) and the design notes in `CLAUDE.md`. The site is light, not dark. Cal Sans
  is retired and must not be reintroduced.

## Evidence on Hand

**Cleared and published** (approved 2026-08-13): the M.A. thesis and its PDF, peer-reviewed
publications, the 358 granted patents, three redacted Tessa case studies, five AT&T
method-only case studies as text with all images removed, and the patent-development workshop
case study with the client unnamed.

**Never publish without a fresh yes from James:** any AT&T case-study image (all five carry
AT&T-proprietary or IBM-confidential stamps, permission pending), the AT&T white paper PDFs
(published-vs-internal status unconfirmed), PART instrument memos, the Liz User Research plugin
(no redacted cut exists), the Trading Bot (public framing unconfirmed), Tessa financials,
traction, raise terms, team specifics, competitor names, the internal advisor-politics
material, and James's phone number.

`/work/` carries a short "Not published here" section that acknowledges this body of work
exists without naming any of it. Keep it that way.

**Publication count: nine.** Settled 2026-09-09. `/research/` renders nine peer-reviewed
publications (nine `.row-pub` entries) and `design.md` agreed; the "six" in the `CLAUDE.md`
clearance note and the README was the stale figure, and both were corrected to nine. Nine is
the citable number.

**Absences that must not be fabricated:** no testimonials, no client logos, no named
enterprise references, no engagement pricing, no traction or revenue figures. None of these
exist to publish.

## Product Principles

1. **The record carries the page.** 358 patents and the research line are the strongest assets
   here. Promote them as artifacts, not as tables, and let the chrome recede behind them.
2. **Confirm, do not introduce.** The visitor already knows who James is. Optimize for fast
   verification of a claim they arrived with, not for an origin story.
3. **The booking is the only conversion.** Every page should leave a verifying buyer one
   obvious step from cal.com. No competing calls to action.
4. **Clearance outranks completeness.** A gap in the public record is correct when the material
   behind it is not cleared. Acknowledge the gap, never fill it.
5. **Every claim is traceable.** No number, title, or date ships without a source in the Career
   Management workstation.

## Accessibility & Inclusion

No client-mandated standard. The site holds itself above WCAG AA by its own computed floors,
documented in `design.md`: headings 14.75:1, body 9.53:1, muted labels 5.34:1, indigo as text
7.09:1, control boundaries 3.24:1, white on accent 6.02:1. Nothing renders below 11px. These
are floors, not targets, and are not to be lowered.

Keyboard and touch parity is a hard requirement: any affordance that appears only on hover is
a defect. `prefers-reduced-motion: reduce` must collapse all spatial motion. Drawn records
(`/patents/`, `/research/`) always keep a complete table or list companion as the accessible
data view.
