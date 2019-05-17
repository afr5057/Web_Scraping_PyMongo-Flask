# Import Dependencies 
from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
# from flask_flatpages import FlatPages
# need to research: https://nicolas.perriault.net/code/2012/dead-easy-yet-powerful-static-website-generator-with-flask/
# https://stevenloria.com/hosting-static-flask-sites-on-github-pages/
import scrape_mars
import os

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

# Create route that renders index.html template and finds documents from mongo
@app.route("/")
def home(): 

    # Find data
    mars_info = mongo.db.mars_info.find_one()

    # Return template and data
    return render_template("index.html", mars_info=mars_info)

# Route that will trigger scrape function
@app.route("/scrape")
def newhome(): 

    # Find data
    mars_info = mongo.db.mars_info.find_one()

    # Return template and data
    return render_template("index.html", mars_info=mars_info)

if __name__ == "__main__": 
    app.run(port=8000)