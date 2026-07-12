"""Service catalogue for bestfixit.ae.

Kept as plain Python data so the site has no database dependency for its
marketing pages. Each service has a stable ``slug`` used in the URL.
"""

SERVICES = [
    {
        "slug": "plumbing",
        "title": "Plumbing",
        "icon": "faucet",
        "short": "Leaks, blockages, water heaters, tap and mixer fittings.",
        "description": (
            "From a dripping tap to a full re-pipe, our licensed plumbers "
            "handle it fast and clean. We fix leaks, unblock drains, install "
            "and repair water heaters, and sort out low-pressure problems."
        ),
        "points": [
            "Leak detection & repair",
            "Blocked drains & toilets",
            "Water heater install & repair",
            "Tap, mixer & shower fitting",
            "Water tank cleaning",
        ],
    },
    {
        "slug": "electrical",
        "title": "Electrical",
        "icon": "bolt",
        "short": "Wiring, sockets, lighting, DB boards and safety checks.",
        "description": (
            "Certified electricians for everything from a flickering light to "
            "a full circuit upgrade. We work to UAE wiring standards so your "
            "home stays safe and compliant."
        ),
        "points": [
            "Socket & switch replacement",
            "Light fitting & chandelier install",
            "Wiring & rewiring",
            "DB board & MCB repair",
            "Fault finding & safety checks",
        ],
    },
    {
        "slug": "ac-maintenance",
        "title": "AC Maintenance",
        "icon": "snowflake",
        "short": "Servicing, gas top-up, deep cleaning and repairs.",
        "description": (
            "Keep cool through the UAE summer. We service split, window and "
            "ducted units, top up refrigerant, deep-clean coils and fix "
            "cooling faults before they get expensive."
        ),
        "points": [
            "Full AC servicing",
            "Gas / refrigerant top-up",
            "Coil & filter deep clean",
            "Cooling fault repair",
            "Annual maintenance contracts",
        ],
    },
    {
        "slug": "carpentry",
        "title": "Carpentry",
        "icon": "hammer",
        "short": "Doors, cabinets, wardrobes and custom wood work.",
        "description": (
            "Skilled carpenters for repairs and custom builds. We hang and "
            "align doors, fix cabinets and wardrobes, assemble furniture and "
            "craft made-to-measure joinery."
        ),
        "points": [
            "Door repair & alignment",
            "Cabinet & wardrobe fixing",
            "Furniture assembly",
            "Custom shelving & joinery",
            "Lock & hinge replacement",
        ],
    },
    {
        "slug": "painting",
        "title": "Painting",
        "icon": "roller",
        "short": "Interior and exterior painting with a clean finish.",
        "description": (
            "A fresh coat, done right. Our painters prep surfaces properly, "
            "protect your furniture and leave a smooth, even finish with no "
            "mess left behind."
        ),
        "points": [
            "Interior wall painting",
            "Exterior & villa painting",
            "Crack filling & prep",
            "Wood & metal painting",
            "Waterproof coatings",
        ],
    },
    {
        "slug": "handyman",
        "title": "General Handyman",
        "icon": "toolbox",
        "short": "Odd jobs, mounting, fixing and small home repairs.",
        "description": (
            "The go-to for every small job on your list. Mounting TVs and "
            "shelves, fixing fittings, patching walls — one call, one skilled "
            "handyman, no job too small."
        ),
        "points": [
            "TV & shelf mounting",
            "Curtain & blind fitting",
            "Wall patching & fixing",
            "Furniture & fixture repair",
            "General odd jobs",
        ],
    },
    {
        "slug": "masonry-tiling",
        "title": "Masonry & Tiling",
        "icon": "trowel",
        "short": "Tiling, grouting, plaster and small build works.",
        "description": (
            "Clean tiling and solid masonry work. We lay and re-grout tiles, "
            "repair cracked plaster and handle small build and finishing jobs "
            "around the home."
        ),
        "points": [
            "Floor & wall tiling",
            "Grout repair & sealing",
            "Plaster & POP repair",
            "Small brick & block work",
            "Bathroom & kitchen finishing",
        ],
    },
    {
        "slug": "appliance-repair",
        "title": "Appliance Repair",
        "icon": "washer",
        "short": "Washing machines, fridges, ovens and dishwashers.",
        "description": (
            "Don't replace it — repair it. Our technicians diagnose and fix "
            "major home appliances, source genuine parts and get things "
            "running again the same day where possible."
        ),
        "points": [
            "Washing machine repair",
            "Fridge & freezer repair",
            "Oven & cooker repair",
            "Dishwasher repair",
            "Genuine spare parts",
        ],
    },
]

# Fast slug -> service lookup.
SERVICE_BY_SLUG = {s["slug"]: s for s in SERVICES}

SERVICE_AREAS = [
    "Dubai",
    "Abu Dhabi",
    "Sharjah",
    "Ajman",
    "Ras Al Khaimah",
]

TESTIMONIALS = [
    {
        "name": "Aisha R.",
        "area": "Dubai Marina",
        "text": "Booked a plumber in the morning, fixed by afternoon. Clean, "
                "polite and fair pricing. My go-to now.",
        "rating": 5,
    },
    {
        "name": "James M.",
        "area": "Jumeirah",
        "text": "The AC deep clean made a real difference. Professional team "
                "and they left the place spotless.",
        "rating": 5,
    },
    {
        "name": "Fatima K.",
        "area": "Abu Dhabi",
        "text": "Great handyman service. Mounted three TVs and fixed a "
                "wardrobe in one visit. Highly recommend.",
        "rating": 5,
    },
]
