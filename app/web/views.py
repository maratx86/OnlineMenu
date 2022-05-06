from flask import g, render_template

from app import get_locale

from . import app


@app.route('/')
def index():
    return render_template('web/index.html')


@app.before_request
def before_request():
    g.locale = str(get_locale())
