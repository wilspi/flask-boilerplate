
# Imports
##########

from flask import abort, Flask, request

from myapp.utils import get_instance_folder_path
from myapp.api_routes import *
from myapp.config import configure_app
from myapp.models import db

###############################################################################


# Initialise
#############

app = Flask(
    __name__,
    instance_path=get_instance_folder_path(),
    instance_relative_config=True)

configure_app(app) # load configurations
db.init_app(app) # init app to db

###############################################################################


# Error Handling
#################

@app.errorhandler(404)
def page_not_found(error):
    app.logger.error('Page not found: %s', (request.path, error))
    return "404"

@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error('Server Error: %s', (error))
    return "500"

@app.errorhandler(Exception)
def unhandled_exception(error):
    app.logger.error('Unhandled Exception: %s', (error))
    return "500"

###############################################################################


# Pre/Post Request Processing
##############################

@app.before_first_request
def initialize_database():
    db.create_all()

###############################################################################


# Routings
###########

@app.route('/')
@app.route('/<lang_code>/')
def home(lang_code=None):
    return "homepage"
    abort(404)


# register all routes
app.register_blueprint(api_routes, url_prefix='/api/v1')

###############################################################################
