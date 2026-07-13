"""Call-to-action banner configuration for the homepage.

Plain Python config so the banner's copy, links and background image are
all data-driven — nothing is hardcoded in the template. Consumed by
``components/cta_banner.html`` via the context processor.
"""

CTA_BANNER = {
    "badge": "Feel Free",
    "eyebrow": "To Contact Us",
    "title": "Get Premium Handyman Service From Us!",
    "primary_label": "Get Our Service",
    "primary_url": "#services",
    "secondary_label": "Contact Us",
    "secondary_url": "#bfc",
    "background": "/static/img/hero-team.webp",
}
