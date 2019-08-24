# import necessary libraries
from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape

# create instance of Flask app
app = Flask(__name__)

# create mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_data")
mongo.db.collection.drop()

@app.route("/")
def home():
    mars_data = mongo.db.collection.find_one()
    return  render_template('index.html', mars_data=mars_data)

@app.route("/scrape")
def web_scrape():
    mongo.db.collection.remove({})
    mars_data = scrape.scrape()
    mongo.db.collection.insert_one(mars_data)
    return  render_template('scrape.html')

if __name__ == "__main__":
    app.run(debug=True)