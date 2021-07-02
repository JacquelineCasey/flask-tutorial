# The main file for the project

from flask import Flask
from app.src.pages import add_pages


# Creates the app object. It is run automatically by flask or gunicorn, so there
# is no need to explicitely call app.run().
app = Flask(__name__) 

# Adds pages to the app object.
add_pages(app)
