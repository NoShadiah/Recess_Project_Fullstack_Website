from models.db import db

class Restaurant(db.Model):
        __tablename__ = "settings"
        id = db.Column('restaurant_id', db.Integer, primary_key = True)
        name = db.Column(db.String(100), nullable=False)
        location = db.Column(db.String(50))  
        contact = db.Column(db.Integer)
        opening_hrs = db.Column(db.String(6))
        closing_hrs = db.Column(db.String(6))
        reg_by = db.Column(db.Integer, db.ForeignKey('admins.id'))



        def __init__(self,id,name, location, contact, opening_hrs, closing_hrs):
                self.id=id
                self.name=name
                self.location=location
                self.contact=contact
                self.opening_hrs=opening_hrs
                self.closing_hrs = closing_hrs
        def __repr__(self) -> str:
                return f"Restaurant>>>>>>{Restaurant.name}"