from flask import jsonify, request, Blueprint
from flask_jwt_extended import JWTManager
from models.menu.model import MenuItem
from models.db import db


# an instance of the blue print
menu = Blueprint('menu', __name__, url_prefix='/menu')


@menu.route("/create", methods=["POST"])
def create():
    item_name=request.json["name"] 
    item_reg_by=request.json["reg_by"]
    # item_updateitem_by=request.json["updateitem_by"]
    item_image=request.json["image"]
    item_description=request.json["description"] 
    

    if not item_name:
        return ({"message":"The name is required"}, 400)
    if not item_reg_by:
        return ({"message":"The reg_by is required"}, 400)
    # if not item_updateitem_by:
    #     return ({"message":"The menu updateitem_by is required"}, 400)
    if not item_image:
        return ({"message":"The region id is required"}, 400)
    if not item_description:
        return ({"message":"The menu description is required"}, 400)
    

    # Working on the conflicts
    if MenuItem.query.filter_by(name=item_name).first():
        return {"message":"Sorry, Menu Item name already in use"}, 400
    
    
    newMenuItem = MenuItem(name=item_name,
                             reg_by=item_reg_by,
                            #  updateitem_by=item_updateitem_by,
                             image=item_image, 
                             MenuItem_description=item_description)
    db.session.add(newMenuItem)
    db.session.commit()

    return f"You successfully added the MenuItem with id {newMenuItem.id}"

@menu.route("/all")
def all_menu():
    #return "This is from the first menu route"
    menu= MenuItem.query.all()
    results = [
        {
            "name":item.name,
            "reg_by":item.reg_by,
            "updateitem_by":item.updateitem_by
        }for item in menu]
    
    return {"count":len(results), "menu":results} 

@menu.route("/get_MenuItem/<id>")
def get_MenuItem(id):
    item=MenuItem.query.get_oitem_404(id)
    item_details={
        "name":item.name,
        "reg_by":item.reg_by,
        "updated_by":item.updateitem_by,
        "item_description":item.description
                        }
    return {f"Item {item.id}":item_details}

@menu.route("/delete_MenuItem/<id>")
def delete(id):
    delete_MenuItem=MenuItem.query.delete(id)
    # if delete_menu is None:
    #     return{"message":"Specified id not found"}, 404
    # else:
    db.session.delete(id)
    db.session.commit()
    return {"message":"successfully deleted specified MenuItem"}, 200