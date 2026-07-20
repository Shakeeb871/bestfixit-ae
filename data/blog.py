"""Blog content for the site — real, unique articles (no placeholders).

``POSTS`` is the single source of truth for the blog: it drives the homepage
blog section (``components/blog_section.html``), the /blog listing and each
/blog/<slug> article page. Each post has a stable ``slug`` used in the URL.
"""

POSTS = [
    {
        "slug": "how-often-service-ac-in-dubai",
        "title": "How Often Should You Service Your AC in Dubai?",
        "date": "18 March 2026",
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
        "slug": "signs-you-need-an-electrician",
        "title": "6 Early Warning Signs You Need an Electrician",
        "date": "2 March 2026",
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
        "slug": "prevent-plumbing-leaks",
        "title": "Stop Small Leaks Before They Become Big Repairs",
        "date": "20 February 2026",
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
        "slug": "home-maintenance-checklist-uae",
        "title": "A Simple Home Maintenance Checklist for UAE Homes",
        "date": "5 February 2026",
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
]

POST_BY_SLUG = {p["slug"]: p for p in POSTS}


def _card(p):
    """Homepage-card view of a post (adds the article URL)."""
    return {**p, "url": "/blog/" + p["slug"]}


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
    "foot_url": "/blog",
}
