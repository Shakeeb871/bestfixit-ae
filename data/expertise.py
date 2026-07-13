"""'Service expertise' section configuration for the homepage.

Plain Python config (no database) for the image-and-content expertise
block rendered by ``components/service_expertise.html``. Every string,
image path and link is data-driven — nothing is hardcoded in the
template. ``features[].icon`` is a key into the template's allow-list of
inline SVGs, never raw markup.

NOTE: ``secondary_image`` currently reuses the main team photo as a
placeholder. Drop a second photo into static/img/ (e.g.
img/expertise-detail.webp) and point ``secondary_image`` at it.
"""

SERVICE_EXPERTISE = {
    "eyebrow_badge": "Quality Handyman",
    "eyebrow_text": "Solution",
    "title_lead": "We are Expert in All",
    "title_highlight": "Handyman Solutions",
    "description": (
        "From fixing leaks and faulty wiring to AC servicing and full home "
        "maintenance, our licensed Dubai technicians handle every job with "
        "the right tools and genuine care — done right the first time."
    ),
    "main_image": "/static/img/hero-team.webp",
    "main_image_alt": "Best Fix technicians on a home service call",
    "secondary_image": "/static/img/hero-team.webp",
    "secondary_image_alt": "Technician repairing an appliance",
    "features": [
        {"label": "Reliable Repairs", "icon": "check"},
        {"label": "Quickly Repair", "icon": "check"},
        {"label": "Absolute Works", "icon": "check"},
        {"label": "Standard Work", "icon": "check"},
    ],
    "cta_label": "Read More",
    "cta_url": "#services",
    "phone_label": "Call Us For Service",
    "phone_display": "+971 54 739 3716",
    "phone_tel": "+971547393716",
}
