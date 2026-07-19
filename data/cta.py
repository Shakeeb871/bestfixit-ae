"""Call-to-action banner configuration for the homepage.

Plain Python config so the banner's copy, links and background image are
all data-driven — nothing is hardcoded in the template. Consumed by
``components/cta_banner.html`` via the context processor.
"""

CTA_BANNER = {
    "badge": "Feel Free",
    "eyebrow": "To Contact Us",
    "title": "Service You Can Trust!",
    "subtext": "Let us know how we can help you today.",
    "primary_label": "Easy Online Booking",
    "primary_url": "/contact",
    "secondary_label": "Contact Us",
    "secondary_url": "#bfc",
    "background": "/static/img/cta-banner-bg.webp",
}
