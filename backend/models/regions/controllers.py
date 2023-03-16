from flask import jsonify, request, Blueprint
from flask_jwt_extended import JWTManager
from models.settings.model import Restaurant
from models.db import db


# an instance of the blue print
restaurants = Blueprint('restaurants', __name__, url_prefix='/restaurants')


@restaurants.route("/create", methods=["POST"])
def create():
    r_name=request.json["name"] 
    r_location=request.json["location"]
    r_contact=request.json["contact"]
    r_opening_hrs=request.json["opening_hrs"] 
    r_closing_hrs=request.json["closing_hrs"]

    if not r_name:
        return ({"message":"The name is required"}, 400)
    if not r_location:
        return ({"message":"The location is required"}, 400)
    if not r_contact:
        return ({"message":"The restaurant contact is required"}, 400)
    if not r_opening_hrs:
        return ({"message":"The opening time is required"}, 400)
    if not r_closing_hrs:
        return ({"message":"The closing time is required"}, 400)

    # Working on the conflicts
    if Restaurant.query.filter_by(contact=r_contact).first():
        return {"message":"Sorry, contact already in use"}, 400
    
    
    new_restaurant = Restaurant(name=r_name, location=r_name,contact=r_contact,opening_hrs=r_opening_hrs, closing_hrs=r_closing_hrs)
    db.session.add(new_restaurant)
    db.session.commit()

    return f"You successfully added the user {new_restaurant.id}"

@restaurants.route("/all")
def all_restaurants():
    #return "This is from the first restaurant route"
    restaurants= Restaurant.query.all()
    results = [
        {
            "name":restaurant.name,
            "location":restaurant.location,
            "contact":restaurant.contact
        }for restaurant in restaurants]
    
    return {"count":len(results), "restaurants":results} 

@restaurants.route("/get_restaurant/<id>")
def get_user(id):
    restaurant=Restaurant.query.get_or_404(id)
    restaurant_details={
        "name":restaurant.name,
        "location":restaurant.location,
        "contact":restaurant.contact,
        "opens at":restaurant.opening_hrs,
        "closes at":restaurant.closing_hrs
    }
    return {f"Restaurant {restaurant.id}":restaurant_details}

@restaurants.route("/delete_restaurant/<id>")
def delete(id):
    delete_user=Restaurant.query.delete(id)
    # if delete_user is None:
    #     return{"message":"Specified id not found"}, 404
    # else:
    db.session.delete(id)
    db.session.commit()
    return {"message":"successfully deleted specified"}, 200