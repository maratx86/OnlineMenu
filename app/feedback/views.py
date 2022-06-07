from flask import g, render_template, redirect, url_for
from flask_mail import Message

from app import get_locale, mail
import config

from . import app, forms


@app.route('/', methods=('GET', 'POST'))
def index():
    form = forms.FeedbackForm()
    if form.validate_on_submit():
        text = 'From: {}\n\n{}'.format(form.feedback_email.data, form.feedback_body.data)
        message = Message(form.feedback_theme.data)
        for recipient in config.admins_email:
            message.add_recipient(recipient)
        message.body = text
        message.html = None
        mail.send(message)
        return redirect(url_for('feedback.thanks'))
    return render_template(
        'feedback/main.html',
        feedback=True, form=form,
    )


@app.route('/thanks/')
def thanks():
    return render_template(
        'feedback/thanks.html',
    )


@app.before_request
def before_request():
    g.locale = str(get_locale())
