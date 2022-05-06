from os import path as __path
from flask_admin import Admin

import config
from app import logger
import app.storage as storage
import app.admin.views as views

admin = Admin(name='Online Menu', template_mode='bootstrap3')


def init_app(app):
    admin.init_app(app, index_view=views.AdminBashBoardView())
    admin.add_view(views.SecureModelView(storage.database.models.User, storage.db.session, name='Users'))
    path = __path.join(config.basedir, 'app', 'static')
    path_log = __path.join(config.basedir, 'log')
    admin.add_view(views.Static(path, name='Static Files'))
    admin.add_view(views.Log(path_log, name='Log Files'))

