# BestFixIt — bestfixit.ae

A clean, fast marketing website for **BestFixIt**, a UAE home-maintenance and
handyman service. Built with **Python + Flask** and server-rendered Jinja2
templates. No database required — enquiries are saved to a simple JSONL file
and can optionally be emailed via SMTP.

## Features

- Responsive, accessible UI with a proper design system (`static/css/style.css`)
- Home, About, Services, per-service detail pages, Contact, Thank-you, 404
- Contact form with server-side validation and lead capture
- Click-to-call, WhatsApp deep links and floating WhatsApp button
- SEO-friendly meta + Open Graph tags, inline SVG icons (no image deps)
- Configurable brand/contact details via environment variables

## Tech stack

| Layer      | Choice                          |
|------------|---------------------------------|
| Backend    | Python 3.9+, Flask 3            |
| Templates  | Jinja2                          |
| Styling    | Hand-written CSS (design tokens)|
| JS         | Vanilla (progressive enhancement)|
| Prod server| gunicorn                        |

## Project structure

```
bestfixit-ae/
├── app.py               # Flask app, routes, form handling
├── config.py            # Env-driven configuration
├── wsgi.py              # Production entry point (gunicorn)
├── requirements.txt
├── .env.example         # Copy to .env and edit
├── data/
│   └── services.py      # Service catalogue, areas, testimonials
├── templates/           # Jinja2 templates (base + pages)
│   ├── base.html
│   ├── _icons.html      # Inline SVG icon macro
│   ├── index.html
│   ├── about.html
│   ├── services.html
│   ├── service_detail.html
│   ├── contact.html
│   ├── thank_you.html
│   └── 404.html
└── static/
    ├── css/style.css
    ├── js/main.js
    └── img/favicon.svg
```

## Run locally

```bash
# 1. Clone and enter the project
cd bestfixit-ae

# 2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. (Optional) configure brand details
cp .env.example .env             # then edit values

# 5. Run
python app.py
```

Open <http://127.0.0.1:5000>.

## Configuration

All settings are environment variables (see `.env.example`):

| Variable          | Purpose                                    |
|-------------------|--------------------------------------------|
| `SITE_NAME`       | Brand name shown across the site           |
| `CONTACT_PHONE`   | Phone number for call links                |
| `WHATSAPP_NUMBER` | WhatsApp number (digits only) for wa.me     |
| `CONTACT_EMAIL`   | Contact email address                      |
| `SECRET_KEY`      | Flask session/flash secret                 |
| `LEADS_FILE`      | Path where enquiries are appended (JSONL)   |
| `SMTP_*`          | Optional SMTP to email enquiries           |

## Deploy

Any host that runs Python works (Render, Railway, Fly.io, a VPS, or cPanel
with Passenger). Example with gunicorn:

```bash
gunicorn -w 3 -b 0.0.0.0:8000 wsgi:app
```

Set the environment variables from `.env.example` in your host's dashboard.

## Leads

Contact-form submissions are appended to `leads.jsonl` (one JSON object per
line). If SMTP is configured, each enquiry is also emailed to `MAIL_TO`.

---

© BestFixIt · bestfixit.ae
