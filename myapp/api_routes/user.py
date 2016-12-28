
# Imports
##########

from flask import current_app
from . import api_routes

###############################################################################

# Routes
#########

@api_routes.route('/users', methods=['GET', 'POST'])
def users():
	current_app.logger.info('/api/v1/users')

	return "this is /api/v1/users"

###############################################################################
