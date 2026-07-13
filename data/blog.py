"""Blog landing section configuration for the homepage.

Plain Python data (no database) driving the blog section rendered by
``components/blog_section.html``: a featured article on the left and three
compact related entries on the right, plus the intro + CTA banner.

NOTE: images reuse the team photo as placeholders — drop real blog images
into static/img/ and update each ``image`` path.
"""

BLOG = {
    "label": "Blog",
    "title_lead": "Learn more from",
    "title_accent": "blog",
    "intro": (
        "We handle every job around the house — from AC servicing to "
        "plumbing and electrical. Licensed Dubai technicians are on the "
        "road near you, ready to help."
    ),
    "cta_message": "Require commercial building maintenance and/or installation services?",
    "cta_button_label": "Contact us!",
    "cta_button_url": "#bfc",

    "featured": {
        "image": "/static/img/hero-team.webp",
        "image_alt": "Technician using pressure gauges on an air-conditioning system",
        "title": "Employee Productivity And Air Conditioning",
        "tags": "Air Conditioner, Plumbing",
        "comments": 1,
        "excerpt": (
            "Providing an environment to support maximum employee "
            "productivity is a goal for most businesses. Ventilation of the "
            "workspace is vital, as uncomfortable temperatures can cause..."
        ),
        "url": "#",
    },

    "related": [
        {
            "image": "/static/img/hero-team.webp",
            "image_alt": "Technician handling air-conditioning pressure gauges",
            "title": "Employee Productivity And Air Conditioning",
            "excerpt": (
                "Providing an environment to support maximum employee "
                "productivity is a goal for most businesses. Ventilation of..."
            ),
            "url": "#",
        },
        {
            "image": "/static/img/hero-team.webp",
            "image_alt": "Technician servicing an indoor split air-conditioning unit",
            "title": "Our systems are designed to suit any domestic purposes...",
            "excerpt": (
                "Providing an environment to support maximum employee "
                "productivity is a goal for most businesses. Ventilation of..."
            ),
            "url": "#",
        },
        {
            "image": "/static/img/hero-team.webp",
            "image_alt": "Technician repairing an outdoor air-conditioning condenser",
            "title": "We offer Air Conditioning solutions for Residential.",
            "excerpt": (
                "Providing an environment to support maximum employee "
                "productivity is a goal for most businesses. Ventilation of..."
            ),
            "url": "#",
        },
    ],

    "foot_link_label": "Read more",
    "foot_text": "new blogs from blog page.",
    "foot_url": "#",
}
