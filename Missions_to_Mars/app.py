# Jadd Cheng
# October 15, 2019
# See activity 7.
# See craigslist example.
# jinja doesn't like HTML comments!

# Import dependencies.
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create Flask instance.
app = Flask(__name__)

# NB mars_app --> db name. flaskpymongo --> looks for this. need to add db you want to connect to.
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)
# app.config is a dict object.

# home page
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    # run scrape function and save the results. should return dict.
    mars = mongo.db.mars

    # Run scrape method of scrape_mars function. Save to var.
    mars_data = scrape_mars.scrape()
    
    # Update mongo database. what is field you're matching against.'
    mongo.db.mars.update({}, mars_data, upsert=True)

    # After scrape return to homepage.
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)