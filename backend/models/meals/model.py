from models.db import db
from datetime import datetime
class Meal(db.Model):
        __tablename__ = "meals"
        id = db.Column(db.Integer, primary_key = True)
        name = db.Column(db.String(100), nullable=False)
        serving_time = db.Column(db.String(50)) 
        meal_description = db.Column(db.String(200))  
        reg_at = db.Column(db.DateTime, default=datetime.now())
        reg_by = db.Column(db.Integer, db.ForeignKey('admins.id'))
        update_at = db.Column(db.DateTime, onupdate=datetime.now())
        updated_by = db.Column(db.Integer, onupdate= db.ForeignKey('admins.id') )
        

        def __init__(self,
                     name, 
                     serving_time, 
                     reg_by, 
                    #  updated_by, 
                     meal_description):
                
                self.name=name
                self.serving_time=serving_time
                self.reg_by=reg_by
               #  self.updated_by=updated_by
                self.meal_description=meal_description
        def __repr__(self):
            return f"Meal>>>>>{Meal.name}"