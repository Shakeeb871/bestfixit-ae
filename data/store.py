"""Editable content store — a JSON overlay seeded from the base data modules.

The admin panel writes to this store and the public site reads from it, so
admin edits persist (to ``content_store.json``) and appear live immediately.
On first run the store is seeded from the existing ``data/*.py`` content, so
the site looks identical until something is edited.

Only list-structured, frequently-edited content lives here (blog posts &
categories, FAQs, testimonials, service areas). The larger structured page
content (service pages, AMC, etc.) still lives in code.
"""
from __future__ import annotations

import copy
import json
import os
import re
import threading
from datetime import datetime

_STORE_PATH = os.environ.get("CONTENT_STORE", "content_store.json")
_LOCK = threading.RLock()
_CACHE: dict | None = None


def _svg(inner: str) -> str:
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">'
            + inner + "</svg>")


# Icon options offered in the CMS icon picker (key -> full inline SVG).
ICON_SET = {
    "gear": _svg('<circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"></path>'),
    "bolt": _svg('<path d="M13 2 3 14h9l-1 8 10-12h-9z"></path>'),
    "droplet": _svg('<path d="M12 2.7 6.3 9a8 8 0 1 0 11.4 0z"></path>'),
    "wind": _svg('<path d="M9.6 4.6A2 2 0 1 1 11 8H2M12.6 19.4A2 2 0 1 0 14 16H2M17.7 7.8A2.5 2.5 0 1 1 19.5 12H2"></path>'),
    "brush": _svg('<rect x="3" y="3" width="15" height="6" rx="1"></rect><path d="M16 6h3a2 2 0 0 1 2 2v2a2 2 0 0 1-2 2h-7v3"></path><rect x="10" y="15" width="4" height="6" rx="1"></rect>'),
    "ruler": _svg('<path d="M3 17 17 3l4 4L7 21z"></path><path d="M7 9l2 2M11 5l2 2M15 13l2 2"></path>'),
    "home": _svg('<path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><path d="M9 22V12h6v10"></path>'),
    "wrench": _svg('<path d="M14.7 6.3a4 4 0 0 0-5.6 5.6L3 18l3 3 6.1-6.1a4 4 0 0 0 5.6-5.6l-2.9 2.9-2.6-.7-.7-2.6z"></path>'),
    "building": _svg('<rect x="4" y="2" width="16" height="20" rx="2"></rect><path d="M9 22v-4h6v4"></path><path d="M8 6h.01M12 6h.01M16 6h.01M8 10h.01M12 10h.01M16 10h.01"></path>'),
    "leaf": _svg('<path d="M11 20A7 7 0 0 1 4 13C4 7 11 4 20 4c0 9-3 16-9 16z"></path><path d="M4 20 12 12"></path>'),
    "pool": _svg('<path d="M2 6c.6.5 1.2 1 2.5 1C7 7 7 5 9.5 5c2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1"></path><path d="M2 12c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1"></path><path d="M2 18c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1"></path>'),
    "check": _svg('<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><path d="m9 11 3 3L22 4"></path>'),
}

_NAV_LABELS = {
    "home-appliances-repair": "Appliances", "electrical-services": "Electrical",
    "electromechanical-services": "Electro-Mech", "hvac-services": "HVAC",
    "plumbing-services": "Plumbing", "swimming-pool-services": "Pool",
    "painting-cleaning-services": "Painting", "false-ceiling-partition-services": "Ceilings",
    "renovation": "Renovation",
}
_ICON_KEYS = {
    "home-appliances-repair": "gear", "electrical-services": "bolt",
    "electromechanical-services": "gear", "hvac-services": "wind",
    "plumbing-services": "droplet", "swimming-pool-services": "pool",
    "painting-cleaning-services": "brush", "false-ceiling-partition-services": "ruler",
    "renovation": "home",
}


def _seed_services() -> list:
    from data.services import SERVICES
    out = []
    for i, s in enumerate(SERVICES):
        out.append({
            "slug": s["slug"], "num": s.get("num", ""), "title": s["title"],
            "nav_label": _NAV_LABELS.get(s["slug"], s["title"]),
            "icon": s["icon"],                       # keep original custom SVG
            "icon_key": _ICON_KEYS.get(s["slug"], "gear"),
            "short": s.get("short", ""), "description": s.get("description", ""),
            "points": list(s.get("points", [])),
            "enabled": True, "order": i, "custom": False,
        })
    return out


def _seed() -> dict:
    from data.blog import POSTS, CATEGORIES
    from data.faq import FAQS
    from data.testimonials import TESTIMONIAL_SHOWCASE
    from data.services import SERVICE_AREAS

    return {
        "blog_categories": copy.deepcopy(CATEGORIES),
        "blog_posts": copy.deepcopy(POSTS),
        "faqs": copy.deepcopy(FAQS),
        "testimonials": copy.deepcopy(TESTIMONIAL_SHOWCASE.get("items", [])),
        "areas": list(SERVICE_AREAS),
        "services": _seed_services(),
    }


def load() -> dict:
    global _CACHE
    with _LOCK:
        if _CACHE is None:
            data = None
            if os.path.exists(_STORE_PATH):
                try:
                    with open(_STORE_PATH, encoding="utf-8") as fh:
                        data = json.load(fh)
                except (OSError, ValueError):
                    data = None
            if data is None:
                data = _seed()
                _write(data)
            # backfill any missing top-level keys from the seed
            for k, v in _seed().items():
                data.setdefault(k, v)
            _CACHE = data
        return _CACHE


def _write(data: dict) -> None:
    tmp = _STORE_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
    os.replace(tmp, _STORE_PATH)


def save() -> None:
    with _LOCK:
        if _CACHE is not None:
            _write(_CACHE)


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def slugify(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-")
    return s or "item"


def unique_slug(base: str, existing: set) -> str:
    slug = base
    i = 2
    while slug in existing:
        slug = f"{base}-{i}"
        i += 1
    return slug


def _iso(date_str: str) -> str:
    for fmt in ("%d %B %Y", "%Y-%m-%d", "%d/%m/%Y"):
        try:
            return datetime.strptime(date_str, fmt).strftime("%Y-%m-%d")
        except (ValueError, TypeError):
            continue
    return ""


def _cat_slug_map() -> dict:
    return {c["name"]: c["slug"] for c in load()["blog_categories"]}


def normalize_post(p: dict) -> dict:
    cats = _cat_slug_map()
    p.setdefault("slug", slugify(p.get("title", "post")))
    p["category_slug"] = cats.get(p.get("category", ""), "")
    p["url"] = "/blog/" + p["slug"] + "/"
    p["iso_date"] = _iso(p.get("date", ""))
    p.setdefault("tags", p.get("category", ""))
    p.setdefault("image", "/static/img/hero-team.webp")
    p.setdefault("image_alt", p.get("title", ""))
    p.setdefault("excerpt", "")
    p.setdefault("sections", [])
    return p


# ---- blog views ----------------------------------------------------------- #
def blog_posts() -> list:
    return [normalize_post(p) for p in load()["blog_posts"]]


def blog_post(slug: str):
    for p in blog_posts():
        if p["slug"] == slug:
            return p
    return None


def blog_categories() -> list:
    return load()["blog_categories"]


def blog_categories_with_count() -> list:
    posts = blog_posts()
    return [
        {**c, "count": sum(1 for p in posts if p["category_slug"] == c["slug"])}
        for c in blog_categories()
    ]


def category_by_slug(slug: str):
    for c in blog_categories():
        if c["slug"] == slug:
            return c
    return None


def posts_in_category(cat_slug: str) -> list:
    return [p for p in blog_posts() if p["category_slug"] == cat_slug]


def recent_posts(n: int = 5) -> list:
    return blog_posts()[:n]


# ---- core services -------------------------------------------------------- #
def services_all() -> list:
    """All services (including disabled), sorted by their order field."""
    items = load().get("services", [])
    return sorted(items, key=lambda s: s.get("order", 0))


def services_public() -> list:
    """Enabled services only, in order — what the public site shows."""
    return [s for s in services_all() if s.get("enabled", True)]


def get_service(slug: str):
    for s in services_all():
        if s.get("slug") == slug:
            return s
    return None


def save_service(data: dict, orig_slug: str = "") -> str:
    """Create or update a service. Returns the (possibly new) slug."""
    with _LOCK:
        items = load().setdefault("services", [])
        existing = {s["slug"] for s in items if s["slug"] != orig_slug}
        base = slugify(data.get("slug") or data.get("title") or "service")
        current = None
        if orig_slug:
            current = next((s for s in items if s["slug"] == orig_slug), None)
        if current is None:
            slug = unique_slug(base, existing)
            order = (max((s.get("order", 0) for s in items), default=-1)) + 1
            rec = {"slug": slug, "custom": True, "order": order}
            items.append(rec)
        else:
            rec = current
            slug = current["slug"] if not current.get("custom") else unique_slug(base, existing)
        # apply editable fields
        rec["slug"] = slug
        rec["title"] = data.get("title", rec.get("title", ""))
        rec["nav_label"] = data.get("nav_label") or rec.get("title", "")
        rec["num"] = data.get("num", rec.get("num", ""))
        rec["icon_key"] = data.get("icon_key", rec.get("icon_key", "gear"))
        # custom services draw their icon from the picker; seeded ones keep custom SVG
        if rec.get("custom"):
            rec["icon"] = ICON_SET.get(rec["icon_key"], ICON_SET["gear"])
        rec["short"] = data.get("short", rec.get("short", ""))
        rec["description"] = data.get("description", rec.get("description", ""))
        if "points" in data:
            rec["points"] = data["points"]
        if "enabled" in data:
            rec["enabled"] = bool(data["enabled"])
        # page content for custom service detail pages
        if "page_intro" in data:
            rec["page_intro"] = data["page_intro"]
        if "page_features" in data:
            rec["page_features"] = data["page_features"]
        save()
        return slug


def delete_service(slug: str) -> bool:
    with _LOCK:
        items = load().get("services", [])
        svc = next((s for s in items if s["slug"] == slug), None)
        if not svc or not svc.get("custom"):
            return False  # only custom services can be deleted
        load()["services"] = [s for s in items if s["slug"] != slug]
        save()
        return True


def reorder_services(slugs: list) -> None:
    with _LOCK:
        order = {slug: i for i, slug in enumerate(slugs)}
        for s in load().get("services", []):
            if s["slug"] in order:
                s["order"] = order[s["slug"]]
        save()


# ---- generic list mutation ------------------------------------------------ #
def get_list(key: str) -> list:
    return load().get(key, [])


def replace_list(key: str, items: list) -> None:
    load()[key] = items
    save()
