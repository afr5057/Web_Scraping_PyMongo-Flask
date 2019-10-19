# Import Dependencies 
from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/marsDatabase")


@app.route("/")
def home(): 
    mars_info = mongo.db.collection.find_one()
    print(mars_info)
    return render_template("index.html", mars=mars_info)

@app.route("/scrape")
def newhome(): 
    mars_info = scrape_mars.mars_rescrape()
    mongo.db.collection.update({}, mars_info, upsert=True)
    return redirect("/")

if __name__ == "__main__": 
    app.run(debug=True)