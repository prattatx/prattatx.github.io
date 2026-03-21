# CLAUDE.md — AI Assistant Guide for prattatx.github.io

## Project Overview

This is a personal website for James Pratt, built with **Jekyll** and hosted on **GitHub Pages**. The site serves as a personal blog, portfolio, and CV. It is a minimal Jekyll static site with no Node.js or Ruby dependency management files — GitHub Pages handles building and serving automatically.

---

## Repository Structure

```
prattatx.github.io/
├── _config.yml           # Jekyll site configuration
├── _includes/            # Reusable HTML snippets
│   ├── analytics.html    # Google Analytics tracking
│   └── disqus.html       # Disqus comments embed
├── _layouts/             # Page layout templates (Liquid)
│   ├── default.html      # Base layout (nav, footer, fonts)
│   └── post.html         # Blog post layout (includes Disqus)
├── _posts/               # Blog posts (Markdown)
│   └── YYYY-MM-DD-slug.md
├── about/
│   └── index.html        # About page (placeholder)
├── blog/
│   ├── index.html        # Blog listing page
│   └── atom.xml          # Atom feed
├── css/
│   └── main.css          # Site-wide custom styles
├── cv/
│   └── index.html        # CV page (placeholder)
├── index.html            # Homepage
└── README.md
```

---

## Technology Stack

| Layer | Technology |
|---|---|
| Static site generator | Jekyll (Ruby) |
| Templating | Liquid |
| Markup | Markdown (kramdown dialect) |
| Styling | CSS3 (custom, no framework) |
| Fonts | Google Fonts (Open Sans, Work Sans) |
| Analytics | Google Analytics (UA-78948113-1) |
| Comments | Disqus (shortname: `prattatx`) |
| Hosting | GitHub Pages (automatic Jekyll build) |

---

## Jekyll Configuration (`_config.yml`)

```yaml
name: James Pratt, Horrible Cop
markdown: kramdown
permalink: /blog/:year/:month/:day/:title
paginate: 5
```

- Site name: **James Pratt, Horrible Cop**
- Blog URLs follow the pattern `/blog/YYYY/MM/DD/post-title`
- Pagination: 5 posts per page
- Markdown processor: kramdown

---

## Development Workflow

### Local Development

GitHub Pages uses Jekyll to build the site automatically on push. For local development:

```bash
# Install Jekyll (requires Ruby)
gem install jekyll bundler

# Serve locally with live reload
jekyll serve

# Build static output into _site/
jekyll build
```

The `_site/` directory is gitignored — it is the build output and should never be committed.

### Adding a Blog Post

1. Create a new file in `_posts/` with the naming convention: `YYYY-MM-DD-post-title.md`
2. Add front matter at the top:

```markdown
---
layout: post
title: "Your Post Title"
---

Post content here in Markdown.
```

3. Commit and push to `master` — GitHub Pages will rebuild automatically.

### Modifying Layouts

- Edit `_layouts/default.html` for site-wide changes (nav, footer, fonts, head)
- Edit `_layouts/post.html` for changes specific to blog post pages
- Edit `_includes/analytics.html` or `_includes/disqus.html` for third-party integrations

### Modifying Styles

All styles live in `css/main.css`. There is no CSS preprocessor (no Sass/Less). Write plain CSS3.

---

## Conventions

### File Naming
- Blog posts: `YYYY-MM-DD-kebab-case-title.md` (Jekyll requirement)
- Layouts/includes: lowercase with hyphens (e.g., `my-component.html`)
- Pages: placed in their own directory with `index.html` (e.g., `about/index.html`)

### Front Matter
Every content page must include a `layout` key. Blog posts use `layout: post`, other pages use `layout: default`:

```yaml
---
layout: default
title: "Page Title"
---
```

### Liquid Templating
- Output: `{{ variable }}`
- Logic: `{% if %} ... {% endif %}`, `{% for item in list %} ... {% endfor %}`
- Includes: `{% include filename.html %}`
- Access site config: `{{ site.name }}`
- Access page data: `{{ page.title }}`, `{{ page.url }}`, `{{ page.date }}`

---

## Incomplete / Placeholder Sections

The following sections exist structurally but need content:
- **`about/index.html`** — placeholder, needs personal bio content
- **`cv/index.html`** — placeholder, needs CV/resume content
- **Data Projects** — mentioned in README but not yet implemented

---

## Git Workflow

- Primary branch: `master` (auto-deployed by GitHub Pages)
- Feature branches: `claude/<description>-<id>` for AI-assisted changes
- No CI/CD pipelines — GitHub Pages handles deployment on push to `master`

---

## External Service IDs

| Service | ID |
|---|---|
| Google Analytics | UA-78948113-1 |
| Disqus shortname | prattatx |
