
# Imports
##########

from . import db
from .base import Base

###############################################################################


# User Class
#############

class User(Base):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255), unique = True)

###############################################################################
