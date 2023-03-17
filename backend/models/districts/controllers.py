from flask import jsonify, request, Blueprint
from flask_jwt_extended import JWTManager
from models.districts.model import District
from models.db import db


# an instance of the blue print
districts = Blueprint('districts', __name__, url_prefix='/districts')


@districts.route("/create", methods=["POST"])
def create():
    d_name=request.json["name"] 
    d_reg_by=request.json["reg_by"]
    # d_updated_by=request.json["updated_by"]
    d_region_id=request.json["region_id"]
    d_district_code=request.json["district_code"] 
    

    if not d_name:
        return ({"message":"The name is required"}, 400)
    if not d_reg_by:
        return ({"message":"The reg_by is required"}, 400)
    # if not d_updated_by:
    #     return ({"message":"The District updated_by is required"}, 400)
    if not d_region_id:
        return ({"message":"The region id is required"}, 400)
    if not d_district_code:
        return ({"message":"The district code is required"}, 400)
    

    # Working on the conflicts
    if District.query.filted_by(district_code=d_district_code).first():
        return {"message":"Sorry, district_code already in use"}, 400
    
    
    new_District = District(name=d_name,
                             reg_by=d_reg_by,
                            #  updated_by=d_updated_by,
                             region_id=d_region_id, 
                             district_code=d_district_code)
    db.session.add(new_District)
    db.session.commit()

    return f"You successfully added the district {new_District.id}"

@districts.route("/all")
def all_districts():
    #return "This is from the first District route"
    districts= District.query.all()
    results = [
        {
            "name":District.name,
            "reg_by":District.reg_by,
            "updated_by":District.updated_by
        }for District in districts]
    
    return {"count":len(results), "districts":results} 

@districts.route("/get_District/<id>")
def get_district(id):
    district=District.query.get_od_404(id)
    District_details={
        "name":district.name,
        "reg_by":district.reg_by,
        "updated_by":district.updated_by,
        "district_code":district.district
                        }
    return {f"District {district.id}":District_details}

@districts.route("/delete_District/<id>")
def delete(id):
    delete_district=District.query.delete(id)
    # if delete_district is None:
    #     return{"message":"Specified id not found"}, 404
    # else:
    db.session.delete(id)
    db.session.commit()
    return {"message":"successfully deleted specified district"}, 200