from flask_wtf import FlaskForm
from flask_babel import lazy_gettext as _l

from wtforms import SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired, Email


class FeedbackForm(FlaskForm):
    feedback_email = StringField(_l('E-mail'), validators=[Email()], render_kw={"placeholder": _l('E-mail')})
    feedback_theme = StringField(_l('Feedback Theme'),
                        validators=[DataRequired()], render_kw={"placeholder": _l('Feedback Theme')})
    feedback_body = TextAreaField(_l('Feedback Body'),
                         validators=[DataRequired()], render_kw={"placeholder": _l('Feedback Body')})
    submit = SubmitField(_l('Send'))
