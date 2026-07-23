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

# Common home-appliance brands we repair.
_BRANDS = [
    "Samsung", "LG", "Bosch", "Siemens", "Whirlpool", "Hoover",
    "Electrolux", "Haier", "Beko", "Panasonic", "Hitachi", "Miele",
    "Ariston", "Nikai", "Daewoo", "Nobel", "Super General", "Elekta",
    "Hisense", "Kenwood", "Toshiba", "Sharp",
]

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
        {"name": "Microwave & Small Appliance Repair", "slug": "microwave-repair"},
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
            "list": _BRANDS[:20],
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
            "list": _BRANDS,
        },
        "codes": None,
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
            "list": _BRANDS,
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
            "list": _BRANDS[:20],
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
    # 5 · MICROWAVE & SMALL APPLIANCES
    # ===================================================================== #
    "microwave-repair": {
        "parent_slug": "home-appliances-repair",
        "meta_title": "Microwave & Small Appliance Repair in Dubai | Best Fix",
        "meta_description": (
            "Same-day microwave and small-appliance repair in Dubai by Best Fix. "
            "Not-heating, turntable, door, sparking and control faults fixed for all "
            "brands by experienced technicians at a fair price."
        ),
        "breadcrumb": "Microwave & Small Appliance Repair",
        "hero": {
            "eyebrow": "Microwave Repair",
            "h1_accent": "Microwave & Small Appliance Repair in Dubai",
            "h1": "Fast, Same-Day Repairs",
            "subheading": (
                "Microwaves that won't heat, spark or respond — plus everyday small "
                "appliances — diagnosed properly and repaired at a fair price."
            ),
            "image": "img/small appliances repair.jpg",
            "image_alt": "Best Fix technician repairing a microwave in Dubai",
        },
        "intro": [
            "Need quick microwave repair in Dubai? Best Fix Technical Services provides "
            "complete microwave and small-appliance diagnosis, repair and servicing across "
            "the city — often on the same day and always at a reasonable, clearly explained "
            "cost.",
            "Our technicians work on every major type and brand and begin each visit with a "
            "proper inspection. Alongside microwaves we repair the full range of home "
            "appliances, so one trusted team can look after your whole home. Book now for "
            "quick help and a confirmed slot.",
        ],
        "types": {
            "h2": "Repair Support for All Microwave & Small-Appliance Types",
            "intro": "We service every microwave configuration, plus a wide range of small "
                     "kitchen appliances:",
            "list": [
                "Solo microwaves",
                "Grill microwaves",
                "Convection microwaves",
                "Built-in microwaves",
                "Kettles and toasters",
                "Blenders and food processors",
                "Coffee machines",
                "Other small kitchen appliances",
            ],
        },
        "services": {
            "h2": "Microwave & Small-Appliance Repair Services We Provide",
            "intro": "From a microwave that won't heat to a small appliance that won't power "
                     "on, we cover the full range of faults:",
            "rows": [
                {"title": "Not-Heating Repair",
                 "text": "A microwave that runs but won't heat usually has a magnetron, diode "
                         "or high-voltage fault. We test the heating components and advise on "
                         "the best repair."},
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
                 "text": "A microwave that's completely dead often has a blown fuse or power "
                         "fault. We carry out safe fault-finding and repair."},
                {"title": "Small-Appliance Repair",
                 "text": "Kettles, toasters, blenders, coffee machines and more — we repair "
                         "everyday small appliances where it's safe and cost-effective to do so."},
            ],
        },
        "problems": {
            "h2": "Common Microwave Problems We Fix",
            "intro": "These are the microwave and small-appliance faults we're called out "
                     "for most:",
            "list": [
                "The microwave runs but does not heat the food.",
                "The turntable does not rotate during cooking.",
                "The microwave sparks or arcs inside the cavity.",
                "The buttons or display are unresponsive.",
                "The microwave is completely dead and won't switch on.",
                "A small appliance has stopped working or is tripping the power.",
            ],
        },
        "band": {
            "title": "Skilled Microwave & Small-Appliance Repair Across Dubai",
            "text": "Book your service now for quick, affordable and professional repairs — "
                    "with an honest diagnosis before any work begins.",
        },
        "why": {
            "h2": "Why Choose Best Fix for Microwave Repair",
            "image": "img/Appliance Repair Should Begin With Evidence, Not Guesswork.webp",
            "image_alt": "Best Fix technician repairing a microwave in Dubai",
            **_why("microwave and small-appliance",
                   "Best Fix is built around doorstep, quick and reliable appliance repair "
                   "in Dubai. Our technicians are highly experienced across microwaves and "
                   "everyday small appliances, and always work safely around high-voltage parts."),
        },
        "brands": {
            "h2": "Microwave Brands We Repair",
            "intro": "We repair and service all major microwave brands in Dubai, with "
                     "same-day support wherever possible:",
            "list": _BRANDS[:20],
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
            {"q": "Do you repair small kitchen appliances too?",
             "a": "Yes. We repair kettles, toasters, blenders, coffee machines and other small "
                  "appliances where it's safe and cost-effective to do so."},
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
                "Unplug small appliances when not in use and keep them dry.",
                "Book an inspection at the first sign of heating, door or power faults.",
            ],
        },
    },
}
