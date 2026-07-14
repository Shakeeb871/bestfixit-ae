"""Service catalogue for bestfixit.ae.

Single source of truth for services — used by the homepage "Our Services"
slider, the /services listing, each /services/<slug> detail page and the
header mega menu. Kept as plain Python data (no database). Each service has
a stable ``slug`` used in the URL and an inline ``icon`` (trusted SVG
rendered with ``|safe``).
"""

# ── reusable line icons (stroke = currentColor so the theme drives colour) ──
_IC_APPLIANCE = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">'
    '<rect x="4" y="2" width="16" height="20" rx="2"></rect>'
    '<path d="M4 7h16"></path><path d="M7 4.5h.01"></path>'
    '<circle cx="12" cy="14" r="4.5"></circle>'
    '<path d="M12 18a2.2 2.2 0 0 0 0-4.4"></path></svg>'
)
_IC_ELECTRIC = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">'
    '<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>'
)
_IC_GEAR = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">'
    '<circle cx="12" cy="12" r="3"></circle>'
    '<path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83'
    'l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 '
    '1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 '
    '0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51'
    '-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82'
    'l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 '
    '1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 '
    '1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 '
    '0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 '
    '0 0 0-1.51 1z"></path></svg>'
)
_IC_HVAC = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">'
    '<path d="M17.7 7.7a2.5 2.5 0 1 1 1.8 4.3H2"></path>'
    '<path d="M9.6 4.6A2 2 0 1 1 11 8H2"></path>'
    '<path d="M12.6 19.4A2 2 0 1 0 14 16H2"></path></svg>'
)
_IC_PLUMBING = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">'
    '<path d="M12 22a7 7 0 0 0 7-7c0-2-1-3.9-3-5.5s-3.5-4-4-6.5c-.5 2.5-2 '
    '4.9-4 6.5C6 11.1 5 13 5 15a7 7 0 0 0 7 7z"></path></svg>'
)
_IC_POOL = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">'
    '<path d="M2 6c.6.5 1.2 1 2.5 1C7 7 7 5 9.5 5c2.6 0 2.4 2 5 2 2.5 0 '
    '2.5-2 5-2 1.3 0 1.9.5 2.5 1"></path>'
    '<path d="M2 12c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 2.6 0 2.4 2 5 2 2.5 0 '
    '2.5-2 5-2 1.3 0 1.9.5 2.5 1"></path>'
    '<path d="M2 18c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 2.6 0 2.4 2 5 2 2.5 0 '
    '2.5-2 5-2 1.3 0 1.9.5 2.5 1"></path></svg>'
)
_IC_PAINT = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">'
    '<rect x="2" y="3" width="14" height="6" rx="1"></rect>'
    '<path d="M16 6h3a2 2 0 0 1 2 2v2a2 2 0 0 1-2 2h-7v3"></path>'
    '<rect x="10" y="15" width="4" height="6" rx="1"></rect></svg>'
)
_IC_CEILING = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">'
    '<rect x="3" y="3" width="18" height="18" rx="2"></rect>'
    '<path d="M3 9h18"></path><path d="M9 21V9"></path>'
    '<path d="M15 21V9"></path></svg>'
)

SERVICES = [
    {
        "slug": "home-appliances-repair",
        "num": "01",
        "title": "Home Appliances Repair",
        "icon": _IC_APPLIANCE,
        "short": "Repairs for washing machines, fridges, ovens and more.",
        "description": (
            "Fast, reliable repairs for all your major home appliances by "
            "trained technicians. We diagnose the real fault and fix it right "
            "— with genuine parts and a workmanship guarantee."
        ),
        "points": [
            "Washing Machines",
            "Refrigerators & Freezers",
            "Ovens & Cookers",
            "Dishwashers",
            "Small Appliances",
        ],
    },
    {
        "slug": "electrical-services",
        "num": "02",
        "title": "Electrical Services",
        "icon": _IC_ELECTRIC,
        "short": "Wiring, sockets, lighting, DB boards and fault-finding.",
        "description": (
            "Safe, DEWA-standard electrical fittings, fixtures and maintenance "
            "for homes and businesses. From a flickering light to a full "
            "rewire, our certified electricians work to code."
        ),
        "points": [
            "Wiring & Rewiring",
            "Sockets & Switches",
            "Lighting Installation",
            "DB Board & MCB Repair",
            "Fault Finding & Safety Checks",
        ],
    },
    {
        "slug": "electromechanical-services",
        "num": "03",
        "title": "Electromechanical Services",
        "icon": _IC_GEAR,
        "short": "Installation and maintenance of electromechanical plant.",
        "description": (
            "Installation and preventive maintenance of electromechanical "
            "equipment and building systems — motors, pumps, control panels "
            "and generators kept running reliably."
        ),
        "points": [
            "Motors & Pumps",
            "Control Panels",
            "Generators",
            "Preventive Maintenance",
            "System Upgrades",
        ],
    },
    {
        "slug": "hvac-services",
        "num": "04",
        "title": "HVAC Services",
        "icon": _IC_HVAC,
        "short": "AC installation, servicing, duct cleaning and repairs.",
        "description": (
            "Complete air-conditioning, ventilation and air-filtration "
            "services. We install, service and deep-clean split, window and "
            "ducted systems to keep your space cool and healthy."
        ),
        "points": [
            "AC Installation",
            "AC Servicing & Repair",
            "Duct Cleaning",
            "Gas Refill & Top-up",
            "Ventilation Systems",
        ],
    },
    {
        "slug": "plumbing-services",
        "num": "05",
        "title": "Plumbing Services",
        "icon": _IC_PLUMBING,
        "short": "Leaks, drainage, water heaters and sanitary fittings.",
        "description": (
            "Complete plumbing and sanitary installation, repairs and "
            "maintenance you can rely on — from a dripping tap to a full "
            "bathroom fit-out, done fast and clean."
        ),
        "points": [
            "Leak Detection & Repair",
            "Drain Unblocking",
            "Water Heater Install",
            "Sanitary Ware Fitting",
            "Pipe & Drainage Works",
        ],
    },
    {
        "slug": "swimming-pool-services",
        "num": "06",
        "title": "Swimming Pool Services",
        "icon": _IC_POOL,
        "short": "Pool cleaning, water treatment and equipment care.",
        "description": (
            "Year-round swimming pool cleaning, water treatment and equipment "
            "maintenance to keep your pool crystal clear and safe all season."
        ),
        "points": [
            "Pool Cleaning",
            "Pump & Filter Service",
            "Water Treatment",
            "Tiling & Repairs",
            "Equipment Installation",
        ],
    },
    {
        "slug": "painting-cleaning-services",
        "num": "07",
        "title": "Painting & Cleaning Services",
        "icon": _IC_PAINT,
        "short": "Interior & exterior painting and deep cleaning.",
        "description": (
            "Professional painting and building cleaning services for a "
            "spotless, fresh finish — interior and exterior painting, facade "
            "and deep cleaning by a tidy, reliable team."
        ),
        "points": [
            "Interior Painting",
            "Exterior Painting",
            "Deep Cleaning",
            "Facade Cleaning",
            "Post-construction Cleaning",
        ],
    },
    {
        "slug": "false-ceiling-partition-services",
        "num": "08",
        "title": "False Ceiling & Partition Services",
        "icon": _IC_CEILING,
        "short": "Gypsum ceilings, partitions and drywall works.",
        "description": (
            "False ceilings and light partitions designed and installed to a "
            "high standard — gypsum ceilings, glass and drywall partitions and "
            "acoustic solutions."
        ),
        "points": [
            "Gypsum Ceilings",
            "Glass Partitions",
            "Drywall Works",
            "Acoustic Panels",
            "Light Partitions",
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
