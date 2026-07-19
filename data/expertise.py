"""'Service expertise' section configuration for the homepage.

Plain Python config (no database) for the image-and-content expertise
block rendered by ``components/service_expertise.html``. Every string,
image path and link is data-driven — nothing is hardcoded in the
template. ``features[].icon`` is a key into the template's allow-list of
inline SVGs, never raw markup.

A single team photo is shown (``main_image``).
"""

SERVICE_EXPERTISE = {
    "eyebrow_badge": "Quality Handyman",
    "eyebrow_text": "Solution",
    "title_lead": "Responsive, Reliable Maintenance Help",
    "title_highlight": "When You Need It Most",
    "description": (
        "What we really deliver is peace of mind. As a local Dubai team you "
        "can count on, we pair fast, dependable service with honest, upfront "
        "pricing — no hidden charges and no surprises when the bill arrives. "
        "It is the punctuality, care and skilled workmanship behind every "
        "visit that keep our customers coming back and recommending us right "
        "across the emirate."
    ),
    "main_image": "/static/img/professional-maintenance-team.webp",
    "main_image_alt": "Our professional Best Fix maintenance team in Dubai",
    "features": [
        {"label": "Licensed Dubai technicians", "icon": "check"},
        {"label": "Genuine parts & materials", "icon": "check"},
        {"label": "Honest, upfront pricing", "icon": "check"},
        {"label": "Two-year workmanship guarantee", "icon": "check"},
    ],
    "cta_label": "Read More",
    "cta_url": "#services",
    "phone_label": "Call Us For Service",
    "phone_display": "+971 54 739 3716",
    "phone_tel": "+971547393716",
}
