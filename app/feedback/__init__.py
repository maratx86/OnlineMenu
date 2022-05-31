from flask import Blueprint, request, jsonify

app = Blueprint('feedback', __name__, url_prefix='/feedback')

from .views import index
