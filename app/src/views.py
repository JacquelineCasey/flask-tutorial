# Adds all of the pages of the site to the flask app object.

from flask import render_template, redirect, url_for
from os import getenv
from app.src.login import require_password, add_login_system


# Adds all views to the app object. Called in main.py
def add_views(app):
    # Sets up the login and logout pages
    add_login_system(app, login_route="/login", logout_route="/logout")

    # Homepage
    @app.route("/")
    def home_page():
        return render_template('index.html')

    # Sample HTML page (non template)
    @app.route("/sample")
    def sample():
        return render_template('sample.html')

    # Old Homepage (Add /deprecated to url)
    @app.route("/deprecated")
    def old_view():
        return "<h1>Welcome to my website! :D </h1>"

    # A demonstration of environment variables
    @app.route("/environment")
    def env_check():
        message = getenv("EFLASK_MESSAGE")
        if message is None:
            return "<h1>Checking environment variable $MESSAGE: No variable found </h1>"
        else:
            return "<h1>Checking environment variable $MESSAGE: " + message + " </h1>"
    
    # A demonstration of a redirect response.
    @app.route("/redirect")
    def redirecting_page():
        return redirect(url_for("old_view"))
    
    # A secret page that tests out the login feature.
    @app.route("/secret")
    @require_password # This temporarily redirects to /login, but bounces back
    def secret():
        return "<h1> You got to my secret page! </h1>"
