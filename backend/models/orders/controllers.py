from flask import jsonify, request, Blueprint
from flask_jwt_extended import JWTManager
from models.orders.model import Order
from models.db import db


# an instance of the blue print
orders = Blueprint('orders', __name__, url_prefix='/orders')


@orders.route("/create", methods=["POST"])
def create():
    
    o_made_by=request.json["made_by"]
    # o_updated_by=request.json["updated_by"]
    o_status=request.json["status"]
    o_quantity=request.json["quantity"] 
    o_grandtotal = request.json["grand total"]
    

    if not o_grandtotal:
        return ({"message":"The grand_total is required"}, 400)
    if not o_made_by:
        return ({"message":"The made_by is required"}, 400)
    # if not o_updated_by:
    #     return ({"message":"The orders updated_by is required"}, 400)
    if not o_status:
        return ({"message":"The order status is required"}, 400)
    if not o_quantity:
        return ({"message":"The order quantity is required"}, 400)
    

    # Working on the conflicts
    # if Order.query.filteo_by(Order_grand_total=o_grandtotal).first():
    #     return {"message":"Sorry, Order_grand_total already in use"}, 400
    
    
    newOrder = Order(grand_total=o_grandtotal,
                             made_by=o_made_by,
                            #  updated_by=o_updated_by,
                             status=o_status, 
                             order_quantity=o_quantity)
    db.session.add(newOrder)
    db.session.commit()

    return f"You successfully added the Order with id {newOrder.id}"

@orders.route("/all")
def all_orders():
    #return "This is from the first orders route"
    orders= Order.query.all()
    results = [
        {
            "grand_total":order.grand_total,
            "made_by":order.made_by,
            "order_status":order.status
        }for order in orders]
    
    return {"count":len(results), "orders":results} 

@orders.route("/get_Order/<id>")
def get_Order(id):
    order=Order.query.get_oo_404(id)
    order_details={
        "grand_total":order.grand_total,
        "made_by":order.made_by,
        "order_status":order.status,
        "order_quantity":order.quantity
                        }
    return {f"Order {order.id}":order_details}

@orders.route("/delete_Order/<id>")
def delete(id):
    delete_Order=Order.query.delete(id)
    # if delete_orders is None:
    #     return{"message":"Specified id not found"}, 404
    # else:
    db.session.delete(id)
    db.session.commit()
    return {"message":"successfully deleted specified Order"}, 200