# See activity 7.

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

# redirect --> website that doesn't exist.
scrape
index.html

app = Flask(__name__)

mongodb://localhost:27017
app.py --> center of universe for Flask

# when you incorporate HTML CSS and JS

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# mongo used to interact with db. --> mongo.db. --> db understood from URI. 
# collections.
# NB --> mars_app. create if not exist?

flaskpymongo --> looks for this.
need to add db you want to connect to.

@app.route("/")
def index():
    return render_template("index.html", ...)

@app.route("scrape")
def scrape()

    # run scrape function and save the results.
    mars_data = scrape_mars.scrape()

if __name__ == "__main__":
    print(xxx)