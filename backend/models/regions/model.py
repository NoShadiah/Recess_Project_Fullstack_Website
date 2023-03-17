from models.db import db
from datetime import datetime
class Region(db.Model):
        __tablename__ = "regions"
        id = db.Column(db.Integer, primary_key = True)
        name = db.Column(db.String(100), nullable=False)
        country = db.Column(db.String(50))  
        reg_at = db.Column(db.DateTime, default=datetime.now())
        reg_by = db.Column(db.Integer, db.ForeignKey('admins.id'))
        update_at = db.Column(db.DateTime, onupdate=datetime.now())
        updated_by = db.Column(db.Integer, onupdate=db.ForeignKey('admins.id') )
        districts = db.relationship("District", backref="region", remote_side=[id], lazy='dynamic')

        def __init__(self,name, country, reg_by):
                
                self.name=name
                self.country=country
                self.reg_by=reg_by
                # self.updated_by=updated_by
        def __repr__(self):
            return f"Region>>>>>{Region.name}"