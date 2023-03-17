from models.db import db
from datetime import datetime
class District(db.Model):
        __tablename__ = "districts"
        id = db.Column(db.Integer, primary_key = True)
        name = db.Column(db.String(100), nullable=False)
        region_id = db.Column(db.String(50), db.ForeignKey('regions.id')) 
        district_code = db.Column(db.String(50))  
        reg_at = db.Column(db.DateTime, default=datetime.now())
        reg_by = db.Column(db.Integer, db.ForeignKey('admins.id'))
        update_at = db.Column(db.DateTime, onupdate=datetime.now())
        updated_by = db.Column(db.Integer, onupdate= db.ForeignKey('admins.id') )
        divisions = db.relationship("Division", backref="district", remote_side=[id], lazy='dynamic')

        def __init__(self,
                     name, 
                     region_id, 
                     reg_by, 
                #      updated_by, 
                     district_code):
                
                self.name=name
                self.region_id=region_id
                self.reg_by=reg_by
                # self.updated_by=updated_by
                self.district_code=district_code
        def __repr__(self):
            return f"District>>>>>{District.name}"