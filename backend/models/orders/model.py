from models.db import db
from datetime import datetime
class Order(db.Model):
        __tablaname__ = "orders"
        id = db.Column(db.Integer, primary_key = True)
        made_by = db.Column(db.Integer, db.ForeignKey('users.id')) 
        # delivery_destination = db.Column(db.Integer, db.ForeignKey('divisions.id'))
        local_address = db.Column(db.String(200))
        menu_item = db.Column(db.Integer, db.ForeignKey('menu.id'))
        quantity = db.Column(db.Integer) 
        made_at = db.Column(db.DateTime, default=datetime.now())
        grand_total = db.Column(db.Integer, nullable=False)
        status = db.Column(db.String(10), default='Pending')
        update_at = db.Column(db.DateTime, onupdate=datetime.now())
        updated_by = db.Column(db.Integer, db.ForeignKey('admins.id'))
        # users = db.relationship("Users", remote_side=[id])
        users = db.relationship("User", backref='orders', primaryjoin=('Order.made_by'=='User.id'))
        
        def __init__(self,
                     grand_total, 
                     status, 
                     made_by, 
                    #  updated_by, 
                    menu_item, 
                    local_address,
                    delivery_destination,
                    quantity):
                
                self.grand_total=grand_total
                self.status=status
                self.made_by=made_by
                self.menu_item = menu_item
                self.delivery_destination = delivery_destination
                self.local_address=local_address
               #  self.updated_by=updated_by
                self.quantity=quantity
        def __repr__(self):
            return f"Category>>>>>{Order.made_by}"