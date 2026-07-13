"""Homepage "Our Services" cards.

Drives the three hover-fill service cards rendered inline in
``index.html`` (the ``.svc2`` section). Each card shows an icon, a
decorative number, a title and a short description at rest; on hover /
tap / focus a coloured layer slides down, the icon collapses and the
service ``items`` list is revealed. Content here is intentionally plain
data so titles, descriptions and sub-services can be edited without
touching the template.

``icon`` holds trusted, hand-authored inline SVG markup and is rendered
with ``|safe`` in the template.
"""

HOME_SERVICES = [
    {
        "num": "01",
        "title": "AC & HVAC",
        "desc": "Installation, servicing and deep-cleaning to keep your "
                "home cool and efficient through every Dubai summer.",
        "url": "#contact",
        "icon": (
            '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">'
            '<path d="M17.7 7.7a2.5 2.5 0 1 1 1.8 4.3H2"></path>'
            '<path d="M9.6 4.6A2 2 0 1 1 11 8H2"></path>'
            '<path d="M12.6 19.4A2 2 0 1 0 14 16H2"></path></svg>'
        ),
        "items": [
            "AC Installation",
            "AC Servicing & Repair",
            "Duct Cleaning",
            "Gas Refill & Top-up",
        ],
    },
    {
        "num": "02",
        "title": "Plumbing",
        "desc": "Leaks, blockages, water heaters and fittings — fixed fast "
                "and clean by licensed plumbers you can trust.",
        "url": "#contact",
        "icon": (
            '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">'
            '<path d="M12 22a7 7 0 0 0 7-7c0-2-1-3.9-3-5.5s-3.5-4-4-6.5c-.5 '
            '2.5-2 4.9-4 6.5C6 11.1 5 13 5 15a7 7 0 0 0 7 7z"></path></svg>'
        ),
        "items": [
            "Leak Detection & Repair",
            "Water Heater Install",
            "Drain Unblocking",
            "Tap & Mixer Fitting",
        ],
    },
    {
        "num": "03",
        "title": "Electrical",
        "desc": "Wiring, sockets, lighting and DB boards to UAE safety "
                "standards — done right the first time, every time.",
        "url": "#contact",
        "icon": (
            '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">'
            '<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2">'
            '</polygon></svg>'
        ),
        "items": [
            "Wiring & Rewiring",
            "Socket & Switch Fitting",
            "Lighting Installation",
            "DB Board & MCB Repair",
        ],
    },
]
