"""Counter / stats configuration for the homepage.

Plain Python data driving the animated counters rendered by
``components/stats_counter.html``. Each item counts up on scroll and has a
circle behind the number that slides right and changes colour on hover.
"""

STATS = [
    {"number": 980, "suffix": "+", "label": "Successful Services"},
    {"number": 900, "suffix": "+", "label": "Satisfied Clients"},
    {"number": 250, "suffix": "+", "label": "Expert Technicians"},
    {"number": 120, "suffix": "+", "label": "Areas Covered"},
]
