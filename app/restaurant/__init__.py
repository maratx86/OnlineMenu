from flask import Blueprint, request, jsonify, g

app = Blueprint('r', __name__, url_prefix='/r')

import app.restaurant.views as views
