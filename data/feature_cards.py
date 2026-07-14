"""Homepage feature cards (the curved-top "Repair / Residential / Maintenance"
cards). Server-rendered from this Python data by
``components/feature_cards.html`` — so the content, colours and card shape
are managed in one place instead of being hardcoded in the template.

``icon`` is trusted inline SVG (stroke = currentColor; the colour comes from
``icon_color``). ``bg`` is the card background, ``circle_bg`` the icon circle.
"""

FEATURE_CARDS = [
    {
        "title": "Repair Services",
        "text": "Fast, reliable repairs across plumbing, electrical and "
                "appliances — our licensed technicians diagnose the real "
                "problem and fix it properly the first time.",
        "bg": "#1c2836",
        "circle_bg": "#ffffff",
        "icon_color": "#024d87",
        "icon": (
            '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'
            '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77'
            '-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91'
            '-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path></svg>'
        ),
    },
    {
        "title": "Residential Services",
        "text": "Complete home maintenance for villas and apartments — from "
                "AC servicing and plumbing to painting, carpentry and full "
                "fit-outs by one trusted team.",
        "bg": "#2c74c0",
        "circle_bg": "#024d87",
        "icon_color": "#ffffff",
        "icon": (
            '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'
            '<path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>'
            '<polyline points="9 22 9 12 15 12 15 22"></polyline></svg>'
        ),
    },
    {
        "title": "Maintenance & Installations",
        "text": "Scheduled upkeep and new installations done to code — genuine "
                "parts, tidy work, clear pricing and a full twelve-month "
                "warranty on every job.",
        "bg": "#1c2836",
        "circle_bg": "#ffffff",
        "icon_color": "#024d87",
        "icon": (
            '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'
            '<circle cx="12" cy="12" r="3"></circle>'
            '<path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 '
            '2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a'
            '2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33'
            'l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 '
            '1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a'
            '1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 '
            '1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a'
            '1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 '
            '2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 '
            '1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>'
        ),
    },
]
