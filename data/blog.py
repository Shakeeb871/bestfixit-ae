"""Blog content for the site — real, unique articles (no placeholders).

``POSTS`` is the single source of truth for the blog: it drives the homepage
blog section (``components/blog_section.html``), the /blog listing, the
/blog/category/<slug> category pages and each /blog/<slug> article page. Each
post has a stable ``slug`` and a ``category`` (matched to ``CATEGORIES``).
"""

from datetime import datetime

# ── Blog categories (order = display order) ────────────────────────────────
CATEGORIES = [
    {"name": "Air Conditioning", "slug": "air-conditioning"},
    {"name": "Electrical", "slug": "electrical"},
    {"name": "Plumbing", "slug": "plumbing"},
    {"name": "Home Maintenance", "slug": "home-maintenance"},
    {"name": "Renovation", "slug": "renovation"},
]
CATEGORY_BY_SLUG = {c["slug"]: c for c in CATEGORIES}
_CAT_SLUG = {c["name"]: c["slug"] for c in CATEGORIES}

POSTS = [
    {
        "slug": "how-often-service-ac-in-dubai",
        "title": "How Often Should You Service Your AC in Dubai?",
        "date": "18 March 2026",
        "category": "Air Conditioning",
        "tags": "Air Conditioning, Maintenance",
        "image": "/static/img/testimonial-ac.webp",
        "image_alt": "Best Fix technician servicing a split air-conditioning unit in Dubai",
        "excerpt": (
            "In Dubai's climate an AC works far harder than in most places. "
            "Here is how often to service it, and the warning signs that mean "
            "you should not wait for the next scheduled visit."
        ),
        "sections": [
            {"heading": "", "paras": [
                "Air conditioning in the UAE isn't a summer-only appliance — it runs for most of the year and often around the clock. That constant load means dust, reduced gas and worn parts build up faster than the once-a-year service many homeowners assume is enough.",
            ]},
            {"heading": "The short answer", "paras": [
                "For a home in Dubai we recommend a full service every three to four months, with a lighter filter clean in between. Villas with ducted systems and homes near the coast (where humidity and salt are higher) sit at the shorter end of that range.",
                "Regular servicing keeps cooling strong, lowers your DEWA bill by keeping the system efficient, and catches small faults — a weak capacitor, a slow gas leak — before they turn into a breakdown on the hottest day of the year.",
            ]},
            {"heading": "Signs you shouldn't wait", "paras": [
                "Book a visit sooner if you notice weak airflow, warm air, water dripping from the indoor unit, a musty smell when it starts, or a sudden jump in your electricity bill. Any of these usually means the system is straining and losing efficiency.",
            ]},
        ],
    },
    {
        "slug": "why-is-my-ac-not-cooling",
        "title": "Why Is My AC Not Cooling Properly?",
        "date": "12 March 2026",
        "category": "Air Conditioning",
        "tags": "Air Conditioning, Troubleshooting",
        "image": "/static/img/testimonial-ac.webp",
        "image_alt": "Air-conditioning unit being checked by a Best Fix technician",
        "excerpt": (
            "Weak or warm airflow usually isn't just 'low gas'. Here are the most "
            "common reasons an AC stops cooling in Dubai — and which ones you can "
            "check yourself before calling a technician."
        ),
        "sections": [
            {"heading": "", "paras": [
                "When an AC stops cooling, topping up refrigerant is often the first thing people ask for. But gas only runs low if there's a leak — and there are several more common culprits worth ruling out first.",
            ]},
            {"heading": "The usual causes", "paras": [
                "A clogged filter or dirty coil is the number-one reason for weak airflow — dust chokes the system and cooling drops. Beyond that, a blocked condensate drain, a failing capacitor, a tripped breaker, or a thermostat set or wired incorrectly can all stop a unit from cooling properly.",
                "A genuine gas leak is possible too, but a technician should trace and repair the leak — not simply refill it, which only hides the problem for a few weeks.",
            ]},
            {"heading": "What you can check first", "paras": [
                "Clean or replace the filter, make sure the outdoor unit is clear of dust and obstructions, and confirm the thermostat is set to cool at a sensible temperature. If cooling is still weak after that, it's time for a proper inspection.",
            ]},
        ],
    },
    {
        "slug": "signs-you-need-an-electrician",
        "title": "6 Early Warning Signs You Need an Electrician",
        "date": "2 March 2026",
        "category": "Electrical",
        "tags": "Electrical, Safety",
        "image": "/static/img/hero-team.webp",
        "image_alt": "Licensed Best Fix electrician checking a distribution board",
        "excerpt": (
            "Most electrical problems give you a warning first. Spotting these "
            "six signs early keeps a minor fix from becoming a fire risk or a "
            "full rewire."
        ),
        "sections": [
            {"heading": "", "paras": [
                "Electrical faults rarely appear out of nowhere. Catching the early signs protects your home and your family, and almost always means a cheaper repair than the one you'd face by ignoring it.",
            ]},
            {"heading": "What to look out for", "paras": [
                "Watch for breakers that trip repeatedly, lights that flicker or dim when an appliance switches on, warm or discoloured sockets, a faint burning smell, a mild tingle from a switch or metal appliance, and sockets that no longer hold a plug firmly.",
                "Any one of these means a circuit is overloaded, a connection is loose, or wiring is ageing. A tingle or burning smell is urgent — switch the circuit off at the board and call a licensed electrician before using it again.",
            ]},
            {"heading": "Why a licensed electrician matters", "paras": [
                "In the UAE electrical work should be done to DEWA standards by a qualified technician. Correct wiring, the right breaker ratings and proper earthing are what keep a home safe — and they're not something to guess at.",
            ]},
        ],
    },
    {
        "slug": "why-breakers-keep-tripping",
        "title": "Why Your Circuit Breakers Keep Tripping",
        "date": "24 February 2026",
        "category": "Electrical",
        "tags": "Electrical, Troubleshooting",
        "image": "/static/img/hero-team.webp",
        "image_alt": "Best Fix electrician inspecting a tripped distribution board",
        "excerpt": (
            "A breaker that trips is doing its job — but if it keeps happening, "
            "something needs attention. Here's what a tripping fuse board is "
            "actually telling you."
        ),
        "sections": [
            {"heading": "", "paras": [
                "A circuit breaker trips to protect you and your wiring from an unsafe current. An occasional trip is normal; a repeated one is a signal that shouldn't be reset and forgotten.",
            ]},
            {"heading": "The three common reasons", "paras": [
                "Overload — too many high-draw appliances on one circuit — is the most frequent cause, and often solved by redistributing the load. A short circuit (a live wire touching neutral or earth) trips instantly and needs tracing. A ground fault, common in wet areas like kitchens and bathrooms, trips an RCD and points to moisture or a faulty appliance.",
            ]},
            {"heading": "When to call an electrician", "paras": [
                "If a breaker won't stay on, trips the moment you plug something in, or is accompanied by a burning smell or warm board, stop using the circuit and call a licensed electrician. Repeated tripping is worth diagnosing properly rather than living with.",
            ]},
        ],
    },
    {
        "slug": "prevent-plumbing-leaks",
        "title": "Stop Small Leaks Before They Become Big Repairs",
        "date": "20 February 2026",
        "category": "Plumbing",
        "tags": "Plumbing, Maintenance",
        "image": "/static/img/testimonial-plumbing.webp",
        "image_alt": "Best Fix plumber fixing a pipe connection under a sink",
        "excerpt": (
            "A slow drip seems harmless, but in an apartment it can mean damaged "
            "cabinets, mould and a claim from the neighbour below. Here's how to "
            "catch leaks early."
        ),
        "sections": [
            {"heading": "", "paras": [
                "Plumbing leaks are one of the most common — and most expensive — problems in UAE homes, precisely because they're easy to ignore until the damage is done.",
            ]},
            {"heading": "Simple checks that save money", "paras": [
                "Every couple of months, look under sinks and behind the washing machine for damp patches or a musty smell. Check that taps close fully without dripping, and that the seal around the bath and shower isn't cracked or peeling.",
                "A quick way to spot a hidden leak: note your water meter reading, avoid using any water for an hour, then check it again. If it has moved, water is escaping somewhere.",
            ]},
            {"heading": "When to call us", "paras": [
                "Low water pressure, a running toilet, a slow drain or a stain spreading on a wall or ceiling are all worth a same-day look. Fixing a joint or seal early costs a fraction of repairing water-damaged cabinetry and plaster later.",
            ]},
        ],
    },
    {
        "slug": "blocked-drains-causes-prevention",
        "title": "Blocked Drains in Dubai: Causes and Prevention",
        "date": "10 February 2026",
        "category": "Plumbing",
        "tags": "Plumbing, Drainage",
        "image": "/static/img/testimonial-plumbing.webp",
        "image_alt": "Best Fix plumber clearing a blocked drain",
        "excerpt": (
            "A slow or blocked drain is one of the most common call-outs we get. "
            "Here's what causes them and the simple habits that keep your drains "
            "flowing."
        ),
        "sections": [
            {"heading": "", "paras": [
                "Most blockages build up slowly from everyday use, then announce themselves at the worst possible moment. Knowing what causes them makes them easy to avoid.",
            ]},
            {"heading": "What clogs a drain", "paras": [
                "In kitchens, cooking oil and food scraps are the main offenders — grease cools and hardens inside the pipe. In bathrooms, it's hair, soap scum and small objects. Hard water can also leave scale that narrows pipes over time.",
                "Pouring oil down the sink, flushing wipes or cotton pads, and skipping drain guards are the fastest ways to a blockage.",
            ]},
            {"heading": "Keeping drains clear", "paras": [
                "Use drain strainers, bin food waste and oil instead of rinsing them away, and flush drains with hot water regularly. If water is draining slowly across several fittings at once, the blockage may be in the main line — that's one to have cleared professionally before it backs up.",
            ]},
        ],
    },
    {
        "slug": "home-maintenance-checklist-uae",
        "title": "A Simple Home Maintenance Checklist for UAE Homes",
        "date": "5 February 2026",
        "category": "Home Maintenance",
        "tags": "Home Maintenance, Tips",
        "image": "/static/img/professional-maintenance-team.webp",
        "image_alt": "Best Fix maintenance team ready for a home service call in Dubai",
        "excerpt": (
            "A little upkeep through the year prevents most emergency call-outs. "
            "Use this quick checklist to keep your home running smoothly in the "
            "UAE climate."
        ),
        "sections": [
            {"heading": "", "paras": [
                "The heat, dust and humidity of the UAE are hard on a home. A short routine spread across the year keeps everything working and helps you avoid the breakdowns that always seem to happen at the worst time.",
            ]},
            {"heading": "Through the year", "paras": [
                "Clean or replace AC filters every few weeks in summer and book a full AC service before the heat peaks. Test smoke detectors and check that all sockets and switches feel firm and cool.",
                "Reseal wet areas — around baths, showers and kitchen counters — once a year, clear slow drains, and check taps and the water heater for drips. Outside, clear balcony and AC drainage points so water can't pool.",
            ]},
            {"heading": "Let one team handle it", "paras": [
                "The easiest option is a single maintenance visit that covers AC, plumbing, electrical and general repairs in one go. That's exactly what Best Fix is built for — one trusted team you can call for the whole list.",
            ]},
        ],
    },
    {
        "slug": "get-your-home-summer-ready-dubai",
        "title": "Getting Your Home Summer-Ready in Dubai",
        "date": "28 January 2026",
        "category": "Home Maintenance",
        "tags": "Home Maintenance, Seasonal",
        "image": "/static/img/professional-maintenance-team.webp",
        "image_alt": "Best Fix team preparing a Dubai home for summer",
        "excerpt": (
            "Dubai summers push a home to its limits. A little preparation before "
            "the heat arrives keeps you cool, safe and clear of the peak-season "
            "breakdown rush."
        ),
        "sections": [
            {"heading": "", "paras": [
                "By the time the heat is at its worst, every maintenance company is booked solid. Getting ahead of it in spring is the single best thing you can do for a comfortable summer.",
            ]},
            {"heading": "Before the heat peaks", "paras": [
                "Service the AC while technicians are still easy to book, and have the gas, coils and drainage checked. Test that every unit cools properly, and clear the outdoor condensers of the dust that builds up over winter.",
                "Check window and door seals so cool air isn't leaking out, and make sure the water heater and pressure are working — demand on both rises sharply in summer.",
            ]},
            {"heading": "Small jobs, big difference", "paras": [
                "Bundling these checks into one visit is cheaper and quicker than reacting to failures later. A cool, efficient home in July starts with a service in spring.",
            ]},
        ],
    },
    {
        "slug": "planning-a-villa-renovation-dubai",
        "title": "Planning a Villa Renovation in Dubai: A Practical Guide",
        "date": "15 January 2026",
        "category": "Renovation",
        "tags": "Renovation, Planning",
        "image": "/static/img/Home renovation, villa renovation, office renovation, exterior design, interior design.jpg",
        "image_alt": "Villa renovation project in Dubai by Best Fix",
        "excerpt": (
            "A villa renovation touches every trade at once. A clear plan up "
            "front is what keeps it on budget, on time and free of the surprises "
            "that derail so many projects."
        ),
        "sections": [
            {"heading": "", "paras": [
                "Renovating a villa is one of the biggest jobs a homeowner takes on. The projects that go smoothly are almost always the ones that were planned properly before any work began.",
            ]},
            {"heading": "Start with scope and survey", "paras": [
                "Decide what you actually want to change — layout, kitchens, bathrooms, finishes — then get the villa surveyed so the condition of the existing electrics, plumbing and structure is understood. A realistic plan beats a rushed quote every time.",
                "Because a renovation involves construction, MEP and finishing together, using one coordinated team avoids the gaps and delays that appear when separate contractors don't talk to each other.",
            ]},
            {"heading": "Budget, permits and timeline", "paras": [
                "Agree a clear, itemised scope and price before work starts, and factor in the approvals your community or authority requires. A well-planned villa renovation delivers a home that matches the drawings — handed over clean and on time.",
            ]},
        ],
    },
]

# Derive category slugs, ISO dates and URLs.
for _p in POSTS:
    _p["category_slug"] = _CAT_SLUG.get(_p.get("category"), "")
    _p["url"] = "/blog/" + _p["slug"] + "/"
    try:
        _p["iso_date"] = datetime.strptime(_p["date"], "%d %B %Y").strftime("%Y-%m-%d")
    except ValueError:
        _p["iso_date"] = ""

POST_BY_SLUG = {p["slug"]: p for p in POSTS}


def posts_in_category(cat_slug):
    return [p for p in POSTS if p["category_slug"] == cat_slug]


# Category list with post counts (for sidebars / filter bars).
CATEGORIES_WITH_COUNT = [
    {**c, "count": len(posts_in_category(c["slug"]))} for c in CATEGORIES
]

# Most recent posts (POSTS is already newest-first).
RECENT_POSTS = POSTS[:5]


def _card(p):
    """Homepage-card view of a post (adds the article URL)."""
    return {**p, "url": "/blog/" + p["slug"] + "/"}


# Homepage blog section: intro + one featured post + three related posts.
BLOG = {
    "label": "Our Blog",
    "title_lead": "Learn More From",
    "title_accent": "Blog",
    "intro": (
        "Practical advice on keeping your home cool, safe and well cared for "
        "in the UAE — from AC servicing to plumbing, electrical and general "
        "maintenance."
    ),
    "cta_message": "Require commercial building maintenance and/or installation services?",
    "cta_button_label": "Contact us!",
    "cta_button_url": "#bfc",
    "featured": _card(POSTS[0]),
    "related": [_card(p) for p in POSTS[1:4]],
    "foot_link_label": "Read",
    "foot_text": "all articles on our blog.",
    "foot_url": "/blog/",
}
