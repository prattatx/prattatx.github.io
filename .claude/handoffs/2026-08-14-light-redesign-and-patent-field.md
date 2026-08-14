# Session Handoff — Light redesign of prattatx.github.io and the patent field

## Where it started

Session opened with `/hallmark audit` on the site. That surfaced 3 critical and 10 major/minor
findings, which were fixed in sequence. After the fixes were committed, James said "I still don't
like the look" — that reframed the work from remediation to redirection. Two reference sites were
studied via `hallmark study` (URL mode), a light v2 system was designed and implemented, and the
patents page was rebuilt around a unit chart. Brand lock was explicitly opened by James
("Open, I'll update the brand book"), which authorized retiring Cal Sans and inverting dark to light.

## Decisions locked + what shipped

- **`design.md` is now the design authority**, not `CLAUDE.md` — `/Users/james/Documents/git/prattatx.github.io/design.md`.
  v1 codified the shipped dark system; v2 records the light direction. `CLAUDE.md` gained a pointer
  block at its `## Design` section saying `design.md` wins on disagreement.
- **Dark to warm light.** Paper `#faf8f4`, every neutral at hue 75-85 (v1 sat at 264-275).
  All contrast computed, not estimated: headings 14.75:1, body 9.53:1, muted 5.34:1,
  accent-text 7.09:1, control boundaries 3.24:1, white on accent 6.02:1.
- **Accent is continuity, not invention.** `#4f52d4` was already the v1 print stylesheet's light-surface
  indigo, so the brand hue survived the flip.
- **Type inverted.** Inter carries structure, a serif carries reading. Mono cut 43 -> 16 usages, all data.
  Section labels went from 12px mono caps to 20px headings. Cal Sans retired entirely (font-face,
  preload, colophon).
- **The patent field** — `/patents/` leads with 358 marks, one per grant, in 16 year columns. Sorted
  within column so statuses band. 16 keyboard stops not 358; marks dim rather than vanish when filtered;
  table remains the complete data view.
- **`build-preview.py` rewrites root-relative URLs** to page depth, so `_preview` opens over `file://`
  with no server.
- **Deleted `css/main.css`** (orphaned pre-rebuild stylesheet, Work Sans, nothing referenced it).
- **Three commits on `site-rebuild`**: `fd345c2` (audit fixes), `c445af2` (light redesign + field),
  `081f566` (server-independent previews). All pushed.

## Key files for next session

- `/Users/james/Documents/git/prattatx.github.io/design.md` — read first. The system of record:
  tokens with computed contrast, macrostructure families, type roles, the field spec, and 6 open questions.
- `/Users/james/Documents/git/prattatx.github.io/assets/css/main.css` — v2 stylesheet. Hallmark stamp at
  top records `studied-DNA`, both DNA sources, and the axes.
- `/Users/james/Documents/git/prattatx.github.io/patents/index.html` — the field markup + `buildField()`.
- `/Users/james/Documents/git/prattatx.github.io/CLAUDE.md` — still says "Dark mode only" and describes
  Cal Sans. Stale and needs updating.
- `/Users/james/Documents/git/prattatx.github.io/.hallmark/log.json` — both builds recorded for diversification.
- Plan file: none.
- Memory files touched: none.

## Running state

- Background processes: shell `bped8a6mc` — `python3 -m http.server 4000` serving `_preview/`.
  Kill with `KillShell` on that ID, or it may already be reaped (it was killed 3x this session).
- Dev servers / ports: http://127.0.0.1:4000 (preview). Also openable with no server at
  `file:///Users/james/Documents/git/prattatx.github.io/_preview/index.html`.
- Open worktrees / branches: on `site-rebuild`, clean, pushed. **PR #8 open and mergeable**:
  https://github.com/prattatx/prattatx.github.io/pull/8

## Verification — how to confirm things still work

- `cd /Users/james/Documents/git/prattatx.github.io && git status --porcelain` — expect empty.
- `python3 -c "import re;s=open('assets/css/main.css').read();d=set(re.findall(r'(--[a-z0-9-]+)\s*:',s));u=set(re.findall(r'var\(\s*(--[a-z0-9-]+)',s));print('unresolved:',u-d or 'none')"` — expect none.
- `python3 build-preview.py index.html _preview/index.html` — expect "wrote ... KB".
- `gh api repos/prattatx/prattatx.github.io/pages --jq .build_type` — expect `legacy` (Jekyll runs;
  if this ever reads `workflow`, the site will serve raw front matter).
- `curl -s https://prattatx.github.io/ | grep -c "layout: default"` — expect 0 (no raw front matter live).

## Deferred + open questions

- Deferred: **Source Serif 4 woff2 is not in the repo.** Body copy falls back to Iowan Old Style /
  Georgia. Needs the file added to `assets/fonts/` plus an `@font-face` block. Largest remaining gap.
- Deferred: **`/research/`** still lists 9 publications rather than drawing them. Same problem as
  patents at smaller scale; 9 items may not warrant a drawn view.
- Deferred: **portrait is a dark image on a now-light page**, border/radius were tuned for dark.
- Deferred: **`CLAUDE.md` still claims dark mode and Cal Sans.**
- Open: **`.github/workflows/static.yml` races the Jekyll builder.** Both fire on master push and
  both succeed (static 21s, Jekyll 47s). Jekyll has won every time so far, which is luck not design;
  if static.yml wins, every page serves raw front matter. `CLAUDE.md`'s precondition for touching it
  ("confirm Pages source is Deploy from a branch") is satisfied — `build_type: legacy`. James was
  offered deletion and has not answered.
- Open: **merging PR #8 was blocked by the permission classifier.** James must merge from the web UI
  or grant permission. Merge is safe: Pages is `legacy` on `master:/`.

## Pick up here

Merge PR #8 to publish v2, then decide whether to delete `.github/workflows/static.yml` to remove
the deploy race.
