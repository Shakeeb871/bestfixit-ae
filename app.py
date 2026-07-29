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
from data.blog import (
    BLOG,
    POSTS,
    POST_BY_SLUG,
    CATEGORIES,
    CATEGORIES_WITH_COUNT,
    CATEGORY_BY_SLUG,
    RECENT_POSTS,
    posts_in_category,
)
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
    return {
        "site_name": app.config["SITE_NAME"],
        "site_domain": app.config["SITE_DOMAIN"],
        "contact_phone": app.config["CONTACT_PHONE"],
        "whatsapp_number": app.config["WHATSAPP_NUMBER"],
        "contact_email": app.config["CONTACT_EMAIL"],
        "service_areas": SERVICE_AREAS,
        "all_services": SERVICES,
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
        "testimonial_showcase": TESTIMONIAL_SHOWCASE,
        "blog": BLOG,
        "stats": STATS,
        "faqs": FAQS,
        "feature_cards": FEATURE_CARDS,
        "why_choose": WHY_CHOOSE,
        "nav_subservices": SERVICE_SUBLINKS,
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
    return render_template("services.html", services=SERVICES)


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
            abort(404)
        service = {
            "title": page.get("breadcrumb", "Service"),
            "slug": slug,
            "short": "",
            "description": "",
            "points": [],
        }
    # A few "other services" for cross-linking at the bottom of the page.
    others = [s for s in SERVICES if s["slug"] != slug][:4]
    return render_template(
        "service_detail.html",
        service=service,
        others=others,
        page=page,
    )


@app.route("/blog/")
def blog():
    return render_template(
        "blog.html",
        posts=POSTS,
        categories=CATEGORIES_WITH_COUNT,
        recent_posts=RECENT_POSTS,
        active_category=None,
        featured=POSTS[0],
    )


@app.route("/blog/category/<cat_slug>/")
def blog_category(cat_slug):
    cat = CATEGORY_BY_SLUG.get(cat_slug)
    if cat is None:
        abort(404)
    return render_template(
        "blog.html",
        posts=posts_in_category(cat_slug),
        categories=CATEGORIES_WITH_COUNT,
        recent_posts=RECENT_POSTS,
        active_category=cat,
        featured=None,
    )


@app.route("/blog/<slug>/")
def blog_post(slug):
    post = POST_BY_SLUG.get(slug)
    if post is None:
        abort(404)
    # related: same category first, then fill with other recent posts.
    related = [p for p in posts_in_category(post["category_slug"]) if p["slug"] != slug]
    if len(related) < 3:
        related += [p for p in POSTS if p["slug"] != slug and p not in related]
    others = related[:3]
    return render_template(
        "blog_post.html",
        post=post,
        others=others,
        categories=CATEGORIES_WITH_COUNT,
        recent_posts=RECENT_POSTS,
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
        "services": len(SERVICES),
        "subservices": len(SUBSERVICE_PAGES),
        "posts": len(POSTS),
        "enquiries": len(leads),
        "amc": len(AMC_PLANS),
        "testimonials": len(TESTIMONIAL_SHOWCASE.get("items", [])),
        "faqs": len(FAQS),
        "areas": len(SERVICE_AREAS),
    }
    return render_template(
        "admin/dashboard.html", active="dashboard", page_title="Dashboard",
        page_sub="Overview of your website content and activity.",
        stats=stats, recent_enquiries=leads[:6], recent_posts=POSTS[:6],
    )


@app.route("/admin/services/")
@_admin_required
def admin_services():
    return render_template(
        "admin/services.html", active="services", page_title="Core Services",
        page_sub="The main service categories shown across the site.",
        services=SERVICES, sublinks=SERVICE_SUBLINKS,
    )


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
        page_sub="Articles and categories.", posts=POSTS,
        categories=CATEGORIES_WITH_COUNT,
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
        showcase=TESTIMONIAL_SHOWCASE,
    )


@app.route("/admin/faqs/")
@_admin_required
def admin_faqs():
    return render_template(
        "admin/faqs.html", active="faqs", page_title="FAQs",
        page_sub="Frequently asked questions on the homepage.", faqs=FAQS,
    )


@app.route("/admin/areas/")
@_admin_required
def admin_areas():
    return render_template(
        "admin/areas.html", active="areas", page_title="Service Areas",
        page_sub="Areas the business covers.", areas=SERVICE_AREAS,
    )


@app.route("/admin/enquiries/")
@_admin_required
def admin_enquiries():
    return render_template(
        "admin/enquiries.html", active="enquiries", page_title="Enquiries",
        page_sub="Contact and booking form submissions, newest first.",
        enquiries=_read_leads(),
    )


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
    paths += [(f"/blog/category/{c['slug']}/", "0.5") for c in CATEGORIES]
    paths += [(f"/blog/{p['slug']}/", "0.6") for p in POSTS]

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
