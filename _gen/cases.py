#!/usr/bin/env python3
"""
Generate the /work/ index and the nine case-study pages as plain Jekyll pages
(front matter + default layout, no collections). Source of truth for the copy
is Career Management/Portfolio/Portfolio Resources/*.md, sanitized per the
2026-08-13 clearance: text only, all confidential-stamped images removed.

Since 2026-11-14 each case also carries a drawn figure of its method (see
Figures below) and is written in a leader's voice: "I" for the decisions and
the direction, "we" for the work a team did. No team sizes, and no reporting
lines the career record does not support.
"""

import os
import textwrap

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# What kind of work each case study is. These replaced the A to E engagement
# types on 2026-11-12, when the site stopped offering services: the old codes
# sorted the work by what a client could buy, these sort it by what was done.
KINDS = {
    "R": "Research",
    "P": "Product design",
    "W": "Workshop",
    "S": "Strategy",
    "T": "Writing",
}
KIND_ORDER = "RPWST"

CASES = [
    {
        'slug': 'patent-development-workshop',
        'title': "Turning a founder's invention into a patent pipeline",
        'kicker': 'Case study / Workshop',
        'year': '2025',
        'sort': '2025-06',
        'blurb': ('A one-day workshop I designed and led for an early-stage hardware '
                  'startup. Product dissection, use-journey mapping and my 10x ideation '
                  'method, scored down to a shortlist for patent counsel.'),
        'role': ('Designed the workshop and led the day. I set the agenda, ran the '
                 'strategy and ideation segments, and led the colleagues who '
                 'co-facilitated the other segments.'),
        'context': ('An early-stage hardware startup in the balance and movement-training '
                    'space. Client unnamed.'),
        'kinds': ['W', 'S'],
        'date': 'June 2025',
        'sanitized': ("Method-only. Client unnamed. The client's specific inventions, "
                      'scoring frameworks, and filings are withheld. The facilitation '
                      'method described is my own.'),
        'figure': [{'type': 'steps',
                    'label': 'One day, five segments, one result',
                    'items': [['Why patents', 'What the portfolio is for'],
                              ['Product dissection', 'Features, mechanisms, materials'],
                              ['Use-journey mapping', 'Use cases across markets'],
                              ['10x ideas', 'Three prompt categories'],
                              ['Sort and score', 'Patent test, then a vote']],
                    'out': ['Shortlist for counsel', 'With a filing direction']}],
        'figcap': ("The sequence of the day. The client's inventions and scores are not "
                   'shown.'),
        'body': [
            ('The problem', [
                ('<p>A founder with deep domain expertise and a shippable product had real'
                 ' invention in hand but no structured way to convert it into a defensible'
                 ' patent portfolio. The goal was to surface novel, non-obvious, '
                 'patentable concepts, prioritize them, and give patent counsel clear '
                 'direction.</p>'),
            ]),
            ('The approach', [
                ('<p>I designed a single day that moved from strategy to a prioritized '
                 'shortlist ready for counsel.</p>'),
                ('<ul><li><strong>Why patents.</strong> Facilitated discussion to pin down'
                 ' what the portfolio was actually for: licensing, defensibility, '
                 'visibility, and how aggressively to file.</li><li><strong>Product '
                 'dissection.</strong> Deconstructed the existing product into features, '
                 'mechanisms, and materials, the raw surface area where claims '
                 'live.</li><li><strong>Customer-use journey mapping.</strong> Mapped '
                 'diverse use cases across markets to expose where new, ownable utility '
                 'could emerge.</li><li><strong>10x ideas.</strong> My own facilitation '
                 'method: push participants to imagine the product ten times bigger, not '
                 'ten percent better, across three prompt categories (extreme use cases, '
                 'exponential technology jumps, unexpected user mashups), favoring '
                 'quantity and non-obviousness over feasibility.</li><li><strong>Sort, '
                 'score, prioritize.</strong> Affinity-grouped the ideas, filtered each '
                 'against a patent test (novel, useful, non-obvious, describable, '
                 'strategically valuable), then dot-voted to a shortlist.</li></ul>'),
            ]),
            ('The outcome', [
                ('<p>A prioritized shortlist of patentable concepts with a clear filing '
                 'direction, including provisional strategy, that fed directly to patent '
                 'counsel. Ad-hoc filing replaced with a deliberate, founder-aligned '
                 'portfolio plan.</p>'),
            ]),
            ('How I led it', [
                ('<ul><li>I set the agenda and the method, and led a group of '
                 'co-facilitators through the day.</li><li>I held every idea to what the '
                 'founder wanted the portfolio to do: licensing, defensibility and '
                 'visibility.</li><li>I closed the day with a decision: a scored shortlist'
                 ' and a filing direction that went to patent counsel.</li><li>The method '
                 'draws on my own record as a named inventor on 358 granted U.S. '
                 'patents.</li></ul>'),
            ]),
            ('The method', [
                ('<p>The <strong>10x Ideas facilitation guide</strong> (three prompt '
                 'categories, timed divergent rounds, affinity sorting, patent-filter '
                 'voting) is my own method, which is why it can be described here. The '
                 "client's session content is theirs and is not reproduced.</p>"),
            ]),
        ],
    },
    {
        'slug': 'att-design-thinking-workshop',
        'title': 'Thirty ideas to one product vision, in a day',
        'kicker': 'Case study / Enterprise program',
        'year': '2019',
        'sort': '2019-04',
        'blurb': ('A design-thinking program I conceived, funded and led inside a Fortune '
                  '10 Chief Data Office. Ten participants and thirty ideas became one '
                  'prioritized vision for a developer hub.'),
        'role': ('Sponsor and lead. I conceived the program within the Chief Data Office '
                 '(AI User Experience), funded it, set the design of the session, and '
                 'engaged an external firm to facilitate it to that design.'),
        'context': 'Chief Data Office of a Fortune 10 telecom.',
        'kinds': ['W', 'S'],
        'date': '2019',
        'sanitized': ('Method-only. Proprietary tool names, participant names, and '
                      'specific persona detail removed. No confidential employer material '
                      'reproduced.'),
        'figure': [{'type': 'funnel',
                    'items': [['10', 'participants'],
                              ['30', 'raw ideas'],
                              ['1', 'prioritized product vision']]},
                   {'type': 'steps',
                    'label': 'The session, in order',
                    'items': [['Persona grounding', None],
                              ['As-is scenario mapping', None],
                              ['Big-idea generation', None],
                              ['Prioritization', 'Impact against feasibility']],
                    'out': ['Prototype deep dive', 'The winning direction, made tangible']}],
        'figcap': ('The counts and the sequence of the session. Persona detail and tool '
                   'names are not shown.'),
        'body': [
            ('The problem', [
                ('<p>Developers inside a large enterprise were losing time to tool sprawl:'
                 ' five to six tools in a single development workflow, redundant systems '
                 'with overlapping features, weak ways to find and reuse existing work, '
                 'and almost no social or recognition layer connecting people doing '
                 'similar things.</p>'),
                ('<p>The question driving the work: how do you streamline the way '
                 'developers access resources and innovate, in a way that fosters '
                 'collaboration and reuse?</p>'),
            ]),
            ('The approach', [
                ('<p>A structured design-thinking workshop built on prior-state research: '
                 'an earlier discovery workshop plus developer interviews. The session '
                 'moved through a deliberate sequence.</p>'),
                ('<ul><li><strong>Persona grounding</strong>, so every later decision '
                 'traced back to a real user.</li>'
                 '<li><strong>As-is scenario mapping</strong> to surface '
                 'where the current experience broke down.</li><li><strong>Big-idea '
                 'generation</strong>, producing roughly thirty candidate '
                 'concepts.</li><li><strong>Prioritization</strong> on an '
                 'impact-versus-feasibility matrix, separating no-brainers from big bets '
                 'and save-for-laters.</li><li><strong>Prototype deep dive</strong> to '
                 'make the winning direction tangible.</li></ul>'),
            ]),
            ('The outcome', [
                ('<p>Ten participants and thirty raw ideas converged to a single '
                 'prioritized product vision: a developer hub combining a community layer,'
                 ' recommendation of existing components and data, contribution '
                 'recognition, and individualized profiles.</p>'),
                ('<p>The prioritization matrix gave leadership a defensible rationale for '
                 'what to build first versus defer, and the session closed with a concrete'
                 ' prototype and a next-step timeline.</p>'),
            ]),
            ('How I led it', [
                ('<ul><li>I made the case for the program, funded it, and owned it from '
                 'the discovery research through the final session.</li><li>I set the '
                 'design of the session and engaged an external firm to facilitate '
                 'it.</li><li>I gave leadership a prioritization matrix that showed what '
                 'to build first, what to defer, and why.</li></ul>'),
            ]),
        ],
    },
    {
        'slug': 'tessa-investor-narrative',
        'title': 'Making a new category legible to investors',
        'kicker': 'Case study / Founder work',
        'year': '2026',
        'sort': '2026-01',
        'blurb': ('As CEO I owned the story the company told investors. One protagonist, '
                  'then the market, then the wedge, with every claim sourced or labeled as'
                  ' an assumption.'),
        'role': ('Founder and CEO. I set the narrative, wrote and designed the deck, and '
                 'revised it against investor feedback.'),
        'context': ('Pre-seed ambient-AI consumer hardware and software startup. My own '
                    'company.'),
        'kinds': ['S', 'T'],
        'date': '2025 to 2026, iterated across versions',
        'sanitized': ('Method-only. Traction, financials, raise terms, and team specifics '
                      'removed. Focus is the narrative architecture and the craft.'),
        'figure': [{'type': 'steps',
                    'label': 'The arc of the deck, one job per slide',
                    'items': [['Problem', 'One named protagonist'],
                              ['Scale and why now', 'The story becomes a market'],
                              ['Solution', 'Quantified outcomes'],
                              ['Proof', 'Traction, model, go-to-market'],
                              ['Competition', 'A positioning table']],
                    'out': ['The ask', 'Team, roadmap, next milestone']}],
        'figcap': ('The order of the narrative. Traction, financials and raise terms are '
                   'not shown.'),
        'body': [
            ('The problem', [
                ('<p>A novel product in an unfamiliar category had to be made instantly '
                 'legible to investors: what it is, why now, who buys it, and why it wins.'
                 ' Roughly fifteen slides, without drowning the story in features.</p>'),
            ]),
            ('The approach', [
                '<p>I sequenced the deck so that each slide did one job.</p>',
                ('<ul><li><strong>Problem</strong> told through a single named '
                 'protagonist, so the pain lands before it is sized.</li><li><strong>Scale'
                 ' and why-now</strong> to turn the personal story into a '
                 'market.</li><li><strong>Solution</strong> framed as quantified outcomes:'
                 ' what changes for the user.</li><li><strong>Traction, how it works, '
                 'market, model, go-to-market</strong> in an order that answers the next '
                 'question an investor would ask, in the order they ask '
                 'it.</li><li><strong>Competition</strong> as a positioning table that '
                 'makes the wedge clear at a glance.</li><li><strong>Team, roadmap, and '
                 'the ask</strong> to close on credibility and a concrete next '
                 'milestone.</li></ul>'),
                ('<p>Every claim was tied to a cited source or labeled as an assumption, '
                 'so the deck held up under diligence.</p>'),
            ]),
            ('The outcome', [
                ('<p>A tight, diligence-ready investor narrative that distills a complex '
                 'ambient-AI product into a legible, sequenced story with a clear wedge '
                 'and a concrete milestone. Iterated across multiple versions against '
                 'investor feedback.</p>'),
            ]),
            ('How I led it', [
                ('<ul><li>I decided what the company would claim, and what it would label '
                 'as an assumption.</li><li>I ordered the deck around the questions '
                 'investors ask, in the order they ask them.</li><li>I revised the '
                 'narrative across versions as investor feedback came in.</li></ul>'),
            ]),
        ],
    },
    {
        'slug': 'tessa-competitive-analysis',
        'title': 'Keeping a competitive picture current',
        'kicker': 'Case study / Founder work',
        'year': '2026',
        'sort': '2026-02',
        'blurb': ('A competitive-intelligence program I directed as CEO for an emerging '
                  'consumer-AI category: comparable deep dives, a positioning map, a '
                  'dashboard the team used, and a weekly scan to keep it current.'),
        'role': ('Founder and CEO. I directed the program, chose the competitors and the '
                 'frame, and used the result to set where the company would compete.'),
        'context': 'Emerging consumer-AI category. My own company.',
        'kinds': ['R', 'S'],
        'date': '2026',
        'sanitized': ('Method-only. Competitor names, strategic conclusions, threat '
                      'assessments, and partner targets removed. Focus is the analysis '
                      'method.'),
        'figure': [{'type': 'grid',
                    'rows': ['Direct analog', 'Best-funded peer', 'Adjacent category', 'Wildcard'],
                    'cols': ['Buyer', 'Wedge', 'Funding', 'Technology', 'Defensibility'],
                    'label': 'Every competitor, read on the same five questions'}],
        'figcap': ('The frame of the analysis: four kinds of competitor, five questions '
                   'each. Competitor names and conclusions are not shown.'),
        'body': [
            ('The problem', [
                ('<p>A fast-moving category with well-funded entrants and no settled '
                 'positioning. The company needed a rigorous, independently sourced read '
                 'of the landscape, and a way to keep it current, to decide where to '
                 'differentiate.</p>'),
            ]),
            ('The approach', [
                '<p>I set this up as a standing program with a weekly cadence.</p>',
                ('<ul><li><strong>Shortlist discipline.</strong> A defined set of '
                 'competitors, each chosen to stress-test the positioning thesis from a '
                 'different angle: direct analog, best-funded peer, adjacent category, '
                 'wildcard.</li><li><strong>Structured deep dives.</strong> Each '
                 'competitor analyzed on a consistent frame (buyer, wedge, funding, '
                 'technology approach, defensibility) so they could be '
                 'compared.</li><li><strong>Positioning map.</strong> Defined the axes '
                 'that actually separated the field and placed every player on them, '
                 'exposing the unoccupied position.</li><li><strong>Interactive '
                 'dashboard</strong> so the team could explore the analysis and reuse '
                 'it.</li><li><strong>Ongoing monitoring.</strong> A weekly news-scan '
                 'cadence so the picture stayed live as competitors raised, launched, and '
                 'pivoted.</li></ul>'),
            ]),
            ('The outcome', [
                ('<p>A living competitive picture that turned a noisy field into a clear, '
                 'defensible wedge and an ongoing intelligence cadence, used to align the '
                 'team and prioritize where to compete.</p>'),
            ]),
            ('How I led it', [
                ('<ul><li>I chose the shortlist so that each competitor tested the '
                 'positioning thesis from a different angle.</li><li>I set one frame for '
                 'every deep dive, so the team compared like with like.</li><li>I used the'
                 ' map to align the team on where to compete.</li></ul>'),
            ]),
        ],
    },
    {
        'slug': 'tessa-product-design-decision',
        'title': 'Designing for engagement without losing safety positioning',
        'kicker': 'Case study / Founder work',
        'year': '2026',
        'sort': '2026-03',
        'blurb': ('A shipped app built around urgent alerts showed almost nothing on a '
                  "normal day. I led the analysis, framed three options for the company's "
                  'decision-makers, and recommended one.'),
        'role': ('Founder and CEO. I led the product and UX analysis, framed the decision,'
                 ' and made the recommendation.'),
        'context': 'Consumer ambient-AI app. My own company.',
        'kinds': ['P', 'S'],
        'date': '2026',
        'sanitized': ('Method-only. Internal strategy, advisor dynamics, financials, and '
                      'unreleased specifics removed. Focus is the product-design '
                      'reasoning.'),
        'figure': [{'type': 'steps',
                    'label': 'Three options for a quiet day. Alerts stay the lead in each one.',
                    'items': [['Empty baseline', 'Nothing shows on a quiet day'],
                              ['Status rollup', 'A low-cost proof of life']],
                    'out': ['Reassurance layer',
                            'Recommended: routine signals the system already detects']}],
        'figcap': ('The three options, from least to most shown on a quiet day. Unreleased'
                   ' specifics are not shown.'),
        'body': [
            ('The problem', [
                ('<p>A shipped app was built around urgent alerts, so on a normal day it '
                 'showed almost nothing. That is correct for a pure safety net and wrong '
                 'for building a habit. When nothing fires there is nothing to open, no '
                 'habit forms, and the product feels dead during the long stretches when '
                 'nothing is wrong.</p>'),
                ('<p>The documented engagement targets (regular weekly opens, opens '
                 'without a preceding notification) could not be met by an alerts-only '
                 'screen.</p>'),
            ]),
            ('The approach', [
                ('<p>I framed the design decision as three options, each with its '
                 'evidence.</p>'),
                ('<ul><li><strong>Named the real question.</strong> Should the app deliver'
                 ' ambient value between alerts, or stay an intentionally quiet safety '
                 'net? The UI choice and the strategy question were the same '
                 'question.</li><li><strong>Designed three quiet-day options</strong> '
                 'along a clear spectrum: an empty baseline, a low-cost proof-of-life '
                 'status rollup, and a reassurance layer surfacing routine signals the '
                 'system already detects. Alerts stayed the hero in every '
                 'option.</li><li><strong>Grounded each in evidence:</strong> documented '
                 "caregiver needs and the team's own behavioral "
                 'targets.</li><li><strong>Made the case with a customer-journey '
                 'narrative:</strong> the same quiet week experienced two ways, showing '
                 'how an empty app loses a friendly user while a reassurance layer earns a'
                 ' daily habit.</li><li><strong>Kept it pragmatic.</strong> The '
                 'recommended option reused signals the backend already produced: light UI'
                 ' work, no new ML.</li></ul>'),
            ]),
            ('The outcome', [
                ('<p>A clear, evidence-backed recommendation with a low-risk build path '
                 'that resolved an engagement-versus-safety tension, framed so '
                 'decision-makers could choose on merits.</p>'),
            ]),
            ('How I led it', [
                ('<ul><li>I named the strategy question behind the screen design, so the '
                 'team settled both together.</li><li>I held every option to the same '
                 "evidence: documented caregiver needs and the team's behavioral "
                 'targets.</li><li>I recommended the option with the lowest build risk, '
                 'which reused signals the backend already produced.</li></ul>'),
            ]),
        ],
    },
    {
        'slug': 'att-persona-research',
        'title': 'North Star: customer-centric design for enterprise analytics',
        'kicker': 'Case study / Enterprise research program',
        'year': '2018',
        'sort': '2018-11',
        'blurb': ('A mixed-method research program I led inside a Fortune 10 Chief Data '
                  'Office. Contextual inquiry, cognitive task analysis and a validating '
                  'survey produced personas that leadership used to set priorities.'),
        'role': ('Program lead within the Chief Data Office (AI User Experience). I set '
                 'the research plan and methods, directed the work, and turned the '
                 'findings into product direction for leadership.'),
        'context': ('Chief Data Office of a Fortune 10 telecom, designing service and '
                    'self-service analytics systems for internal data analysts.'),
        'kinds': ['R'],
        'date': '2018 to 2019',
        'sanitized': ('Method-only. Proprietary tool names, real persona content, and '
                      'internal data removed. No confidential employer material '
                      'reproduced. Consolidates the North Star customer-centric design '
                      'program and its persona-research workstream, which were one body of'
                      ' work.'),
        'figure': [{'type': 'converge',
                    'in_label': 'Six methods',
                    'ins': ['Contextual inquiry',
                            'Cognitive task analysis',
                            'Empathy mapping',
                            'Training-needs and tool-gap analysis',
                            'UI analysis',
                            'Survey research'],
                    'out_label': 'One design approach',
                    'outs': ['Personas', 'Objectives', 'A vision-casting frame']}],
        'figcap': ('The methods and what they produced. Persona content and internal data '
                   'are not shown.'),
        'body': [
            ('The problem', [
                ('<p>The organization wanted data-powered decision-making across a '
                 '200,000-person company, but the analytics tools its own data analysts '
                 'used carried friction that slowed adoption. Leadership needed product '
                 'decisions grounded in how analysts actually worked, to raise '
                 'effectiveness without taxing the efficiency of skilled users.</p>'),
            ]),
            ('The approach', [
                ('<p>I wrote a formal User Experience Research Plan that applied '
                 'human-factors engineering to persona development. We then used those '
                 'personas to drive design.</p>'),
                ('<ul><li><strong>Contextual inquiry</strong>, observing analysts doing '
                 'real work in their existing tool suite.</li><li><strong>Cognitive task '
                 'analysis</strong> to locate pain points and the drivers of '
                 'productivity.</li><li><strong>Empathy mapping</strong> (think, feel, '
                 'say, do) to build a shared, human picture of the '
                 'user.</li><li><strong>Training-needs and tool-gap analysis</strong> to '
                 'separate capability gaps from design gaps.</li><li><strong>UI '
                 'analysis</strong> to surface usability issues in current and proposed '
                 'systems.</li><li><strong>Survey research</strong> to quantify and '
                 'validate the qualitative signal at scale.</li></ul>'),
                ('<p>Findings rolled up into a customer-centric design approach: personas,'
                 ' objectives, and a vision-casting frame that gave the organization a '
                 'common reference for prioritization.</p>'),
            ]),
            ('The outcome', [
                ('<p>A validated persona set and a customer-centric design framework that '
                 'grounded analytics-product decisions in real analyst behavior. '
                 'Leadership got a defensible basis for prioritizing friction reduction '
                 'where it mattered most, in service of enabling data-driven decisions '
                 'company-wide.</p>'),
            ]),
            ('How I led it', [
                ('<ul><li>I set the research plan and chose the six methods.</li><li>I '
                 'paired the qualitative work with a survey, so the personas were '
                 'validated at scale.</li><li>I tied the findings to business objectives '
                 '(adoption and effectiveness) and took them to leadership as a basis for '
                 'priorities.</li></ul>'),
            ]),
        ],
    },
    {
        'slug': 'att-focus-groups',
        'title': 'Validating a discovery concept before anyone built it',
        'kicker': 'Case study / Enterprise research',
        'year': '2019',
        'sort': '2019-09',
        'blurb': ('Before engineering built a new discovery concept, I had it tested with '
                  'analysts. Task-based focus groups against an interactive prototype gave'
                  ' the team comparable feedback on every flow.'),
        'role': ('Research lead within the Chief Data Office (AI User Experience). I '
                 'directed the study and set its protocol, task flows and prototype-driven'
                 ' test plan.'),
        'context': ('Chief Data Office of a Fortune 10 telecom, validating a data and '
                    'analytics discovery concept before build.'),
        'kinds': ['R'],
        'date': '2019',
        'sanitized': ('Method-only. Proprietary tool names, real participant names and '
                      'IDs, and internal data removed. No confidential employer material '
                      'reproduced.'),
        'figure': [{'type': 'paths',
                    'label': 'Four fixed flows through the prototype',
                    'rows': [['Orient', ['Home page']],
                             ['Find a person', ['Home page', 'Expert card', 'Detail view']],
                             ['Find data', ['Home page', 'Data card', 'Detail view']],
                             ['Search',
                              ['Home page', 'Filters and type-ahead', 'Results', 'Detail page']]]}],
        'figcap': ('The four task flows every group walked. Screens, tool names and '
                   'participants are not shown.'),
        'body': [
            ('The problem', [
                ('<p>A new analytics discovery concept needed validation with real users '
                 'before engineering invested in building it. The team needed evidence '
                 'that the core flows, finding the right people, finding the right data, '
                 'and searching effectively, matched how analysts actually think and '
                 'work.</p>'),
            ]),
            ('The approach', [
                ('<p>We ran structured, task-based focus groups against an interactive '
                 'prototype. The protocol walked participants through a defined set of '
                 'flows.</p>'),
                ('<ul><li>Reviewing and orienting on the home page.</li><li>Selecting a '
                 'subject-matter-expert card and reaching the detail '
                 'view.</li><li>Selecting a data card and reaching the detail '
                 'view.</li><li>Searching from the home page, including filters and '
                 'type-ahead suggestion, through to results and a detail page.</li></ul>'),
                ('<p>Each flow had a fixed sequence of prototype screens, so feedback was '
                 'comparable across participants and tied to a concrete interaction.</p>'),
            ]),
            ('The outcome', [
                ('<p>Comparable, flow-level feedback on a concept before build, letting '
                 'the team refine the prototype and de-risk the engineering investment. '
                 'The protocol turned subjective reactions into structured signal mapped '
                 'to specific screens and tasks.</p>'),
            ]),
            ('How I led it', [
                ('<ul><li>I put the concept in front of analysts before engineering '
                 'committed to building it.</li><li>I fixed the flows and the screen '
                 'sequence, so feedback from every group could be compared.</li><li>I gave'
                 ' the team findings mapped to specific screens and tasks, which they used'
                 ' to refine the prototype.</li></ul>'),
            ]),
        ],
    },
    {
        'slug': 'att-data-product-catalog',
        'title': 'Making enterprise data findable, traceable, and reusable',
        'kicker': 'Case study / Product and UI design',
        'year': '2021',
        'sort': '2021-06',
        'blurb': ('A data product catalog for a Fortune 10 Chief Data Office. I led a team'
                  ' of engineers and leaders to one design that put search, lineage and '
                  'data flows in a single interface, for web and mobile.'),
        'role': ('Product and UX design lead within the Chief Data Office (AI User '
                 'Experience). I brought a multidisciplinary team of engineers and leaders'
                 ' to a shared design, using human-factors methods to get there.'),
        'context': ('Chief Data Office of a Fortune 10 telecom, building self-service data'
                    ' findability for internal analysts and data scientists.'),
        'kinds': ['P'],
        'date': '2021',
        'sanitized': ('Method-only. No confidential employer material reproduced. '
                      'Interface visuals are withheld pending permission clearance.'),
        'figure': [{'type': 'converge',
                    'in_label': 'Before: three places to look',
                    'ins': ['Metadata in one place', 'The data in another', 'Lineage somewhere else'],
                    'out_label': 'After: one catalog',
                    'outs': ['Search with type-ahead and filters',
                             'Visible lineage and data flows',
                             'Detail views with access paths']}],
        'figcap': ('What the catalog brought together. Interface visuals are withheld '
                   'pending permission.'),
        'body': [
            ('The problem', [
                ('<p>In a large enterprise, analysts and data scientists struggled to '
                 'find, understand, and reuse data products across business units. '
                 'Metadata lived in one place, the data in another, lineage somewhere '
                 'else, so people fell back on emailing data owners or asking their team. '
                 'The result was duplicated effort and slow time-to-insight.</p>'),
            ]),
            ('The approach', [
                ('<p>I led a product and UX design effort to make data discoverable and '
                 'reusable through a single catalog, designed for both web and mobile.</p>'),
                ('<ul><li>A browseable, searchable catalog of data products with '
                 'type-ahead and filtering.</li><li>Visible product lineage and data '
                 'flows, so users could trust and trace what they found.</li><li>Detail '
                 'views connecting metadata to access paths, collapsing the hop between '
                 'learning about a data product and using it.</li><li>Designed across web '
                 'and mobile so the experience held up wherever analysts worked.</li></ul>'),
                ('<p>The work was grounded in the same human-factors research that '
                 'produced the persona and customer-centric design program. Design '
                 'decisions traced back to how analysts actually search and decide.</p>'),
            ]),
            ('The outcome', [
                ('<p>A concrete, designed catalog concept that turned scattered '
                 'data-discovery behavior into a single coherent interface, giving '
                 'engineering a clear target and leadership a tangible vision for '
                 'self-service data findability.</p>'),
            ]),
            ('How I led it', [
                ('<ul><li>I brought engineers and leaders who each held part of the '
                 'problem to one shared design.</li><li>I grounded the design in the '
                 'research from the persona program: how analysts search and '
                 'decide.</li><li>I gave engineering a clear target and leadership a '
                 'concrete picture of self-service data findability.</li></ul>'),
            ]),
        ],
    },
    {
        'slug': 'att-white-papers',
        'title': 'Giving a 200,000-person company shared language for AI',
        'kicker': 'Case study / Thought leadership',
        'year': '2017',
        'sort': '2017-01',
        'blurb': ('I was lead author of an enterprise automation white paper and the Data '
                  'Powered series. I convened engineers and senior leaders, brought their '
                  'views into one account, and wrote it.'),
        'role': ('Lead author. I convened contributors from engineering and senior '
                 'leadership, ran the multi-author review, and wrote the synthesis.'),
        'context': 'Chief Data Office of a Fortune 10 telecom.',
        'kinds': ['T', 'S'],
        'date': '2017 and following',
        'sanitized': ('Describes authorship and method. Proprietary internal detail not '
                      'reproduced. The papers themselves are not published here.'),
        'figure': [{'type': 'converge',
                    'in_label': 'Many partial views',
                    'ins': ['Engineers', 'Senior leaders', 'Contributors across teams'],
                    'out_label': 'One shared reference',
                    'outs': ['Enterprise automation white paper',
                             'The Data Powered series',
                             'A five-milestone maturity model']}],
        'figcap': ('Who contributed and what the work produced. The papers themselves are '
                   'not published here.'),
        'body': [
            ('The problem', [
                ('<p>A large enterprise pushing into AI, automation, and data-driven '
                 'decision-making lacked shared language and frameworks for it. Many smart'
                 ' people held pieces of the picture across different teams, but there was'
                 ' no authoritative, common reference to align strategy and '
                 'investment.</p>'),
            ]),
            ('The approach', [
                ('<p>My method was the same across the papers, including an enterprise '
                 'automation white paper and the Data Powered series: convene the right '
                 'experts, align them, and write the synthesis.</p>'),
                ('<ul><li>Bring engineers and leaders together and surface what each '
                 'actually knew.</li><li>Use human-factors and facilitation techniques to '
                 'converge many viewpoints into one coherent narrative.</li><li>Author and'
                 ' structure the synthesis, including durable frameworks such as a '
                 'five-milestone automation maturity model.</li></ul>'),
                ('<p>The papers carried many authors, and the company ordered bylines by '
                 'seniority. I wrote the papers and ran the review across the authors.</p>'),
            ]),
            ('The outcome', [
                ('<p>Published internal thought leadership that gave the organization '
                 'shared language and frameworks for AI and automation, used to align '
                 'strategy and orient teams. The papers became a common reference point '
                 'across teams.</p>'),
            ]),
            ('How I led it', [
                ('<ul><li>I convened engineers and senior leaders and drew out what each '
                 'of them knew.</li><li>I ran the review across the authors and resolved '
                 'their differences into one narrative.</li><li>I wrote durable frameworks'
                 ' into the papers, including a five-milestone automation maturity '
                 'model.</li></ul>'),
            ]),
        ],
    },
]

ORDER = [c["slug"] for c in sorted(CASES, key=lambda c: c["sort"], reverse=True)]


def tags_html(kinds, year=None):
    out = "".join('<span class="tag">%s</span>' % KINDS[k] for k in kinds)
    if year:
        out += '<span class="tag tag-quiet">%s</span>' % year
    return out


# ---------------------------------------------------------------------------
# Figures. Each case carries a "figure" list: one or more parts drawn in HTML
# and CSS (section 29 of main.css). They diagram the method only. Nothing in a
# figure may state a fact the case text does not, and none reproduces employer
# or client material.

def _step(n, item, out=False):
    title, sub_text = item
    sub_html = '<span class="cs-sub">%s</span>' % sub_text if sub_text else ""
    cls = ' class="is-out"' if out else ""
    return ('<li%s><span class="cs-n">%s</span><span class="cs-t">%s</span>%s</li>'
            % (cls, n, title, sub_html))


def fig_steps(part):
    items = [_step(i + 1, it) for i, it in enumerate(part["items"])]
    if part.get("out"):
        items.append(_step(len(items) + 1, part["out"], out=True))
    label = '<p class="cs-label">%s</p>' % part["label"] if part.get("label") else ""
    return ('%s<ol class="cs-steps" style="--n:%d">%s</ol>'
            % (label, len(items), "".join(items)))


def fig_funnel(part):
    cells = []
    last = len(part["items"]) - 1
    for i, (num, label) in enumerate(part["items"]):
        cells.append('<div class="cs-stat%s"><span class="n">%s</span><span class="k">%s</span></div>'
                     % (" is-out" if i == last else "", num, label))
    return '<div class="cs-funnel" style="--n:%d">%s</div>' % (len(cells), "".join(cells))


def fig_converge(part):
    ins = "".join('<li class="chip">%s</li>' % x for x in part["ins"])
    outs = "".join('<li class="chip">%s</li>' % x for x in part["outs"])
    return ('<div class="cs-converge">'
            '<div class="cs-side"><p class="cs-label">%s</p><ul>%s</ul></div>'
            '<div class="cs-join" aria-hidden="true"></div>'
            '<div class="cs-side cs-side--out"><p class="cs-label">%s</p><ul>%s</ul></div>'
            '</div>' % (part["in_label"], ins, part["out_label"], outs))


def fig_grid(part):
    head = "".join('<th scope="col">%s</th>' % c for c in part["cols"])
    rows = []
    for r in part["rows"]:
        cells = '<td><i aria-hidden="true"></i><span class="visually-hidden">assessed</span></td>' * len(part["cols"])
        rows.append('<tr><th scope="row">%s</th>%s</tr>' % (r, cells))
    label = '<p class="cs-label">%s</p>' % part["label"] if part.get("label") else ""
    return ('%s<div class="cs-scroll"><table class="cs-grid"><thead><tr><td></td>%s</tr></thead>'
            '<tbody>%s</tbody></table></div>' % (label, head, "".join(rows)))


def fig_paths(part):
    rows = []
    for name, screens in part["rows"]:
        chips = "".join('<li class="chip">%s</li>' % x for x in screens)
        rows.append('<div class="cs-path"><span class="cs-t">%s</span><ol>%s</ol></div>' % (name, chips))
    label = '<p class="cs-label">%s</p>' % part["label"] if part.get("label") else ""
    return '%s<div class="cs-paths">%s</div>' % (label, "".join(rows))


LEFT_SECTIONS = ("The problem", "The approach")

FIGURES = {"steps": fig_steps, "funnel": fig_funnel, "converge": fig_converge,
           "grid": fig_grid, "paths": fig_paths}


def figure_html(case):
    parts = "\n".join("        " + FIGURES[p["type"]](p) for p in case["figure"])
    return ('    <figure class="cs-fig reveal">\n%s\n'
            '        <figcaption class="caption">%s</figcaption>\n    </figure>'
            % (parts, case["figcap"]))


def write_case(case):
    idx = ORDER.index(case["slug"])
    prev_slug = ORDER[idx - 1] if idx > 0 else None
    next_slug = ORDER[idx + 1] if idx < len(ORDER) - 1 else None
    by_slug = {c["slug"]: c for c in CASES}

    # The body is laid out on the page's two halves. Left: the problem and the
    # approach. Right: the outcome, then "How I led it" as a card, then any
    # further section and the clearance note. The two columns start level, and
    # on a phone they stack in reading order.
    left, right = [], []
    for heading, blocks in case["body"]:
        inner = "\n".join("          " + b for b in blocks)
        if heading == "How I led it":
            right.append('        <section class="cs-led">\n          <h2>%s</h2>\n%s\n        </section>'
                         % (heading, inner))
        else:
            block = "        <h2>%s</h2>\n%s" % (heading, inner)
            (left if heading in LEFT_SECTIONS else right).append(block)

    kinds_dd = ", ".join(KINDS[k] for k in case["kinds"])

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
    <header class="page-head cs-head">
      <div class="g2">
        <div>
          <p class="kicker">
            <a href="/work/" style="color:var(--accent-text)">Work</a>
            <span class="sep">/</span> %(kicker)s
            <span class="sep">/</span> %(year)s
          </p>
          <h1>%(title)s</h1>
          <p class="lede">%(blurb)s</p>
        </div>
        <dl class="cs-meta">
          <div class="wide"><dt>Role</dt><dd>%(role)s</dd></div>
          <div class="wide"><dt>Context</dt><dd>%(context)s</dd></div>
          <div><dt>Kind of work</dt><dd>%(kinds_dd)s</dd></div>
          <div><dt>Date</dt><dd>%(date)s</dd></div>
        </dl>
      </div>
    </header>

%(figure)s

    <div class="g2 cs-cols">
      <div class="case-body">
%(left)s
      </div>
      <div class="case-body">
%(right)s

        <p class="note">%(sanitized)s</p>
      </div>
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
        kinds_dd=kinds_dd,
        figure=figure_html(case),
        date=case["date"],
        left="\n\n".join(left),
        right="\n\n".join(right),
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
        items.append("""      <a class="item" href="/work/%(slug)s/" data-kind="%(kindattr)s">
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
            kindattr=" ".join(c["kinds"]),
            tags=tags_html(c["kinds"], c["year"]),
            title=c["title"],
            blurb=c["blurb"],
        ))

    buttons = ['        <button type="button" data-f="all" aria-pressed="true">All</button>']
    for k in KIND_ORDER:
        buttons.append('        <button type="button" data-f="%s" aria-pressed="false">%s</button>'
                       % (k, KINDS[k]))

    html = """---
layout: default
nav: work
title: "Work"
description: "Nine case studies: patent development, enterprise design-thinking programs, mixed-method UX research, product and UI design at scale, and founder-side product and investor work."
---

<div class="shell">

  <header class="page-head">
    <p class="kicker">Work <span class="sep">/</span> 9 case studies <span class="sep">/</span> 2017 to 2026</p>
    <h1>Nine case studies</h1>
    <p class="lede">
      Each one is cut down to the method. Client and employer material is removed, clients are
      unnamed, and nothing confidential is reproduced. What remains is how the problem was
      framed, what method was run, and what changed as a result.
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
        Some of the work is not public. Interface visuals from the enterprise programs are held
        pending permission, and a research tooling build for a collaborator is not cleared for
        a public page.
      </p>
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
      var show = f === 'all' || el.dataset.kind.split(' ').indexOf(f) > -1;
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
