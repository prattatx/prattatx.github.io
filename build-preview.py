#!/usr/bin/env python3
"""
Render a self-contained single-file preview of a Jekyll page.

Not a Jekyll replacement. It resolves just enough Liquid to produce an
accurate visual preview that can be opened without a server: fonts, CSS,
and JS are inlined so the file works anywhere.

Usage: python3 build-preview.py index.html _preview/home.html
"""

import base64
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

SITE = {
    "title": "James H. Pratt, Ph.D.",
    "author": "James H. Pratt",
    "description": (
        "Cognitive psychologist, founder, and AI product leader in Austin. "
        "Advisory, fractional AI product leadership, board seats, strategy "
        "sprints, and workshops."
    ),
    "url": "https://prattatx.github.io",
    "time": "2026",
    "calendar_url": "https://www.cal.com/james-pratt",
    "ga4": "",
}


def split_front_matter(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.S)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta, m.group(2)


def resolve_liquid(html, page):
    # {% if site.x %}...{% endif %}
    def sitecond(m):
        return m.group(2) if SITE.get(m.group(1)) else ""

    html = re.sub(
        r"\{%\s*if\s+site\.(\w+)\s*%\}(.*?)\{%\s*endif\s*%\}",
        sitecond, html, flags=re.S,
    )
    # {% if page.x == 'y' %}...{% endif %}
    def cond(m):
        key, want, body = m.group(1), m.group(2), m.group(3)
        return body if page.get(key) == want else ""

    html = re.sub(
        r"\{%\s*if\s+page\.(\w+)\s*==\s*'([^']*)'\s*%\}(.*?)\{%\s*endif\s*%\}",
        cond, html, flags=re.S,
    )
    # {% if page.x %}A{% else %}B{% endif %}
    def cond2(m):
        return m.group(2) if page.get(m.group(1)) else m.group(3)

    html = re.sub(
        r"\{%\s*if\s+page\.(\w+)\s*%\}(.*?)\{%\s*else\s*%\}(.*?)\{%\s*endif\s*%\}",
        cond2, html, flags=re.S,
    )
    # {{ page.x | default: site.y }}
    def dflt(m):
        return page.get(m.group(1)) or SITE.get(m.group(2), "")

    html = re.sub(
        r"\{\{\s*page\.(\w+)\s*\|\s*default:\s*site\.(\w+)\s*\}\}", dflt, html
    )
    # {{ site.time | date: '...' }}
    html = re.sub(r"\{\{\s*site\.time[^}]*\}\}", SITE["time"], html)
    # {{ site.x }} and {{ page.x }}
    html = re.sub(r"\{\{\s*site\.(\w+)\s*\}\}", lambda m: SITE.get(m.group(1), ""), html)
    html = re.sub(r"\{\{\s*page\.(\w+)\s*\}\}", lambda m: page.get(m.group(1), ""), html)
    # anything left over
    html = re.sub(r"\{%.*?%\}", "", html, flags=re.S)
    html = re.sub(r"\{\{.*?\}\}", "", html, flags=re.S)
    return html


def inline_fonts(css):
    def repl(m):
        rel = m.group(1).lstrip("/")
        path = os.path.join(ROOT, rel)
        with open(path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
        return "url('data:font/woff2;base64,%s')" % b64

    return re.sub(r"url\('([^']+\.woff2)'\)", repl, css)


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else "index.html"
    out = sys.argv[2] if len(sys.argv) > 2 else "_preview/home.html"

    with open(os.path.join(ROOT, src), encoding="utf-8") as f:
        page_meta, page_body = split_front_matter(f.read())

    layout = page_meta.get("layout", "default")
    with open(os.path.join(ROOT, "_layouts", layout + ".html"), encoding="utf-8") as f:
        shell = f.read()

    html = shell.replace("{{ content }}", page_body)
    html = resolve_liquid(html, page_meta)

    with open(os.path.join(ROOT, "assets/css/main.css"), encoding="utf-8") as f:
        css = inline_fonts(f.read())
    with open(os.path.join(ROOT, "assets/js/site.js"), encoding="utf-8") as f:
        js = f.read()

    html = re.sub(
        r'<link rel="preload"[^>]*>\s*', "", html
    )
    html = re.sub(
        r'<link rel="stylesheet" href="/assets/css/main\.css">',
        "<style>\n%s\n</style>" % css,
        html,
    )
    html = re.sub(
        r'<script src="/assets/js/site\.js" defer></script>',
        "<script>\n%s\n</script>" % js,
        html,
    )
    html = re.sub(r'<link rel="alternate"[^>]*>\s*', "", html)

    if "/assets/data/patents.json" in html:
        with open(os.path.join(ROOT, "assets/data/patents.json"), encoding="utf-8") as f:
            html = html.replace(
                "</head>",
                "<script>window.__PATENTS__=%s;</script>\n</head>" % f.read(),
            )

    os.makedirs(os.path.join(ROOT, os.path.dirname(out)), exist_ok=True)
    with open(os.path.join(ROOT, out), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote %s (%.0f KB)" % (out, os.path.getsize(os.path.join(ROOT, out)) / 1024))


if __name__ == "__main__":
    main()
