"""'Here For You' promise cards for the homepage.

Plain Python data (no database) driving the four promise/benefit cards
rendered by ``components/why_choose.html``, shown just below the service
expertise section. ``icon`` is a key into the template's allow-list of
inline SVGs — never raw markup.
"""

WHY_CHOOSE = {
    "eyebrow": "Why Best Fix",
    "title_lead": "Here For You",
    "title_highlight": "When You Need Us Most",
    "intro": (
        "From an early-morning breakdown to a planned upgrade, our Dubai "
        "team turns up ready, works cleanly and treats your home with care "
        "— here is what you can count on with every single visit."
    ),
    "cards": [
        {
            "icon": "clock",
            "image": "Round the Clock Availability.png",
            "title": "Round-the-Clock Availability",
            "text": (
                "Whatever goes wrong and whenever it happens, our team is "
                "ready to step in — day or night — so an unexpected "
                "breakdown never leaves you waiting."
            ),
        },
        {
            "icon": "shield",
            "image": "Workmanship Guarantee.png",
            "title": "Two-Year Workmanship Guarantee",
            "text": (
                "We stand behind our parts, labour and craftsmanship for a "
                "full two years from the date of your service, so the job "
                "stays done."
            ),
        },
        {
            "icon": "tag",
            "image": "Clear, Upfront Pricing.png",
            "title": "Clear, Upfront Pricing",
            "text": (
                "Before any work starts, we talk you through your options "
                "and the exact cost — so you know precisely what you are "
                "getting, with no hidden fees."
            ),
        },
        {
            "icon": "calendar",
            "image": "On Time, or It's On Us.png",
            "title": "On Time, or It's On Us",
            "text": (
                "Your time matters. We arrive within the appointment window "
                "you choose — and if we are ever late, that call-out is on "
                "us."
            ),
        },
    ],
}
