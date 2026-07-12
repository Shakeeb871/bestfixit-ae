"""WSGI entry point for production servers (gunicorn / passenger).

Example:
    gunicorn -w 3 -b 0.0.0.0:8000 wsgi:app
"""
from app import app

if __name__ == "__main__":
    app.run()
