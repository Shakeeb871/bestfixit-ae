"""Rich content for the main service-category landing pages.

Each entry drives the full ``service_detail.html`` layout (hero, trust bar,
coverage, appliance grid, why-choose, steps, brands, areas, reviews, FAQ and
final CTA) plus the page's structured data. Slugs match ``data/services.py``.

Only categories with an entry here render the rich layout; the rest fall back
to the simple detail view until their content is written. ``icon`` values are
keys into the allow-list of inline SVGs in the template — never raw markup.
Set image paths to ``None`` to render a themed placeholder (swapped later).
"""

SERVICE_PAGES = {
    "home-appliances-repair": {
        "meta_title": "Home Appliance Repair in Dubai | Best Fix Technical Services",
        "meta_description": (
            "Licensed home appliance repair in Dubai for washing machines, "
            "fridges, ovens and dishwashers. Upfront pricing, genuine parts, "
            "two-year guarantee. Book today."
        ),
        "breadcrumb": "Home Appliances Repair",
        # 1 — Hero
        "hero": {
            "h1_accent": "Home Appliance Repair",
            "h1": "In Dubai, Fixed Right the First Time",
            "sub": (
                "When a fridge stops cooling or a washing machine floods the "
                "floor, you want one call that ends it. A licensed Best Fix "
                "technician finds the real fault and repairs it properly."
            ),
            "trust": "Rated 4.8 on Google · Two-year guarantee · Serving Dubai since 2012",
            "image": "img/Professional Home appliances repair services.webp",
            "image_alt": "Best Fix technician repairing a home appliance in a Dubai home",
        },
        # 2 — Trust bar
        "trust_bar": [
            {"num": "6,500+", "label": "Jobs completed"},
            {"num": "2,500+", "label": "Happy customers"},
            {"num": "40+", "label": "Technicians"},
            {"num": "4.8★", "label": "Google rating"},
        ],
        # 3 — Coverage prose
        "coverage": {
            "h2": "What Home Appliance Repair in Dubai Actually Covers",
            "body": (
                "Home appliance repair is the diagnosis and repair of the "
                "machines that run your household, from washing machines and "
                "refrigerators to ovens, dishwashers and smaller kitchen "
                "units. Our technicians trace the fault back to its cause, "
                "whether that is a worn drum bearing, a blocked drain pump, a "
                "failed thermostat or a tripped control board, then repair the "
                "part rather than paper over the symptom. You get the exact "
                "cost in writing before any work starts."
            ),
        },
        # 4 — Appliances grid (detailed issue points per appliance)
        "appliances": {
            "h2": "Washing Machine, Fridge, Oven and Dishwasher Repair We Handle",
            "intro": (
                "Whatever the fault, we repair it — not just the common ones. "
                "Here is the kind of issue our technicians fix every day."
            ),
            "rows": [
                {"icon": "washer", "img": "washing machine repair.jpg", "title": "Washing Machine Repair", "points": [
                    "Will not spin, drain or switch on",
                    "Water not heating on a cycle",
                    "Loud banging or heavy vibration",
                    "Door won't open or lock faults",
                    "Leaking from the door or hoses",
                    "Error codes and control-board faults",
                ]},
                {"icon": "fridge", "img": "fridge repair.jpg", "title": "Fridge & Freezer Repair", "points": [
                    "Not cooling or not freezing",
                    "Gas top-up and compressor faults",
                    "Water leaking or pooling inside",
                    "Excess ice or frost build-up",
                    "Noisy or non-stop running",
                    "Faulty thermostat, fan or sensor",
                ]},
                {"icon": "oven", "img": "cooking range, oven and stove repair.jpg", "title": "Oven & Cooker Repair", "points": [
                    "Dead or weak heating elements",
                    "Gas ignition not sparking",
                    "Uneven or wrong temperature",
                    "Faulty thermostat or timer",
                    "Broken door seal or hinge",
                    "Control knob and switch faults",
                ]},
                {"icon": "dishwasher", "img": "dishwasher repair.jpg", "title": "Dishwasher Repair", "points": [
                    "Not draining or not filling",
                    "Plates left dirty or filmy",
                    "Water leaking onto the floor",
                    "Not heating or not drying",
                    "Blocked spray arms or filter",
                    "Error codes and pump faults",
                ]},
                {"icon": "microwave", "img": "small appliances repair.jpg", "title": "Small Appliance Repair", "points": [
                    "Microwaves not heating",
                    "Cooktops and hobs with dead zones",
                    "Water heaters and geysers",
                    "Cooker hoods and extractor fans",
                    "Toasters, kettles and blenders",
                    "Vacuum cleaners and irons",
                ]},
                {"icon": "bolt", "img": "emergency repair service.jpg", "title": "Emergency Call-Outs", "points": [
                    "Water leaking from an appliance",
                    "Sparking or a burning smell",
                    "Appliance tripping the electrics",
                    "Total breakdown before an event",
                    "Same-day and after-hours visits",
                    "Fast make-safe, then a full repair",
                ]},
            ],
        },
        # 5 — Why choose
        "why": {
            "h2": "Why Dubai Homeowners Choose Best Fix for Appliance Repair",
            "rows": [
                {"icon": "shield", "title": "Two-Year Workmanship Guarantee",
                 "text": "Parts and labour covered for two full years. Same fault returns, we come back free."},
                {"icon": "tag", "title": "Upfront, Fixed Pricing",
                 "text": "Exact price on site before work starts. No surprise charges."},
                {"icon": "gear", "title": "Genuine Parts Only",
                 "text": "Manufacturer-grade parts, so the repair lasts."},
                {"icon": "clock", "title": "On Time, or It's On Us",
                 "text": "We arrive in your chosen window. If we are late, the call-out is free."},
            ],
        },
        # 6 — How it works
        "steps": {
            "h2": "How Our Appliance Repair Service Works",
            "rows": [
                {"n": "01", "title": "Tell Us What's Wrong",
                 "text": "By phone, WhatsApp or the form."},
                {"n": "02", "title": "On-Site Inspection & Quote",
                 "text": "A licensed technician checks it and gives a clear price."},
                {"n": "03", "title": "We Carry Out the Repair",
                 "text": "Genuine parts, right tools, on schedule."},
                {"n": "04", "title": "Tested & Handed Back",
                 "text": "We test, tidy up and leave it working."},
            ],
        },
        # 7 — Brands
        "brands": {
            "h2": "Appliance Brands We Repair in Dubai",
            "intro": (
                "We repair the mainstream brands in most Dubai homes, so the "
                "diagnosis stays the same whatever you own. Our technicians "
                "work across every make and model."
            ),
            "logos": [
                {"name": "Bosch", "img": "Brands/bosch2.jpg"},
                {"name": "Siemens", "img": "Brands/siemens1.jpg"},
                {"name": "Samsung", "img": "Brands/samsung1.jpg"},
                {"name": "LG", "img": "Brands/lg2.jpg"},
                {"name": "Whirlpool", "img": "Brands/whirl-pool.jpg"},
                {"name": "Ariston", "img": "Brands/ariston.jpg"},
                {"name": "Daewoo", "img": "Brands/daewoo1.jpg"},
                {"name": "Super General", "img": "Brands/super-general.jpg"},
                {"name": "Beko", "img": "Brands/beko.jpg"},
                {"name": "Midea", "img": "Brands/midea.jpg"},
                {"name": "Hitachi", "img": "Brands/hitaachi.jpg"},
                {"name": "Panasonic", "img": "Brands/panasonic.jpg"},
                {"name": "Electrolux", "img": "Brands/electrolux1.jpg"},
                {"name": "Teka", "img": "Brands/teka.jpg"},
            ],
        },
        # 8 — Areas
        "areas": {
            "h2": "Appliance Repair Across Dubai and the UAE",
            "body": (
                "Our technicians work across Dubai and the wider UAE, "
                "including Abu Dhabi, Sharjah, Ajman and Ras Al Khaimah, with "
                "more than 120 areas covered. From JVC and Dubai Marina to "
                "Downtown and Al Barsha, there is usually a Best Fix van near "
                "you."
            ),
        },
        # 9 — Reviews
        "reviews": {
            "h2": "What Our Customers Say",
            "rows": [
                {"quote": "Booked in the morning, fixed by afternoon. Clean, polite and fair pricing.", "name": "Aisha R."},
                {"quote": "Arrived on schedule, professional team, left the place spotless.", "name": "James M."},
                {"quote": "Tidy, careful and genuinely helpful from start to finish.", "name": "Fatima K."},
            ],
        },
        # 10 — FAQ
        "faq_h2": "Home Appliance Repair in Dubai — Frequently Asked Questions",
        "faqs": [
            {"q": "How much does appliance repair cost in Dubai?",
             "a": "It depends on the appliance and the fault, so we never quote blind. A technician inspects the unit on site, explains what failed, and gives the exact price before any work begins. Nothing is added later."},
            {"q": "Do you repair all brands?",
             "a": "We service most major brands sold in the UAE, from Bosch and Siemens to LG and Whirlpool. Tell us the make and model when you book and we bring the likely parts on the first visit."},
            {"q": "How soon can a technician come?",
             "a": "Same-day slots are usually available, and emergency call-outs run outside standard hours for problems that cannot wait. Book early for the best chance of a same-day visit."},
            {"q": "Is the repair guaranteed?",
             "a": "Yes. Every repair carries a two-year workmanship guarantee on parts and labour. If the same fault returns in that period, we put it right at no cost."},
        ],
        # 11 — Final CTA + form
        "cta": {
            "h2": "Get Your Appliance Working Again Today",
            "sub": (
                "Book a licensed technician, get an upfront quote, and have it "
                "fixed with a two-year guarantee behind the work."
            ),
            "services": [
                "Washing Machine", "Fridge & Freezer", "Oven & Cooker",
                "Dishwasher", "Small Appliance", "Other Appliance",
            ],
        },
    },
}
