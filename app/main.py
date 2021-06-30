
# Following the tutorial here: https://www.geeksforgeeks.org/deploy-python-flask-app-on-heroku/

from flask import Flask
  
app = Flask(__name__)
  
@app.route("/")
def home_view():
    return "<h1>Welcome to my website! :D </h1>"
