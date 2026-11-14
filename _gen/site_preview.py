#!/usr/bin/env python3
"""
Build a browsable preview of the whole site without Jekyll.

build-preview.py renders one page into one self-contained file. This renders
every page into a folder with root-relative URLs intact, so the result can be
served and clicked through like the live site:

    python3 _gen/site_preview.py            # writes _preview/site
    python3 -m http.server 4173 --directory _preview/site

It is not Jekyll. It reuses build-preview.py's Liquid resolver, copies assets
as they are, and renders posts through the post layout. Markdown posts are
converted with mistune, standing in for kramdown; if mistune is not installed
the script says so and stops, because a preview that shows raw Markdown looks
like a broken post (2026-11-14: two posts were reported as broken when only
the preview was).

What it cannot show: the Atom feed, the sitemap, and anything kramdown does
that mistune does not. The first push to GitHub Pages is still the real test
of the templates.
"""
import importlib.util
import os
import re
import shutil
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.join(REPO, "_preview", "site")

try:
    import mistune
except ImportError:
    sys.exit("site_preview.py needs mistune to render Markdown posts: pip install mistune")

spec = importlib.util.spec_from_file_location("bp", os.path.join(REPO, "build-preview.py"))
bp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bp)

SKIP_DIRS = {".git", "_preview", "_gen", "docs", "node_modules", ".claude", ".hallmark",
             ".impeccable", ".superpowers", "_layouts", "_includes", "_posts", "_site"}
SKIP_FILES = {"CLAUDE.md", "README.md", "PRODUCT.md", "design.md", "build-preview.py",
              "LICENSE", ".DS_Store", ".gitignore", "_config.yml"}
POSTDATE = "__POSTDATE__"


def to_html(md):
    """Markdown to HTML. Raw HTML blocks, such as <figure>, pass through."""
    if hasattr(mistune, "create_markdown"):
        return mistune.create_markdown(escape=False, plugins=["table", "strikethrough", "footnotes"])(md)
    return mistune.markdown(md, escape=False)


def layout(name):
    with open(os.path.join(REPO, "_layouts", name + ".html"), encoding="utf-8") as f:
        # build-preview.py drops {{ page.date | date: ... }}; keep a marker for it
        text = re.sub(r"\{\{\s*page\.date\s*\|[^}]*\}\}", POSTDATE, f.read())
        return bp.split_front_matter(text)


def render(meta, body):
    name = meta.get("layout", "default")
    depth = 0
    while name and name != "null" and depth < 4:
        lmeta, lbody = layout(name)
        body = lbody.replace("{{ content }}", body)
        for key, value in lmeta.items():
            if key != "layout":
                meta.setdefault(key, value)
        name = lmeta.get("layout")
        depth += 1
    return bp.resolve_liquid(body, meta)


def write(rel, text):
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    pages = 0
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            if name in SKIP_FILES:
                continue
            src = os.path.join(root, name)
            rel = os.path.relpath(src, REPO)
            if name.endswith((".html", ".xml")):
                with open(src, encoding="utf-8") as f:
                    text = f.read()
                if text.startswith("---"):
                    meta, body = bp.split_front_matter(text)
                    meta["url"] = "/" + rel.replace("index.html", "")
                    write(rel, render(meta, body))
                    pages += 1
                    continue
            dst = os.path.join(OUT, rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copyfile(src, dst)

    for post in bp.load_posts():
        y, mo, d, slug = post["url"].strip("/").split("/")[1:]
        for ext in ("html", "md"):
            src = os.path.join(REPO, "_posts", "%s-%s-%s-%s.%s" % (y, mo, d, slug, ext))
            if not os.path.exists(src):
                continue
            with open(src, encoding="utf-8") as f:
                meta, body = bp.split_front_matter(f.read())
            meta["url"] = post["url"]
            if ext == "md":
                body = to_html(body)
            html = render(meta, body).replace(POSTDATE, post["date"].strftime("%B %-d, %Y"))
            write(post["url"].strip("/") + "/index.html", html)
            pages += 1

    print("built %d pages into %s" % (pages, OUT))
    unresolved = []
    for root, _, files in os.walk(OUT):
        for name in files:
            if name.endswith(".html"):
                with open(os.path.join(root, name), encoding="utf-8") as f:
                    if re.search(r"\{%|\{\{", f.read()):
                        unresolved.append(os.path.relpath(os.path.join(root, name), OUT))
    print("pages with unresolved Liquid:", unresolved or "none")
    if unresolved:
        sys.exit(1)


if __name__ == "__main__":
    main()
