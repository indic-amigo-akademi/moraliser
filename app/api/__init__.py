from flask_restful import Api
from flask import Blueprint

api_bp = Blueprint('api_bp', __name__, url_prefix='/api')
api_rest = Api(api_bp)

from .user_route import *
from .chat_route import *