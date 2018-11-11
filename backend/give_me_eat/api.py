"""
api.py  
- provides the API endpoints for consuming and producing
  REST requests and responses
"""

from flask import Blueprint, jsonify, request
from .models import db, Restaurant, User
from flask_login import current_user, login_user
from .yelp import request, API_HOST, SEARCH_PATH, API_KEY

api = Blueprint('api', __name__)

@api.route('/hello/<string:name>/')
def say_hello(name):  
    response = { 'msg': "Hello {}".format(name) }
    return jsonify(response)

@api.route("/restaurant/zip/<int:zipcode>/")
def get_restaurant(zipcode):
    yelpstuff = request(API_HOST, SEARCH_PATH, API_KEY, 
    {
     "location" : "85281",
     "radius" : "8000", 
     "sort_by" : "rating", 
     "open_now" : "true",
     "term" : "restaurants",
     "price" : "1,2,3,4"   
    }
    )
    businesses = yelpstuff["businesses"]
    jsons = []
    keywords = ["alias", "name", "image_url", "url", "review_count", "rating"]
    # get the first 3 objects from the yelp api call.
    for i in range(3):
        jsonObject = {}
        for word in keywords:
            jsonObject[word] = businesses[i][word]
        jsons.append(jsonObject)
    response = jsons
    #restaurants = Restaurant.query.all()
    #response = [r.to_dict() for r in restaurants]
    return jsonify(response)

@api.route("/restaurant/id/<int:id>")
def get_restaurant_id(id):
    restaurant = Restaurant.query.get(id)
    response = { "restaurant" : restaurant.to_dict()}
    return jsonify(response)
