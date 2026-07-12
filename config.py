"""Application configuration for bestfixit.ae.

Values are read from environment variables so the same code runs locally and
in production without edits. Copy ``.env.example`` to ``.env`` and adjust.
"""
import os


class Config:
    # Business / brand details — surfaced across the site.
    SITE_NAME = os.environ.get("SITE_NAME", "BestFixIt")
    SITE_DOMAIN = os.environ.get("SITE_DOMAIN", "bestfixit.ae")
    CONTACT_PHONE = os.environ.get("CONTACT_PHONE", "+971 50 000 0000")
    # WhatsApp number in international format, digits only (for wa.me links).
    WHATSAPP_NUMBER = os.environ.get("WHATSAPP_NUMBER", "971500000000")
    CONTACT_EMAIL = os.environ.get("CONTACT_EMAIL", "hello@bestfixit.ae")

    # Flask
    SECRET_KEY = os.environ.get("SECRET_KEY", "change-me-in-production")

    # Where contact-form enquiries are appended (simple, DB-free storage).
    LEADS_FILE = os.environ.get("LEADS_FILE", "leads.jsonl")

    # Optional SMTP — if configured, enquiries are also emailed.
    SMTP_HOST = os.environ.get("SMTP_HOST")
    SMTP_PORT = int(os.environ.get("SMTP_PORT", "587"))
    SMTP_USER = os.environ.get("SMTP_USER")
    SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")
    MAIL_TO = os.environ.get("MAIL_TO", CONTACT_EMAIL)
