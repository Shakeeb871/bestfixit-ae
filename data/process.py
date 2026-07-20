"""'Working process' step data for the homepage.

Plain Python data (no database) driving the "Easy Quick Following Steps"
section. Each step maps to a card in ``components/process_steps.html``.
``icon`` is a key into the allow-list of inline SVGs defined in that
template — never raw markup, so nothing here is rendered unescaped.
"""

# Small, configurable header copy for the section.
PROCESS_EYEBROW_PRIMARY = "Our Working Process"
PROCESS_EYEBROW_SECONDARY = ""
PROCESS_TITLE = "Four steps. One trusted team."
PROCESS_DESC = (
    "Every job — from a dripping tap to a full fit-out — runs through the "
    "same tidy, honest process."
)

PROCESS_STEPS = [
    {
        "number": "01",
        "title": "Register For Work",
        "description": (
            "Tell us what needs fixing by phone, WhatsApp or the form — "
            "we log your request in minutes."
        ),
        "icon": "clipboard",
    },
    {
        "number": "02",
        "title": "Inspect & Analyze",
        "description": (
            "A licensed technician assesses the job on site and gives you "
            "a clear, upfront quote."
        ),
        "icon": "search",
    },
    {
        "number": "03",
        "title": "Work Processing",
        "description": (
            "We carry out the repair or maintenance with the right tools "
            "and genuine parts, on schedule."
        ),
        "icon": "gear",
    },
    {
        "number": "04",
        "title": "Handover",
        "description": (
            "We test everything, tidy up, and hand back a job done right "
            "the first time — guaranteed."
        ),
        "icon": "package",
    },
]
