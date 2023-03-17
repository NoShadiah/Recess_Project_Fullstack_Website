from flask import jsonify, request, Blueprint
from flask_jwt_extended import JWTManager
from models.regions.model import Region
from models.db import db


# an instance of the blue print
regions = Blueprint('regions', __name__, url_prefix='/regions')


@regions.route("/create", methods=["POST"])
def create():
    r_name=request.json["name"] 
    r_reg_by=request.json["reg_by"]
    r_updated_by=request.json["updated_by"]
    r_country=request.json["country"] 
    

    if not r_name:
        return ({"message":"The name is required"}, 400)
    if not r_reg_by:
        return ({"message":"The reg_by is required"}, 400)
    if not r_updated_by:
        return ({"message":"The Region updated_by is required"}, 400)
    if not r_country:
        return ({"message":"The opening time is required"}, 400)
    

    # Working on the conflicts
    if Region.query.filter_by(updated_by=r_updated_by).first():
        return {"message":"Sorry, updated_by already in use"}, 400
    
    
    new_Region = Region(name=r_name, reg_by=r_name,updated_by=r_updated_by,country=r_country)
    db.session.add(new_Region)
    db.session.commit()

    return f"You successfully added the user {new_Region.id}"

@regions.route("/all")
def all_regions():
    #return "This is from the first Region route"
    regions= Region.query.all()
    results = [
        {
            "name":Region.name,
            "reg_by":Region.reg_by,
            "updated_by":Region.updated_by
        }for Region in regions]
    
    return {"count":len(results), "regions":results} 

@regions.route("/get_Region/<id>")
def get_user(id):
    Region=Region.query.get_or_404(id)
    Region_details={
        "name":Region.name,
        "reg_by":Region.reg_by,
        "updated_by":Region.updated_by,
        "opens at":Region.country
        }
    return {f"Region {Region.id}":Region_details}

@regions.route("/delete_Region/<id>")
def delete(id):
    delete_user=Region.query.delete(id)
    # if delete_user is None:
    #     return{"message":"Specified id not found"}, 404
    # else:
    db.session.delete(id)
    db.session.commit()
    return {"message":"successfully deleted specified"}, 200