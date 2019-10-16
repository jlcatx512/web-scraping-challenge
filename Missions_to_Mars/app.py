# Jadd Cheng
# October 15, 2019

# Import dependencies.
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create Flask instance.
app = Flask(__name__)

# NB mars_app --> db name. flask_pymongo looks for this. Need to specify db you want to connect to.
# app.config is a dict object.
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# home page
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

# scrape page
@app.route("/scrape")
def scrape():
    # Run scrape function and save the results to a variable. Return dictionary.
    mars = mongo.db.mars

    # Run scrape method of scrape_mars function. Save results to a variable.
    mars_data = scrape_mars.scrape()
    
    # Update mongo database.
    mongo.db.mars.update({}, mars_data, upsert=True)

    # After scrape return to homepage.
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)