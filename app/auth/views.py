from flask import request, redirect, url_for, render_template
from flask_login import current_user, logout_user, login_user
from flask_babel import gettext as _

import app.storage as storage
import app.storage.database.models as models
from . import app
from . import forms


@app.route('/')
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    return redirect(url_for('web.index'))


@app.route('/login/', methods=('GET', 'POST'))
def login():
    if current_user.is_authenticated:
        return redirect(url_for('web.index'))
    error_message = None
    form = forms.LoginForm()
    if form.validate_on_submit():
        user = models.User.query.filter_by(email=form.email.data).first()
        if not user:
            error_message = _('User not found with that email!')
        elif user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('web.index'))
        else:
            error_message = _('Password not correct!')

    return render_template(
        'auth/login.html',
        form=form, error_message=error_message,
    )


@app.route('/reg/', methods=('GET', 'POST'))
def reg():
    error_message = None
    form = forms.RegistrationForm()
    if form.validate_on_submit():
        user = models.User.query.filter_by(email=form.email.data).first()
        if user:
            error_message = _('User with that email already exist! Try to log in.')
        else:
            user = models.User(
                email=form.email.data,
                firstname=form.firstname.data or None,
                lastname=form.lastname.data or None,
            )
            user.change_password(form.password.data)
            if not models.User.query.filter_by(username=form.username.data).first():
                user.username = form.username.data
            storage.db.session.add(user)
            storage.db.session.commit()
            login_user(user)
            return redirect(url_for('web.index'))
    return render_template(
        'auth/registration.html',
        form=form, error_message=error_message,
    )


@app.route('/logout/')
def logout():
    if current_user.is_authenticated:
        logout_user()
    return 'logout'
