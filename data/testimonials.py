"""Testimonial-showcase configuration for the homepage.

Plain Python data (no database) driving the dark testimonial slider
rendered by ``components/testimonial_showcase.html``. The two left stat
circles are static; only ``items`` are cycled by the slider. Each item's
``image`` is a portrait shown on the right, synced to its text.

NOTE: portraits currently reuse the team photo as a placeholder — drop
real customer photos into static/img/ and update each ``image`` path.
"""

TESTIMONIAL_SHOWCASE = {
    "eyebrow_badge": "Our Customers",
    "eyebrow_text": "Testimonial",
    "stats": [
        {
            "number": "200+",
            "title": "Handyman Solution",
            "text": "Trusted repairs across every trade, delivered on time.",
        },
        {
            "number": "12k+",
            "title": "Happy Customers",
            "text": "Homes and offices served across the UAE since 2012.",
        },
    ],
    "items": [
        {
            "headline": "Highest Rated Company",
            "quote": (
                "Booked a plumber in the morning and it was fixed by "
                "afternoon. Clean, polite and fair pricing — they're my "
                "go-to team now for anything around the house."
            ),
            "name": "Aisha R.",
            "role": "Home Repair Client · Dubai Marina",
            "rating": "5.0/5",
            "image": "/static/img/hero-team.webp",
            "review_url": "#bfc",
        },
        {
            "headline": "Fast & Reliable Service",
            "quote": (
                "The AC deep clean made a real difference to the cooling. "
                "Professional team, arrived on schedule and left the whole "
                "place spotless. Highly recommended."
            ),
            "name": "James M.",
            "role": "AC Service Client · Jumeirah",
            "rating": "5.0/5",
            "image": "/static/img/hero-team.webp",
            "review_url": "#bfc",
        },
        {
            "headline": "Spotless & Professional",
            "quote": (
                "Great handyman service — they mounted three TVs and fixed "
                "a wardrobe in a single visit. Tidy, careful and genuinely "
                "helpful from start to finish."
            ),
            "name": "Fatima K.",
            "role": "Handyman Client · Abu Dhabi",
            "rating": "5.0/5",
            "image": "/static/img/hero-team.webp",
            "review_url": "#bfc",
        },
    ],
}
