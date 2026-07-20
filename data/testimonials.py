"""Testimonial / reviews configuration for the homepage.

Plain Python data (no database) driving the reviews section rendered by
``components/testimonial_showcase.html``: an intro column with a Google
rating badge on the left and a two-per-view review slider on the right.
"""

TESTIMONIAL_SHOWCASE = {
    "heading": "We have a reputation for being reliable, friendly and professional",
    "rating": "4.8",
    "rating_label": "Rated on Google",
    "reviews_url": "#bfc",
    "cta_label": "Read More Reviews",
    "cta_url": "#bfc",
    "items": [
        {
            "quote": (
                "Booked a plumber in the morning and it was fixed by afternoon. "
                "Clean, polite and fair pricing — they're my go-to team now for "
                "anything around the house."
            ),
            "name": "Aisha R.",
            "time": "2 weeks ago",
            "rating": 5,
        },
        {
            "quote": (
                "The AC deep clean made a real difference to the cooling. "
                "Professional team, arrived on schedule and left the whole place "
                "spotless. Highly recommended."
            ),
            "name": "James M.",
            "time": "a month ago",
            "rating": 5,
        },
        {
            "quote": (
                "Great handyman service — they mounted three TVs and fixed a "
                "wardrobe in a single visit. Tidy, careful and genuinely helpful "
                "from start to finish."
            ),
            "name": "Fatima K.",
            "time": "3 weeks ago",
            "rating": 5,
        },
    ],
}
