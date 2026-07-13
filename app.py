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
import re
import smtplib
from datetime import datetime, timezone
from email.message import EmailMessage

from flask import (
    Flask,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

try:  # load a local .env if python-dotenv is installed
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

from config import Config
from data.blog import BLOG
from data.cta import CTA_BANNER
from data.expertise import SERVICE_EXPERTISE
from data.process import (
    PROCESS_EYEBROW_PRIMARY,
    PROCESS_EYEBROW_SECONDARY,
    PROCESS_STEPS,
    PROCESS_TITLE,
)
from data.testimonials import TESTIMONIAL_SHOWCASE
from data.services import (
    SERVICE_AREAS,
    SERVICE_BY_SLUG,
    SERVICES,
    TESTIMONIALS,
)
from data.stats import STATS

app = Flask(__name__)
app.config.from_object(Config)
# Re-read templates on every request so a git pull shows template changes
# without needing a full app restart (cPanel/Passenger keeps the process alive).
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.jinja_env.auto_reload = True

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


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
        "cta_badge": CTA_BANNER["badge"],
        "cta_eyebrow": CTA_BANNER["eyebrow"],
        "cta_title": CTA_BANNER["title"],
        "cta_primary_label": CTA_BANNER["primary_label"],
        "cta_primary_url": CTA_BANNER["primary_url"],
        "cta_secondary_label": CTA_BANNER["secondary_label"],
        "cta_secondary_url": CTA_BANNER["secondary_url"],
        "cta_background": CTA_BANNER["background"],
        "service_expertise": SERVICE_EXPERTISE,
        "testimonial_showcase": TESTIMONIAL_SHOWCASE,
        "blog": BLOG,
        "stats": STATS,
    }


# --------------------------------------------------------------------------- #
# Routes
# --------------------------------------------------------------------------- #
@app.route("/")
def index():
    # Full single-page design (self-contained template).
    return render_template("index.html")


@app.route("/hero-demo")
def hero_demo():
    # Preview-only page (not linked from the homepage). Deploy to the
    # homepage later on request.
    return render_template("hero_demo.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/services")
def services():
    return render_template("services.html", services=SERVICES)


@app.route("/services/<slug>")
def service_detail(slug):
    service = SERVICE_BY_SLUG.get(slug)
    if service is None:
        abort(404)
    # A few "other services" for cross-linking at the bottom of the page.
    others = [s for s in SERVICES if s["slug"] != slug][:4]
    return render_template(
        "service_detail.html", service=service, others=others
    )


@app.route("/contact", methods=["GET", "POST"])
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

    # No standalone contact page — send visitors to the homepage form.
    return redirect(url_for("index") + "#contact")


@app.route("/thank-you")
def thank_you():
    return render_template("thank_you.html")


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
