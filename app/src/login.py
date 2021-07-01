
from flask import request, session, redirect, url_for
from functools import wraps

def add_login_system(app, login_route, logout_route):
    # This is used for signing the session cookies, and should be kept VERY SECRET 
    # (and generated to be MUCH better)
    app.secret_key = b'a_very_secret_key'
    
    # See https://flask.palletsprojects.com/en/2.0.x/quickstart/#sessions
    @app.route(login_route, methods=["GET", "POST"])
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
                # Session (dictionary) sends an encrypted cooke upon modification
                session["logged_in"] = True; 

                # Send to original target, otherwise send to homepage
                if "next" in request.args:
                    return redirect(request.args["next"])
                else:
                    return redirect(url_for("home_page"))
            else:
                return "<h1> WRONG PASSWORD </h1>"
    
    @app.route(logout_route)
    def logout():
        # remove the username from the session if it's there
        session.pop('logged_in', None)
        return redirect(url_for('home_page'))
    

# I am definining my own decorator here, for requiring functions to have a login
def require_password(wrapped_func):
    @wraps(wrapped_func)
    def wrapper_check_login(*args, **kwargs):
        if "logged_in" not in session or session["logged_in"] is not True:
            # next sets up the url parameter (any name works?)
            return redirect(url_for("login", next=request.url))
        return wrapped_func(*args, **kwargs)
    return wrapper_check_login