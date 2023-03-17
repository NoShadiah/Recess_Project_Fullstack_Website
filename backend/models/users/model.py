from models.db import db
from datetime import datetime


class User(db.Model):
        __tablename__ = 'users'

        id = db.Column(db.Integer, primary_key = True)
        name = db.Column(db.String(100),nullable=False)
        email = db.Column(db.String(50))  
        contact = db.Column(db.String(200))
        password = db.Column(db.String(10))
        registered_by= db.Column(db.String(30), default='self_registered')
        user_type = db.Column(db.String(100), default='customer')
        registered_at = db.Column(db.DateTime, default=datetime.now())
        # update_by = db.Column(db.String(30))
        updated_at = db.Column(db.DateTime, onupdate=datetime.now())
        orders = db.relationship("Order", backref='user', remote_side=[id])

        
        def __init__(self, name, email,contact,user_type,password,):
            self.name = name
            self.email = email
            self.contact = contact
            self.user_type = user_type
            self.password = password


        def __rep__ (self):
              return f"User>>>>>>{self.user_id}"