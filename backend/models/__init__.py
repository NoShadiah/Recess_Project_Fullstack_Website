from flask import Flask
from config import config
from backend.db import db


def create_app(config_name): #Application Factory Funciton
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.config.from_pyfile("../config.py")


    db.init_app(app)

    @app.route('/')
    def greet():
        return "Hallo there"
    #import the blueprints
    
    # from backend.books.controllers import books

    # #registering blue prints
    #app.register_blueprint()
    # app.register_blueprint(books)

    return app
