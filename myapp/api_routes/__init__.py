from flask import Blueprint
api_routes = Blueprint('api_routes', __name__)

# list of all router files
from .index import *
from .user import *