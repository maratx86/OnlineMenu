from os.path import basename

from flask import redirect, url_for
from flask_admin import AdminIndexView, expose
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

from .. import logger
import config


class AdminBashBoardView(AdminIndexView):
    @expose('/')
    def index(self):
        logger.info('admin index (success): {} admins: {}'.format(current_user, config.admins_email))
        return self.render(
            'admin/index.html',
        )

    def inaccessible_callback(self, name, **kwargs):
        logger.info('admin index (fail): {} admins: {}'.format(current_user, config.admins_email))
        return redirect(url_for('auth.login'))

    def is_accessible(self):
        if not current_user.is_authenticated:
            return False
        if current_user.email not in config.admins_email:
            return False
        return True


class SecureModelView(ModelView):
    def inaccessible_callback(self, name, **kwargs):
        logger.info('admin entity <{}> (failed): {}'.format(self.endpoint, current_user))
        return redirect(url_for('auth.login'))

    def render(self, template, **kwargs):
        logger.info('admin entity <{}> (render): {}'.format(self.endpoint, current_user))
        return super(SecureModelView, self).render(template, **kwargs)

    def is_accessible(self):
        if not current_user.is_authenticated:
            return False
        if current_user.email not in config.admins_email:
            return False
        return True


class SecureFileAdmin(FileAdmin):
    def __init__(self, *args, **kwargs):
        super(SecureFileAdmin, self).__init__(*args, **kwargs)
        self.view_name = 'SecureFileAdmin'

    def render(self, template, **kwargs):
        logger.info('admin file <{}> (render): {}'.format(self.view_name, current_user))
        return super(SecureFileAdmin, self).render(template, **kwargs)

    def inaccessible_callback(self, name, **kwargs):
        logger.info('admin file <{}> (fail): {}'.format(self.view_name, current_user))
        return redirect(url_for('auth.login'))

    def is_accessible(self):
        if not current_user.is_authenticated:
            return False
        if current_user.email not in config.admins_email:
            return False
        return True


class Static(SecureFileAdmin):
    def __init__(self, *args, **kwargs):
        super(SecureFileAdmin, self).__init__(*args, **kwargs)
        self.view_name = 'Static'


class Log(SecureFileAdmin):
    def __init__(self, *args, **kwargs):
        super(SecureFileAdmin, self).__init__(*args, **kwargs)
        self.view_name = 'Logging'
        self.can_upload = True
        self.can_mkdir = False

    def delete_file(self, file_path):
        filename = basename(file_path)
        logger.info(filename)
        if filename not in ('debug.log', 'info.log', 'warning.log', 'error.log', 'critical.log'):
            super(Log, self).delete_file(file_path)
            return
        mode = basename(file_path).split('.')[0]
        logger.close_file(mode)
        super(Log, self).delete_file(file_path)
        logger.open_file(mode)

    def on_rename(self, full_path, dir_base, filename):
        old_file = basename(full_path)
        if old_file in ('debug.log', 'info.log', 'warning.log', 'error.log', 'critical.log'):
            mode = old_file.split('.')[0]
            logger.open_file(mode)

    def render(self, template, **kwargs):
        if template == self.rename_template:
            name = kwargs.get('name')
            if name in ('debug.log', 'info.log', 'warning.log', 'error.log', 'critical.log'):
                mode = name.split('.')[0]
                logger.close_file(mode)
        return super(Log, self).render(template, **kwargs)


