import os

# base class
class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    @staticmethod
    def init_app(app):
        pass


# sub classes of the base class
class DevelopmentConfig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:''@localhost/online_food_delivery_ms' #we have the databse driver, the username, the location, and the name of the database
    JWT_SECRET_KEY=os.environ.get('JWT_SECRET_KEY')
    basedir = os.path.abspath(os.path.dirname(__file__))
    # In this, am telling SQLAlchemy tha in the os library, set a path, 
    # the absolute path is a function that takes in the path of the working directory, where this file is.
    conn = os.path.join(basedir, 'online_food_delivery system.db')
    # configuring the application/connecting to the database
    SQLALCHEMY_DATABASE_URI=\
                                'sqlite:///'+conn
class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URI")

# configuration object
config = {
    'development' : DevelopmentConfig,
    'testing' : TestingConfig,
    'default' : DevelopmentConfig
}
