#!/usr/bin/env python3
"""
Sort the 358 granted patents into subject categories, by title.

The patent record carries no classification codes, so the category is read
from the title. RULES is an ordered list: the first rule whose pattern matches
wins, so the more specific subjects sit above the broader ones. A title that
matches nothing stops the run, because a silent "Other" bucket would hide a
patent nobody looked at.

Run on its own to add or refresh the categories in assets/data/patents.json:

    python3 _gen/patent_categories.py

_gen/patents.py imports categorize() so a rebuild from the CSV keeps them.
The category is the seventh field of each patent row: an index into the
top-level "categories" list.
"""

import json
import os
import re
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "assets", "data", "patents.json")

CATEGORIES = [
    "AI and machine learning",
    "Extended reality and avatars",
    "Video and media",
    "TV and remote control",
    "Sensing, sound and health",
    "Security, identity and trust",
    "Networks, edge and satellite",
    "Messaging, social and collaboration",
    "Commerce and customer service",
    "Vehicles, drones and devices",
]

# (category, pattern). Order matters: first match wins.
RULES = [
    # Titles a broader rule below would misfile. Each was read and placed by
    # hand on 2026-11-14.
    ("Sensing, sound and health", r"monitor a person|sound sensors|sound signatures|alertness levels"),
    ("Networks, edge and satellite", r"network slices|subscriber identification module \(SIM\) capabilities|"
                                     r"transmission profile"),
    ("Messaging, social and collaboration", r"nonhuman social media"),
    ("Commerce and customer service", r"in-store visualizations"),
    ("Video and media", r"image-based techniques for audio|video annotation"),
    ("Vehicles, drones and devices", r"screensaver"),

    # Remote controls and the television set come next: their titles also
    # mention "device", "media" and "network".
    ("TV and remote control", r"remote control|set-top box|television|internet protocol television|"
                              r"screensaver|media display functions|network back-channel"),

    ("Extended reality and avatars", r"reality|metaverse|meta verse|avatar|immersi|virtual historical|"
                                     r"virtual interaction|in-store visualizations"),

    ("Vehicles, drones and devices", r"drone|aerial vehicle|vehicle|vehicular|robot|movement assistance|"
                                     r"3-d printing|luggage|dinnerware|display orientation|display timeout|"
                                     r"skin contact|predictive human interface|appearance of a surf|"
                                     r"interactive surface|wireless energy|antenna selection|"
                                     r"device capability signaling|configuration settings of a device|"
                                     r"user output preferences|micro-environment|environmental control|"
                                     r"customized settings"),

    ("AI and machine learning", r"machine learning|machine cognition|automated assistant|multi-agent|"
                                r"synthetic media|predicted capacity|propensities|predictive search|"
                                r"emotion detection|personalization according to mood|"
                                r"consistent generation of media|algorithmic content|"
                                r"optimization of events|alertness levels|applied machine"),

    ("Security, identity and trust", r"authenticat|security|trust|fraud|malware|threat|anonymizer|"
                                     r"obfuscate|masking content|watermark|blockchain|ledger|"
                                     r"temporary identifiers|electronic influence|hijack|"
                                     r"documentary evidence|controlling access|control access|"
                                     r"policy definition|subscriber identification module"),

    ("Sensing, sound and health", r"sensor|acoustic|sound|scent|audio adjustment|electromagnetic|"
                                  r"monitoring health|monitor a person|telemedicine|nutritional|"
                                  r"cognitive stimulation|neurological|biological|physical environment|"
                                  r"modifying behavior|space characterization|ambient data|"
                                  r"image-based techniques for audio"),

    ("Networks, edge and satellite", r"satellite|network slices|edge|network resources|"
                                     r"network attached compute|virtual network function|connectivity|"
                                     r"routing areas|transmission profile|quality of service|"
                                     r"communication network events|managing a network|packet loss|"
                                     r"bandwidth|data synchronization|cross-service broker|"
                                     r"traffic policy|data parking|location data|location information|"
                                     r"network access|network-based services"),

    ("Commerce and customer service", r"point-of-sale|point of sale|advertis|promotion|merchandising|"
                                      r"customer service|purchase|hospitality|billing|supply chain|"
                                      r"reuse of an asset|products and mobile devices|consumable items"),

    ("Video and media", r"video|media|content|streaming|playback|images|audio signals|"
                        r"interactive voice response|gaming"),

    ("Messaging, social and collaboration", r"messaging|social|communit|collaborat|meeting|conferencing|"
                                            r"calendar|address book|communication|expertise|"
                                            r"audience feedback|members of a group|event-share|"
                                            r"role membership|navigation"),
]

COMPILED = [(CATEGORIES.index(name), re.compile(pattern, re.I)) for name, pattern in RULES]


def categorize(title):
    """Index into CATEGORIES for a patent title, or None if no rule matches."""
    for idx, pattern in COMPILED:
        if pattern.search(title):
            return idx
    return None


def main():
    with open(DATA, encoding="utf-8") as f:
        data = json.load(f)

    missing = []
    for row in data["patents"]:
        cat = categorize(row[1])
        if cat is None:
            missing.append(row[1])
            continue
        if len(row) > 6:
            row[6] = cat
        else:
            row.append(cat)
    if missing:
        sys.exit("no category for:\n  " + "\n  ".join(sorted(set(missing))))

    data["categories"] = CATEGORIES
    with open(DATA, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, separators=(",", ":"))

    counts = Counter(row[6] for row in data["patents"])
    assert sum(counts.values()) == len(data["patents"])
    for i, name in enumerate(CATEGORIES):
        print("%3d  %s" % (counts[i], name))
    print("%3d  total" % sum(counts.values()))

    if "--list" in sys.argv:
        seen = {}
        for row in data["patents"]:
            seen.setdefault(row[6], set()).add(row[1])
        for i, name in enumerate(CATEGORIES):
            print("\n## " + name)
            for title in sorted(seen.get(i, ())):
                print("  " + title[:100])


if __name__ == "__main__":
    main()
