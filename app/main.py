# Following the tutorial here: https://www.geeksforgeeks.org/deploy-python-flask-app-on-heroku/

from flask import Flask


# This app uses the functions with the @app.route() decorator.
# Additionally, Procfile tells gunicorn to run this variable.
app = Flask(__name__) 
  
  
# Homepage
@app.route("/")
def home_page():
    return "<h1> This is the homepage. </h1>"

# Old Homepage (Add /deprecated to url)
@app.route("/deprecated")
def old_view():
    return "<h1>Welcome to my website! :D </h1>"


# Runs the app
if __name__ == "__main__":
    app.run()
