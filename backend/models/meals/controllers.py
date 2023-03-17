from flask import jsonify, request, Blueprint
from flask_jwt_extended import JWTManager
from models.meals.model import Meal
from models.db import db


# an instance of the blue print
meals = Blueprint('meals', __name__, url_prefix='/meals')


@meals.route("/create", methods=["POST"])
def create():
    d_name=request.json["name"] 
    d_reg_by=request.json["reg_by"]
    # d_updated_by=request.json["updated_by"]
    d_serving_time=request.json["serving_time"]
    d_Meals_description=request.json["Meals_description"] 
    

    if not d_name:
        return ({"message":"The name is required"}, 400)
    if not d_reg_by:
        return ({"message":"The reg_by is required"}, 400)
    # if not d_updated_by:
    #     return ({"message":"The Meals updated_by is required"}, 400)
    if not d_serving_time:
        return ({"message":"The region id is required"}, 400)
    if not d_Meals_description:
        return ({"message":"The Meals description is required"}, 400)
    

    # Working on the conflicts
    if Meal.query.filted_by(meal_description=d_Meals_description).first():
        return {"message":"Sorry, Meals_description already in use"}, 400
    
    
    new_Meal = Meal(name=d_name,
                             reg_by=d_reg_by,
                            #  updated_by=d_updated_by,
                             serving_time=d_serving_time, 
                             meal_description=d_Meals_description)
    db.session.add(new_Meal)
    db.session.commit()

    return f"You successfully added the Meals {new_Meal.id}"

@meals.route("/all")
def all_meals():
    #return "This is from the first Meals route"
    meals= Meal.query.all()
    results = [
        {
            "name":meal.name,
            "reg_by":meal.reg_by,
            "updated_by":meal.updated_by
        }for meal in meals]
    
    return {"count":len(results), "meals":results} 

@meals.route("/get_Meals/<id>")
def get_Meals(id):
    meal=Meal.query.get_od_404(id)
    meal_details={
        "name":meal.name,
        "reg_by":meal.reg_by,
        "updated_by":meal.updated_by,
        "meal_description":meal.description
                        }
    return {f"meal {meal.id}":meal_details}

@meals.route("/delete_Meals/<id>")
def delete(id):
    delete_Meal=Meal.query.delete(id)
    # if delete_Meals is None:
    #     return{"message":"Specified id not found"}, 404
    # else:
    db.session.delete(id)
    db.session.commit()
    return {"message":"successfully deleted specified Meals"}, 200