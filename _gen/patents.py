#!/usr/bin/env python3
"""
Build assets/data/patents.json from the verified patent database.

Source: Cowork OS/00_Resources/2026-08-07-james-pratt-patents-confirmed.csv
Only rows with Status == "Granted" are published. Granted U.S. patents are
public record; nothing here is confidential.

Compact schema keeps the payload small:
  p = [number, title, year, statusIdx, assigneeIdx, [inventorIdx, ...]]
"""

import csv
import json
import os
import re
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = "/mnt/user-data/uploads/Cowork OS/00_Resources/2026-08-07-james-pratt-patents-confirmed.csv"

STATUS = ["In force", "Expired", "Too recent to index"]
STATUS_MAP = {
    "Active (in force)": 0,
    "Expired, maintenance fees not paid": 1,
    "Unknown, too recent for Google Patents": 2,
}


def norm_name(n):
    """Merge 'Steven M. Belz' and 'Steven Belz' into one person."""
    n = re.sub(r"\s+", " ", n.strip())
    parts = [p for p in n.split(" ") if not re.fullmatch(r"[A-Z]\.?", p)]
    return " ".join(parts) if len(parts) >= 2 else n


def norm_assignee(a):
    u = a.upper()
    if "AT&T" in u or "AT&T" in a:
        return "AT&T"
    if "HYUNDAI" in u:
        return "Hyundai Motor Company"
    if "SIMPLISAFE" in u:
        return "SimpliSafe, Inc."
    return a.strip() or "Unassigned"


def main():
    all_rows = list(csv.DictReader(open(SRC, encoding="utf-8")))
    granted = [r for r in all_rows if r["Status"] == "Granted"]

    # canonical display name = most common spelling for each normalised person
    spellings = {}
    for r in granted:
        for raw in r["Co-inventors"].split(";"):
            raw = raw.strip()
            if not raw or raw.lower() == "none":
                continue
            spellings.setdefault(norm_name(raw), Counter())[raw] += 1
    canon = {k: v.most_common(1)[0][0] for k, v in spellings.items()}

    freq = Counter()
    for r in granted:
        seen = set()
        for raw in r["Co-inventors"].split(";"):
            raw = raw.strip()
            if not raw or raw.lower() == "none":
                continue
            seen.add(norm_name(raw))
        for k in seen:
            freq[k] += 1

    inventors = [canon[k] for k, _ in freq.most_common()]
    inv_idx = {canon[k]: i for i, (k, _) in enumerate(freq.most_common())}

    assignees = []
    asg_idx = {}
    patents = []
    for r in granted:
        num = r["Patent number"].strip()
        a = norm_assignee(r["Assignee / current owner"])
        if a not in asg_idx:
            asg_idx[a] = len(assignees)
            assignees.append(a)
        ppl = []
        seen = set()
        for raw in r["Co-inventors"].split(";"):
            raw = raw.strip()
            if not raw or raw.lower() == "none":
                continue
            k = norm_name(raw)
            if k in seen:
                continue
            seen.add(k)
            ppl.append(inv_idx[canon[k]])
        patents.append([
            num,
            r["Title"].strip(),
            int(r["Year"]) if r["Year"].isdigit() else 0,
            STATUS_MAP.get(r["Legal status"].strip(), 2),
            asg_idx[a],
            sorted(ppl),
        ])

    patents.sort(key=lambda p: (-p[2], p[0]))

    counts = {
        "records": len(all_rows),
        "granted": len(granted),
        "inForce": sum(1 for p in patents if p[3] == 0),
        "expired": sum(1 for p in patents if p[3] == 1),
        "tooRecent": sum(1 for p in patents if p[3] == 2),
        "publishedApps": sum(1 for r in all_rows if r["Status"].startswith("Published")),
        "noGrant": sum(1 for r in all_rows
                       if r["Status"] == "Published application, no grant on record"),
        "applications": len({r["Application number"] for r in all_rows
                             if r["Application number"].strip()}),
        "continuations": sum(1 for r in granted
                             if not r["Continuity to parent"].startswith("Original")),
        "collaborators": len(inventors),
    }

    years = Counter(p[2] for p in patents)
    hist = [[y, years.get(y, 0)] for y in range(min(years), max(years) + 1)]

    out = {
        "verified": "2026-08-07",
        "counts": counts,
        "status": STATUS,
        "assignees": assignees,
        "inventors": inventors,
        "hist": hist,
        "patents": patents,
    }

    d = os.path.join(ROOT, "assets", "data")
    os.makedirs(d, exist_ok=True)
    path = os.path.join(d, "patents.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, separators=(",", ":"), ensure_ascii=False)

    print("wrote %s (%.0f KB)" % (path, os.path.getsize(path) / 1024))
    print(json.dumps(counts, indent=2))
    print("years %d to %d, peak %d in %d" % (
        hist[0][0], hist[-1][0], max(h[1] for h in hist),
        max(hist, key=lambda h: h[1])[0]))
    print("top collaborators:", ", ".join(
        "%s (%d)" % (inventors[i], freq.most_common()[i][1]) for i in range(6)))


if __name__ == "__main__":
    main()
