# The main file for the project

from flask import Flask
from app.src.views import add_views


# Creates the app object. It is run automatically by flask or gunicorn, so there
# is no need to explicitely call app.run().
app = Flask(__name__) 

# Adds views to the app object.
add_views(app)
