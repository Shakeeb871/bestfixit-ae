"""Appliance sub-service pages (two-column layout).

These sit *under* the core ``home-appliances-repair`` service and share a
dedicated two-column template (``subservice_detail.html``): long-form,
well-structured content on the left; internal links, a booking form and
customer testimonials in a sticky sidebar on the right.

``SUBSERVICE_PAGES`` is keyed by slug and is checked first inside the
``/services/<slug>/`` route, so a sub-service page keeps the clean
``/services/<slug>/`` URL shape used everywhere else on the site.
"""

# --------------------------------------------------------------------------- #
# Sidebar: sibling appliance repair services (internal linking).
# The current page is highlighted; the others cross-link to the parent
# core-service page until they have dedicated pages of their own.
# --------------------------------------------------------------------------- #
APPLIANCE_PARENT = {
    "name": "Home Appliances Repair",
    "href": "/services/home-appliances-repair/",
}

APPLIANCE_SERVICES = [
    {"name": "Washing Machine Repair", "href": "/services/washing-machine-repair/"},
    {"name": "Refrigerator & Freezer Repair", "href": "/services/home-appliances-repair/"},
    {"name": "Oven, Cooker & Hob Repair", "href": "/services/home-appliances-repair/"},
    {"name": "Dishwasher Repair", "href": "/services/home-appliances-repair/"},
    {"name": "Microwave & Small Appliance Repair", "href": "/services/home-appliances-repair/"},
]

# Short, appliance-specific reviews for the sidebar.
SUBSERVICE_TESTIMONIALS = [
    {
        "name": "Maryam S.",
        "area": "Dubai Marina",
        "text": "My front-loader stopped draining on a Saturday. Best Fix came the same "
                "afternoon, found a blocked pump and had it running before dinner.",
        "rating": 5,
    },
    {
        "name": "Imran K.",
        "area": "Business Bay",
        "text": "Loud banging on every spin. The technician diagnosed worn drum bearings, "
                "quoted honestly and finished the repair cleanly. Fair price.",
        "rating": 5,
    },
    {
        "name": "Rita P.",
        "area": "Jumeirah Village Circle",
        "text": "Machine kept flashing a door-lock error and wouldn't start. Fixed in one "
                "visit and explained exactly what had failed. Highly recommend.",
        "rating": 5,
    },
]


SUBSERVICE_PAGES = {
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
                {
                    "title": "Drainage Repair",
                    "text": "Water left standing in the drum after a wash cycle usually points "
                            "to a blocked filter, a kinked drain hose or a failing pump. We "
                            "trace the blockage and restore proper drainage.",
                },
                {
                    "title": "Spin-Cycle Repair",
                    "text": "Clothes coming out soaking wet, or a drum that won't spin up, often "
                            "means a worn belt, a motor fault or an unbalanced load. We inspect "
                            "the spin system and put it right.",
                },
                {
                    "title": "Water Leakage Repair",
                    "text": "Water escaping from the door, a hose or the base of the machine can "
                            "quickly damage flooring. We check seals, inlet pipes and internal "
                            "leak points and reseal or replace as needed.",
                },
                {
                    "title": "Drum Repair",
                    "text": "A drum that wobbles, runs loose or makes unusual sounds needs a "
                            "proper technical inspection. We handle drum, bearing and spider-arm "
                            "faults across all brands.",
                },
                {
                    "title": "Door-Lock Repair",
                    "text": "A machine that won't start or won't complete its cycle is often a "
                            "door-lock issue. We inspect door switches, latches and the locking "
                            "mechanism and replace faulty parts.",
                },
                {
                    "title": "Noise & Vibration Repair",
                    "text": "Loud banging, grinding or heavy vibration during a wash usually comes "
                            "from worn bearings, a drum imbalance or loose internal parts. We "
                            "locate the source and quieten the machine.",
                },
                {
                    "title": "Power & Electrical Fault Repair",
                    "text": "A machine that won't switch on, or stops partway through a cycle, may "
                            "have an electrical, control-board or switch fault. We carry out safe, "
                            "methodical fault-finding.",
                },
                {
                    "title": "Water-Inlet Repair",
                    "text": "A machine that won't fill, or fills too slowly, often has an inlet "
                            "valve, hose or water-flow problem. We identify the cause and carry "
                            "out the correct repair.",
                },
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
            "paras": [
                "Best Fix is built around doorstep, quick and reliable appliance repair "
                "in Dubai. Our technicians are highly experienced, with years of hands-on "
                "work across washing machines and every other major home appliance.",
                "We are a team of professionals who inspect, diagnose and fix your washing "
                "machine correctly the first time — so a small fault doesn't turn into a "
                "repeat call-out or a bigger repair later on.",
                "Most importantly, we come to your location whenever you need us and offer "
                "same-day appointments wherever the schedule allows. You get a clear "
                "diagnosis, a fair price and tidy work at your doorstep.",
            ],
            "areas_intro": "We provide fast washing machine repair across Dubai, including:",
            "areas": [
                "JLT", "Al Barsha", "Palm Jumeirah", "Downtown", "Emirates Hills",
                "Jumeirah", "Bur Dubai", "The Greens", "Jebel Ali", "IMPZ",
                "Sports City", "Motor City", "Al Barari", "Arabian Ranches",
                "Dubai Marina", "Deira", "Satwa", "Karama", "Business Bay",
                "Garhoud", "Nad Al Sheba", "Nad Al Hamar", "Al Warqa",
                "International City", "Silicon Oasis", "JVC", "JBR",
            ],
        },
        "brands": {
            "h2": "Washing Machine Brands We Repair",
            "intro": "We provide repair and servicing for all major washing machine brands "
                     "in Dubai, with same-day support wherever possible:",
            "list": [
                "Samsung", "LG", "Bosch", "Siemens", "Whirlpool", "Hoover",
                "Electrolux", "Haier", "Beko", "Panasonic", "Hitachi", "Miele",
                "Ariston", "Nikai", "Daewoo", "Nobel", "Super General", "Elekta",
                "Hisense", "Kenwood",
            ],
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
            {
                "q": "My washing machine is not draining water properly. What could be wrong?",
                "a": "A machine that stops draining usually has a blocked filter, a clogged "
                     "drain hose or a faulty drain pump. A technical inspection identifies the "
                     "exact cause and restores normal drainage.",
            },
            {
                "q": "Why is my washing machine not spinning properly?",
                "a": "Spin-cycle problems often come from a damaged drive belt, a motor fault, "
                     "an unbalanced drum or a control issue. When the machine can't spin "
                     "correctly, clothes are left very wet at the end of the cycle.",
            },
            {
                "q": "Why is my washing machine leaking water?",
                "a": "Leaks can come from a damaged door seal, a loose hose, a faulty inlet "
                     "connection or an internal component. Early inspection helps limit any "
                     "water damage around the laundry area.",
            },
            {
                "q": "Why is my washing machine making a loud noise?",
                "a": "Banging, grinding or vibrating sounds can point to a drum imbalance, worn "
                     "bearings, loose components or an item trapped inside the machine. The "
                     "appliance should be checked once the noise becomes frequent.",
            },
            {
                "q": "Why is my washing machine not turning on?",
                "a": "A machine may fail to start because of a power issue, a door-lock fault, "
                     "a damaged switch or a control-panel problem. A technician can inspect the "
                     "electrical and operating parts to find the cause.",
            },
            {
                "q": "Why is my washing machine not cleaning clothes properly?",
                "a": "Poor washing results can come from low water intake, detergent build-up, "
                     "blocked filters, drum-movement faults or an incorrect cycle. An inspection "
                     "pinpoints the part affecting wash quality.",
            },
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
}
