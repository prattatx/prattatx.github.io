#!/usr/bin/env python3
"""
Generate the /work/ index and the nine case-study pages as plain Jekyll pages
(front matter + default layout, no collections). Source of truth for the copy
is Career Management/Portfolio/Portfolio Resources/*.md, sanitized per the
2026-08-13 clearance: text only, all confidential-stamped images removed.
"""

import os
import textwrap

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENGAGEMENTS = {
    "A": "Fractional / advisory AI product lead",
    "B": "Expert consult",
    "C": "Board or advisor",
    "D": "Strategy sprint",
    "E": "Workshops and speaking",
}

CASES = [
    {
        "slug": "patent-development-workshop",
        "title": "Turning a founder's invention into a patent pipeline",
        "kicker": "Case study / Consulting engagement",
        "year": "2025",
        "sort": "2025-06",
        "blurb": "A single-day workshop for an early-stage hardware startup. Product dissection, "
                 "use-journey mapping, my own 10x ideation method, then scored down to a "
                 "counsel-ready shortlist.",
        "role": "Designed and led the workshop as a paid consulting engagement. Set the agenda, "
                "facilitated the strategy and ideation segments, and authored the method. "
                "Colleagues co-facilitated individual segments.",
        "context": "An early-stage hardware startup in the balance and movement-training space. "
                   "Client unnamed.",
        "eng": ["E", "B"],
        "date": "June 2025",
        "sanitized": "Method-only. Client unnamed. The client's specific inventions, scoring "
                     "frameworks, and filings are withheld. The facilitation method described is my own.",
        "body": [
            ("The problem", ["<p>A founder with deep domain expertise and a shippable product had real "
                             "invention in hand but no structured way to convert it into a defensible "
                             "patent portfolio. The goal was to surface novel, non-obvious, patentable "
                             "concepts, prioritize them, and hand clean direction to patent counsel, "
                             "rather than filing reactively one idea at a time.</p>"]),
            ("The approach", ["<p>A single-day workshop I designed to move from strategy to a prioritized, "
                              "counsel-ready shortlist.</p>",
                              "<ul>"
                              "<li><strong>Why patents.</strong> Facilitated discussion to pin down what the "
                              "portfolio was actually for: licensing, defensibility, visibility, and how "
                              "aggressively to file.</li>"
                              "<li><strong>Product dissection.</strong> Deconstructed the existing product into "
                              "features, mechanisms, and materials, the raw surface area where claims live.</li>"
                              "<li><strong>Customer-use journey mapping.</strong> Mapped diverse use cases across "
                              "markets to expose where new, ownable utility could emerge.</li>"
                              "<li><strong>10x ideas.</strong> My own facilitation method: push participants to "
                              "imagine the product ten times bigger, not ten percent better, across three prompt "
                              "categories (extreme use cases, exponential technology jumps, unexpected user mashups), "
                              "favoring quantity and non-obviousness over feasibility.</li>"
                              "<li><strong>Sort, score, prioritize.</strong> Affinity-grouped the ideas, filtered each "
                              "against a patent test (novel, useful, non-obvious, describable, strategically "
                              "valuable), then dot-voted to a shortlist.</li>"
                              "</ul>"]),
            ("The outcome", ["<p>A prioritized shortlist of patentable concepts with a clear filing direction, "
                             "including provisional strategy, that fed directly to patent counsel. Ad-hoc "
                             "filing replaced with a deliberate, founder-aligned portfolio plan.</p>"]),
            ("What it demonstrates", ["<ul>"
                                      "<li>A repeatable method for turning a founder's raw invention into a "
                                      "prioritized, defensible patent pipeline.</li>"
                                      "<li>Facilitating strategy and divergent ideation, then converging to a "
                                      "scored, decision-ready shortlist.</li>"
                                      "<li>Bridging product, human-factors thinking, and IP strategy, drawing on a "
                                      "track record as named inventor on 358 granted U.S. patents.</li>"
                                      "</ul>"]),
            ("Reusable asset", ["<p>The <strong>10x Ideas facilitation guide</strong> (three prompt categories, "
                                "timed divergent rounds, affinity sorting, patent-filter voting) is a standalone "
                                "method I can run for any inventive team. It is mine to share. The client's "
                                "session content is not.</p>"]),
        ],
    },
    {
        "slug": "att-design-thinking-workshop",
        "title": "Thirty ideas to one product vision, in a day",
        "kicker": "Case study / Enterprise program",
        "year": "2019",
        "sort": "2019-04",
        "blurb": "Conceived, funded, and led a design-thinking program inside a Fortune 10 Chief Data "
                 "Office. Ten participants, thirty raw ideas, one prioritized developer-hub vision "
                 "leadership could defend.",
        "role": "Conceived, designed, and funded the program within the Chief Data Office (AI User "
                "Experience), and led it end to end. Engaged an external firm to facilitate the "
                "session to my design.",
        "context": "Chief Data Office of a Fortune 10 telecom.",
        "eng": ["D", "E"],
        "date": "2019",
        "sanitized": "Method-only. Proprietary tool names, participant names, and specific persona "
                     "detail removed. No confidential employer material reproduced.",
        "body": [
            ("The problem", ["<p>Developers inside a large enterprise were losing time to tool sprawl: five "
                             "to six tools in a single development workflow, redundant systems with "
                             "overlapping features, weak ways to find and reuse existing work, and almost no "
                             "social or recognition layer connecting people doing similar things.</p>",
                             "<p>The question driving the work: how do you streamline the way developers "
                             "access resources and innovate, in a way that fosters collaboration and reuse?</p>"]),
            ("The approach", ["<p>A structured design-thinking workshop built on prior-state research: an "
                              "earlier discovery workshop plus developer interviews. The session moved through "
                              "a deliberate sequence.</p>",
                              "<ul>"
                              "<li><strong>Persona grounding</strong>, so every later decision traced back to a "
                              "real user rather than an abstraction.</li>"
                              "<li><strong>As-is scenario mapping</strong> to surface where the current experience "
                              "broke down.</li>"
                              "<li><strong>Big-idea generation</strong>, producing roughly thirty candidate "
                              "concepts.</li>"
                              "<li><strong>Prioritization</strong> on an impact-versus-feasibility matrix, "
                              "separating no-brainers from big bets and save-for-laters.</li>"
                              "<li><strong>Prototype deep dive</strong> to make the winning direction tangible.</li>"
                              "</ul>"]),
            ("The outcome", ["<p>Ten participants and thirty raw ideas converged to a single prioritized "
                             "product vision: a developer hub combining a community layer, recommendation of "
                             "existing components and data, contribution recognition, and individualized "
                             "profiles.</p>",
                             "<p>The prioritization matrix gave leadership a defensible rationale for what to "
                             "build first versus defer, and the session closed with a concrete prototype and a "
                             "next-step timeline rather than a list of opinions.</p>"]),
            ("What it demonstrates", ["<ul>"
                                      "<li>Running human-centered method at enterprise scale to turn diffuse "
                                      "frustration into a prioritized, buildable direction.</li>"
                                      "<li>Anchoring product decisions in personas and as-is reality, not feature "
                                      "wish-lists.</li>"
                                      "<li>Facilitated convergence: many voices, one vision, with a transparent "
                                      "prioritization rationale stakeholders can stand behind.</li>"
                                      "</ul>"]),
        ],
    },
    {
        "slug": "tessa-investor-narrative",
        "title": "Making a new category legible to investors",
        "kicker": "Case study / Founder work",
        "year": "2026",
        "sort": "2026-01",
        "blurb": "The narrative architecture behind a pre-seed ambient-AI deck. One protagonist, then "
                 "the market, then the wedge. Every claim sourced or labeled an assumption so it held "
                 "under diligence.",
        "role": "Authored and designed the investor narrative and deck as founder and CEO.",
        "context": "Pre-seed ambient-AI consumer hardware and software startup. My own company.",
        "eng": ["A", "D"],
        "date": "2025 to 2026, iterated across versions",
        "sanitized": "Method-only. Traction, financials, raise terms, and team specifics removed. "
                     "Focus is the narrative architecture and the craft.",
        "body": [
            ("The problem", ["<p>A novel product in an unfamiliar category had to be made instantly legible "
                             "to investors: what it is, why now, who buys it, and why it wins. Roughly fifteen "
                             "slides, without drowning the story in features.</p>"]),
            ("The approach", ["<p>A deliberately sequenced narrative arc, each slide doing exactly one job.</p>",
                              "<ul>"
                              "<li><strong>Problem</strong> told through a single named protagonist, not "
                              "statistics, so the pain lands emotionally before it is sized.</li>"
                              "<li><strong>Scale and why-now</strong> to turn the personal story into a market.</li>"
                              "<li><strong>Solution</strong> framed as quantified outcomes, what changes for the "
                              "user, not a feature list.</li>"
                              "<li><strong>Traction, how it works, market, model, go-to-market</strong> in an "
                              "order that answers the next question an investor would ask, in the order they "
                              "ask it.</li>"
                              "<li><strong>Competition</strong> as a positioning table that makes the wedge "
                              "obvious at a glance, rather than claiming superiority on every axis.</li>"
                              "<li><strong>Team, roadmap, and the ask</strong> to close on credibility and a "
                              "concrete next milestone.</li>"
                              "</ul>",
                              "<p>Every claim was tied to a cited source or labeled as an assumption, so the "
                              "deck held up under diligence.</p>"]),
            ("The outcome", ["<p>A tight, diligence-ready investor narrative that distills a complex ambient-AI "
                             "product into a legible, sequenced story with a clear wedge and a concrete "
                             "milestone. Iterated across multiple versions against investor feedback.</p>"]),
            ("What it demonstrates", ["<ul>"
                                      "<li>Architecting an investor narrative: sequencing, emotional hook, then "
                                      "proof.</li>"
                                      "<li>Framing a product as quantified user outcomes rather than features.</li>"
                                      "<li>Positioning a new entrant in a crowded category so the wedge is "
                                      "unmistakable.</li>"
                                      "</ul>"]),
        ],
    },
    {
        "slug": "tessa-competitive-analysis",
        "title": "A living competitive picture, not a one-off teardown",
        "kicker": "Case study / Founder work",
        "year": "2026",
        "sort": "2026-02",
        "blurb": "A structured competitive-intelligence program for an emerging consumer-AI category: "
                 "comparable deep dives, a positioning map, an interactive dashboard, and a weekly scan "
                 "that keeps it current.",
        "role": "Directed and produced the competitive-analysis program as founder and CEO.",
        "context": "Emerging consumer-AI category. My own company.",
        "eng": ["A", "B", "D"],
        "date": "2026",
        "sanitized": "Method-only. Competitor names, strategic conclusions, threat assessments, and "
                     "partner targets removed. Focus is the analysis method.",
        "body": [
            ("The problem", ["<p>A fast-moving category with well-funded entrants and no settled positioning. "
                             "The company needed a rigorous, independently sourced read of the landscape, and "
                             "a way to keep it current, to decide where to differentiate rather than where to "
                             "match.</p>"]),
            ("The approach", ["<p>A structured competitive-intelligence program rather than a one-off scan.</p>",
                              "<ul>"
                              "<li><strong>Shortlist discipline.</strong> A defined set of competitors, each "
                              "chosen to stress-test the positioning thesis from a different angle: direct "
                              "analog, best-funded peer, adjacent category, wildcard.</li>"
                              "<li><strong>Structured deep dives.</strong> Each competitor analyzed on a "
                              "consistent frame (buyer, wedge, funding, technology approach, defensibility) so "
                              "they were comparable, not anecdotal.</li>"
                              "<li><strong>Positioning map.</strong> Defined the axes that actually separated the "
                              "field and placed every player on them, exposing the unoccupied position.</li>"
                              "<li><strong>Interactive dashboard</strong> so the analysis was navigable and "
                              "reusable by the team, not a static slide.</li>"
                              "<li><strong>Ongoing monitoring.</strong> A weekly news-scan cadence so the picture "
                              "stayed live as competitors raised, launched, and pivoted.</li>"
                              "</ul>"]),
            ("The outcome", ["<p>A living competitive picture that turned a noisy field into a clear, defensible "
                             "wedge and an ongoing intelligence cadence, used to align the team and prioritize "
                             "where to compete.</p>"]),
            ("What it demonstrates", ["<ul>"
                                      "<li>Designing a repeatable competitive-intelligence method, not a one-off "
                                      "teardown.</li>"
                                      "<li>Building comparable, structured analysis and a navigable dashboard from "
                                      "messy market signal.</li>"
                                      "<li>Translating landscape analysis into a positioning thesis and prioritized "
                                      "moves.</li>"
                                      "</ul>"]),
        ],
    },
    {
        "slug": "tessa-product-design-decision",
        "title": "Designing for engagement without losing safety positioning",
        "kicker": "Case study / Founder work",
        "year": "2026",
        "sort": "2026-03",
        "blurb": "A shipped app built around urgent alerts showed almost nothing on a normal day. "
                 "Three optioned designs, grounded in evidence, resolved the tension between habit and "
                 "safety.",
        "role": "Led the product and UX design analysis and authored the recommendation.",
        "context": "Consumer ambient-AI app. My own company.",
        "eng": ["A", "D"],
        "date": "2026",
        "sanitized": "Method-only. Internal strategy, advisor dynamics, financials, and unreleased "
                     "specifics removed. Focus is the product-design reasoning.",
        "body": [
            ("The problem", ["<p>A shipped app was built around urgent alerts, so on a normal day it showed "
                             "almost nothing. That is correct for a pure safety net and wrong for building a "
                             "habit. When nothing fires there is nothing to open, no habit forms, and the "
                             "product feels dead during the long stretches when nothing is wrong.</p>",
                             "<p>The documented engagement targets (regular weekly opens, opens without a "
                             "preceding notification) could not be met by an alerts-only screen.</p>"]),
            ("The approach", ["<p>A crisp design decision framed as options, not opinions.</p>",
                              "<ul>"
                              "<li><strong>Named the real question.</strong> Should the app deliver ambient value "
                              "between alerts, or stay an intentionally quiet safety net? The UI choice and the "
                              "strategy question were the same question.</li>"
                              "<li><strong>Designed three quiet-day options</strong> along a clear spectrum: an "
                              "empty baseline, a low-cost proof-of-life status rollup, and a reassurance layer "
                              "surfacing routine signals the system already detects. Alerts stayed the hero in "
                              "every option.</li>"
                              "<li><strong>Grounded each in evidence:</strong> documented caregiver needs and the "
                              "team's own behavioral targets, not preference.</li>"
                              "<li><strong>Made the case with a customer-journey narrative:</strong> the same quiet "
                              "week experienced two ways, showing how an empty app loses a friendly user while a "
                              "reassurance layer earns a daily habit.</li>"
                              "<li><strong>Kept it pragmatic.</strong> The recommended option reused signals the "
                              "backend already produced: light UI work, no new ML.</li>"
                              "</ul>"]),
            ("The outcome", ["<p>A clear, evidence-backed recommendation with a low-risk build path that "
                             "resolved an engagement-versus-safety tension, framed so decision-makers could "
                             "choose on merits.</p>"]),
            ("What it demonstrates", ["<ul>"
                                      "<li>Turning a fuzzy product tension into a crisp, optioned decision with a "
                                      "recommendation.</li>"
                                      "<li>Grounding design choices in documented user needs and behavioral "
                                      "targets.</li>"
                                      "<li>Using customer-journey storytelling to make a product case, with a "
                                      "pragmatic, low-cost build path.</li>"
                                      "</ul>"]),
        ],
    },
    {
        "slug": "att-persona-research",
        "title": "North Star: customer-centric design for enterprise analytics",
        "kicker": "Case study / Enterprise research program",
        "year": "2018",
        "sort": "2018-11",
        "blurb": "A mixed-method UX research program inside a Fortune 10 Chief Data Office. Contextual "
                 "inquiry, cognitive task analysis, and survey validation produced personas leadership "
                 "could actually prioritize against.",
        "role": "Led and directed the UX research program within the Chief Data Office (AI User "
                "Experience), defining the research plan and methods and translating findings into "
                "product direction.",
        "context": "Chief Data Office of a Fortune 10 telecom, designing service and self-service "
                   "analytics systems for internal data analysts.",
        "eng": ["B", "D", "E"],
        "date": "2018 to 2019",
        "sanitized": "Method-only. Proprietary tool names, real persona content, and internal data "
                     "removed. No confidential employer material reproduced. Consolidates the North Star "
                     "customer-centric design program and its persona-research workstream, which were one "
                     "body of work.",
        "body": [
            ("The problem", ["<p>The organization wanted data-powered decision-making across a "
                             "200,000-person company, but the analytics tools its own data analysts used "
                             "carried friction that slowed adoption. Leadership needed product decisions "
                             "grounded in how analysts actually worked, not assumptions, to raise "
                             "effectiveness without taxing the efficiency of skilled users.</p>"]),
            ("The approach", ["<p>A formal User Experience Research Plan applying human-factors engineering "
                              "to persona development, then using those personas to drive design.</p>",
                              "<ul>"
                              "<li><strong>Contextual inquiry</strong>, observing analysts doing real work in "
                              "their existing tool suite.</li>"
                              "<li><strong>Cognitive task analysis</strong> to locate pain points and the drivers "
                              "of productivity.</li>"
                              "<li><strong>Empathy mapping</strong> (think, feel, say, do) to build a shared, "
                              "human picture of the user.</li>"
                              "<li><strong>Training-needs and tool-gap analysis</strong> to separate capability "
                              "gaps from design gaps.</li>"
                              "<li><strong>UI analysis</strong> to surface usability issues in current and proposed "
                              "systems.</li>"
                              "<li><strong>Survey research</strong> to quantify and validate the qualitative signal "
                              "at scale.</li>"
                              "</ul>",
                              "<p>Findings rolled up into a customer-centric design approach: personas, "
                              "objectives, and a vision-casting frame that gave the organization a common "
                              "reference for prioritization.</p>"]),
            ("The outcome", ["<p>A validated persona set and a customer-centric design framework that "
                             "grounded analytics-product decisions in real analyst behavior. Leadership got a "
                             "defensible basis for prioritizing friction reduction where it mattered most, in "
                             "service of enabling data-driven decisions company-wide.</p>"]),
            ("What it demonstrates", ["<ul>"
                                      "<li>Standing up rigorous, mixed-method UX research, qualitative plus survey "
                                      "validation, inside a large enterprise.</li>"
                                      "<li>Translating human-factors findings into personas and a design framework "
                                      "leadership can act on.</li>"
                                      "<li>Connecting research to a business objective (adoption, effectiveness, "
                                      "cost and revenue) rather than usability for its own sake.</li>"
                                      "</ul>"]),
        ],
    },
    {
        "slug": "att-focus-groups",
        "title": "Validating a discovery concept before anyone built it",
        "kicker": "Case study / Enterprise research",
        "year": "2019",
        "sort": "2019-09",
        "blurb": "Task-based focus groups run against an interactive prototype. Fixed flows, comparable "
                 "signal, and a de-risked engineering investment.",
        "role": "Led and directed the research within the Chief Data Office (AI User Experience): "
                "designed the protocol, the task flows, and the prototype-driven test plan.",
        "context": "Chief Data Office of a Fortune 10 telecom, validating a data and analytics discovery "
                   "concept before build.",
        "eng": ["B", "E"],
        "date": "2019",
        "sanitized": "Method-only. Proprietary tool names, real participant names and IDs, and internal "
                     "data removed. No confidential employer material reproduced.",
        "body": [
            ("The problem", ["<p>A new analytics discovery concept needed validation with real users before "
                             "engineering invested in building it. The team needed evidence that the core "
                             "flows, finding the right people, finding the right data, and searching "
                             "effectively, matched how analysts actually think and work.</p>"]),
            ("The approach", ["<p>Structured, task-based focus groups run against an interactive prototype "
                              "rather than open-ended discussion. The protocol walked participants through a "
                              "defined set of flows.</p>",
                              "<ul>"
                              "<li>Reviewing and orienting on the home page.</li>"
                              "<li>Selecting a subject-matter-expert card and reaching the detail view.</li>"
                              "<li>Selecting a data card and reaching the detail view.</li>"
                              "<li>Searching from the home page, including filters and type-ahead suggestion, "
                              "through to results and a detail page.</li>"
                              "</ul>",
                              "<p>Each flow had a fixed sequence of prototype screens, so feedback was "
                              "comparable across participants and tied to a concrete interaction rather than a "
                              "hypothetical.</p>"]),
            ("The outcome", ["<p>Comparable, flow-level feedback on a concept before build, letting the team "
                             "refine the prototype and de-risk the engineering investment. The protocol turned "
                             "subjective reactions into structured signal mapped to specific screens and "
                             "tasks.</p>"]),
            ("What it demonstrates", ["<ul>"
                                      "<li>Designing a rigorous, task-based concept-testing protocol rather than "
                                      "unstructured feedback sessions.</li>"
                                      "<li>Using interactive prototypes to validate flows with users before "
                                      "committing build effort.</li>"
                                      "<li>Producing comparable, decision-ready research signal at enterprise "
                                      "scale.</li>"
                                      "</ul>"]),
        ],
    },
    {
        "slug": "att-data-product-catalog",
        "title": "Making enterprise data findable, traceable, and reusable",
        "kicker": "Case study / Product and UI design",
        "year": "2021",
        "sort": "2021-06",
        "blurb": "A data product catalog for a Fortune 10 Chief Data Office. Search, lineage, and data "
                 "flows in one interface, designed for web and mobile, so analysts stopped emailing data "
                 "owners.",
        "role": "Led the product and UX design within the Chief Data Office (AI User Experience). "
                "Spearheaded a multidisciplinary team of engineers and leaders to a shared design, "
                "applying human-factors methods without labeling them as such.",
        "context": "Chief Data Office of a Fortune 10 telecom, building self-service data findability "
                   "for internal analysts and data scientists.",
        "eng": ["A", "D"],
        "date": "2021",
        "sanitized": "Method-only. No confidential employer material reproduced. Interface visuals are "
                     "withheld pending permission clearance.",
        "body": [
            ("The problem", ["<p>In a large enterprise, analysts and data scientists struggled to find, "
                             "understand, and reuse data products across business units. Metadata lived in one "
                             "place, the data in another, lineage somewhere else, so people fell back on "
                             "emailing data owners or asking their team. The result was duplicated effort and "
                             "slow time-to-insight.</p>"]),
            ("The approach", ["<p>A product and UX design effort to make data discoverable and reusable "
                              "through a single catalog, designed for both web and mobile.</p>",
                              "<ul>"
                              "<li>A browseable, searchable catalog of data products with type-ahead and "
                              "filtering.</li>"
                              "<li>Visible product lineage and data flows, so users could trust and trace what "
                              "they found.</li>"
                              "<li>Detail views connecting metadata to access paths, collapsing the hop between "
                              "learning about a data product and using it.</li>"
                              "<li>Designed across web and mobile so the experience held up wherever analysts "
                              "worked.</li>"
                              "</ul>",
                              "<p>The work was grounded in the same human-factors research that produced the "
                              "persona and customer-centric design program. Design decisions traced back to how "
                              "analysts actually search and decide.</p>"]),
            ("The outcome", ["<p>A concrete, designed catalog concept that turned scattered data-discovery "
                             "behavior into a single coherent interface, giving engineering a clear target and "
                             "leadership a tangible vision for self-service data findability.</p>"]),
            ("What it demonstrates", ["<ul>"
                                      "<li>AI product and UI design at enterprise scale, web and mobile.</li>"
                                      "<li>Designing for data findability, trust through lineage, and reuse, not "
                                      "just screens.</li>"
                                      "<li>Translating user research into a shippable interface concept.</li>"
                                      "</ul>"]),
        ],
    },
    {
        "slug": "att-white-papers",
        "title": "Giving a 200,000-person company shared language for AI",
        "kicker": "Case study / Thought leadership",
        "year": "2017",
        "sort": "2017-01",
        "blurb": "Lead author of an enterprise automation white paper and the Data Powered series. "
                 "Convene the experts, converge the viewpoints, author the synthesis, ship a framework "
                 "people actually use.",
        "role": "Lead author. Spearheaded and aligned multidisciplinary contributors, engineers and "
                "senior leaders, to produce shared, authoritative artifacts, applying human-factors "
                "methods to get everyone on the same page without labeling the method as such.",
        "context": "Chief Data Office of a Fortune 10 telecom.",
        "eng": ["B", "C", "E"],
        "date": "2017 and following",
        "sanitized": "Describes authorship and method. Proprietary internal detail not reproduced. "
                     "The papers themselves are not published here.",
        "body": [
            ("The problem", ["<p>A large enterprise pushing into AI, automation, and data-driven "
                             "decision-making lacked shared language and frameworks for it. Many smart people "
                             "held pieces of the picture across different teams, but there was no "
                             "authoritative, common reference to align strategy and investment.</p>"]),
            ("The approach", ["<p>Convene the right experts, align them, and synthesize the result into "
                              "authoritative thought leadership. Across multiple papers, including an "
                              "enterprise automation white paper and the Data Powered series, the method was "
                              "consistent.</p>",
                              "<ul>"
                              "<li>Bring engineers and leaders together and surface what each actually knew.</li>"
                              "<li>Use human-factors and facilitation techniques to converge many viewpoints into "
                              "one coherent narrative.</li>"
                              "<li>Author and structure the synthesis, including durable frameworks such as a "
                              "five-milestone automation maturity model.</li>"
                              "</ul>",
                              "<p>On the automation white paper, a senior leader was listed first for "
                              "internal-political reasons, understood by everyone involved. The lead authorship "
                              "and synthesis were mine.</p>"]),
            ("The outcome", ["<p>Published internal thought leadership that gave the organization shared "
                             "language and frameworks for AI and automation, used to align strategy and orient "
                             "teams. The work established a common reference point rather than another siloed "
                             "opinion.</p>"]),
            ("What it demonstrates", ["<ul>"
                                      "<li>Lead authorship of enterprise AI and automation thought leadership.</li>"
                                      "<li>Orchestrating multidisciplinary experts to a shared, authoritative "
                                      "artifact.</li>"
                                      "<li>Human-factors-driven facilitation and synthesis applied to strategy, not "
                                      "just interfaces.</li>"
                                      "</ul>"]),
        ],
    },
]

ORDER = [c["slug"] for c in sorted(CASES, key=lambda c: c["sort"], reverse=True)]


def tags_html(eng, year=None):
    out = "".join('<span class="tag" title="%s">%s</span>' % (ENGAGEMENTS[e], e) for e in eng)
    if year:
        out += '<span class="tag tag-quiet">%s</span>' % year
    return out


def write_case(case):
    idx = ORDER.index(case["slug"])
    prev_slug = ORDER[idx - 1] if idx > 0 else None
    next_slug = ORDER[idx + 1] if idx < len(ORDER) - 1 else None
    by_slug = {c["slug"]: c for c in CASES}

    sections = []
    for heading, blocks in case["body"]:
        sections.append("      <h2>%s</h2>\n%s" % (
            heading, "\n".join("      " + b for b in blocks)))

    eng_dd = "".join(
        '<span class="tag" title="%s">%s</span>' % (ENGAGEMENTS[e], e) for e in case["eng"]
    ) + '<div class="eng-names">%s</div>' % (
        ", ".join(ENGAGEMENTS[e] for e in case["eng"])
    )

    nav = []
    if prev_slug:
        nav.append('        <a class="prev" href="/work/%s/"><span class="k">&larr; Previous</span>'
                   '<span class="t">%s</span></a>' % (prev_slug, by_slug[prev_slug]["title"]))
    if next_slug:
        nav.append('        <a class="next" href="/work/%s/"><span class="k">Next &rarr;</span>'
                   '<span class="t">%s</span></a>' % (next_slug, by_slug[next_slug]["title"]))

    html = """---
layout: default
nav: work
title: "%(title)s"
description: "%(blurb)s"
---

<article>

  <div class="shell">
    <header class="page-head">
      <p class="kicker">
        <a href="/work/" style="color:var(--accent-text)">Work</a>
        <span class="sep">/</span> %(kicker)s
        <span class="sep">/</span> %(year)s
      </p>
      <h1>%(title)s</h1>
      <p class="lede">%(blurb)s</p>

      <dl class="meta-grid">
        <div><dt>Role</dt><dd>%(role)s</dd></div>
        <div><dt>Context</dt><dd>%(context)s</dd></div>
        <div><dt>Engagement types</dt><dd>%(eng_dd)s</dd></div>
        <div><dt>Date</dt><dd>%(date)s</dd></div>
      </dl>
    </header>

    <div class="case-body">
%(sections)s

      <p class="note">%(sanitized)s</p>
    </div>

    <nav class="case-nav">
%(nav)s
    </nav>
  </div>

</article>
""" % dict(
        title=case["title"],
        blurb=case["blurb"],
        kicker=case["kicker"],
        year=case["year"],
        role=case["role"],
        context=case["context"],
        eng_dd=eng_dd,
        date=case["date"],
        sections="\n\n".join(sections),
        sanitized=case["sanitized"],
        nav="\n".join(nav),
    )

    d = os.path.join(ROOT, "work", case["slug"])
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)


def write_index():
    items = []
    for slug in ORDER:
        c = [x for x in CASES if x["slug"] == slug][0]
        items.append("""      <a class="item" href="/work/%(slug)s/" data-eng="%(engattr)s">
        <div>
          <div class="tags">%(tags)s</div>
          <h3>%(title)s</h3>
        </div>
        <div>
          <p>%(blurb)s</p>
          <span class="more">Read the case study <span class="arrow" aria-hidden="true">&rarr;</span></span>
        </div>
      </a>""" % dict(
            slug=c["slug"],
            engattr=" ".join(c["eng"]),
            tags=tags_html(c["eng"], c["year"]),
            title=c["title"],
            blurb=c["blurb"],
        ))

    buttons = ['        <button type="button" data-f="all" aria-pressed="true">All</button>']
    for k in "ABCDE":
        buttons.append('        <button type="button" data-f="%s" aria-pressed="false">%s &middot; %s</button>'
                       % (k, k, ENGAGEMENTS[k]))

    html = """---
layout: default
nav: work
title: "Work"
description: "Nine case studies: patent development, enterprise design-thinking programs, mixed-method UX research, product and UI design at scale, and founder-side product and investor work."
---

<div class="shell">

  <header class="page-head">
    <p class="kicker">Selected proof <span class="sep">/</span> 9 case studies <span class="sep">/</span> 2017 to 2026</p>
    <h1>What the work actually looked like</h1>
    <p class="lede">
      Every one of these is a method-only cut. Client and employer material is sanitized, named
      clients stay unnamed, and nothing confidential is reproduced. What is left is the part that
      transfers: how the problem was framed, what method was run, and what changed as a result.
    </p>
  </header>

  <div class="filters">
    <span class="flabel">Filter</span>
%(buttons)s
    <span class="fcount" id="fcount">9 shown</span>
  </div>

  <div class="work-list" id="worklist">
%(items)s
  </div>

  <section class="section" style="border-top:0">
    <div class="sec-head">
      <h2 class="label">Not published here</h2>
    </div>
    <div class="prose">
      <p>
        Some work is real but not public. Interface visuals from the enterprise programs are held
        pending permission clearance. A co-owned assessment venture, a research tooling build for a
        collaborator, and an autonomous trading agent are all live but not cleared for a public page.
        Happy to walk through any of it directly.
      </p>
      <p><a href="/#contact">Get in touch</a></p>
    </div>
  </section>

</div>

<script>
(function () {
  var list = document.getElementById('worklist');
  if (!list) return;
  var items = list.querySelectorAll('.item');
  var buttons = document.querySelectorAll('.filters button');
  var count = document.getElementById('fcount');

  function apply(f) {
    var n = 0;
    Array.prototype.forEach.call(items, function (el) {
      var show = f === 'all' || el.dataset.eng.split(' ').indexOf(f) > -1;
      el.hidden = !show;
      if (show) n++;
    });
    count.textContent = n + (n === 1 ? ' shown' : ' shown');
    Array.prototype.forEach.call(buttons, function (b) {
      b.setAttribute('aria-pressed', b.dataset.f === f ? 'true' : 'false');
    });
  }

  Array.prototype.forEach.call(buttons, function (b) {
    b.addEventListener('click', function () { apply(b.dataset.f); });
  });
})();
</script>
""" % dict(buttons="\n".join(buttons), items="\n\n".join(items))

    d = os.path.join(ROOT, "work")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    for c in CASES:
        write_case(c)
    write_index()
    print("wrote %d case studies + index" % len(CASES))
    print("order:", ", ".join(ORDER))
