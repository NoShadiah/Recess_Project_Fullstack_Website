from models.db import db
from datetime import datetime
class Category(db.Model):
        __tablename__ = "categories"
        id = db.Column(db.Integer, primary_key = True)
        name = db.Column(db.String(100), nullable=False) 
        ctaegory_description = db.Column(db.String(200))
        image = db.Column(db.String(50))  
        reg_at = db.Column(db.DateTime, default=datetime.now())
        reg_by = db.Column(db.Integer, db.ForeignKey('admins.id'))
        update_at = db.Column(db.DateTime, onupdate=datetime.now())
        updated_by = db.Column(db.Integer, onupdate= db.ForeignKey('admins.id') )
        menu = db.relationship("MenuItem", backref='category', remote_side=[id], lazy='dynamic')

        def __init__(self,
                     name, 
                     image, 
                     reg_by, 
                    #  updated_by, 
                     ctaegory_description):
                
                self.name=name
                self.image=image
                self.reg_by=reg_by
               #  self.updated_by=updated_by
                self.ctaegory_description=ctaegory_description
        def __repr__(self):
            return f"Category>>>>>{Category.name}"