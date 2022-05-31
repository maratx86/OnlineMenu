from flask import g, render_template, request

from app import get_locale

from . import app
from app.storage import db, models


@app.route('/<restaurant_id>/')
def index(restaurant_id):
    r = db.session.query(models.Restaurant).filter_by(id=restaurant_id).first()
    if not r:
        return 'Not Found!', 404
    return render_template(
        'web/restaurant/index.html',
        restaurant=r,
    )


@app.route('/<restaurant_id>/position/<position_id>/')
def position(restaurant_id, position_id):
    r = db.session.query(models.Restaurant).filter_by(id=restaurant_id).first()
    if not r:
        return 'Not Found!', 404
    p = db.session.query(models.Position).filter_by(id=position_id, restaurant_id=restaurant_id).first()
    if not p:
        return 'Not Found Position!', 404
    return 'Found'


@app.route('/<restaurant_id>/menu/<menu_id>/')
def menu(restaurant_id, menu_id):
    r = db.session.query(models.Restaurant).filter_by(id=restaurant_id).first()
    if not r:
        return 'Not Found!', 404
    m = db.session.query(models.Menu).filter_by(id=menu_id, restaurant_id=restaurant_id).first()
    if not m:
        return 'Not Found Menu!', 404
    return render_template(
        'web/restaurant/menu.html',
        restaurant=r, menu=m,
    )
