# Following the tutorial here: https://www.geeksforgeeks.org/deploy-python-flask-app-on-heroku/

from flask import Flask, render_template
import os # For checking environment variables.


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
