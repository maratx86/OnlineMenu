from flask import Blueprint, request, jsonify, g

app = Blueprint('web', __name__, template_folder='templates', static_folder='static')

import app.web.views as views
