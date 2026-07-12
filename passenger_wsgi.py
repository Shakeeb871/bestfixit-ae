"""Passenger entry point for cPanel hosting (Spaceship / Namecheap).

cPanel's "Setup Python App" runs the site through Phusion Passenger, which
looks for a module-level callable named ``application`` in this file.
"""
from app import app as application

if __name__ == "__main__":
    application.run()
