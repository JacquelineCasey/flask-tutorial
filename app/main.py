# Following the tutorial here: https://www.geeksforgeeks.org/deploy-python-flask-app-on-heroku/

from flask import Flask
from src.pages import add_pages

# This app uses the functions with the @app.route() decorator.
app = Flask(__name__) 

add_pages(app)
