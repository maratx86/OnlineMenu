from flask import g, render_template, request, redirect, url_for
from flask_login import current_user, login_required

from app import get_locale

from . import app
from app.storage import db, models
from app.restaurant import forms
import utils
import app.restaurant.mvc_views as mvc_views


@app.route('/create/')
@login_required
def create():
    r = models.Restaurant(title='Default Title')
    w = models.Worker(user_id=current_user.id, role='owner')
    db.session.add(r)
    db.session.commit()
    w.restaurant_id = r.id
    db.session.add(w)
    db.session.commit()
    return redirect(url_for('r.editor', restaurant_id=r.id))


@app.route('/<restaurant_id>/')
def index(restaurant_id):
    r = db.session.query(models.Restaurant).filter_by(id=restaurant_id).first()
    if not r:
        return 'Not Found!', 404
    is_worker = utils.has_user_worker_status(current_user, r.workers)
    view = mvc_views.RestaurantView()
    if utils.has_user_edit_access(current_user, r.workers):
        view.add_button('Edit', 'window.location="{0}";'.format(
            url_for('r.editor', restaurant_id=restaurant_id)
        ))
    return render_template(
        'web/restaurant/index.html',
        restaurant=r, worker=is_worker, view=view,
    )


@app.route('/<restaurant_id>/editor/', methods=('GET', 'POST'))
def editor(restaurant_id):
    r = db.session.query(models.Restaurant).filter_by(id=restaurant_id).first()
    if not r:
        return 'Not Found!', 404
    is_worker = utils.has_user_worker_status(current_user, r.workers)
    f = forms.REditorForm()
    if not is_worker:
        return 'You have no right'
    if f.validate_on_submit():
        f.out(r)
        db.session.commit()
        return redirect(url_for('r.index', restaurant_id=restaurant_id))
    f.fill(r)
    return render_template(
        'web/restaurant/editor.html',
        restaurant=r, form=f,
    )


@app.route('/<restaurant_id>/menu/<menu_id>/position/<position_id>/')
def position(restaurant_id, menu_id, position_id):
    r = db.session.query(models.Restaurant).filter_by(id=restaurant_id).first()
    if not r:
        return 'Not Found!', 404
    #p = db.session.query(models.Position).filter_by(id=position_id, restaurant_id=restaurant_id).first()
    pm = db.session.query(models.MenuPosition).filter_by(menu_id=menu_id, position_id=position_id).first()
    p = pm.position
    p.cost = pm.cost
    if not p:
        return 'Not Found Position!', 404
    view = mvc_views.RestaurantMenuPositionView(r.title, pm)
    if utils.has_user_edit_access(current_user, r.workers):
        view.add_button('Edit', 'window.location="{0}";'.format(
            url_for('r.position_editor', restaurant_id=restaurant_id, menu_id=menu_id, position_id=position_id)
        ))
    return render_template(
        'web/restaurant/position.html',
        restaurant=r, position=p, view=view,
    )


@app.route('/<restaurant_id>/menu/<menu_id>/position/<position_id>/editor/', methods=('GET', 'POST'))
def position_editor(restaurant_id, menu_id, position_id):
    r = db.session.query(models.Restaurant).filter_by(id=restaurant_id).first()
    if not r:
        return 'Not Found!', 404
    #p = db.session.query(models.Position).filter_by(id=position_id, restaurant_id=restaurant_id).first()
    pm = db.session.query(models.MenuPosition).filter_by(menu_id=menu_id, position_id=position_id).first()
    p = pm.position
    p.cost = pm.cost

    form = forms.MenuPositionEditorForm()
    if not p:
        return 'Not Found Position!', 404
    if form.validate_on_submit():
        form.out(pm)
        db.session.commit()
        return redirect(url_for('r.position',
                                restaurant_id=restaurant_id, position_id=position_id, menu_id=menu_id))
    form.fill(pm)
    return render_template(
        'web/restaurant/menu_position_editor.html',
        restaurant=r, position=p, form=form,
    )


@app.route('/<restaurant_id>/menu/<menu_id>/')
def menu(restaurant_id, menu_id):
    r = db.session.query(models.Restaurant).filter_by(id=restaurant_id).first()
    if not r:
        return 'Not Found!', 404
    m = db.session.query(models.Menu).filter_by(id=menu_id, restaurant_id=restaurant_id).first()
    if not m:
        return 'Not Found Menu!', 404
    view = mvc_views.RestaurantMenuView(r.title)
    if utils.has_user_edit_access(current_user, r.workers):
        view.add_button('Edit', 'window.location="{0}";'.format(
            url_for('r.menu_editor', restaurant_id=restaurant_id, menu_id=menu_id)
        ))
    return render_template(
        'web/restaurant/menu.html',
        restaurant=r, menu=m, view=view,
    )


@app.route('/<restaurant_id>/menu/<menu_id>/editor/', methods=('GET', 'POST'))
def menu_editor(restaurant_id, menu_id):
    r = db.session.query(models.Restaurant).filter_by(id=restaurant_id).first()
    if not r:
        return 'Not Found!', 404
    m = db.session.query(models.Menu).filter_by(id=menu_id, restaurant_id=restaurant_id).first()
    if not m:
        return 'Not Found Menu!', 404
    form = forms.MEditorForm()
    if form.validate_on_submit():
        form.out(m)
        db.session.commit()
        return redirect(url_for('r.menu',
                                restaurant_id=restaurant_id, menu_id=menu_id))
    form.fill(m)
    return render_template(
        'web/restaurant/editor/menu.html',
        restaurant=r, menu=m, form=form,
    )
