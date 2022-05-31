from flask_wtf import FlaskForm
from flask_babel import lazy_gettext as _l

from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class QueryForm(FlaskForm):
    text = StringField(_l('Type Query'), validators=[DataRequired()])

    def params(self, params):
        if 'text' in params:
            self.text.data = params['text']
