# prattatx.github.io

Personal site for James H. Pratt, Ph.D. Jekyll on GitHub Pages, no build step beyond what Pages runs.

## What it is for

A public record of who James is, for someone who has looked him up and wants to verify him. It
sells nothing: no offers, prices or services (repositioned 2026-11-12). See `CLAUDE.md`.

## Structure

```
/                  home: hero figure, four numbers, the record, speaking, founder, selected work, writing, say hello
/method/           "How we decide who does what": function allocation, with a narrated film
/work/             case study index, filterable by kind of work
/work/<slug>/      nine case studies (generated, see _gen/cases.py)
/patents/          searchable explorer over 358 granted patents
/research/         M.A. thesis, dissertation, nine publications
/cv/               full CV, doubles as the source for the downloadable PDF
/writing/          posts from _posts/
/speaking/         talks, panels, judging
/about/            bio
```

`/blog/` redirects to `/writing/`, `/presentations/` to `/speaking/`, and `/capabilities/` (removed
2026-11-12) to `/about/`.

## Editing

- **Copy on a page:** edit the page's `index.html` directly.
- **A case study:** edit `_gen/cases.py` and run `python3 _gen/cases.py`. The script writes both the
  nine case-study pages and the `/work/` index, so they never drift apart.
- **Patent data:** re-run `python3 _gen/patents.py` against a refreshed CSV export. It writes
  `assets/data/patents.json`.
- **A post:** add `_posts/YYYY-MM-DD-slug.md` with `layout: post`, `title`, `date`, and an optional
  `summary` used on the index.
- **Styles:** `assets/css/main.css`, plain CSS built on the Personal Brand System tokens. No
  preprocessor, no framework.

## Previewing without Ruby

`build-preview.py` renders any page to a single self-contained HTML file with fonts, CSS, JS, and
the patent JSON inlined, so it opens with no server:

```
python3 build-preview.py index.html _preview/home.html
```

To browse the whole site locally, with working links between pages:

```
python3 _gen/site_preview.py
python3 -m http.server 4173 --directory _preview/site
```

It resolves only enough Liquid for an accurate visual preview. It handles the landing page's
`{% for post in site.posts limit:3 %}` loop from post front matter, but not post bodies: the feed,
the sitemap and the posts themselves still need a real Jekyll build to see.

## Regenerating the CV PDF

The PDF is rendered from `/cv/` through the print stylesheet, so it can never contradict the page:

```
node -e "const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();
const p=await b.newPage({viewport:{width:1100,height:1400}});
await p.goto('file:///ABS/PATH/_preview/cv.html');await p.emulateMedia({media:'print'});
await p.pdf({path:'assets/pdf/james-pratt-cv.pdf',format:'Letter',
margin:{top:'13mm',bottom:'13mm',left:'12mm',right:'12mm'}});await b.close();})();"
```

## Config switches

`_config.yml` has three keys the pages read:

- `calendar_url`: set to `https://www.cal.com/james-pratt`. Drives "Book a time" in the
  home page's closing block, the only place booking appears. Blank it and the button vanishes.
  The masthead "Say hello" button links to that block (`/#contact`) and does not read this key.
- `email`: the one published address. Every `mailto:` on the site reads it.
- `ga4`: set to `G-LPYRNPZYB1`. Loads gtag.js asynchronously from `_includes/analytics.html`,
  with `anonymize_ip` on. Blank it out and the script stops shipping entirely, no other edit needed.
  Note this is a GA4 property and has nothing to do with the old `UA-78948113-1` tag that used to be
  hardcoded in the head: Universal Analytics no longer processes data, and its history does not
  carry over.

## Content rules

Every factual claim on this site traces to a source in the Career Management workstation. Patent
counts come from the verified 2026-08-07 database (358 granted, 226 in force), never the older
"300+" figure. The case studies are method-only cuts; no employer-confidential images or documents
are published here. See `CLAUDE.md` for the full editorial and clearance rules.
