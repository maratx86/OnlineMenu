from flask import g, render_template, request
from flask_login import current_user

from app import get_locale

from . import app, forms, mvc_views
from app.storage import db, models


@app.route('/')
def index():
    form = forms.QueryForm()
    return render_template(
        'web/index.html',
        feedback=True, form=form, user=current_user,
    )


@app.route('/query/', methods=('GET', 'POST'))
def query():
    form = forms.QueryForm()
    form.params(request.args)
    view = mvc_views.QueryResults()
    if form.validate_on_submit():
        view.__text = form.text.data
        q = db.session.query(models.Restaurant).filter(
            models.Restaurant.title.like(
                '%{}%'.format(form.text.data)
            )
        ).all()
        if q:
            view.add_section('Restaurants', len(q), q)
        q = db.session.query(models.Menu).filter(
            models.Menu.title.like(
                '%{}%'.format(form.text.data)
            )
        ).all()
        if q:
            view.add_section('Menus', len(q), q)
        q = db.session.query(models.Position).filter(
            models.Position.title.like(
                '%{}%'.format(form.text.data)
            )
        ).all()
        if q:
            view.add_section('Positions', len(q), q)
    return render_template(
        'web/query.html',
        feedback=True, form=form, view=view, user=current_user,
    )


@app.before_request
def before_request():
    g.locale = str(get_locale())
