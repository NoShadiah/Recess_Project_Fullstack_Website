from flask import jsonify, request, Blueprint
from flask_jwt_extended import JWTManager
from models.food_categories.model import Category
from models.db import db


# an instance of the blue print
categories = Blueprint('categories', __name__, url_prefix='/categories')


@categories.route("/create", methods=["POST"])
def create():
    c_name=request.json["name"] 
    c_reg_by=request.json["reg_by"]
    # c_updatec_by=request.json["updatec_by"]
    c_image=request.json["image"]
    c_description=request.json["description"] 
    

    if not c_name:
        return ({"message":"The name is required"}, 400)
    if not c_reg_by:
        return ({"message":"The reg_by is required"}, 400)
    # if not c_updatec_by:
    #     return ({"message":"The categories updatec_by is required"}, 400)
    if not c_image:
        return ({"message":"The region id is required"}, 400)
    if not c_description:
        return ({"message":"The categories description is required"}, 400)
    

    # Working on the conflicts
    if Category.query.filtec_by(category_name=c_name).first():
        return {"message":"Sorry, category_name already in use"}, 400
    
    
    newCategory = Category(name=c_name,
                             reg_by=c_reg_by,
                            #  updatec_by=c_updatec_by,
                             image=c_image, 
                             category_description=c_description)
    db.session.add(newCategory)
    db.session.commit()

    return f"You successfully added the category with id {newCategory.id}"

@categories.route("/all")
def all_categories():
    #return "This is from the first categories route"
    categories= Category.query.all()
    results = [
        {
            "name":category.name,
            "reg_by":category.reg_by,
            "updatec_by":category.updatec_by
        }for category in categories]
    
    return {"count":len(results), "categories":results} 

@categories.route("/get_category/<id>")
def get_category(id):
    category=Category.query.get_oc_404(id)
    category_details={
        "name":category.name,
        "reg_by":category.reg_by,
        "updated_by":category.updatec_by,
        "category_description":category.description
                        }
    return {f"Category {category.id}":category_details}

@categories.route("/delete_category/<id>")
def delete(id):
    delete_Category=Category.query.delete(id)
    # if delete_categories is None:
    #     return{"message":"Specified id not found"}, 404
    # else:
    db.session.delete(id)
    db.session.commit()
    return {"message":"successfully deleted specified category"}, 200