from models.db import db
from datetime import datetime
class Division(db.Model):
        __tablename__ = "Divisions"
        id = db.Column(db.Integer, primary_key = True)
        name = db.Column(db.String(100), nullable=False)
        district_id = db.Column(db.String(50), db.ForeignKey('districts.id'))  
        reg_at = db.Column(db.DateTime, default=datetime.now())
        reg_by = db.Column(db.Integer, db.ForeignKey('admins.id'))
        update_at = db.Column(db.DateTime, onupdate=datetime.now())
        updated_by = db.Column(db.Integer, 
                        #        onupdate=
                               db.ForeignKey('admins.id') )
        menu = db.relationship("MenuItem", backref='division', remote_side=[id])
   

        def __init__(self,name, district_id, reg_by, updated_by):
                
                self.name=name
                self.district_id=district_id
                self.reg_by=reg_by
                self.updated_by=updated_by
        def __repr__(self):
            return f"Division>>>>>{Division.name}"