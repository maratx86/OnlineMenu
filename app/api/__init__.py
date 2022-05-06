from flask import Blueprint, request, jsonify

app = Blueprint('api', __name__, url_prefix='/api')

from .views import index
