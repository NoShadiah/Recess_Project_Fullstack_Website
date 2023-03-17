from flask import jsonify, request, Blueprint
from flask_jwt_extended import JWTManager
from models.divisions.model import Division
from models.db import db


# an instance of the blue print
divisions = Blueprint('divisions', __name__, url_prefix='/divisions')


@divisions.route("/create", methods=["POST"])
def create():
    div_name=request.json["name"] 
    div_reg_by=request.json["reg_by"]
    div_updated_by=request.json["updated_by"]
    div_district_id=request.json["district_id"] 
    

    if not div_name:
        return ({"message":"The name is required"}, 400)
    if not div_reg_by:
        return ({"message":"The reg_by is required"}, 400)
    if not div_updated_by:
        return ({"message":"The Division updated_by is required"}, 400)
    if not div_district_id:
        return ({"message":"The district id is required"}, 400)
    

    # Working on the conflicts
    if Division.query.filtediv_by(name=div_name).first():
        return {"message":"Sorry, name already in existing"}, 400
    
    
    new_Division = Division(name=div_name, reg_by=div_reg_by,updated_by=div_updated_by,district_id=div_district_id)
    db.session.add(new_Division)
    db.session.commit()

    return f"You successfully added the division {new_Division.id}"

@divisions.route("/all")
def all_divisions():
    #return "This is from the first Division route"
    divisions= Division.query.all()
    results = [
        {
            "name":Division.name,
            "reg_by":Division.reg_by,
            "updated_by":Division.updated_by
        }for Division in divisions]
    
    return {"count":len(results), "divisions":results} 

@divisions.route("/get_Division/<id>")
def get_division(id):
    Division=Division.query.get_odiv_404(id)
    Division_details={
        "name":Division.name,
        "reg_by":Division.reg_by,
        "updated_by":Division.updated_by,
        "opens at":Division.district_id
        }
    return {f"Division {Division.id}":Division_details}

@divisions.route("/delete_Division/<id>")
def delete(id):
    delete_division=Division.query.delete(id)
    # if delete_division is None:
    #     return{"message":"Specified id not found"}, 404
    # else:
    db.session.delete(id)
    db.session.commit()
    return {"message":"successfully deleted specified"}, 200