from flask_wtf import FlaskForm
from flask_babel import lazy_gettext as _l

from wtforms import SubmitField, PasswordField, StringField
from wtforms.validators import DataRequired, Email, Regexp


class LoginForm(FlaskForm):
    email = StringField(
        _l('E-mail'),
        validators=[DataRequired(), Email()],
        render_kw={
            'placeholder': _l('E-mail'),
            'autocomplete': 'mail',
            'class': 'auth-container-data-input',
        }
    )
    password = PasswordField(
        _l('Password'),
        validators=[
            DataRequired(),
            Regexp(
                r'((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W]).{6,20})',
                message=_l('Notice - password should contains lowercase, uppercase, digit and special symbols')
            ),
        ],
        render_kw={
            'placeholder': _l('Password'),
            'autocomplete': 'current-password',
            'class': 'auth-container-data-input',
        }
    )
    submit = SubmitField(_l('Log In'))
