from flask import Blueprint

app = Blueprint('auth', __name__, template_folder='templates', static_folder='static', url_prefix='/auth')


from .views import index
