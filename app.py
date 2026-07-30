"""bestfixit.ae — Flask application entry point.

A lightweight, database-free marketing site for a UAE home-maintenance
company. Pages are server-rendered with Jinja2; the contact form saves
enquiries to a JSONL file and (optionally) emails them.

Run locally:
    pip install -r requirements.txt
    python app.py
Then open http://127.0.0.1:5000
"""
from __future__ import annotations

import json
import os
import re
import smtplib
from datetime import datetime, timezone
from email.message import EmailMessage

from functools import wraps

from flask import (
    Flask,
    Response,
    abort,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

try:  # load a local .env if python-dotenv is installed
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

from config import Config
from data.blog import BLOG
from data import store
from data.cta import CTA_BANNER
from data.expertise import SERVICE_EXPERTISE
from data.process import (
    PROCESS_DESC,
    PROCESS_EYEBROW_PRIMARY,
    PROCESS_EYEBROW_SECONDARY,
    PROCESS_STEPS,
    PROCESS_TITLE,
)
from data.testimonials import TESTIMONIAL_SHOWCASE
from data.feature_cards import FEATURE_CARDS
from data.why_choose import WHY_CHOOSE
from data.services import (
    SERVICE_AREAS,
    SERVICE_BY_SLUG,
    SERVICES,
    TESTIMONIALS,
)
from data.stats import STATS
from data.faq import FAQS
from data.service_pages import SERVICE_PAGES
from data.amc import (
    AMC_META,
    AMC_HERO,
    AMC_PLANS,
    AMC_COMPARISON,
    AMC_BENEFITS,
    AMC_DETAILS,
    AMC_FAQ,
)
from data.subservice_pages import (
    APPLIANCE_PARENT,
    APPLIANCE_SERVICES,
    GOOGLE_RATING,
    SERVICE_SUBLINKS,
    SUBSERVICE_PAGES,
    SUBSERVICE_TESTIMONIALS,
)

app = Flask(__name__)
app.config.from_object(Config)
# Re-read templates on every request so a git pull shows template changes
# without needing a full app restart (cPanel/Passenger keeps the process alive).
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.jinja_env.auto_reload = True

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

# Map every service page slug (core, sub-service and level-3) back to its core
# service, so the top-level nav item highlights on the core page and any of its
# child pages.
_SLUG_TO_CORE = {}
for _s in SERVICES:
    _SLUG_TO_CORE[_s["slug"]] = _s["slug"]
for _core_slug, _items in SERVICE_SUBLINKS.items():
    for _it in _items:
        _SLUG_TO_CORE[_it["slug"]] = _core_slug
        for _c in _it.get("children", []):
            _SLUG_TO_CORE[_c["slug"]] = _core_slug


def _active_core() -> str:
    """Top-level service slug to highlight in the nav for the current path.

    Uses the static core→sub→level-3 map, and falls back to any custom
    (CMS-created) service whose slug matches the current /services/<slug>/ URL.
    """
    if not request.path.startswith("/services/"):
        return ""
    slug = request.path[len("/services/"):].strip("/")
    if not slug:
        return ""
    core = _SLUG_TO_CORE.get(slug)
    if core:
        return core
    # custom service pages have no sub-links; the slug is its own core.
    if store.get_service(slug):
        return slug
    return ""


def _custom_service_page(svc: dict) -> dict:
    """Build a service_detail-compatible ``page`` dict for a CMS service.

    Custom services created in the admin don't have a hand-authored rich page
    module, so we synthesise a clean banner-hero + feature-grid layout from the
    fields the editor filled in (title, description, intro, feature cards,
    highlight points).
    """
    title = svc.get("title", "Service")
    paras = [p for p in (svc.get("description", ""), svc.get("page_intro", "")) if p]
    features = svc.get("page_features") or [
        {"title": p, "text": ""} for p in svc.get("points", [])
    ]
    _desc = (svc.get("short") or svc.get("description")
             or f"Professional {title.lower()} in Dubai by Best Fix.")
    page = {
        "layout": "grid",
        "breadcrumb": title,
        "meta_title": f"{title} in Dubai | Best Fix Technical Services",
        "meta_description": _desc,
        "faqs": [],
        "hero": {
            "image": "img/best fix it mainetnance fixerman.webp",
            "image_alt": f"{title} — Best Fix Dubai",
            "trustline": "Licensed Dubai Maintenance Company",
            "h1_accent": title,
            "h1": "in Dubai",
            "subheading": svc.get("short", ""),
            "paras": paras or [svc.get("short", "")],
            "note": "Same-day response across Dubai · Transparent pricing",
            "cta_label": "Book a Service",
        },
    }
    if features:
        page["why"] = {
            "h2": f"Why choose Best Fix for {title.lower()}",
            "intro": svc.get("short", ""),
            "rows": [
                {"icon": f.get("icon", svc.get("icon_key", "check")),
                 "title": f.get("title", ""), "text": f.get("text", "")}
                for f in features
            ],
        }
    return page


def _service_badges() -> set:
    """Slugs that have a slider badge PNG (static/img/service-<slug>.png).

    The homepage "Our Services" slider uses these PNG badges; a service
    without one (e.g. renovation) falls back to its inline SVG icon.
    """
    badges = set()
    try:
        img_dir = os.path.join(app.static_folder, "img")
        for s in SERVICES:
            if os.path.exists(os.path.join(img_dir, f"service-{s['slug']}.png")):
                badges.add(s["slug"])
    except OSError:
        pass
    return badges


_SERVICE_BADGES = _service_badges()


def _css_version() -> str:
    """Cache-busting token for site.css — its last-modified time.

    Appended as ``?v=…`` to the stylesheet URL so browsers always fetch the
    latest CSS after a deploy instead of serving a stale cached copy (which
    makes new markup look "broken" until a hard refresh).
    """
    try:
        path = os.path.join(app.static_folder, "css", "site.css")
        return str(int(os.path.getmtime(path)))
    except OSError:
        return "1"


# --------------------------------------------------------------------------- #
# Template context — brand details available in every template.
# --------------------------------------------------------------------------- #
@app.context_processor
def inject_globals():
    _posts = store.blog_posts()
    _blog = {**BLOG,
             "featured": _posts[0] if _posts else None,
             "related": _posts[1:4]}
    _testi = {**TESTIMONIAL_SHOWCASE, "items": store.get_list("testimonials")}
    return {
        "site_name": app.config["SITE_NAME"],
        "site_domain": app.config["SITE_DOMAIN"],
        "contact_phone": app.config["CONTACT_PHONE"],
        "whatsapp_number": app.config["WHATSAPP_NUMBER"],
        "contact_email": app.config["CONTACT_EMAIL"],
        "service_areas": store.get_list("areas"),
        "all_services": store.services_public(),
        "current_year": datetime.now(timezone.utc).year,
        "process_steps": PROCESS_STEPS,
        "process_eyebrow_primary": PROCESS_EYEBROW_PRIMARY,
        "process_eyebrow_secondary": PROCESS_EYEBROW_SECONDARY,
        "process_title": PROCESS_TITLE,
        "process_desc": PROCESS_DESC,
        "cta_badge": CTA_BANNER["badge"],
        "cta_eyebrow": CTA_BANNER["eyebrow"],
        "cta_title": CTA_BANNER["title"],
        "cta_subtext": CTA_BANNER["subtext"],
        "cta_primary_label": CTA_BANNER["primary_label"],
        "cta_primary_url": CTA_BANNER["primary_url"],
        "cta_secondary_label": CTA_BANNER["secondary_label"],
        "cta_secondary_url": CTA_BANNER["secondary_url"],
        "cta_background": CTA_BANNER["background"],
        "service_expertise": SERVICE_EXPERTISE,
        "testimonial_showcase": _testi,
        "blog": _blog,
        "stats": STATS,
        "faqs": store.get_list("faqs"),
        "feature_cards": FEATURE_CARDS,
        "why_choose": WHY_CHOOSE,
        "nav_subservices": SERVICE_SUBLINKS,
        "nav_active_core": _active_core(),
        "service_badges": _SERVICE_BADGES,
        "amc_plans": AMC_PLANS,
        "css_version": _css_version(),
    }


# --------------------------------------------------------------------------- #
# Routes
# --------------------------------------------------------------------------- #
@app.route("/")
def index():
    # Full single-page design (self-contained template).
    return render_template("index.html")


@app.route("/hero-demo/")
def hero_demo():
    # Preview-only page (not linked from the homepage). Deploy to the
    # homepage later on request.
    return render_template("hero_demo.html")


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/services/")
def services():
    return render_template("services.html", services=store.services_public())


@app.route("/amc/")
def amc():
    return render_template(
        "amc.html",
        amc_meta=AMC_META,
        amc_hero=AMC_HERO,
        amc_plans=AMC_PLANS,
        amc_comparison=AMC_COMPARISON,
        amc_benefits=AMC_BENEFITS,
        amc_details=AMC_DETAILS,
        amc_faq=AMC_FAQ,
    )


@app.route("/services/<slug>/")
def service_detail(slug):
    # Appliance sub-service pages (two-column layout) are matched first so they
    # keep the clean /services/<slug>/ URL shape.
    sub = SUBSERVICE_PAGES.get(slug)
    if sub is not None:
        return render_template(
            "subservice_detail.html",
            sub=sub,
            appliance_parent=APPLIANCE_PARENT,
            appliance_services=APPLIANCE_SERVICES,
            reviews=sub.get("reviews", SUBSERVICE_TESTIMONIALS),
            google=GOOGLE_RATING,
        )

    page = SERVICE_PAGES.get(slug)
    service = SERVICE_BY_SLUG.get(slug)
    # Renovation sub-service / level-3 pages live in SERVICE_PAGES but are not
    # top-level core services, so synthesise a minimal service object for them.
    if service is None:
        if page is None:
            # CMS-created custom service: build its page from stored fields.
            svc = store.get_service(slug)
            if svc and svc.get("enabled", True):
                service = svc
                page = _custom_service_page(svc)
            else:
                abort(404)
        else:
            service = {
                "title": page.get("breadcrumb", "Service"),
                "slug": slug,
                "short": "",
                "description": "",
                "points": [],
            }
    # A few "other services" for cross-linking at the bottom of the page.
    others = [s for s in store.services_public() if s["slug"] != slug][:4]
    return render_template(
        "service_detail.html",
        service=service,
        others=others,
        page=page,
    )


@app.route("/blog/")
def blog():
    posts = store.blog_posts()
    return render_template(
        "blog.html",
        posts=posts,
        categories=store.blog_categories_with_count(),
        recent_posts=store.recent_posts(),
        active_category=None,
        featured=posts[0] if posts else None,
    )


@app.route("/blog/category/<cat_slug>/")
def blog_category(cat_slug):
    cat = store.category_by_slug(cat_slug)
    if cat is None:
        abort(404)
    return render_template(
        "blog.html",
        posts=store.posts_in_category(cat_slug),
        categories=store.blog_categories_with_count(),
        recent_posts=store.recent_posts(),
        active_category=cat,
        featured=None,
    )


@app.route("/blog/<slug>/")
def blog_post(slug):
    post = store.blog_post(slug)
    if post is None:
        abort(404)
    all_posts = store.blog_posts()
    related = [p for p in store.posts_in_category(post["category_slug"]) if p["slug"] != slug]
    if len(related) < 3:
        related += [p for p in all_posts if p["slug"] != slug and p not in related]
    others = related[:3]
    return render_template(
        "blog_post.html",
        post=post,
        others=others,
        categories=store.blog_categories_with_count(),
        recent_posts=store.recent_posts(),
    )


@app.route("/contact/", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        form = {
            "name": request.form.get("name", "").strip(),
            "phone": request.form.get("phone", "").strip(),
            "email": request.form.get("email", "").strip(),
            "service": request.form.get("service", "").strip(),
            "message": request.form.get("message", "").strip(),
        }
        # Lenient capture: the site's forms range from a single phone field
        # to a full callback form. Save whenever we have a usable contact.
        digits = re.sub(r"\D", "", form["phone"])
        if len(digits) >= 7 or form["email"]:
            _save_lead(form)
            _maybe_email_lead(form)
        return redirect(url_for("thank_you"))

    return render_template("contact.html")


@app.route("/privacy/")
def privacy():
    return render_template("privacy.html")


@app.route("/terms/")
def terms():
    return render_template("terms.html")


@app.route("/mission/")
def mission():
    return render_template("mission.html")


@app.route("/vision/")
def vision():
    return render_template("vision.html")


@app.route("/cookies/")
def cookies():
    return render_template("cookies.html")


@app.route("/thank-you/")
def thank_you():
    return render_template("thank_you.html")


# --------------------------------------------------------------------------- #
# Admin panel (session-gated overview of all site content + live enquiries)
# --------------------------------------------------------------------------- #
def _admin_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not session.get("admin"):
            return redirect(url_for("admin_login"))
        return view(*args, **kwargs)

    return wrapped


def _read_leads() -> list:
    """Read enquiries from the JSONL store, newest first."""
    out = []
    try:
        with open(app.config["LEADS_FILE"], encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    out.append(json.loads(line))
                except ValueError:
                    continue
    except OSError:
        return []
    for r in out:
        ts = r.get("received_at", "")
        r["when"] = ts.replace("T", " ")[:16] if ts else ""
    out.reverse()
    return out


@app.route("/admin/login/", methods=["GET", "POST"])
def admin_login():
    if session.get("admin"):
        return redirect(url_for("admin_dashboard"))
    error = None
    if request.method == "POST":
        user = request.form.get("username", "").strip()
        pw = request.form.get("password", "")
        if user == app.config["ADMIN_USERNAME"] and pw == app.config["ADMIN_PASSWORD"]:
            session["admin"] = True
            session.permanent = True
            return redirect(url_for("admin_dashboard"))
        error = "Invalid username or password."
    return render_template("admin/login.html", error=error)


@app.route("/admin/logout/")
def admin_logout():
    session.pop("admin", None)
    return redirect(url_for("admin_login"))


@app.route("/admin/")
@_admin_required
def admin_dashboard():
    leads = _read_leads()
    stats = {
        "services": len(store.services_all()),
        "subservices": len(SUBSERVICE_PAGES),
        "posts": len(store.blog_posts()),
        "enquiries": len(leads),
        "amc": len(AMC_PLANS),
        "testimonials": len(TESTIMONIAL_SHOWCASE.get("items", [])),
        "faqs": len(FAQS),
        "areas": len(SERVICE_AREAS),
    }
    return render_template(
        "admin/dashboard.html", active="dashboard", page_title="Dashboard",
        page_sub="Overview of your website content and activity.",
        stats=stats, recent_enquiries=leads[:6], recent_posts=store.recent_posts(6),
    )


@app.route("/admin/services/")
@_admin_required
def admin_services():
    return render_template(
        "admin/services.html", active="services", page_title="Core Services",
        page_sub="Add, edit, reorder, enable or remove the main service categories.",
        services=store.services_all(), sublinks=SERVICE_SUBLINKS,
        rich_pages=set(SERVICE_PAGES.keys()),
    )


@app.route("/admin/services/new/")
@app.route("/admin/services/<slug>/edit/")
@_admin_required
def admin_service_form(slug=None):
    svc = store.get_service(slug) if slug else None
    if slug and svc is None:
        abort(404)
    features = svc.get("page_features", []) if svc else []
    features_text = "\n".join(
        f"{f.get('title', '')} :: {f.get('text', '')}" for f in features
    )
    points_text = "\n".join(svc.get("points", [])) if svc else ""
    return render_template(
        "admin/service_form.html", active="services",
        page_title=("Edit Service" if svc else "New Service"),
        page_sub="Custom services get their own auto-built page; the nav, homepage "
                 "slider and services list all update automatically.",
        svc=svc, icons=list(store.ICON_SET.keys()), icon_set=store.ICON_SET,
        features_text=features_text, points_text=points_text,
        has_rich_page=(slug in SERVICE_PAGES) if slug else False,
    )


def _parse_features(text: str) -> list:
    rows = []
    for line in (text or "").splitlines():
        line = line.strip()
        if not line:
            continue
        if "::" in line:
            t, _, d = line.partition("::")
            rows.append({"title": t.strip(), "text": d.strip()})
        else:
            rows.append({"title": line, "text": ""})
    return rows


@app.route("/admin/services/save/", methods=["POST"])
@_admin_required
def admin_service_save():
    f = request.form
    orig = f.get("orig_slug", "").strip()
    points = [p.strip() for p in f.get("points", "").splitlines() if p.strip()]
    data = {
        "title": f.get("title", "").strip(),
        "nav_label": f.get("nav_label", "").strip(),
        "num": f.get("num", "").strip(),
        "icon_key": f.get("icon_key", "gear").strip(),
        "short": f.get("short", "").strip(),
        "description": f.get("description", "").strip(),
        "points": points,
        "enabled": f.get("enabled") == "on",
        "page_intro": f.get("page_intro", "").strip(),
        "page_features": _parse_features(f.get("page_features", "")),
    }
    if f.get("slug", "").strip():
        data["slug"] = f.get("slug").strip()
    store.save_service(data, orig)
    flash("Service saved.", "success")
    return redirect(url_for("admin_services"))


@app.route("/admin/services/<slug>/toggle/", methods=["POST"])
@_admin_required
def admin_service_toggle(slug):
    svc = store.get_service(slug)
    if svc:
        store.save_service({**svc, "enabled": not svc.get("enabled", True)}, slug)
        flash("Service visibility updated.", "success")
    return redirect(url_for("admin_services"))


@app.route("/admin/services/<slug>/delete/", methods=["POST"])
@_admin_required
def admin_service_delete(slug):
    if store.delete_service(slug):
        flash("Service deleted.", "success")
    else:
        flash("Built-in services can't be deleted — you can disable them instead.",
              "error")
    return redirect(url_for("admin_services"))


@app.route("/admin/services/reorder/", methods=["POST"])
@_admin_required
def admin_service_reorder():
    order = request.form.get("order", "")
    slugs = [s for s in order.split(",") if s]
    if slugs:
        store.reorder_services(slugs)
        flash("Order updated.", "success")
    return redirect(url_for("admin_services"))


@app.route("/admin/subservices/")
@_admin_required
def admin_subservices():
    groups = []
    for core_slug, items in SERVICE_SUBLINKS.items():
        svc = SERVICE_BY_SLUG.get(core_slug)
        groups.append({
            "parent": svc["title"] if svc else core_slug.replace("-", " ").title(),
            "items": items,
        })
    return render_template(
        "admin/subservices.html", active="subservices", page_title="Sub-Services",
        page_sub="Sub-service and level-3 pages grouped by parent service.",
        groups=groups,
    )


@app.route("/admin/blog/")
@_admin_required
def admin_blog():
    return render_template(
        "admin/blog.html", active="blog", page_title="Blog Posts",
        page_sub="Articles and categories.", posts=store.blog_posts(),
        categories=store.blog_categories_with_count(),
    )


@app.route("/admin/amc/")
@_admin_required
def admin_amc():
    return render_template(
        "admin/amc.html", active="amc", page_title="AMC Plans",
        page_sub="Annual Maintenance Contract plans and full comparison.",
        plans=AMC_PLANS, comparison=AMC_COMPARISON,
    )


@app.route("/admin/testimonials/")
@_admin_required
def admin_testimonials():
    return render_template(
        "admin/testimonials.html", active="testimonials", page_title="Testimonials",
        page_sub="Customer reviews shown on the site.",
        showcase={**TESTIMONIAL_SHOWCASE, "items": store.get_list("testimonials")},
    )


@app.route("/admin/faqs/")
@_admin_required
def admin_faqs():
    return render_template(
        "admin/faqs.html", active="faqs", page_title="FAQs",
        page_sub="Frequently asked questions on the homepage.",
        faqs=store.get_list("faqs"),
    )


@app.route("/admin/areas/")
@_admin_required
def admin_areas():
    return render_template(
        "admin/areas.html", active="areas", page_title="Service Areas",
        page_sub="Areas the business covers.", areas=store.get_list("areas"),
    )


@app.route("/admin/enquiries/")
@_admin_required
def admin_enquiries():
    return render_template(
        "admin/enquiries.html", active="enquiries", page_title="Enquiries",
        page_sub="Contact and booking form submissions, newest first.",
        enquiries=list(enumerate(_read_leads())),
    )


# ---- content editing helpers ---------------------------------------------- #
def _sections_to_text(sections) -> str:
    """Render a post's sections back into an editable plain-text body."""
    blocks = []
    for s in sections or []:
        if s.get("heading"):
            blocks.append("## " + s["heading"])
        for p in s.get("paras", []):
            blocks.append(p)
    return "\n\n".join(blocks)


def _text_to_sections(text: str) -> list:
    """Parse the editable body: '## ' lines are headings, blank lines split paras."""
    sections = []
    cur = {"heading": "", "paras": []}
    for block in re.split(r"\n\s*\n", (text or "").strip()):
        block = block.strip()
        if not block:
            continue
        if block.startswith("## "):
            if cur["heading"] or cur["paras"]:
                sections.append(cur)
            cur = {"heading": block[3:].strip(), "paras": []}
        else:
            cur["paras"].append(block)
    if cur["heading"] or cur["paras"]:
        sections.append(cur)
    return sections or [{"heading": "", "paras": []}]


# ---- FAQ CRUD ------------------------------------------------------------- #
@app.route("/admin/faqs/save/", methods=["POST"])
@_admin_required
def admin_faq_save():
    faqs = store.get_list("faqs")
    q = request.form.get("q", "").strip()
    a = request.form.get("a", "").strip()
    idx = request.form.get("index", "")
    if not q or not a:
        flash("Both question and answer are required.", "error")
        return redirect(url_for("admin_faqs"))
    if idx == "":
        faqs.append({"q": q, "a": a})
        flash("FAQ added.", "success")
    else:
        i = int(idx)
        faqs[i] = {"q": q, "a": a}
        flash("FAQ updated.", "success")
    store.replace_list("faqs", faqs)
    return redirect(url_for("admin_faqs"))


@app.route("/admin/faqs/<int:i>/delete/", methods=["POST"])
@_admin_required
def admin_faq_delete(i):
    faqs = store.get_list("faqs")
    if 0 <= i < len(faqs):
        faqs.pop(i)
        store.replace_list("faqs", faqs)
        flash("FAQ deleted.", "success")
    return redirect(url_for("admin_faqs"))


# ---- Testimonial CRUD ----------------------------------------------------- #
@app.route("/admin/testimonials/save/", methods=["POST"])
@_admin_required
def admin_testimonial_save():
    items = store.get_list("testimonials")
    name = request.form.get("name", "").strip()
    quote = request.form.get("quote", "").strip()
    time_ = request.form.get("time", "").strip()
    try:
        rating = max(1, min(5, int(request.form.get("rating", "5"))))
    except ValueError:
        rating = 5
    idx = request.form.get("index", "")
    if not name or not quote:
        flash("Name and review text are required.", "error")
        return redirect(url_for("admin_testimonials"))
    rec = {"name": name, "quote": quote, "time": time_ or "Recently", "rating": rating}
    if idx == "":
        items.append(rec)
        flash("Testimonial added.", "success")
    else:
        items[int(idx)] = rec
        flash("Testimonial updated.", "success")
    store.replace_list("testimonials", items)
    return redirect(url_for("admin_testimonials"))


@app.route("/admin/testimonials/<int:i>/delete/", methods=["POST"])
@_admin_required
def admin_testimonial_delete(i):
    items = store.get_list("testimonials")
    if 0 <= i < len(items):
        items.pop(i)
        store.replace_list("testimonials", items)
        flash("Testimonial deleted.", "success")
    return redirect(url_for("admin_testimonials"))


# ---- Service Areas CRUD --------------------------------------------------- #
@app.route("/admin/areas/save/", methods=["POST"])
@_admin_required
def admin_area_save():
    areas = store.get_list("areas")
    name = request.form.get("name", "").strip()
    idx = request.form.get("index", "")
    if not name:
        flash("Area name is required.", "error")
        return redirect(url_for("admin_areas"))
    if idx == "":
        areas.append(name)
        flash("Area added.", "success")
    else:
        areas[int(idx)] = name
        flash("Area updated.", "success")
    store.replace_list("areas", areas)
    return redirect(url_for("admin_areas"))


@app.route("/admin/areas/<int:i>/delete/", methods=["POST"])
@_admin_required
def admin_area_delete(i):
    areas = store.get_list("areas")
    if 0 <= i < len(areas):
        areas.pop(i)
        store.replace_list("areas", areas)
        flash("Area deleted.", "success")
    return redirect(url_for("admin_areas"))


# ---- Blog category CRUD --------------------------------------------------- #
@app.route("/admin/blog/category/save/", methods=["POST"])
@_admin_required
def admin_category_save():
    cats = store.get_list("blog_categories")
    name = request.form.get("name", "").strip()
    if not name:
        flash("Category name is required.", "error")
        return redirect(url_for("admin_blog"))
    slug = store.unique_slug(store.slugify(name), {c["slug"] for c in cats})
    cats.append({"name": name, "slug": slug})
    store.replace_list("blog_categories", cats)
    flash("Category added.", "success")
    return redirect(url_for("admin_blog"))


@app.route("/admin/blog/category/<slug>/delete/", methods=["POST"])
@_admin_required
def admin_category_delete(slug):
    cats = store.get_list("blog_categories")
    if any(p.get("category") and store.slugify(p["category"]) == slug or
           _cat_name_slug(p, cats) == slug for p in store.get_list("blog_posts")):
        flash("Cannot delete a category that still has posts.", "error")
        return redirect(url_for("admin_blog"))
    store.replace_list("blog_categories", [c for c in cats if c["slug"] != slug])
    flash("Category deleted.", "success")
    return redirect(url_for("admin_blog"))


def _cat_name_slug(post, cats):
    m = {c["name"]: c["slug"] for c in cats}
    return m.get(post.get("category", ""), "")


# ---- Blog post CRUD ------------------------------------------------------- #
@app.route("/admin/blog/new/")
@_admin_required
def admin_blog_new():
    return render_template(
        "admin/blog_form.html", active="blog", page_title="New Blog Post",
        page_sub="Create a new article.", post=None, body="",
        categories=store.blog_categories(),
    )


@app.route("/admin/blog/<slug>/edit/")
@_admin_required
def admin_blog_edit(slug):
    post = store.blog_post(slug)
    if post is None:
        abort(404)
    return render_template(
        "admin/blog_form.html", active="blog", page_title="Edit Blog Post",
        page_sub=post["title"], post=post, body=_sections_to_text(post.get("sections")),
        categories=store.blog_categories(),
    )


@app.route("/admin/blog/save/", methods=["POST"])
@_admin_required
def admin_blog_save():
    posts = store.get_list("blog_posts")
    orig = request.form.get("orig_slug", "").strip()
    title = request.form.get("title", "").strip()
    if not title:
        flash("Title is required.", "error")
        return redirect(url_for("admin_blog"))
    rec = {
        "title": title,
        "category": request.form.get("category", "").strip(),
        "date": request.form.get("date", "").strip(),
        "tags": request.form.get("tags", "").strip(),
        "image": request.form.get("image", "").strip() or "/static/img/hero-team.webp",
        "image_alt": request.form.get("image_alt", "").strip() or title,
        "excerpt": request.form.get("excerpt", "").strip(),
        "sections": _text_to_sections(request.form.get("body", "")),
    }
    if orig:  # editing — keep the existing slug so URLs don't break
        for i, p in enumerate(posts):
            if p.get("slug") == orig:
                rec["slug"] = orig
                posts[i] = rec
                break
        flash("Post updated.", "success")
    else:
        rec["slug"] = store.unique_slug(store.slugify(title), {p.get("slug") for p in posts})
        posts.insert(0, rec)
        flash("Post created.", "success")
    store.replace_list("blog_posts", posts)
    return redirect(url_for("admin_blog"))


@app.route("/admin/blog/<slug>/delete/", methods=["POST"])
@_admin_required
def admin_blog_delete(slug):
    posts = store.get_list("blog_posts")
    store.replace_list("blog_posts", [p for p in posts if p.get("slug") != slug])
    flash("Post deleted.", "success")
    return redirect(url_for("admin_blog"))


# ---- Enquiries management ------------------------------------------------- #
def _write_leads(leads: list) -> None:
    """Rewrite the leads store (leads are held newest-first in memory)."""
    try:
        with open(app.config["LEADS_FILE"], "w", encoding="utf-8") as fh:
            for r in reversed(leads):
                rec = {k: v for k, v in r.items() if k != "when"}
                fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    except OSError as exc:
        app.logger.error("Could not rewrite leads: %s", exc)


@app.route("/admin/enquiries/<int:i>/delete/", methods=["POST"])
@_admin_required
def admin_enquiry_delete(i):
    leads = _read_leads()
    if 0 <= i < len(leads):
        leads.pop(i)
        _write_leads(leads)
        flash("Enquiry deleted.", "success")
    return redirect(url_for("admin_enquiries"))


@app.route("/admin/enquiries/clear/", methods=["POST"])
@_admin_required
def admin_enquiry_clear():
    _write_leads([])
    flash("All enquiries cleared.", "success")
    return redirect(url_for("admin_enquiries"))


@app.route("/robots.txt")
def robots_txt():
    lines = [
        "User-agent: *",
        "Allow: /",
        "Disallow: /thank-you/",
        "Disallow: /admin/",
        f"Sitemap: https://{app.config['SITE_DOMAIN']}/sitemap.xml",
    ]
    return Response("\n".join(lines) + "\n", mimetype="text/plain")


@app.route("/sitemap.xml")
def sitemap_xml():
    """A simple, always-current XML sitemap of every indexable page."""
    domain = app.config["SITE_DOMAIN"]
    # (endpoint, priority) for static routes; dynamic ones are added below.
    paths = [
        ("/", "1.0"),
        ("/about/", "0.8"),
        ("/services/", "0.9"),
        ("/blog/", "0.7"),
        ("/contact/", "0.8"),
        ("/mission/", "0.4"),
        ("/vision/", "0.4"),
        ("/privacy/", "0.3"),
        ("/terms/", "0.3"),
        ("/cookies/", "0.3"),
    ]
    paths += [("/amc/", "0.7")]
    paths += [(f"/services/{s['slug']}/", "0.8") for s in SERVICES]
    paths += [(f"/services/{slug}/", "0.7") for slug in SUBSERVICE_PAGES]
    paths += [(f"/blog/category/{c['slug']}/", "0.5") for c in store.blog_categories()]
    paths += [(f"/blog/{p['slug']}/", "0.6") for p in store.blog_posts()]

    items = "".join(
        f"<url><loc>https://{domain}{path}</loc>"
        f"<priority>{prio}</priority></url>"
        for path, prio in paths
    )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f"{items}</urlset>"
    )
    return Response(xml, mimetype="application/xml")


@app.errorhandler(404)
def not_found(_):
    return render_template("404.html"), 404


# --------------------------------------------------------------------------- #
# Contact-form helpers
# --------------------------------------------------------------------------- #
def _validate(form: dict) -> list[str]:
    errors = []
    if len(form["name"]) < 2:
        errors.append("Please enter your name.")
    if len(re.sub(r"\D", "", form["phone"])) < 7:
        errors.append("Please enter a valid phone number.")
    if form["email"] and not EMAIL_RE.match(form["email"]):
        errors.append("That email address doesn't look right.")
    if len(form["message"]) < 5:
        errors.append("Please tell us a little about the job.")
    return errors


def _save_lead(form: dict) -> None:
    """Append the enquiry as one JSON line — no database needed."""
    record = dict(form)
    record["received_at"] = datetime.now(timezone.utc).isoformat()
    record["ip"] = request.remote_addr
    try:
        with open(app.config["LEADS_FILE"], "a", encoding="utf-8") as fh:
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")
    except OSError as exc:  # never let storage break the user's request
        app.logger.error("Could not save lead: %s", exc)


def _maybe_email_lead(form: dict) -> None:
    """Email the enquiry if SMTP is configured; otherwise skip silently."""
    host = app.config.get("SMTP_HOST")
    if not host:
        return
    try:
        msg = EmailMessage()
        msg["Subject"] = f"New enquiry — {form['service'] or 'General'}"
        msg["From"] = app.config["SMTP_USER"] or app.config["CONTACT_EMAIL"]
        msg["To"] = app.config["MAIL_TO"]
        msg.set_content(
            "New enquiry from bestfixit.ae\n\n"
            f"Name:    {form['name']}\n"
            f"Phone:   {form['phone']}\n"
            f"Email:   {form['email']}\n"
            f"Service: {form['service']}\n\n"
            f"{form['message']}\n"
        )
        with smtplib.SMTP(host, app.config["SMTP_PORT"]) as server:
            server.starttls()
            if app.config.get("SMTP_USER"):
                server.login(
                    app.config["SMTP_USER"], app.config["SMTP_PASSWORD"]
                )
            server.send_message(msg)
    except Exception as exc:  # noqa: BLE001 - log and move on
        app.logger.error("Could not email lead: %s", exc)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
