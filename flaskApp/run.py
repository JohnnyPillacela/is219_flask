"""This allows Gunicorn to serve the app in production"""

from flaskApp import create_app

app = create_app()