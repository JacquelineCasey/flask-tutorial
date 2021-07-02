# Setups the login/logout system and a way to require it for accessing a page.
# See https://flask.palletsprojects.com/en/2.0.x/quickstart/#sessions

from flask import request, session, redirect, render_template, url_for
from functools import wraps


# Adds the login and logout pages. Called in views.py
def add_login_system(app, login_route, logout_route):
    # This is required to be set before 
    app.secret_key = b'a_very_secret_key'
    
    # The login page
    @app.route(login_route, methods=["GET", "POST"])
    def login():
        if request.method == "GET":
            # Temporary solution
            return render_template("login.html")
        elif request.method == "POST":
            # Extremely Temporary Password
            if request.form["password"] == "testpassword":
                # Session (dictionary) sends an encrypted cooke upon modification
                session["logged_in"] = True; 

                # Send to original target, otherwise send to homepage
                if "next" in request.args:
                    return redirect(request.args["next"])
                else:
                    return redirect(url_for("home_page"))
            else:
                return "<h1> WRONG PASSWORD </h1>"
    
    # The logout page
    @app.route(logout_route)
    def logout():
        # remove the username from the session if it's there
        session.pop('logged_in', None)
        return redirect(url_for('home_page'))

# This decorator is used  to make a function require a password.
# Put this below the @app.route() decorator.
def require_password(wrapped_func):
    @wraps(wrapped_func)
    def wrapper_check_login(*args, **kwargs):
        if "logged_in" not in session or session["logged_in"] is not True:
            # next sets up the url parameter (any name works?)
            return redirect(url_for("login", next=request.url))
        return wrapped_func(*args, **kwargs)
    return wrapper_check_login
