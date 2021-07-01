# Following the tutorial here: https://www.geeksforgeeks.org/deploy-python-flask-app-on-heroku/

from flask import Flask, render_template, url_for, redirect, session, request
import os # For checking environment variables
import functools

# This app uses the functions with the @app.route() decorator.
app = Flask(__name__) 


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
    message = os.getenv("MESSAGE")
    if message is None:
        return "<h1>Checking environment variable $MESSAGE: No variable found </h1>"
    else:
        return "<h1>Checking environment variable $MESSAGE: " + message + " </h1>"

# A demonstration of a redirect response.
# url_for() determines the url given the FUNCTION NAME of the endpoint, so
# "old_view" redirects to the /deprecated site.
@app.route("/redirect")
def redirecting_page():
    return redirect(url_for("old_view"))


### Sessions and Security (Basic Security, anyways) ###

# This is used for signing the session cookies, and should be kept VERY SECRET 
# (and generated to be MUCH better)
app.secret_key = b'a_very_secret_key'

# See https://flask.palletsprojects.com/en/2.0.x/quickstart/#sessions
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        # Temporary solution
        return '''
        <form method="post">
            <p><input type=text name=password>
            <p><input type=submit value=Login>
        </form>
    '''
    elif request.method == "POST":
        # Extremely Temporary Password
        if request.form["password"] == "testpassword":
            # Adjust current session cookie (Python dictionary that is aware it is accessed)
            session["logged_in"] = True; # This is encrypted and sent
            return redirect(url_for("secret"))
        else:
            return "<h1> WRONG PASSWORD </h1>"

# I am definining my own decorator here, for requiring functions to have a login
def require_password(wrapped_func):
    @functools.wraps(wrapped_func)
    def wrapper_check_login(*args, **kwargs):
        if "logged_in" not in session or session["logged_in"] is not True:
            return redirect(url_for("login"))
        return wrapped_func(*args, **kwargs)
    return wrapper_check_login

@app.route("/secret")
@require_password
def secret():
    return "<h1> You got to my secret page! </h1>"

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('logged_in', None)
    return redirect(url_for('home_page'))
