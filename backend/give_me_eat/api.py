"""
api.py  
- provides the API endpoints for consuming and producing
  REST requests and responses
"""

from flask import Blueprint, jsonify, request
from .models import db, Restaurant, User
from flask_login import current_user, login_user

api = Blueprint('api', __name__)

@api.route('/hello/<string:name>/')
def say_hello(name):  
    response = { 'msg': "Hello {}".format(name) }
    return jsonify(response)

@api.route("/restaurant/zip/<int:zipcode>/")
def get_restaurant(zipcode):
    restaurants = Restaurant.query.all()
    response = { "restaurants": [r.to_dict() for r in restaurants] }
    return jsonify(response)

@api.route("/restaurant/id/<int:id>")
def get_restaurant_id(id):
    restaurant = Restaurant.query.get(id)
    response = { "restaurant" : restaurant.to_dict()}
    return jsonify(response)