"""Homepage "Our Services" cards.

Drives the hover-fill service cards rendered in the ``.svc2`` slider in
``index.html``. Each card shows an icon, a decorative number, a title and
a short description at rest; on hover / tap / focus a coloured layer
slides down, the icon collapses and the service ``items`` list is
revealed. Content here is plain data so titles, descriptions and
sub-services can be edited without touching the template.

``icon`` holds trusted, hand-authored inline SVG markup rendered with
``|safe`` in the template.
"""

# Reusable line-icon SVGs (stroke = currentColor so the theme drives colour).
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
_IC_AC = (
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

HOME_SERVICES = [
    {
        "num": "01",
        "title": "Appliance Repairing",
        "desc": "Fast, reliable repairs for all your major home appliances, "
                "handled by trained technicians.",
        "url": "#contact",
        "icon": _IC_APPLIANCE,
        "items": [
            "Washing Machines",
            "Refrigerators",
            "Ovens & Cookers",
            "Dishwashers",
        ],
    },
    {
        "num": "02",
        "title": "Electrical Fittings & Fixtures Repairing & Maintenance",
        "desc": "Safe, DEWA-standard electrical fittings, fixtures and "
                "ongoing maintenance for your property.",
        "url": "#contact",
        "icon": _IC_ELECTRIC,
        "items": [
            "Wiring & Rewiring",
            "Sockets & Switches",
            "Lighting Fixtures",
            "DB Boards & MCBs",
        ],
    },
    {
        "num": "03",
        "title": "Electromechanical Equipment Installation & Maintenance",
        "desc": "Installation and preventive maintenance of electromechanical "
                "plant and equipment.",
        "url": "#contact",
        "icon": _IC_GEAR,
        "items": [
            "Motors & Pumps",
            "Control Panels",
            "Generators",
            "Preventive Maintenance",
        ],
    },
    {
        "num": "04",
        "title": "Air-Conditioning, Ventilation & Air Filtration Systems",
        "desc": "Cooling, ventilation and air-filtration systems installed "
                "and maintained for cleaner air.",
        "url": "#contact",
        "icon": _IC_AC,
        "items": [
            "AC Installation",
            "Duct Cleaning",
            "Ventilation Systems",
            "Air Filtration",
        ],
    },
    {
        "num": "05",
        "title": "Plumbing & Sanitary Installation",
        "desc": "Complete plumbing and sanitary installation, repairs and "
                "maintenance you can rely on.",
        "url": "#contact",
        "icon": _IC_PLUMBING,
        "items": [
            "Sanitary Ware Fitting",
            "Pipe & Drainage",
            "Water Heaters",
            "Leak Detection & Repair",
        ],
    },
    {
        "num": "06",
        "title": "Swimming Pools Maintenance",
        "desc": "Year-round swimming pool cleaning, water treatment and "
                "equipment maintenance.",
        "url": "#contact",
        "icon": _IC_POOL,
        "items": [
            "Pool Cleaning",
            "Pump & Filter Service",
            "Water Treatment",
            "Tiling & Repairs",
        ],
    },
    {
        "num": "07",
        "title": "Painting Contracting & Building Cleaning Services",
        "desc": "Professional painting and building cleaning services for a "
                "spotless, fresh finish.",
        "url": "#contact",
        "icon": _IC_PAINT,
        "items": [
            "Interior Painting",
            "Exterior Painting",
            "Deep Cleaning",
            "Facade Cleaning",
        ],
    },
    {
        "num": "08",
        "title": "False Ceiling & Light Partitions Installation",
        "desc": "False ceilings and light partitions designed and installed "
                "to a high standard.",
        "url": "#contact",
        "icon": _IC_CEILING,
        "items": [
            "Gypsum Ceilings",
            "Glass Partitions",
            "Drywall Works",
            "Acoustic Panels",
        ],
    },
]
