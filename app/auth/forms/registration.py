from flask_wtf import FlaskForm
from flask_babel import lazy_gettext as _l

from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Regexp


class RegistrationForm(FlaskForm):
    email = StringField(
        _l('E-mail'),
        validators=[DataRequired(), Email()],
        render_kw={
            'placeholder': _l('E-mail'),
            'autocomplete': 'mail',
            'class': 'auth-container-data-input',
        }
    )
    firstname = StringField(_l('First Name'), validators=[DataRequired()],
                            render_kw={
                                'placeholder': _l('First Name'),
                                'class': 'auth-container-data-input',
                            })
    lastname = StringField(_l('Last Name'),
                           render_kw={
                               'placeholder': _l('Last Name'),
                               'class': 'auth-container-data-input',
                           })
    username = StringField(
        _l('Username'),
        validators=[Regexp(r'^[a-zA-Z0-9_]{5,30}$',
                           message=_l('Username should include english letters, numeric digits and symbol "_" only. '
                                      'Also it should contains al lest 5 symbols and not more than 30.'))],
        render_kw={
            'placeholder': _l('Username'),
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
            'class': 'auth-container-data-input',
        }
    )
    submit = SubmitField(_l('Registration'))
