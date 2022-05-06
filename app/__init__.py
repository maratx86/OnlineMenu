import os

from flask import Flask, request
from flask_admin import Admin
from flask_babel import Babel, lazy_gettext as _l
from flask_login import LoginManager
from flask_mail import Mail

from app.log import Logger
from app import storage

app = Flask(__name__, static_folder='static')
app.config.from_object(os.environ.get('FLASK_ENV') or 'config.DevelopmentConfig')
mail = Mail(app)
login = LoginManager()
babel = Babel(app)
logger = Logger()

storage.init_app(app)
login.init_app(app)
login.login_view = 'auth.login'
login.login_message = _l('Please log in to access this page.')


@login.user_loader
def load_user(user_id):
    return storage.database.models.User.query.filter_by(id=user_id).first()


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


from app import auth
from app import api
from app import web
from app.admin import admin, init_app as admin_init_app
from . import cli

admin_init_app(app)

app.register_blueprint(api.app)
app.register_blueprint(auth.app)
app.register_blueprint(web.app)
