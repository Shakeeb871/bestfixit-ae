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


# ---- generic list mutation ------------------------------------------------ #
def get_list(key: str) -> list:
    return load().get(key, [])


def replace_list(key: str, items: list) -> None:
    load()[key] = items
    save()
