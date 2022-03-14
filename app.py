from faulthandler import dump_traceback
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping
import os

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri = "mongodb://localhost:27017/mars_app")

@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   print (os.curdir)
   #return "<!DOCTYPE HTML><head><meta charset=\"utf-8\"></head><body>" + render_template(os.getcwd() + "\\class\\Mission_to_Mars\\index.html")+ "<br />"
   return render_template("index.html", mars = mars)
   #return render_template("class/Mission_to_Mars/index.html", mars=mars) + os.curdir

@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update_one({}, {"$set":mars_data}, upsert=True)
   return redirect('/', code=302)

if __name__ == "__main__":
   app.debug = True
   app.run()