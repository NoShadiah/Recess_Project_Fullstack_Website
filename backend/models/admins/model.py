from models.db import db
from datetime import datetime


class Admin(db.Model):
      __tablename__ = 'admins'

      id = db.Column(db.Integer, primary_key = True)
      name = db.Column(db.String(100),nullable=False)
      email = db.Column(db.String(50))  
      contact = db.Column(db.String(200))
      password = db.Column(db.String(10))
      admin_type = db.Column(db.String(100), default='administrator')
      registered_by= db.Column(db.String(30), default='super_admin')
      registered_at = db.Column(db.DateTime, default=datetime.now())
      # update_by = db.Column(db.String(30))
      updated_at = db.Column(db.DateTime, onupdate=datetime.now())
      settings = db.relationship("Restaurant", backref="admin", remote_side=[id], lazy='dynamic', secondary='admins', primaryjoin=('admins.id'), secondaryjoin=('admins.id'))
      regions = db.relationship("Region", backref="admin", remote_side=[id], lazy='dynamic')
      districts = db.relationship("District", backref="admin", remote_side=[id], lazy='dynamic')
      divisions = db.relationship("Division", backref="admin", remote_side=[id], lazy='dynamic')
      menu = db.relationship("MenuItem", backref='admin', remote_side=[id], lazy='dynamic')
      orders = db.relationship("Order", backref='admin', remote_side=[id], lazy='dynamic')



      def __init__(self, name, email,contact,registered_by,admin_type,password,):
              self.name = name
              self.email = email
              self.contact = contact
              self.user_type = admin_type
              self.password = password
              self.registered_by = registered_by

      def __rep__ (self):
            return f"<User{self.admin_id}>"