from models import create_app, db
from flask_migrate import Migrate
from models.settings.model import Restaurant
from models.users.model import User
from models import db


app = create_app('development')
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Restaurants=Restaurant, Users=User)