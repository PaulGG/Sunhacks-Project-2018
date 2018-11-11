"""
api.py  
- provides the API endpoints for consuming and producing
  REST requests and responses
"""

from flask import Blueprint, jsonify, request
from .models import db, Restaurant, User
from flask_login import current_user, login_user
from .yelp import request, API_HOST, SEARCH_PATH, API_KEY
import random

api = Blueprint('api', __name__)

@api.route('/hello/<string:name>/')
def say_hello(name):  
    response = { 'msg': "Hello {}".format(name) }
    return jsonify(response)

@api.route("/restaurant/lookup/<string:location>/<int:distance>/<int:price>")
@api.route("/restaurant/lookup/<int:location>/<int:distance>/<int:price>")
def get_restaurant(location, distance, price):
    distance = int(distance * 1609.344)
    print(distance)
    print(location)
    print(price)
    switcher = {
        1:"1,2,3,4",
        2:"2,1,3,4",
        3:"3,2,1,4",
        4:"4,3,2,1"
    }
    price = switcher[price]

    yelpstuff = request(API_HOST, SEARCH_PATH, API_KEY, 
    {
     "location" : location,
     "radius" : distance, 
     "sort_by" : "rating", 
     "open_now" : "true",
     "term" : "restaurants",
     "price" : price   
    }
    )
    if "error" in yelpstuff:
        return jsonify({"error" : "Something went wrong with the api call :("})
    businesses = yelpstuff["businesses"]
    jsons = []
    keywords = ["alias", "name", "image_url", "url", "review_count", "rating"]
    # get the first 3 objects from the yelp api call.
    for i in range(3):
        jsonObject = {}
        ran = random.randint(0, len(businesses) - 1) 
        for word in keywords:
            jsonObject[word] = businesses[ran][word]
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
