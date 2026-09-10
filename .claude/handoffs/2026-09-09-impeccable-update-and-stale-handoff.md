# Session Handoff: Impeccable updated to v4.3.1, prior handoff found stale

## Where it started

James asked to load the last handoff for this repo before starting work. The only handoff on file
was `2026-08-14-light-redesign-and-patent-field.md`, which turned out to be stale: nearly every
item it left open or deferred was closed by a later session (PR #9, `site-polish`, merged
2026-08-29). Session then pivoted to `/impeccable` with no argument, which produced a routing menu,
and James chose to take the offered skill update. No site code was changed this session.

## Decisions locked + what shipped

- **Impeccable skill updated 4.0.4 to 4.3.1.** Ran `npx -y impeccable@latest update`. Also installed
  native engine v0.1.5 (darwin-arm64) at
  `/Users/james/.agents/skills/impeccable/scripts/bin/darwin-arm64/impeccable`.
- **Bare `npx impeccable update` does not work here.** It resolves a stale `impeccable@2.3.2` from
  the npx cache, which has no `update` subcommand and fails with "Warning: cannot access update".
  The npm dist-tag latest is 4.1.0 (CLI) while the skills stream is 4.3.1, served from
  `https://impeccable.style/api/version`. Always pin: `npx -y impeccable@latest update`.
- **The detector is no longer degraded on this machine.** v4.3.1 replaced the `.mjs` scripts with a
  single native binary at `/Users/james/.agents/skills/impeccable/scripts/impeccable` that bundles
  its own HTML/CSS parser rather than resolving `htmlparser2` / `css-select` / `css-tree` from
  node_modules. Verified by canary, not assumed: a file with `color: var(--muted)` over
  `background: var(--paper)` fired `low-contrast` twice plus `tiny-text` and `gradient-text`, which
  proves computed contrast, custom-property resolution, and selector matching all evaluate now.
  Under the old `detect.mjs` none of those could fire and roughly 47 of 59 rules were dead.
- **Install layout confirmed.** `/Users/james/.agents/skills/impeccable` is the real directory;
  `/Users/james/.claude/skills/impeccable` and `/Users/james/.kiro/skills/impeccable` are symlinks
  to it, so all three read v4.3.1. The updater's advice to run `git submodule update --remote` was
  it misreading those symlinks as a source checkout. Ignore it.
- **The updater installed hooks without asking**, into
  `/Users/james/.claude/settings.local.json`: two entries calling `impeccable hook`, a 5s
  "Checking UI changes" and a 30s "Design deep pass". Both are guarded by a `[ ! -f ... ]`
  existence check, so they fail safe. James was told and has not asked for their removal.
  `$impeccable hooks off` manages them per project.

## Key files for next session

- `/Users/james/Documents/git/prattatx.github.io/.claude/handoffs/2026-08-14-light-redesign-and-patent-field.md`
  the prior handoff. Read it for the v2 design reasoning, but treat its "Deferred + open questions"
  and "Pick up here" sections as closed. Superseded by this file.
- `/Users/james/Documents/git/prattatx.github.io/design.md` the design authority. Still current on
  tokens, type, and the field spec. Its "Open questions" section at the end is live.
- `/Users/james/Documents/git/prattatx.github.io/CLAUDE.md` product and clearance rules. Accurate on
  the light system, but see drift noted below.
- `/Users/james/.claude/CLAUDE.md` global instructions. The Tools & Stack bullet about the degraded
  impeccable detector is now factually wrong.
- Plan file: none.
- Memory files touched: none.

## Running state

- Background processes: none.
- Dev servers / ports: none. No server was started this session.
- Open worktrees / branches: on `master`, clean, nothing uncommitted. Last commit `ffdae49`
  (merge of PR #9, `site-polish`, 2026-08-29).

## Verification: how to confirm things still work

- `cd /Users/james/Documents/git/prattatx.github.io && git status --porcelain` expect empty.
- `grep -m1 -A2 '^metadata:' /Users/james/.agents/skills/impeccable/SKILL.md` expect `version: 4.3.1`.
- `~/.agents/skills/impeccable/scripts/impeccable detect --json index.html assets/css/main.css`
  expect 4 `overused-font` hits on Inter and NO "DEGRADED" banner on stderr. The Inter hits are a
  deliberate brief decision (Inter carries structure, Source Serif 4 carries reading) and stand.
- `grep -c impeccable /Users/james/.claude/settings.local.json` expect 2 (the hook entries).
- `gh api repos/prattatx/prattatx.github.io/pages --jq .build_type` expect `legacy`.

## Deferred + open questions

- Open: **the global CLAUDE.md detector note is now wrong.** The Tools & Stack bullet in
  `/Users/james/.claude/CLAUDE.md` still says the detector "runs degraded", lists the five modules
  that fail to resolve, and warns that "a clean result is an undercount, not a pass". All of that
  was true of `detect.mjs` and is false of the v4.3.1 native engine. James was asked whether to
  update the bullet and did not answer before ending the session. Do not edit it unilaterally; ask.
- Open: **`CLAUDE.md` Assets section still describes the pre-v2 portrait.** It says "The portrait is
  a dark image on a dark site by design. It carries a 1px border and a 12px radius." What actually
  ships is the matted treatment (paper, then `--bg-muted`, then image, concentric radii 8px inside
  an 8px mount inside 16px) on a light site. `design.md` has the correct account under "Resolved
  after v2 shipped".
- Open: **`design.md` Exports section still emits v1 dark tokens.** `tokens.css`, the Tailwind
  `@theme` block, the DTCG JSON, and the shadcn variables all carry `--bg: #0f1117`,
  `--accent: #6366f1`, and Cal Sans. Anyone copying tokens out of that file gets the retired system.
  Same file's "What pages MUST share" lists "Cal Sans and Inter", and "On changing the look" says
  "Cal Sans is doing all the display work". Cal Sans is retired.
- Open: **two live questions in `design.md`.** (1) `about` and `cv` use `<p class="mono dl-head">`
  where `index` uses `<h3>` for the identical pattern; fixing changes the heading outline on both
  pages, so it wants a deliberate call. (2) `--accent-solid` is now identical to `--accent` and
  could collapse.
- Deferred: **no PRODUCT.md in this repo.** `impeccable context` reports `NO_PRODUCT_MD`. DESIGN.md
  says how the site looks; nothing captures who it is for or what a visit should accomplish.
  `$impeccable init` was the session's top recommendation and was not run.
- Deferred: **the site has never been critiqued under Impeccable.** `critique.latest` is null. Site
  mode is Experience: the record is the artifact and the chrome recedes.
- Note, not blocking: the impeccable npm package declares `node >=22.18.0`, this machine runs
  v20.20.2. It warned `EBADENGINE` and installed anyway; the native binary sidesteps the runtime.

## Pick up here

Run `$impeccable init` to capture PRODUCT.md, which was the session's top recommendation and the
prerequisite that makes every other Impeccable command reason better on this repo.
