"""Appliance sub-service pages (two-column layout).

These sit *under* the core ``home-appliances-repair`` service and share a
dedicated two-column template (``subservice_detail.html``): long-form,
well-structured content on the left; internal links, a booking form and
customer testimonials in a sticky sidebar on the right.

``SUBSERVICE_PAGES`` is keyed by slug and is checked first inside the
``/services/<slug>/`` route, so a sub-service page keeps the clean
``/services/<slug>/`` URL shape used everywhere else on the site.

``SERVICE_SUBLINKS`` maps a core-service slug to its sub-service pages and
drives both the header navigation dropdown and the sidebar cross-links.
"""

# Dubai areas we serve — shared across every appliance sub-service page.
_AREAS = [
    "JLT", "Al Barsha", "Palm Jumeirah", "Downtown", "Emirates Hills",
    "Jumeirah", "Bur Dubai", "The Greens", "Jebel Ali", "IMPZ",
    "Sports City", "Motor City", "Al Barari", "Arabian Ranches",
    "Dubai Marina", "Deira", "Satwa", "Karama", "Business Bay",
    "Garhoud", "Nad Al Sheba", "Nad Al Hamar", "Al Warqa",
    "International City", "Silicon Oasis", "JVC", "JBR",
]

# Common home-appliance brands we repair — shown as logos (reusing the same
# brand-logo set as the core appliance page for a consistent brand wall).
from data.service_pages import _BRANDS as _BRAND_TUPLES

_BRAND_LOGOS = [{"name": n, "img": "Brands/" + f} for n, f in _BRAND_TUPLES]

# --------------------------------------------------------------------------- #
# Sidebar / navigation: sub-service pages grouped under each core service.
# --------------------------------------------------------------------------- #
APPLIANCE_PARENT = {
    "name": "Home Appliances Repair",
    "href": "/services/home-appliances-repair/",
}

SERVICE_SUBLINKS = {
    "home-appliances-repair": [
        {"name": "Washing Machine Repair", "slug": "washing-machine-repair"},
        {"name": "Refrigerator & Freezer Repair", "slug": "refrigerator-repair"},
        {"name": "Oven, Cooker & Hob Repair", "slug": "oven-cooker-repair"},
        {"name": "Dishwasher Repair", "slug": "dishwasher-repair"},
        {"name": "Dryer Repair", "slug": "dryer-repair"},
        {"name": "Microwave Repair", "slug": "microwave-repair"},
        {"name": "Small Appliance Repair", "slug": "small-appliance-repair"},
    ],
}

# Sidebar link list (name + resolved href) for the appliance family.
APPLIANCE_SERVICES = [
    {"name": s["name"], "href": f"/services/{s['slug']}/"}
    for s in SERVICE_SUBLINKS["home-appliances-repair"]
]

# Short, appliance-specific reviews for the sidebar.
SUBSERVICE_TESTIMONIALS = [
    {
        "name": "Maryam S.",
        "area": "Dubai Marina",
        "text": "Same-day visit, honest diagnosis and a clean repair. The technician "
                "explained exactly what had failed before starting. Highly recommend.",
        "rating": 5,
    },
    {
        "name": "Imran K.",
        "area": "Business Bay",
        "text": "Booked in the morning, sorted by the afternoon. Fair price and no "
                "pushing for unnecessary parts. My go-to for appliance repairs now.",
        "rating": 5,
    },
    {
        "name": "Rita P.",
        "area": "Jumeirah Village Circle",
        "text": "Polite, tidy and quick. Fixed the fault in one visit and left everything "
                "working perfectly. Excellent service from Best Fix.",
        "rating": 5,
    },
]


def _why(appliance, first_line):
    """Build the shared "why choose" block with an appliance-specific opener."""
    return {
        "areas_intro": f"We provide fast {appliance} repair across Dubai, including:",
        "areas": _AREAS,
        "paras": [
            first_line,
            "We are a team of professionals who inspect, diagnose and fix your "
            f"{appliance} correctly the first time — so a small fault doesn't turn into "
            "a repeat call-out or a bigger repair later on.",
            "Most importantly, we come to your location whenever you need us and offer "
            "same-day appointments wherever the schedule allows. You get a clear "
            "diagnosis, a fair price and tidy work at your doorstep.",
        ],
    }


SUBSERVICE_PAGES = {
    # ===================================================================== #
    # 1 · WASHING MACHINE
    # ===================================================================== #
    "washing-machine-repair": {
        "parent_slug": "home-appliances-repair",
        "meta_title": "Washing Machine Repair in Dubai — Same-Day Service | Best Fix",
        "meta_description": (
            "Same-day washing machine repair in Dubai by Best Fix. Front & top "
            "loaders, all brands — drainage, spin, leaks, drum, door-lock and "
            "power faults fixed by experienced technicians at a fair price."
        ),
        "breadcrumb": "Washing Machine Repair",
        "hero": {
            "eyebrow": "Washing Machine Repair",
            "h1_accent": "Washing Machine Repair in Dubai",
            "h1": "Same-Day Diagnosis and Repair",
            "subheading": (
                "Front and top loaders, fully and semi-automatic, every major brand — "
                "diagnosed properly and repaired at a fair, transparent price."
            ),
            "image": "img/washing machine repair.jpg",
            "image_alt": "Best Fix technician repairing a washing machine in Dubai",
        },
        "intro": [
            "Looking for reliable washing machine repair in Dubai? Best Fix Technical "
            "Services provides a complete washing machine diagnosis, repair and servicing "
            "solution across the city — often on the same day and always at a reasonable, "
            "clearly explained cost.",
            "Our technicians work on every major type and brand, and each visit starts "
            "with a proper inspection rather than guesswork. Alongside washing machines we "
            "repair the full range of home appliances, so one trusted team can look after "
            "your whole home. Book a technician now for quick help and a confirmed slot.",
        ],
        "types": {
            "h2": "Repair Support for All Washing Machine Types",
            "intro": "Our technicians are experienced across every washing machine "
                     "configuration found in UAE homes and apartments:",
            "list": [
                "Fully automatic washing machines",
                "Semi-automatic washing machines",
                "Top-loading washing machines",
                "Front-loading washing machines",
                "Compact and built-in washing machines",
                "Washer-dryer combination units",
            ],
        },
        "services": {
            "h2": "Washing Machine Repair Services We Provide",
            "intro": "From a machine that won't drain to one that won't start, we cover "
                     "the full range of washing machine faults:",
            "rows": [
                {"title": "Drainage Repair",
                 "text": "Water left standing in the drum after a wash cycle usually points "
                         "to a blocked filter, a kinked drain hose or a failing pump. We "
                         "trace the blockage and restore proper drainage."},
                {"title": "Spin-Cycle Repair",
                 "text": "Clothes coming out soaking wet, or a drum that won't spin up, often "
                         "means a worn belt, a motor fault or an unbalanced load. We inspect "
                         "the spin system and put it right."},
                {"title": "Water Leakage Repair",
                 "text": "Water escaping from the door, a hose or the base of the machine can "
                         "quickly damage flooring. We check seals, inlet pipes and internal "
                         "leak points and reseal or replace as needed."},
                {"title": "Drum Repair",
                 "text": "A drum that wobbles, runs loose or makes unusual sounds needs a "
                         "proper technical inspection. We handle drum, bearing and spider-arm "
                         "faults across all brands."},
                {"title": "Door-Lock Repair",
                 "text": "A machine that won't start or won't complete its cycle is often a "
                         "door-lock issue. We inspect door switches, latches and the locking "
                         "mechanism and replace faulty parts."},
                {"title": "Noise & Vibration Repair",
                 "text": "Loud banging, grinding or heavy vibration during a wash usually comes "
                         "from worn bearings, a drum imbalance or loose internal parts. We "
                         "locate the source and quieten the machine."},
                {"title": "Power & Electrical Fault Repair",
                 "text": "A machine that won't switch on, or stops partway through a cycle, may "
                         "have an electrical, control-board or switch fault. We carry out safe, "
                         "methodical fault-finding."},
                {"title": "Water-Inlet Repair",
                 "text": "A machine that won't fill, or fills too slowly, often has an inlet "
                         "valve, hose or water-flow problem. We identify the cause and carry "
                         "out the correct repair."},
            ],
        },
        "problems": {
            "h2": "Common Washing Machine Problems We Fix",
            "intro": "These are the faults we're called out for most often across Dubai:",
            "list": [
                "The washing machine does not drain water properly after the wash cycle.",
                "The drum does not spin, or clothes come out soaking wet.",
                "Water leaks from the door or from underneath the unit.",
                "The machine makes loud banging, grinding or vibrating sounds while running.",
                "The washing machine will not turn on, or stops before the cycle finishes.",
                "Clothes are not cleaned properly, or the wash takes far too long.",
            ],
        },
        "band": {
            "title": "Skilled Washing Machine Inspection and Repair Across Dubai",
            "text": "Book your service now for quick, affordable and professional washing "
                    "machine solutions — with an honest diagnosis before any work begins.",
        },
        "why": {
            "h2": "Why Choose Best Fix for Washing Machine Repair",
            "image": "img/Appliance Repair Should Begin With Evidence, Not Guesswork.webp",
            "image_alt": "Best Fix technician diagnosing a washing machine fault in Dubai",
            **_why("washing machine",
                   "Best Fix is built around doorstep, quick and reliable appliance repair "
                   "in Dubai. Our technicians are highly experienced, with years of hands-on "
                   "work across washing machines and every other major home appliance."),
        },
        "brands": {
            "h2": "Washing Machine Brands We Repair",
            "intro": "We provide repair and servicing for all major washing machine brands "
                     "in Dubai, with same-day support wherever possible:",
            "logos": _BRAND_LOGOS,
        },
        "codes": {
            "h2": "Common Error Codes in Smart Washing Machines We Fix",
            "intro": "Washing machine error codes are a useful starting point, but they are "
                     "not a complete diagnosis — the same code can mean slightly different "
                     "things depending on the brand and model. We check the model number, "
                     "service history, symptoms and live machine behaviour before "
                     "recommending any repair.",
            "rows": [
                {"code": "UE, UB, dC", "meaning": "Unbalanced load or spin problem"},
                {"code": "OE, 5E, 5C, nd, F9 E1", "meaning": "Drainage fault"},
                {"code": "IE, 1E, 4C, 4E, nF, LO FL, F8 E1", "meaning": "Water-fill problem"},
                {"code": "dE, dS, FL, LO", "meaning": "Door-lock error"},
                {"code": "SUD, Sd, 5UD", "meaning": "Excessive suds"},
                {"code": "LE, LC, E9", "meaning": "Leak-detection code"},
                {"code": "tE, HE", "meaning": "Temperature-sensor error"},
                {"code": "PF, CE, AE", "meaning": "Communication error"},
                {"code": "LE, 3E, E3", "meaning": "Motor error"},
            ],
        },
        "faq_h2": "Washing Machine Repair FAQs",
        "faqs": [
            {"q": "My washing machine is not draining water properly. What could be wrong?",
             "a": "A machine that stops draining usually has a blocked filter, a clogged "
                  "drain hose or a faulty drain pump. A technical inspection identifies the "
                  "exact cause and restores normal drainage."},
            {"q": "Why is my washing machine not spinning properly?",
             "a": "Spin-cycle problems often come from a damaged drive belt, a motor fault, "
                  "an unbalanced drum or a control issue. When the machine can't spin "
                  "correctly, clothes are left very wet at the end of the cycle."},
            {"q": "Why is my washing machine leaking water?",
             "a": "Leaks can come from a damaged door seal, a loose hose, a faulty inlet "
                  "connection or an internal component. Early inspection helps limit any "
                  "water damage around the laundry area."},
            {"q": "Why is my washing machine making a loud noise?",
             "a": "Banging, grinding or vibrating sounds can point to a drum imbalance, worn "
                  "bearings, loose components or an item trapped inside the machine. The "
                  "appliance should be checked once the noise becomes frequent."},
            {"q": "Why is my washing machine not turning on?",
             "a": "A machine may fail to start because of a power issue, a door-lock fault, "
                  "a damaged switch or a control-panel problem. A technician can inspect the "
                  "electrical and operating parts to find the cause."},
            {"q": "Why is my washing machine not cleaning clothes properly?",
             "a": "Poor washing results can come from low water intake, detergent build-up, "
                  "blocked filters, drum-movement faults or an incorrect cycle. An inspection "
                  "pinpoints the part affecting wash quality."},
        ],
        "tips": {
            "h2": "Maintenance Tips to Keep Your Washing Machine at Its Best",
            "intro": "A little routine care keeps a washing machine running well and helps you "
                     "avoid the most common breakdowns:",
            "list": [
                "Avoid overloading the drum — heavy loads affect both spinning and wash quality.",
                "Check pockets before washing to keep coins and small items out of the drum and filter.",
                "Clean the detergent drawer regularly to reduce soap build-up and odours.",
                "Inspect the door seal for trapped dirt, moisture or signs of damage.",
                "Leave the door slightly open after a cycle so the drum can dry out.",
                "Clean the washing machine filter periodically to support proper drainage.",
                "Check the inlet and drain hoses for bends, looseness or visible leaks.",
                "Use the correct amount of detergent for the machine type and load.",
                "Stop using the machine if it produces repeated loud noise or heavy vibration.",
                "Book a technical inspection when the machine won't drain, spin, fill or start correctly.",
            ],
        },
    },

    # ===================================================================== #
    # 2 · REFRIGERATOR & FREEZER
    # ===================================================================== #
    "refrigerator-repair": {
        "parent_slug": "home-appliances-repair",
        "meta_title": "Refrigerator & Freezer Repair in Dubai — Same-Day | Best Fix",
        "meta_description": (
            "Same-day refrigerator and freezer repair in Dubai by Best Fix. Cooling "
            "faults, compressors, water leaks, gas top-ups and thermostats fixed by "
            "experienced technicians for all brands at a fair price."
        ),
        "breadcrumb": "Refrigerator & Freezer Repair",
        "hero": {
            "eyebrow": "Refrigerator Repair",
            "h1_accent": "Refrigerator & Freezer Repair in Dubai",
            "h1": "Same-Day Cooling Repairs",
            "subheading": (
                "Fridges not cooling, freezers over-frosting, leaks and compressor "
                "faults — diagnosed properly and repaired before food starts to spoil."
            ),
            "image": "img/fridge repair.jpg",
            "image_alt": "Best Fix technician repairing a refrigerator in Dubai",
        },
        "intro": [
            "Need fast, reliable refrigerator repair in Dubai? Best Fix Technical Services "
            "provides complete fridge and freezer diagnosis, repair and servicing across "
            "the city — often on the same day, because a cooling fault is rarely something "
            "you can leave until tomorrow.",
            "Our technicians work on every major type and brand and always begin with a "
            "proper inspection. Alongside refrigerators we repair the full range of home "
            "appliances, so one trusted team can look after your whole home. Book now for "
            "quick help and a confirmed slot.",
        ],
        "types": {
            "h2": "Repair Support for All Refrigerator & Freezer Types",
            "intro": "We service every fridge and freezer configuration found in UAE homes "
                     "and businesses:",
            "list": [
                "Single-door refrigerators",
                "Double-door refrigerators",
                "Side-by-side refrigerators",
                "French-door refrigerators",
                "Bottom-freezer refrigerators",
                "Mini and bar fridges",
                "Upright freezers",
                "Chest freezers",
                "Commercial display fridges",
            ],
        },
        "services": {
            "h2": "Refrigerator & Freezer Repair Services We Provide",
            "intro": "From a fridge that won't cool to a freezer building up ice, we cover "
                     "the full range of refrigeration faults:",
            "rows": [
                {"title": "Not-Cooling Repair",
                 "text": "A fridge that stays warm may have a gas leak, a faulty compressor, "
                         "a blocked coil or a fan fault. We find the root cause and restore "
                         "proper cooling."},
                {"title": "Freezer Not Freezing",
                 "text": "A freezer that won't hold temperature often points to a thermostat, "
                         "sensor or airflow problem. We inspect the freezing system and put "
                         "it right."},
                {"title": "Water Leakage Repair",
                 "text": "Water pooling inside or under the fridge is usually a blocked defrost "
                         "drain or a damaged water line. We clear and repair the affected part."},
                {"title": "Excess Frost & Defrost Repair",
                 "text": "Heavy ice build-up can mean a failed defrost timer, heater or sensor. "
                         "We diagnose the defrost system and replace the faulty component."},
                {"title": "Compressor Repair",
                 "text": "A noisy, hot or non-starting compressor affects the whole unit. We "
                         "test the compressor and its start components and advise on the best "
                         "repair option."},
                {"title": "Thermostat & Temperature Control",
                 "text": "Fridges that run too cold or too warm often have a thermostat or "
                         "control-board fault. We recalibrate or replace the control as needed."},
                {"title": "Door Seal & Gasket Repair",
                 "text": "A worn door gasket lets cold air escape, overworking the compressor "
                         "and raising your bill. We replace seals for a tight, efficient close."},
                {"title": "Unusual Noise Repair",
                 "text": "Buzzing, clicking or rattling can come from the fan, compressor or "
                         "loose parts. We trace the noise and correct it."},
                {"title": "Water Dispenser & Ice-Maker Repair",
                 "text": "No water or no ice usually means a valve, line or ice-maker fault. "
                         "We inspect the dispensing system and restore normal function."},
            ],
        },
        "problems": {
            "h2": "Common Refrigerator Problems We Fix",
            "intro": "These are the fridge and freezer faults we're called out for most:",
            "list": [
                "The refrigerator is running but not cooling properly.",
                "The freezer is not freezing, or food is thawing.",
                "Water is leaking inside the fridge or onto the floor.",
                "Ice is building up heavily inside the freezer compartment.",
                "The fridge is making loud buzzing, clicking or rattling noises.",
                "The compressor runs constantly, or the unit won't switch on at all.",
            ],
        },
        "band": {
            "title": "Fast Refrigerator & Freezer Repair Before Food Spoils",
            "text": "Book your service now for quick, affordable and professional cooling "
                    "repairs — with an honest diagnosis before any work begins.",
        },
        "why": {
            "h2": "Why Choose Best Fix for Refrigerator Repair",
            "image": "img/Same-Day Appliance Repair Without Empty Promises.webp",
            "image_alt": "Best Fix technician servicing a refrigerator in Dubai",
            **_why("refrigerator",
                   "Best Fix is built around doorstep, quick and reliable appliance repair "
                   "in Dubai. Our technicians are highly experienced with refrigeration and "
                   "understand how urgent a cooling fault is in the UAE climate."),
        },
        "brands": {
            "h2": "Refrigerator Brands We Repair",
            "intro": "We repair and service all major refrigerator and freezer brands in "
                     "Dubai, with same-day support wherever possible:",
            "logos": _BRAND_LOGOS,
        },
        "codes": {
            "h2": "Common Error Codes in Smart Refrigerators We Fix",
            "intro": "Refrigerator error codes are a useful starting point, but they are not "
                     "a complete diagnosis — the same code can mean slightly different things "
                     "depending on the brand and model. We check the model number, service "
                     "history, symptoms and live behaviour before recommending any repair.",
            "rows": [
                {"code": "1E, 5E, rS, rt, FS, Ft", "meaning": "Temperature-sensor fault"},
                {"code": "21E, 22E, 23E, FF, rF, IF", "meaning": "Fan-motor fault (freezer, fridge or condenser)"},
                {"code": "24E, 25E, 26E, dH", "meaning": "Defrost-system fault"},
                {"code": "40E, 41E", "meaning": "Ice-maker fault"},
                {"code": "84C, 85C, 86C", "meaning": "Compressor or inverter fault"},
                {"code": "OF OF, O FF", "meaning": "Cooling-off or demo mode enabled"},
                {"code": "CO, 88 88, PC ER", "meaning": "Communication or control-board error"},
            ],
        },
        "faq_h2": "Refrigerator Repair FAQs",
        "faqs": [
            {"q": "My fridge is running but not cooling. What could be wrong?",
             "a": "A fridge that runs without cooling may have a refrigerant (gas) leak, a "
                  "faulty compressor, blocked condenser coils or a fan fault. An inspection "
                  "identifies the cause so the right repair can restore cooling."},
            {"q": "Why is ice building up in my freezer?",
             "a": "Heavy frost usually points to a defrost-system fault — a failed defrost "
                  "heater, timer or sensor — or a worn door seal letting warm, humid air in. "
                  "We diagnose the defrost circuit and reseal or replace as needed."},
            {"q": "Why is water leaking from my refrigerator?",
             "a": "Leaks are often caused by a blocked defrost drain or a damaged water line. "
                  "Clearing the drain or repairing the line stops the leak and prevents floor "
                  "damage."},
            {"q": "Is it worth repairing an old refrigerator?",
             "a": "It depends on the fault, the age and the running efficiency of the unit. "
                  "We give an honest assessment so you can decide between a cost-effective "
                  "repair and replacement."},
            {"q": "My fridge is very noisy. Should I be concerned?",
             "a": "Occasional sounds are normal, but constant buzzing, clicking or rattling "
                  "can indicate a fan, compressor or loose-part issue that should be checked "
                  "before it worsens."},
            {"q": "How quickly can you repair my fridge?",
             "a": "Because refrigeration faults are urgent, we prioritise them and offer "
                  "same-day appointments across Dubai wherever the schedule allows."},
        ],
        "tips": {
            "h2": "Maintenance Tips to Keep Your Refrigerator Running Well",
            "intro": "A little routine care keeps a fridge cooling efficiently and helps you "
                     "avoid breakdowns:",
            "list": [
                "Keep the fridge and freezer at the recommended temperatures — not colder than needed.",
                "Leave a gap around the unit so the condenser can release heat.",
                "Clean the condenser coils at the back or base a few times a year.",
                "Check and clean the door seals so cold air doesn't escape.",
                "Avoid overfilling — air needs to circulate to cool evenly.",
                "Let hot food cool before placing it inside.",
                "Clear the defrost drain periodically to prevent internal leaks.",
                "Don't leave the door open longer than necessary, especially in summer.",
                "Defrost manual freezers before ice builds up too thickly.",
                "Book an inspection if cooling weakens or the compressor runs non-stop.",
            ],
        },
    },

    # ===================================================================== #
    # 3 · OVEN, COOKER & HOB
    # ===================================================================== #
    "oven-cooker-repair": {
        "parent_slug": "home-appliances-repair",
        "meta_title": "Oven, Cooker & Hob Repair in Dubai — Same-Day | Best Fix",
        "meta_description": (
            "Same-day oven, cooker and hob repair in Dubai by Best Fix. Heating "
            "elements, igniters, gas burners, thermostats and induction faults fixed "
            "safely for all brands at a fair price."
        ),
        "breadcrumb": "Oven, Cooker & Hob Repair",
        "hero": {
            "eyebrow": "Oven & Cooker Repair",
            "h1_accent": "Oven, Cooker & Hob Repair in Dubai",
            "h1": "Safe, Same-Day Cooking Repairs",
            "subheading": (
                "Electric and gas ovens, cookers and hobs — heating, ignition and "
                "control faults diagnosed and repaired safely by experienced technicians."
            ),
            "image": "img/cooking range, oven and stove repair.jpg",
            "image_alt": "Best Fix technician repairing an oven and cooker in Dubai",
        },
        "intro": [
            "Looking for dependable oven, cooker or hob repair in Dubai? Best Fix "
            "Technical Services provides complete cooking-appliance diagnosis, repair and "
            "servicing across the city — often on the same day and always with safety in "
            "mind, especially on gas appliances.",
            "Our technicians work on every major type and brand and start each visit with "
            "a proper inspection. Alongside ovens and hobs we repair the full range of "
            "home appliances, so one trusted team can look after your whole kitchen. Book "
            "now for quick help and a confirmed slot.",
        ],
        "types": {
            "h2": "Repair Support for All Oven, Cooker & Hob Types",
            "intro": "We service every cooking-appliance configuration found in UAE homes:",
            "list": [
                "Electric ovens",
                "Gas ovens",
                "Built-in ovens",
                "Freestanding cookers",
                "Range cookers",
                "Gas hobs",
                "Electric and ceramic hobs",
                "Induction hobs",
            ],
        },
        "services": {
            "h2": "Oven, Cooker & Hob Repair Services We Provide",
            "intro": "From an oven that won't heat to a hob that won't ignite, we cover the "
                     "full range of cooking-appliance faults:",
            "rows": [
                {"title": "Not-Heating Repair",
                 "text": "An oven that won't heat usually has a failed element, igniter or "
                         "thermostat. We test the heating circuit and replace the faulty part."},
                {"title": "Uneven Heating Repair",
                 "text": "Food cooking unevenly can mean a weak element, a faulty fan or a "
                         "thermostat that's out of calibration. We inspect and correct it."},
                {"title": "Igniter & Spark Repair",
                 "text": "A hob that clicks without lighting, or won't spark at all, often has "
                         "an igniter or spark-module fault. We restore reliable ignition."},
                {"title": "Gas Burner Repair",
                 "text": "Weak flames, uneven burning or a burner that won't stay lit are "
                         "checked carefully — gas work is always handled safely and correctly."},
                {"title": "Thermostat Repair",
                 "text": "An oven that runs too hot or too cold, or ignores its setting, "
                         "usually needs a thermostat or control repair. We recalibrate or "
                         "replace as required."},
                {"title": "Door, Hinge & Glass Repair",
                 "text": "A door that won't seal, sagging hinges or cracked glass affect both "
                         "safety and efficiency. We repair or replace door components."},
                {"title": "Heating Element & Fan Repair",
                 "text": "Blown elements and failed fan motors are common in fan ovens. We "
                         "replace them so heat is delivered evenly again."},
                {"title": "Control Knob & Panel Repair",
                 "text": "Unresponsive knobs, faulty touch panels or blank displays are "
                         "diagnosed and repaired to restore full control."},
                {"title": "Induction Zone Repair",
                 "text": "An induction zone that won't power on, or cuts out, may have a coil "
                         "or control-board fault. We test the affected zone and repair it."},
            ],
        },
        "problems": {
            "h2": "Common Oven & Cooker Problems We Fix",
            "intro": "These are the cooking-appliance faults we're called out for most:",
            "list": [
                "The oven does not heat up, or takes far too long to reach temperature.",
                "Food cooks unevenly, with hot and cold spots.",
                "A gas hob clicks but will not ignite, or the flame keeps going out.",
                "The oven runs much hotter or cooler than the setting.",
                "The oven door won't close properly or the glass is cracked.",
                "An induction or electric hob zone has stopped working.",
            ],
        },
        "band": {
            "title": "Safe, Skilled Oven, Cooker & Hob Repair Across Dubai",
            "text": "Book your service now for quick, affordable and professional cooking-"
                    "appliance repairs — with gas work always handled safely.",
        },
        "why": {
            "h2": "Why Choose Best Fix for Oven & Cooker Repair",
            "image": "img/Repair or Replace the Appliance.webp",
            "image_alt": "Best Fix technician repairing a cooker in Dubai",
            **_why("oven and cooker",
                   "Best Fix is built around doorstep, quick and reliable appliance repair "
                   "in Dubai. Our technicians are highly experienced with both electric and "
                   "gas cooking appliances, and treat safety as the first priority."),
        },
        "brands": {
            "h2": "Oven & Cooker Brands We Repair",
            "intro": "We repair and service all major oven, cooker and hob brands in Dubai, "
                     "with same-day support wherever possible:",
            "logos": _BRAND_LOGOS,
        },
        "codes": None,
        "faq_h2": "Oven & Cooker Repair FAQs",
        "faqs": [
            {"q": "My oven isn't heating up. What could be wrong?",
             "a": "A no-heat fault usually comes from a failed heating element, igniter or "
                  "thermostat, or a control-board issue. We test the heating circuit and "
                  "replace the faulty part."},
            {"q": "Why won't my gas hob light?",
             "a": "A hob that clicks without lighting often has a dirty or faulty igniter, a "
                  "blocked burner or a spark-module fault. We clean or replace the part and "
                  "confirm safe, reliable ignition."},
            {"q": "Do you repair gas cookers safely?",
             "a": "Yes. All gas work is carried out carefully and correctly, with the "
                  "appliance checked for safe operation before we finish."},
            {"q": "Why is my oven cooking unevenly?",
             "a": "Uneven cooking usually points to a weak element, a failing fan or a "
                  "thermostat that's drifted out of calibration. We diagnose and correct the "
                  "cause so heat is delivered evenly."},
            {"q": "Can you fix a single induction zone that stopped working?",
             "a": "Yes. A dead induction zone often has a coil or control-board fault. We test "
                  "the affected zone and carry out the correct repair."},
            {"q": "How soon can you come out?",
             "a": "We offer same-day appointments across Dubai wherever the schedule allows, "
                  "so you're not left without a working oven for long."},
        ],
        "tips": {
            "h2": "Maintenance Tips to Keep Your Oven & Hob at Its Best",
            "intro": "A little routine care keeps a cooker working safely and efficiently:",
            "list": [
                "Clean spills and grease promptly to protect elements and burners.",
                "Keep gas burner heads and igniters clean and dry for reliable lighting.",
                "Check the oven door seal so heat isn't escaping.",
                "Avoid lining the oven base with foil, which can block heat and airflow.",
                "Use the right cookware for induction hobs to keep zones working correctly.",
                "Don't slam the oven door — it can damage hinges and the glass.",
                "Wipe control knobs and touch panels gently to keep them responsive.",
                "Have the oven checked if it heats slowly or the temperature seems off.",
                "Never ignore a gas smell — turn off the supply and call for a check.",
                "Book an inspection at the first sign of ignition, heating or control faults.",
            ],
        },
    },

    # ===================================================================== #
    # 4 · DISHWASHER
    # ===================================================================== #
    "dishwasher-repair": {
        "parent_slug": "home-appliances-repair",
        "meta_title": "Dishwasher Repair in Dubai — Same-Day Service | Best Fix",
        "meta_description": (
            "Same-day dishwasher repair in Dubai by Best Fix. Drainage, cleaning, "
            "leaks, heating, door-latch and spray-arm faults fixed for all brands by "
            "experienced technicians at a fair price."
        ),
        "breadcrumb": "Dishwasher Repair",
        "hero": {
            "eyebrow": "Dishwasher Repair",
            "h1_accent": "Dishwasher Repair in Dubai",
            "h1": "Same-Day Diagnosis and Repair",
            "subheading": (
                "Dishwashers that won't drain, clean, fill or dry — diagnosed properly "
                "and repaired for cleaner dishes and a drier kitchen."
            ),
            "image": "img/dishwasher repair.jpg",
            "image_alt": "Best Fix technician repairing a dishwasher in Dubai",
        },
        "intro": [
            "Searching for reliable dishwasher repair in Dubai? Best Fix Technical Services "
            "provides complete dishwasher diagnosis, repair and servicing across the city — "
            "often on the same day and always at a reasonable, clearly explained cost.",
            "Our technicians work on every major type and brand and start each visit with a "
            "proper inspection. Alongside dishwashers we repair the full range of home "
            "appliances, so one trusted team can look after your whole kitchen. Book now "
            "for quick help and a confirmed slot.",
        ],
        "types": {
            "h2": "Repair Support for All Dishwasher Types",
            "intro": "We service every dishwasher configuration found in UAE homes:",
            "list": [
                "Freestanding dishwashers",
                "Built-in and integrated dishwashers",
                "Semi-integrated dishwashers",
                "Slimline dishwashers",
                "Countertop dishwashers",
            ],
        },
        "services": {
            "h2": "Dishwasher Repair Services We Provide",
            "intro": "From a dishwasher that won't drain to one that won't clean, we cover "
                     "the full range of faults:",
            "rows": [
                {"title": "Not-Draining Repair",
                 "text": "Water left in the base after a cycle usually means a blocked filter, "
                         "a clogged drain hose or a faulty drain pump. We clear the blockage "
                         "and restore drainage."},
                {"title": "Not-Cleaning Repair",
                 "text": "Dishes coming out dirty can be caused by blocked spray arms, low "
                         "water intake or a detergent-dispenser fault. We find and fix the "
                         "cause of poor washing."},
                {"title": "Water Leakage Repair",
                 "text": "Leaks from the door or underneath can damage flooring and cabinets. "
                         "We check seals, hoses and the tub and repair the source."},
                {"title": "Not-Filling Repair",
                 "text": "A dishwasher that won't fill, or fills slowly, often has an inlet "
                         "valve, hose or water-flow issue. We diagnose and repair it."},
                {"title": "Not-Heating & Drying Repair",
                 "text": "Cold washes or wet dishes at the end of a cycle usually point to a "
                         "heating-element or sensor fault. We restore proper heating and drying."},
                {"title": "Door-Latch Repair",
                 "text": "A dishwasher that won't start or won't stay closed often has a "
                         "door-latch or switch fault. We inspect and replace the mechanism."},
                {"title": "Spray-Arm Repair",
                 "text": "Blocked or damaged spray arms leave dishes unclean. We clear the "
                         "jets or replace the arm for full coverage."},
                {"title": "Noise & Vibration Repair",
                 "text": "Grinding or rattling during a cycle can come from the pump, spray "
                         "arm or a trapped item. We locate the source and correct it."},
                {"title": "Power & Control Fault Repair",
                 "text": "A dishwasher that won't switch on, or stops mid-cycle, may have an "
                         "electrical or control-board fault. We carry out safe fault-finding."},
            ],
        },
        "problems": {
            "h2": "Common Dishwasher Problems We Fix",
            "intro": "These are the dishwasher faults we're called out for most:",
            "list": [
                "The dishwasher does not drain, leaving water in the base.",
                "Dishes come out dirty or with food still stuck on them.",
                "Water leaks from the door or from underneath the unit.",
                "The dishwasher does not fill with water, or fills very slowly.",
                "Dishes stay wet, or the wash runs cold with no heating.",
                "The dishwasher won't start, or stops before the cycle finishes.",
            ],
        },
        "band": {
            "title": "Skilled Dishwasher Inspection and Repair Across Dubai",
            "text": "Book your service now for quick, affordable and professional dishwasher "
                    "solutions — with an honest diagnosis before any work begins.",
        },
        "why": {
            "h2": "Why Choose Best Fix for Dishwasher Repair",
            "image": "img/Appliance Repair for Homes and Managed Properties.webp",
            "image_alt": "Best Fix technician servicing a dishwasher in Dubai",
            **_why("dishwasher",
                   "Best Fix is built around doorstep, quick and reliable appliance repair "
                   "in Dubai. Our technicians are highly experienced across every major "
                   "dishwasher brand and type."),
        },
        "brands": {
            "h2": "Dishwasher Brands We Repair",
            "intro": "We repair and service all major dishwasher brands in Dubai, with "
                     "same-day support wherever possible:",
            "logos": _BRAND_LOGOS,
        },
        "codes": {
            "h2": "Common Dishwasher Error Codes We Fix",
            "intro": "Dishwasher error codes are a useful starting point, but they aren't a "
                     "complete diagnosis — the same code can mean slightly different things "
                     "depending on the brand and model. We check the model, symptoms and "
                     "live behaviour before recommending any repair.",
            "rows": [
                {"code": "E1, F1", "meaning": "Water-inlet or fill fault"},
                {"code": "E4, i20, LC", "meaning": "Drainage or blockage fault"},
                {"code": "E15, E9, F2", "meaning": "Leak detected in the base tray"},
                {"code": "E3, i10, HE", "meaning": "Heating or temperature fault"},
                {"code": "E24, E25", "meaning": "Drain-hose or pump restriction"},
                {"code": "E6, dE", "meaning": "Door-latch or switch fault"},
                {"code": "E8, F8", "meaning": "Low water level / spray-arm issue"},
            ],
        },
        "faq_h2": "Dishwasher Repair FAQs",
        "faqs": [
            {"q": "Why is my dishwasher not draining?",
             "a": "Standing water usually means a blocked filter, a clogged drain hose or a "
                  "faulty drain pump. Clearing the blockage or repairing the pump restores "
                  "normal drainage."},
            {"q": "Why are my dishes still dirty after a cycle?",
             "a": "Poor cleaning can be caused by blocked spray arms, low water intake, a "
                  "detergent-dispenser fault or overloading. An inspection pinpoints the part "
                  "affecting wash quality."},
            {"q": "Why is my dishwasher leaking?",
             "a": "Leaks often come from a worn door seal, a loose hose or a cracked tub. "
                  "Early inspection helps prevent damage to flooring and cabinets."},
            {"q": "Why are my dishes wet at the end of the cycle?",
             "a": "Wet dishes usually point to a heating-element or sensor fault affecting the "
                  "dry stage, or a rinse-aid issue. We check the heating and drying system."},
            {"q": "My dishwasher won't start. What should I check?",
             "a": "A dishwasher that won't start often has a door-latch fault, a power issue "
                  "or a control-board problem. A technician can inspect the electrical and "
                  "operating parts."},
            {"q": "How soon can you repair my dishwasher?",
             "a": "We offer same-day appointments across Dubai wherever the schedule allows, "
                  "so your kitchen isn't disrupted for long."},
        ],
        "tips": {
            "h2": "Maintenance Tips to Keep Your Dishwasher at Its Best",
            "intro": "A little routine care keeps a dishwasher cleaning well and draining "
                     "freely:",
            "list": [
                "Clean the filter regularly to prevent blockages and poor drainage.",
                "Scrape large food scraps off plates before loading.",
                "Check and clear the spray-arm jets so water reaches every dish.",
                "Use the correct detergent and rinse aid for better cleaning and drying.",
                "Run a hot maintenance cycle periodically to clear grease and limescale.",
                "Don't overload — dishes need space for water to circulate.",
                "Wipe the door seal to remove trapped food and prevent odours.",
                "Check the drain hose for kinks or blockages.",
                "Leave the door slightly open after a cycle to let the interior dry.",
                "Book an inspection if the dishwasher won't drain, fill, heat or start.",
            ],
        },
    },

    # ===================================================================== #
    # 5 · MICROWAVE
    # ===================================================================== #
    "microwave-repair": {
        "parent_slug": "home-appliances-repair",
        "meta_title": "Microwave Repair in Dubai — Same-Day Service | Best Fix",
        "meta_description": (
            "Same-day microwave repair in Dubai by Best Fix. Not-heating, turntable, "
            "door, sparking and control faults fixed safely for all brands by "
            "experienced technicians at a fair price."
        ),
        "breadcrumb": "Microwave Repair",
        "hero": {
            "eyebrow": "Microwave Repair",
            "h1_accent": "Microwave Repair in Dubai",
            "h1": "Fast, Same-Day Repairs",
            "subheading": (
                "Microwaves that won't heat, spark or respond — diagnosed properly and "
                "repaired safely at a fair, transparent price."
            ),
            "image": "img/Professional Home appliances repair services.webp",
            "image_alt": "Best Fix technician repairing a microwave in Dubai",
        },
        "intro": [
            "Need quick microwave repair in Dubai? Best Fix Technical Services provides "
            "complete microwave diagnosis, repair and servicing across the city — often on "
            "the same day and always at a reasonable, clearly explained cost.",
            "Our technicians work on every major type and brand and begin each visit with a "
            "proper inspection, working safely around the high-voltage parts inside a "
            "microwave. Alongside microwaves we repair the full range of home appliances, so "
            "one trusted team can look after your whole home. Book now for a confirmed slot.",
        ],
        "types": {
            "h2": "Repair Support for All Microwave Types",
            "intro": "We service every microwave configuration found in UAE homes:",
            "list": [
                "Solo microwaves",
                "Grill microwaves",
                "Convection microwaves",
                "Built-in microwaves",
                "Over-the-range microwaves",
                "Countertop microwaves",
            ],
        },
        "services": {
            "h2": "Microwave Repair Services We Provide",
            "intro": "From a microwave that won't heat to one that's completely dead, we cover "
                     "the full range of faults:",
            "rows": [
                {"title": "Not-Heating Repair",
                 "text": "A microwave that runs but won't heat usually has a magnetron, diode "
                         "or high-voltage fault. We test the heating components safely and "
                         "advise on the best repair."},
                {"title": "Turntable Fault Repair",
                 "text": "A turntable that won't rotate often has a motor, coupler or roller "
                         "fault. We inspect and restore smooth rotation."},
                {"title": "Door & Latch Repair",
                 "text": "A microwave that won't start, or stops when the door is closed, may "
                         "have a door-switch or latch fault. We repair it for safe operation."},
                {"title": "Sparking & Arcing Repair",
                 "text": "Sparking inside the cavity can come from a damaged waveguide cover or "
                         "worn interior. We identify the cause and make it safe."},
                {"title": "Control Panel Repair",
                 "text": "Unresponsive buttons, a blank display or keypad faults are diagnosed "
                         "and repaired to restore full control."},
                {"title": "Noise Repair",
                 "text": "Loud humming or grinding can come from the motor, fan or turntable. "
                         "We trace the noise and correct it."},
                {"title": "Fuse & Power Fault Repair",
                 "text": "A microwave that's completely dead often has a blown fuse or a power "
                         "fault. We carry out safe fault-finding and repair."},
            ],
        },
        "problems": {
            "h2": "Common Microwave Problems We Fix",
            "intro": "These are the microwave faults we're called out for most:",
            "list": [
                "The microwave runs but does not heat the food.",
                "The turntable does not rotate during cooking.",
                "The microwave sparks or arcs inside the cavity.",
                "The buttons or display are unresponsive.",
                "The microwave is completely dead and won't switch on.",
                "The microwave makes loud humming or buzzing sounds while running.",
            ],
        },
        "band": {
            "title": "Skilled Microwave Repair Across Dubai",
            "text": "Book your service now for quick, affordable and professional microwave "
                    "repairs — with an honest diagnosis before any work begins.",
        },
        "why": {
            "h2": "Why Choose Best Fix for Microwave Repair",
            "image": "img/Appliance Repair Should Begin With Evidence, Not Guesswork.webp",
            "image_alt": "Best Fix technician repairing a microwave in Dubai",
            **_why("microwave",
                   "Best Fix is built around doorstep, quick and reliable appliance repair "
                   "in Dubai. Our technicians are highly experienced with microwaves and "
                   "always work safely around the high-voltage components inside."),
        },
        "brands": {
            "h2": "Microwave Brands We Repair",
            "intro": "We repair and service all major microwave brands in Dubai, with "
                     "same-day support wherever possible:",
            "logos": _BRAND_LOGOS,
        },
        "codes": None,
        "faq_h2": "Microwave Repair FAQs",
        "faqs": [
            {"q": "My microwave runs but doesn't heat. What's wrong?",
             "a": "A microwave that turns but won't heat usually has a magnetron, diode or "
                  "high-voltage fault. Because these involve high voltage, they should always "
                  "be inspected by a technician."},
            {"q": "Why is my microwave sparking inside?",
             "a": "Sparking is often caused by a damaged waveguide cover, worn interior paint "
                  "or metal in the cavity. Stop using it and have it checked to keep it safe."},
            {"q": "Why won't my microwave turn on at all?",
             "a": "A completely dead microwave often has a blown fuse or a power fault. We "
                  "carry out safe fault-finding to find and fix the cause."},
            {"q": "Is it safe to repair a microwave myself?",
             "a": "No. Microwaves store high voltage even when unplugged, so internal repairs "
                  "should always be left to a qualified technician."},
            {"q": "Why does my microwave stop partway through cooking?",
             "a": "This often points to a door-switch, thermal-cutout or control-board fault. "
                  "A technician can test the safety circuit and identify the cause."},
            {"q": "How soon can you come out?",
             "a": "We offer same-day appointments across Dubai wherever the schedule allows."},
        ],
        "tips": {
            "h2": "Maintenance Tips to Keep Your Microwave at Its Best",
            "intro": "A little routine care keeps a microwave running safely and efficiently:",
            "list": [
                "Keep the interior and waveguide cover clean to prevent sparking.",
                "Never run the microwave empty — it can damage the magnetron.",
                "Avoid metal or non-microwave-safe containers inside the cavity.",
                "Wipe the door seal and edges so the door closes and seals properly.",
                "Don't slam the door — the safety switches are delicate.",
                "Cover food to reduce splatter and keep the cavity clean.",
                "Keep the vents clear so the appliance doesn't overheat.",
                "Stop using it immediately if you see sparking or hear loud humming.",
                "Wipe up spills promptly so they don't bake onto the cavity.",
                "Book an inspection at the first sign of heating, door or power faults.",
            ],
        },
    },

    # ===================================================================== #
    # 6 · DRYER
    # ===================================================================== #
    "dryer-repair": {
        "parent_slug": "home-appliances-repair",
        "meta_title": "Dryer Repair in Dubai — Same-Day Service | Best Fix",
        "meta_description": (
            "Same-day dryer repair in Dubai by Best Fix. Not-heating, not-drying, "
            "no-tumble, overheating and sensor faults fixed for vented, condenser and "
            "heat-pump dryers of all brands at a fair price."
        ),
        "breadcrumb": "Dryer Repair",
        "hero": {
            "eyebrow": "Dryer Repair",
            "h1_accent": "Dryer Repair in Dubai",
            "h1": "Same-Day Diagnosis and Repair",
            "subheading": (
                "Vented, condenser and heat-pump dryers, every major brand — clothes coming "
                "out damp, dryers that won't heat or won't tumble, diagnosed and repaired."
            ),
            "image": "img/washing machine repair.jpg",
            "image_alt": "Best Fix technician repairing a clothes dryer in Dubai",
        },
        "intro": [
            "Looking for reliable dryer repair in Dubai? Best Fix Technical Services provides "
            "complete tumble-dryer diagnosis, repair and servicing across the city — often on "
            "the same day and always at a reasonable, clearly explained cost.",
            "Our technicians work on every major type and brand and start each visit with a "
            "proper inspection. Alongside dryers we repair the full range of home appliances, "
            "so one trusted team can look after your whole laundry and home. Book now for a "
            "confirmed slot.",
        ],
        "types": {
            "h2": "Repair Support for All Dryer Types",
            "intro": "We service every tumble-dryer configuration found in UAE homes and "
                     "apartments:",
            "list": [
                "Vented tumble dryers",
                "Condenser tumble dryers",
                "Heat-pump dryers",
                "Gas dryers",
                "Washer-dryer combination units",
                "Freestanding and stackable dryers",
            ],
        },
        "services": {
            "h2": "Dryer Repair Services We Provide",
            "intro": "From a dryer that won't heat to one that won't tumble, we cover the full "
                     "range of dryer faults:",
            "rows": [
                {"title": "Not-Heating Repair",
                 "text": "Clothes coming out cold and damp usually means a failed heating "
                         "element, thermostat or thermal fuse. We test the heating circuit and "
                         "replace the faulty part."},
                {"title": "Not-Drying / Long-Drying Repair",
                 "text": "A dryer that runs but takes hours often has a blocked vent, a clogged "
                         "filter or a weak element. We restore proper airflow and drying times."},
                {"title": "No-Tumble / Drum Repair",
                 "text": "A drum that won't turn usually points to a snapped belt, a seized "
                         "roller or a motor fault. We inspect the drive system and put it right."},
                {"title": "Overheating Repair",
                 "text": "A dryer that gets too hot or cuts out mid-cycle can be a thermostat, "
                         "airflow or sensor fault — and a safety risk. We diagnose and correct it."},
                {"title": "Noise & Vibration Repair",
                 "text": "Squealing, thumping or grinding usually comes from worn rollers, a "
                         "loose belt or failing bearings. We trace the noise and quieten it."},
                {"title": "Moisture-Sensor Repair",
                 "text": "Sensor dryers that stop too early or run too long often have a dirty "
                         "or faulty moisture sensor. We clean or replace it for accurate cycles."},
                {"title": "Vent & Airflow Repair",
                 "text": "Restricted venting is a common cause of poor drying and overheating. "
                         "We clear the ducting and filters and check airflow end to end."},
                {"title": "Door-Switch Repair",
                 "text": "A dryer that won't start or stops when the door is closed often has a "
                         "door-switch or latch fault. We inspect and replace the mechanism."},
                {"title": "Power & Control Fault Repair",
                 "text": "A dryer that won't switch on, or stops partway through, may have an "
                         "electrical or control-board fault. We carry out safe fault-finding."},
            ],
        },
        "problems": {
            "h2": "Common Dryer Problems We Fix",
            "intro": "These are the dryer faults we're called out for most across Dubai:",
            "list": [
                "The dryer runs but the clothes come out damp or cold.",
                "The drum does not tumble when the dryer is switched on.",
                "The dryer takes far too long to dry a normal load.",
                "The dryer overheats or shuts off partway through the cycle.",
                "The dryer makes loud squealing, thumping or grinding noises.",
                "The dryer will not start, or stops before the cycle finishes.",
            ],
        },
        "band": {
            "title": "Skilled Dryer Inspection and Repair Across Dubai",
            "text": "Book your service now for quick, affordable and professional dryer "
                    "repairs — with an honest diagnosis before any work begins.",
        },
        "why": {
            "h2": "Why Choose Best Fix for Dryer Repair",
            "image": "img/Same-Day Appliance Repair Without Empty Promises.webp",
            "image_alt": "Best Fix technician servicing a tumble dryer in Dubai",
            **_why("dryer",
                   "Best Fix is built around doorstep, quick and reliable appliance repair "
                   "in Dubai. Our technicians are highly experienced across vented, condenser "
                   "and heat-pump dryers of every major brand."),
        },
        "brands": {
            "h2": "Dryer Brands We Repair",
            "intro": "We repair and service all major dryer brands in Dubai, with same-day "
                     "support wherever possible:",
            "logos": _BRAND_LOGOS,
        },
        "codes": {
            "h2": "Common Error Codes in Smart Dryers We Fix",
            "intro": "Dryer error codes are a useful starting point, but they aren't a "
                     "complete diagnosis — the same code can mean slightly different things "
                     "depending on the brand and model. We check the model, symptoms and live "
                     "behaviour before recommending any repair.",
            "rows": [
                {"code": "tE, tO, tC", "meaning": "Temperature-sensor (thermistor) fault"},
                {"code": "HE, hot, E4", "meaning": "Heater or overheating fault"},
                {"code": "dE, dO, dC", "meaning": "Door-lock or door-switch error"},
                {"code": "dF, dC, F0", "meaning": "Airflow, duct or filter blockage"},
                {"code": "bE, E3, EL", "meaning": "Belt or motor fault"},
                {"code": "AE, CE, C8", "meaning": "Communication or control-board error"},
                {"code": "5C, 9C1, PS", "meaning": "Condenser or water-tank fault"},
            ],
        },
        "faq_h2": "Dryer Repair FAQs",
        "faqs": [
            {"q": "Why is my dryer not heating up?",
             "a": "A dryer that tumbles but won't heat usually has a failed heating element, "
                  "thermostat or thermal fuse. We test the heating circuit and replace the "
                  "faulty part."},
            {"q": "Why is my dryer taking so long to dry clothes?",
             "a": "Long drying times are often caused by a blocked vent, a clogged lint filter "
                  "or a weak heating element. Clearing the airflow and checking the element "
                  "usually restores normal drying."},
            {"q": "Why won't my dryer drum turn?",
             "a": "A drum that won't tumble usually has a snapped drive belt, a seized roller "
                  "or a motor fault. We inspect the drive system and carry out the repair."},
            {"q": "My dryer is getting too hot. Is that dangerous?",
             "a": "Overheating can be a fire risk and usually points to restricted airflow or "
                  "a faulty thermostat. Stop using it and book an inspection so it can be made "
                  "safe."},
            {"q": "Why does my dryer stop before the clothes are dry?",
             "a": "Sensor dryers can stop early if the moisture sensor is dirty or faulty, or "
                  "if a thermal cutout is tripping. We test the sensor and safety circuit."},
            {"q": "How soon can you repair my dryer?",
             "a": "We offer same-day appointments across Dubai wherever the schedule allows."},
        ],
        "tips": {
            "h2": "Maintenance Tips to Keep Your Dryer at Its Best",
            "intro": "A little routine care keeps a dryer drying efficiently and safely:",
            "list": [
                "Clean the lint filter before or after every load — this is the biggest cause of poor drying.",
                "Check and clear the vent ducting regularly so air can flow freely.",
                "Empty the water tank on condenser and heat-pump dryers after each cycle.",
                "Clean the condenser unit periodically as recommended for your model.",
                "Don't overload the drum — clothes need room to tumble and dry evenly.",
                "Avoid drying items with foam, rubber or plastic backing that can overheat.",
                "Wipe the door seal and moisture sensor to keep cycles accurate.",
                "Give the dryer space so it can pull in and release air properly.",
                "Stop using the dryer if it overheats, smells hot or won't stop tumbling.",
                "Book an inspection at the first sign of heating, tumbling or airflow faults.",
            ],
        },
    },

    # ===================================================================== #
    # 7 · SMALL APPLIANCES
    # ===================================================================== #
    "small-appliance-repair": {
        "parent_slug": "home-appliances-repair",
        "meta_title": "Small Appliance Repair in Dubai | Best Fix",
        "meta_description": (
            "Same-day small appliance repair in Dubai by Best Fix. Kettles, toasters, "
            "blenders, coffee machines, air fryers and more — heating, motor, power and "
            "switch faults fixed by experienced technicians at a fair price."
        ),
        "breadcrumb": "Small Appliance Repair",
        "hero": {
            "eyebrow": "Small Appliance Repair",
            "h1_accent": "Small Appliance Repair in Dubai",
            "h1": "Fast, Fair Repairs",
            "subheading": (
                "Kettles, toasters, blenders, coffee machines, air fryers and more — "
                "diagnosed properly and repaired where it's safe and worthwhile."
            ),
            "image": "img/small appliances repair.jpg",
            "image_alt": "Best Fix technician repairing small kitchen appliances in Dubai",
        },
        "intro": [
            "Looking for reliable small appliance repair in Dubai? Best Fix Technical "
            "Services repairs and services everyday small kitchen appliances across the city "
            "— often on the same day and always at a reasonable, clearly explained cost.",
            "Our technicians work on every major type and brand and always begin with a "
            "proper inspection, telling you honestly when a repair is worthwhile and when "
            "replacement makes more sense. Alongside small appliances we repair the full "
            "range of home appliances, so one trusted team can look after your whole home.",
        ],
        "types": {
            "h2": "Small Appliances We Repair",
            "intro": "We service a wide range of everyday small kitchen and home appliances:",
            "list": [
                "Kettles and toasters",
                "Blenders and food processors",
                "Coffee machines",
                "Air fryers",
                "Mixers and juicers",
                "Irons and garment steamers",
                "Rice cookers and slow cookers",
                "Sandwich makers and grills",
            ],
        },
        "services": {
            "h2": "Small Appliance Repair Services We Provide",
            "intro": "From an appliance that won't heat to one that won't power on, we cover "
                     "the full range of small-appliance faults:",
            "rows": [
                {"title": "Heating-Element Repair",
                 "text": "Kettles, toasters, irons and sandwich makers that won't heat usually "
                         "have a failed element or thermal cutout. We test and repair where it's "
                         "safe and cost-effective."},
                {"title": "Motor Repair",
                 "text": "Blenders, food processors, mixers and juicers that stall, hum or won't "
                         "spin often have a motor, gear or coupling fault. We inspect and repair "
                         "the drive."},
                {"title": "Power & Switch Repair",
                 "text": "An appliance that's completely dead often has a switch, fuse or "
                         "internal-connection fault. We carry out safe fault-finding and repair."},
                {"title": "Coffee-Machine Repair",
                 "text": "Weak flow, leaks, no pressure or a machine that won't heat usually "
                         "needs pump, seal or descaling work. We service and repair coffee "
                         "machines of most types."},
                {"title": "Air-Fryer Repair",
                 "text": "Air fryers that won't heat, won't switch on or run noisily often have "
                         "an element, fan or control fault. We diagnose and put them right."},
                {"title": "Thermostat & Overheat Repair",
                 "text": "Appliances that overheat, cut out or won't reach temperature usually "
                         "have a thermostat or thermal-cutout fault. We test and replace it."},
                {"title": "Blade & Attachment Repair",
                 "text": "Blenders, processors and mixers with damaged blades, seals or "
                         "attachments are repaired with the correct parts for safe use."},
                {"title": "Cord & Plug Repair",
                 "text": "A frayed cord, loose plug or intermittent connection is a common — and "
                         "unsafe — fault. We replace it and check the appliance is safe to use."},
            ],
        },
        "problems": {
            "h2": "Common Small Appliance Problems We Fix",
            "intro": "These are the small-appliance faults we're called out for most:",
            "list": [
                "A kettle, toaster or iron has stopped heating.",
                "A blender or food processor hums but the blade won't spin.",
                "A coffee machine leaks, won't pump or won't heat the water.",
                "An air fryer won't switch on or won't heat up.",
                "The appliance is completely dead and won't power on.",
                "An appliance trips the power or has a damaged cord or plug.",
            ],
        },
        "band": {
            "title": "Skilled Small Appliance Repair Across Dubai",
            "text": "Book your service now for quick, affordable and professional repairs — "
                    "with an honest diagnosis before any work begins.",
        },
        "why": {
            "h2": "Why Choose Best Fix for Small Appliance Repair",
            "image": "img/Appliance Repair for Homes and Managed Properties.webp",
            "image_alt": "Best Fix technician repairing a small kitchen appliance in Dubai",
            **_why("small appliance",
                   "Best Fix is built around doorstep, quick and reliable appliance repair "
                   "in Dubai. Our technicians are experienced across everyday small kitchen "
                   "appliances and will always tell you honestly when a repair is worthwhile."),
        },
        "brands": {
            "h2": "Small Appliance Brands We Repair",
            "intro": "We repair and service all major small-appliance brands in Dubai, with "
                     "same-day support wherever possible:",
            "logos": _BRAND_LOGOS,
        },
        "codes": None,
        "faq_h2": "Small Appliance Repair FAQs",
        "faqs": [
            {"q": "Is it worth repairing a small appliance?",
             "a": "It depends on the appliance, the fault and the cost of parts. We give an "
                  "honest assessment so you can decide between a cost-effective repair and "
                  "replacing the unit."},
            {"q": "My blender hums but the blade won't spin. What's wrong?",
             "a": "This usually points to a jammed or worn coupling, a gear fault or a motor "
                  "problem. We inspect the drive and repair or replace the affected part."},
            {"q": "Why has my kettle or toaster stopped heating?",
             "a": "A no-heat fault is normally a failed heating element or a tripped thermal "
                  "cutout. We test it and repair where it's safe and cost-effective."},
            {"q": "Can you fix my coffee machine?",
             "a": "Yes. We repair most coffee machines — weak flow, leaks, no pressure and "
                  "heating faults often need pump, seal or descaling work."},
            {"q": "The cord on my appliance is damaged. Can it be repaired?",
             "a": "Yes. A frayed cord or loose plug is unsafe and should not be used. We "
                  "replace it and confirm the appliance is safe before returning it."},
            {"q": "How soon can you come out?",
             "a": "We offer same-day appointments across Dubai wherever the schedule allows."},
        ],
        "tips": {
            "h2": "Maintenance Tips to Keep Your Small Appliances at Their Best",
            "intro": "A little care keeps small appliances working safely and lasting longer:",
            "list": [
                "Descale kettles and coffee machines regularly to prevent limescale build-up.",
                "Empty toaster crumb trays often to reduce fire risk and improve toasting.",
                "Let motors rest during heavy blending or processing to avoid overheating.",
                "Don't exceed the maximum fill line on kettles, blenders and coffee machines.",
                "Clean blades and attachments after each use and dry them fully.",
                "Keep cords away from heat and water, and never wrap them too tightly.",
                "Unplug appliances when not in use and before cleaning.",
                "Use the correct settings and never force jammed blades or attachments.",
                "Stop using any appliance with a damaged cord, plug or burning smell.",
                "Book an inspection at the first sign of heating, motor or power faults.",
            ],
        },
    },
}



# --------------------------------------------------------------------------- #
# Google-style reviews shown in the sidebar. Each sub-service has its own set
# of detailed, story-style, UAE-based testimonials (unique per appliance).
# --------------------------------------------------------------------------- #
GOOGLE_RATING = {"score": "4.9", "count": "100+"}

_REVIEWS = {
    "washing-machine-repair": [
        {"name": "Ayesha M.", "area": "Jumeirah Village Circle", "when": "3 weeks ago", "rating": 5,
         "text": "Our front-loader died mid-wash on a Friday with water and clothes locked "
                 "inside. I expected to wait all weekend, but a Best Fix technician arrived "
                 "within a few hours, found a blocked drain pump and had it running before "
                 "the evening. He even ran two test cycles to be sure. Genuinely impressed."},
        {"name": "Rohan D.", "area": "Dubai Marina", "when": "1 month ago", "rating": 5,
         "text": "The machine shook so badly on the spin cycle it moved across the laundry. "
                 "Two other places just told me to buy a new one. Best Fix opened it up, showed "
                 "me the worn drum bearings and replaced them the same afternoon for a fair "
                 "price. Six months on and it's still running quietly."},
        {"name": "Sara K.", "area": "Al Barsha", "when": "2 weeks ago", "rating": 5,
         "text": "Booked online at night and got a confirmed morning slot. The technician was "
                 "polite, wore shoe covers, and explained the door-lock fault before touching "
                 "anything. No upselling, a clear price and clean work. This is my go-to now."},
    ],
    "refrigerator-repair": [
        {"name": "Imran H.", "area": "Business Bay", "when": "2 weeks ago", "rating": 5,
         "text": "Woke up to a warm fridge and a freezer full of thawing food in peak summer. "
                 "Best Fix treated it as urgent and came the same morning. It was a faulty fan "
                 "plus a gas top-up; he had it cooling again within the hour and saved most of "
                 "our groceries. Lifesaver in this heat."},
        {"name": "Priya S.", "area": "The Greens", "when": "1 month ago", "rating": 5,
         "text": "Our double-door had been leaking water inside for weeks. The technician traced "
                 "it to a blocked defrost drain, cleared it properly and showed me how to keep "
                 "it clear myself. Honest diagnosis, no unnecessary parts and a very fair bill."},
        {"name": "Khalid A.", "area": "Mirdif", "when": "3 weeks ago", "rating": 5,
         "text": "My side-by-side kept tripping the power. He found the compressor start relay "
                 "had failed, replaced it and checked the whole circuit for safety before "
                 "leaving. Professional, on time and tidy — exactly what you hope for."},
    ],
    "oven-cooker-repair": [
        {"name": "Mariam T.", "area": "Jumeirah", "when": "2 weeks ago", "rating": 5,
         "text": "My built-in oven stopped heating right before a family dinner. Best Fix sent "
                 "someone the same evening, diagnosed a blown element and replaced it on the "
                 "spot. He even checked the temperature with his own thermometer before "
                 "leaving. Saved the whole night."},
        {"name": "Daniel R.", "area": "Dubai Marina", "when": "1 month ago", "rating": 5,
         "text": "My gas hob wouldn't light and I was nervous about the smell. The technician "
                 "handled it calmly, cleaned and replaced the igniter, and confirmed everything "
                 "was safe before signing off. Felt reassured the entire time."},
        {"name": "Noor F.", "area": "Al Warqa", "when": "3 weeks ago", "rating": 5,
         "text": "The oven was running far hotter than the dial and burning everything. He "
                 "recalibrated the thermostat, explained exactly what had drifted and why, and "
                 "charged a very reasonable amount. Baking is back to normal — highly recommend."},
    ],
    "dishwasher-repair": [
        {"name": "Hana Q.", "area": "Business Bay", "when": "2 weeks ago", "rating": 5,
         "text": "The dishwasher stopped draining and left a pool of water every cycle. Best Fix "
                 "came the next morning, cleared a blocked pump and filter, and had it working "
                 "perfectly. He also showed me how to clean the filter so it won't happen again."},
        {"name": "Yusuf A.", "area": "Jumeirah Lake Towers", "when": "1 month ago", "rating": 5,
         "text": "Dishes were coming out dirty no matter what I tried. The technician found "
                 "blocked spray arms and a worn inlet valve, sorted both in the same visit and "
                 "didn't push anything I didn't need. Fair, fast and friendly."},
        {"name": "Elena V.", "area": "Palm Jumeirah", "when": "3 weeks ago", "rating": 5,
         "text": "Water was leaking under the unit onto the kitchen floor. They responded "
                 "quickly, replaced the door seal and a cracked hose, and cleaned up after "
                 "themselves. Clear pricing and no mess — a very professional team."},
    ],
    "microwave-repair": [
        {"name": "Bilal S.", "area": "Deira", "when": "2 weeks ago", "rating": 5,
         "text": "The microwave was running but not heating anything. Instead of telling me to "
                 "bin it, the Best Fix technician tested it properly, safely replaced the faulty "
                 "part and now it works like new. Saved me buying a whole new one."},
        {"name": "Aisha R.", "area": "Silicon Oasis", "when": "1 month ago", "rating": 5,
         "text": "There was sparking inside every time I used it, which really scared me. He "
                 "identified a damaged waveguide cover, made it safe and explained what had "
                 "caused it. Quick, knowledgeable and very reassuring."},
        {"name": "Tom H.", "area": "International City", "when": "3 weeks ago", "rating": 5,
         "text": "My built-in microwave went completely dead. Booking was easy, the technician "
                 "arrived on time, found a blown fuse and a control fault, and had it back on in "
                 "the same visit. Tidy work at a fair price."},
    ],
    "dryer-repair": [
        {"name": "Layla H.", "area": "Arabian Ranches", "when": "2 weeks ago", "rating": 5,
         "text": "Our dryer was running full cycles but the clothes came out damp every time. "
                 "The Best Fix technician found a blocked vent and a weak heating element, sorted "
                 "both the same visit, and drying is back to twenty minutes. Really thorough."},
        {"name": "George M.", "area": "The Springs", "when": "1 month ago", "rating": 5,
         "text": "The drum stopped turning completely. He diagnosed a snapped belt within "
                 "minutes, had the part on his van and replaced it there and then. On time, "
                 "clean and a fair price — couldn't ask for more."},
        {"name": "Sana F.", "area": "Dubai Silicon Oasis", "when": "3 weeks ago", "rating": 5,
         "text": "My heat-pump dryer kept stopping mid-cycle and getting very hot. He explained "
                 "it was an airflow and sensor issue, cleaned it out properly and made it safe. "
                 "Reassuring to have someone who actually knew the machine."},
    ],
    "small-appliance-repair": [
        {"name": "Omar B.", "area": "Al Nahda", "when": "2 weeks ago", "rating": 5,
         "text": "My espresso machine had stopped pushing water through and was leaking at the "
                 "base. Best Fix serviced the pump, replaced a seal and descaled it — it's "
                 "pulling shots like new again. Honest advice and no pressure to replace it."},
        {"name": "Nadia K.", "area": "Jumeirah", "when": "1 month ago", "rating": 5,
         "text": "My blender just hummed and wouldn't spin. Rather than tell me to buy a new "
                 "one, the technician found a stripped coupling, replaced it cheaply and it works "
                 "perfectly. Genuinely appreciated the honesty."},
        {"name": "Ahmed R.", "area": "Mirdif", "when": "3 weeks ago", "rating": 5,
         "text": "The air fryer wouldn't heat and the kettle had died the same week. He looked "
                 "at both in one visit, fixed the fryer's element and replaced a faulty cord on "
                 "the kettle. Quick, friendly and very fair on price."},
    ],
}

for _slug, _revs in _REVIEWS.items():
    if _slug in SUBSERVICE_PAGES:
        SUBSERVICE_PAGES[_slug]["reviews"] = _revs
