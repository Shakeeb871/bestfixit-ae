"""Counter / stats configuration for the homepage.

Plain Python data driving the counters rendered by
``components/stats_counter.html``. Each item counts up on scroll and shows
a tinted icon, the number and a label inside a card. Icons are trusted
inline SVG (rendered with ``|safe``); stroke uses ``currentColor`` so the
per-card theme colour drives them.
"""

_IC_WRENCH = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
    'stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 '
    '1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 '
    '0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path></svg>'
)
_IC_HOME = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
    'stroke-linecap="round" stroke-linejoin="round"><path d="M3 9.5 12 3l9 6.5"></path>'
    '<path d="M5 10v10a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V10"></path>'
    '<path d="M9.5 21v-5a1 1 0 0 1 1-1h3a1 1 0 0 1 1 1v5"></path></svg>'
)
_IC_HELMET = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
    'stroke-linecap="round" stroke-linejoin="round"><path d="M2 18h20"></path>'
    '<path d="M20 18a8 8 0 0 0-16 0"></path>'
    '<path d="M10 7V4.2A1.2 1.2 0 0 1 11.2 3h1.6A1.2 1.2 0 0 1 14 4.2V7"></path>'
    '<path d="M7.5 8.6A6 6 0 0 1 16.5 8.6"></path></svg>'
)
_IC_PIN = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
    'stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6'
    '-8-12a8 8 0 0 1 16 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>'
)

STATS = [
    {"number": 6500, "suffix": "+", "label": "Jobs Completed", "icon": _IC_WRENCH},
    {"number": 2500, "suffix": "+", "label": "Happy Customers", "icon": _IC_HOME},
    {"number": 40, "suffix": "+", "label": "Expert Technicians", "icon": _IC_HELMET},
    {"number": 120, "suffix": "+", "label": "Areas Covered", "icon": _IC_PIN},
]
