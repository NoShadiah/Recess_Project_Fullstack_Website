from models import Create_app, db
from flask_migrate import Migrate
from models.users.model import User
from models.admins.model import Admin
from models.settings.controllers import Restaurant
from models.regions.model import Region
from models.districts.model import District
from models.divisions.model import Division
from models.food_categories.model import Category
from models.meals.model import Meal
from models.menu.model import MenuItem
from models.orders.model import Order

app = Create_app('development')
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(
                db=db, 
                user = User, 
                admin=Admin, 
                restaurant=Restaurant, 
                region=Region, 
                district=District, 
                division=Division,
                category=Category,
                meal=Meal,
                menu=MenuItem, 
                order=Order
                )