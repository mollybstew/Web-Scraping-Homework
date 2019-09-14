# import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


# create instance of Flask app
app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mission_to_mars")

# create route that renders index.html template
@app.route("/")
def index():
    destination_data = mongo.db.collection.find_one()
    return render_template("index.html",mars_collection_values = destination_data)

@app.route('/scrape')
def scrape():
    data = scrape_mars.scrape()
    mongo.db.collection.update({}, data, upsert=True)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)