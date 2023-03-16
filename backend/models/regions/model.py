from models.db import db
from datetime import datetime
class Region(db.Model):
        __tablename__ = "regions"
        id = db.Column(db.Integer, primary_key = True)
        name = db.Column(db.String(100), nullable=False)
        country = db.Column(db.String(50))  
        reg_at = db.Column(db.DateTime, default=datetime.now())
        reg_by = db.Column(db.Integer, db.ForeignKey('admin.id'))
        update_at = db.Column(db.DateTime, onupdate=datetime.now())
        updated_by = db.Column(db.Integer, onupdate=db.ForeignKey('admin.id') )
   

        def __init__(self,id,name, location, contact, opening_hrs, closing_hrs, ):
                self.id=id
                self.name=name
                self.location=location
                self.contact=contact
                self.opening_hrs=opening_hrs
                self.closing_hrs = closing_hrs
        def __repr__(self):
            return f"Region>>>>>{Region.name}"