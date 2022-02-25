from flask import Blueprint, render_template, abort, Flask
from jinja2 import TemplateNotFound
from os import getenv
import datetime


bp = Blueprint('simple_pages', __name__,
                        template_folder='templates',static_folder='static')

@bp.route('/page/<page>')
def show(page):
    try:
        return render_template('%s.html' % page)
    except TemplateNotFound:
        abort(404)


@bp.context_processor
def inject_deployment_environment():
    deployment_environment = getenv('FLASK_ENV', None)
    return dict(deployment_environment=deployment_environment)

@bp.context_processor
def inject_deployment_environment():
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    year = date.strftime("%Y")
    return dict(year=year)


