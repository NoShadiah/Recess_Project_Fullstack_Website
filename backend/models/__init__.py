from flask import Flask
from config import config
from models.db import db
import os

def create_app(): #Application Factory Funciton
    app = Flask(__name__)
    config_name = os.getenv('FLASKCONFIG') or 'default'
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.config.from_pyfile("../config.py")


    db.init_app(app)

    @app.route('/')
    def greet():
        return """
        The Online Food Ordering System capstone project is a web and mobile app that lets an organization post its menus and foods and take orders from customers. This is kind of like an e-commerce platform, but it is made for ordering food. In an online food ordering system, a consumer searches for a favorite restaurant, which is usually categorized by cuisine, and then selects from available items as well as delivery or pick-up options.
Payment can be made in a variety of ways, including credit card or cash, with the restaurant remitting a portion of the proceeds to the online food delivery service.For the case of this project, as of now, the payments will be put aside.

The system includes a website or app that allows customers to look at the menu and order food, as well as an admin interface that lets restaurants get and send orders to customers, so they can get and send them food.
Food Ordering Information: Food Ordering Information secures the data needed to display the establishment’s products. They were displayed to market and promote their products.
Customer Order Details: As a major step in the Food Ordering System, it determines the included data when a customer orders or transacts. Customer order details data examples include name, address, and phone number. This process takes consumer meal orders, quantities, and payment information.
Transaction Reports Management: Food Supply Management oversees all supply-related activities. To track all production supplies, enter and exit data must be captured. The Food Ordering System ER Diagram will store this data.
Transaction and Reports Management: This process is considered one of the major processes in the project because it saves the overall transaction within a period of time. These reports will then be helped by the ER Diagram designed for the Food Ordering System.




The ER diagram for the online food ordering system shows how the different things work together. You can think of it as a plan for how the system (or project) will be put together.
"""
    #import the blueprints
    
    from models.settings.controllers import restaurants

    # #registering blue prints
    app.register_blueprint(restaurants)

    return app
