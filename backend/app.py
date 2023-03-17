from models import Create_app, db
from flask_migrate import Migrate
from models.users.model import User
from models.admins.model import Admin
from models.settings.controllers import Restaurant
from models.regions.model import Region
from models.districts.model import District
from models.divisions.model import Division


app = Create_app('development')
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User = User, Admin=Admin, Restaurant=Restaurant, Region=Region, District=District, Division=Division)