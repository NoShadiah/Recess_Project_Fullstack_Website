from flask import Flask
from config import config
from models.db import db
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import os

def Create_app(config_name): #Application Factory Funciton
    app = Flask(__name__)
    # config_name = os.getenv('FLASKCONFIG') or 'default'
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.config.from_pyfile("../config.py")
    

    db.init_app(app)
    JWTManager(app)
    CORS(app)


    @app.route('/')
    def greet():
        return "Welcome to todo list app, sign up or login to access them"
    #import the blueprints
    from models.admins.controller import admins
    from models.users.controller import users
    from models.regions.controllers import regions
    from models.settings.controllers import restaurants
    from models.districts.controllers import districts
    from models.divisions.controllers import divisions
    from models.meals.controllers import meals
    from models.food_categories.controllers import categories
    from models.menu.controllers import menu
    from models.orders.controllers import orders
    
    

    #registering blue prints
    app.register_blueprint(admins)
    app.register_blueprint(users)
    app.register_blueprint(regions)
    app.register_blueprint(restaurants)
    app.register_blueprint(districts)
    app.register_blueprint(divisions)
    app.register_blueprint(meals)
    app.register_blueprint(categories)
    app.register_blueprint(menu)
    app.register_blueprint(orders)

    return app
