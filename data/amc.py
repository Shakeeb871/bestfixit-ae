"""Annual Maintenance Contract (AMC) content.

Drives the /amc/ page and the homepage "Maintenance Plans" section. Prices are
intentionally left as a call-to-action ("Request a Quote") until real figures
are supplied.
"""

AMC_META = {
    "title": "Annual Maintenance Contracts (AMC) in Dubai | Best Fix",
    "description": (
        "Annual Maintenance Contracts (AMC) in Dubai by Best Fix — Basic, "
        "Standard and Premium plans covering preventive maintenance, priority "
        "support and emergency call-outs for homes and businesses across the UAE."
    ),
}

AMC_HERO = {
    "trustline": "Preventive Maintenance · Priority Support · One Contract",
    "h1_accent": "Annual Maintenance Contracts in Dubai",
    "h1": "Planned Care, Fewer Breakdowns",
    "subheading": (
        "Simple annual plans that keep your home or business running — regular "
        "preventive maintenance, priority support and faster response times."
    ),
    "paras": [
        "An Annual Maintenance Contract (AMC) replaces surprise breakdowns and "
        "one-off repair bills with planned, scheduled care. Instead of calling "
        "around when something fails, one team already knows your property and "
        "keeps it maintained.",
        "Best Fix offers AMC plans across all Emirates for HVAC, electrical, "
        "plumbing, appliances and general maintenance — with preventive visits, "
        "priority support and clear, predictable coverage.",
    ],
    "note": "Coverage across all Emirates · Working hours 8:00 AM – 8:00 PM with emergency support.",
    "image": "img/best fix it mainetnance fixerman.webp",
    "image_alt": "Best Fix maintenance technician in Dubai",
    "cta_label": "Request a Quote",
}

# Curated plan cards (the middle plan is highlighted as most popular).
AMC_PLANS = [
    {
        "slug": "basic",
        "name": "Basic AMC",
        "tagline": "Essential preventive care",
        "popular": False,
        "visits": "2 visits / year",
        "response": "48-hour response",
        "features": [
            "2 preventive maintenance visits",
            "Inspection & diagnostics",
            "Cleaning & servicing",
            "Minor repairs included",
            "Labour charges included",
            "Annual performance report",
            "Service reminders",
        ],
        "cta": "Get Basic AMC",
    },
    {
        "slug": "standard",
        "name": "Standard AMC",
        "tagline": "Balanced cover for busy homes",
        "popular": True,
        "visits": "4 visits / year",
        "response": "24-hour response",
        "features": [
            "Everything in Basic",
            "4 preventive maintenance visits",
            "Emergency breakdown support",
            "Priority support",
            "24/7 customer support",
            "Optional spare parts",
            "Quarterly performance report",
        ],
        "cta": "Get Standard AMC",
    },
    {
        "slug": "premium",
        "name": "Premium AMC",
        "tagline": "Complete, monthly peace of mind",
        "popular": False,
        "visits": "12 visits / year (monthly)",
        "response": "Same-day response",
        "features": [
            "Everything in Standard",
            "12 monthly maintenance visits",
            "Same-day emergency response",
            "Unlimited emergency call-outs",
            "Spare parts included (as per contract)",
            "Monthly performance report",
        ],
        "cta": "Get Premium AMC",
    },
]

# Full feature matrix. "yes" -> green tick, "no" -> muted cross, else literal text.
AMC_COMPARISON = {
    "h2": "Compare AMC Plans",
    "intro": "A full breakdown of what each plan covers so you can pick the right level of care.",
    "cols": ["Basic AMC", "Standard AMC", "Premium AMC"],
    "rows": [
        {"feature": "Number of annual visits", "basic": "2", "standard": "4", "premium": "12 (Monthly)"},
        {"feature": "Preventive maintenance", "basic": "yes", "standard": "yes", "premium": "yes"},
        {"feature": "Emergency breakdown support", "basic": "no", "standard": "yes", "premium": "yes"},
        {"feature": "Response time", "basic": "48 Hours", "standard": "24 Hours", "premium": "Same Day"},
        {"feature": "Priority support", "basic": "no", "standard": "yes", "premium": "yes"},
        {"feature": "Inspection & diagnostics", "basic": "yes", "standard": "yes", "premium": "yes"},
        {"feature": "Cleaning & servicing", "basic": "yes", "standard": "yes", "premium": "yes"},
        {"feature": "Minor repairs", "basic": "yes", "standard": "yes", "premium": "yes"},
        {"feature": "Spare parts included", "basic": "no", "standard": "Optional", "premium": "As per contract"},
        {"feature": "Labour charges included", "basic": "yes", "standard": "yes", "premium": "yes"},
        {"feature": "Emergency call-outs", "basic": "Chargeable", "standard": "Limited", "premium": "Unlimited"},
        {"feature": "24/7 customer support", "basic": "no", "standard": "yes", "premium": "yes"},
        {"feature": "Performance report", "basic": "Annual", "standard": "Quarterly", "premium": "Monthly"},
        {"feature": "Service reminder", "basic": "yes", "standard": "yes", "premium": "yes"},
        {"feature": "Contract duration", "basic": "12 Months", "standard": "12 Months", "premium": "12 Months"},
    ],
}

AMC_BENEFITS = {
    "h2": "Why Take an AMC",
    "intro": "A maintenance contract turns unpredictable repair costs into planned, reliable care.",
    "rows": [
        {"icon": "shield", "title": "Prevents Breakdowns", "text": "Scheduled servicing catches faults before they turn into failures."},
        {"icon": "clock", "title": "Faster Response", "text": "Priority scheduling and quicker call-outs when you need help."},
        {"icon": "tag", "title": "Lower Repair Costs", "text": "Preventive care reduces expensive emergency repairs over the year."},
        {"icon": "leaf", "title": "Longer Equipment Life", "text": "Regular maintenance extends the lifespan of your equipment."},
        {"icon": "gear", "title": "Better Efficiency", "text": "Well-maintained systems run more efficiently and cost less to run."},
        {"icon": "users", "title": "Priority Support", "text": "AMC customers come first for technical support and call-outs."},
        {"icon": "check", "title": "Scheduled Servicing", "text": "Planned visits keep everything in good working order year-round."},
        {"icon": "home", "title": "Peace of Mind", "text": "Reliable, scheduled care so you never have to chase a repair."},
    ],
}

AMC_DETAILS = {
    "h2": "What's Included",
    "info": [
        {"label": "Contract Duration", "value": "12 Months"},
        {"label": "Coverage Area", "value": "All Emirates across the UAE"},
        {"label": "Working Hours", "value": "8:00 AM – 8:00 PM · emergency support available"},
        {"label": "Payment Terms", "value": "Annual or quarterly (optional)"},
    ],
    "includes_title": "Service Includes",
    "includes": [
        "Inspection", "Preventive maintenance", "Cleaning",
        "Troubleshooting", "Minor repairs", "Technical support",
    ],
    "excludes_title": "Exclusions",
    "excludes": [
        "Major spare parts",
        "Equipment replacement",
        "Damage caused by misuse or natural disasters (unless otherwise agreed)",
    ],
}

AMC_FAQ = {
    "h2": "AMC FAQs",
    "faqs": [
        {"q": "What is an Annual Maintenance Contract?", "a": "An AMC is a yearly agreement for scheduled preventive maintenance and support. Instead of paying per breakdown, you get planned visits, priority response and predictable coverage for a fixed contract."},
        {"q": "What does an AMC cover?", "a": "Every plan covers inspection, preventive maintenance, cleaning, troubleshooting, minor repairs and technical support. Higher tiers add emergency breakdown support, faster response and spare parts."},
        {"q": "Which services can be put under an AMC?", "a": "HVAC, electrical, plumbing, appliances, refrigeration and general maintenance can all be covered — for homes, offices, retail units and managed properties."},
        {"q": "How fast is the response time?", "a": "It depends on the plan: 48 hours on Basic, 24 hours on Standard and same-day on Premium, with priority support on Standard and Premium."},
        {"q": "Do you cover all of the UAE?", "a": "Yes. AMC coverage is available across all Emirates, with working hours from 8:00 AM to 8:00 PM and emergency support available."},
        {"q": "Can I pay quarterly?", "a": "Yes. Contracts run for 12 months and can be paid annually or quarterly, whichever suits you."},
    ],
}
