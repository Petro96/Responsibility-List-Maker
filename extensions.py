

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
login_manager = LoginManager()