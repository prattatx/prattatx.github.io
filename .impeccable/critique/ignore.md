# Critique ignore list

Findings the detector reports that are deliberate, documented decisions on this
project. Each one is a call recorded in `design.md`, not an oversight.

- **`overused-font` on Inter.** The 2+1 pairing is the system: Inter carries
  structure (headings, nav, labels, controls), Source Serif 4 carries reading,
  mono carries data only. See `design.md`, Typography. Inter appearing on every
  structural element is the brief working, not a defect.

- **`tiny-text` at 11px.** `design.md` sets 11px as a hard floor and nothing on
  the site renders below it. Measured, the 11px text is `--ink-3` on `--paper`
  at 5.34:1, above the 4.5:1 requirement. The detector expects 12px; this
  project deliberately sets 11 and holds the contrast that makes it readable.

- **`tight-leading` and `cramped-padding` on rendered/inlined pages.** Verified
  false positives, 2026-09-09. Reported ratios of 0.13x to 0.18x against a
  measured page minimum of 0.88, and "flush against border-top" against measured
  section padding of 43px to 96px. These fire only on the fully-inlined preview
  build, not on source, and do not correspond to any measurable state.

## Not ignored, still open

- **`wide-tracking`** (0.08em to 0.11em, 3 to 5 hits). Correct on the mono-caps
  label voice, which `design.md` sanctions. Would be a real defect if any of it
  landed on body copy. The detector emits `line: 0` for every finding so it
  cannot name the selectors; this needs one manual pass before it is either
  fixed or added above.
