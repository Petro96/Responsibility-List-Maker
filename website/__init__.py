
import os
from flask import Flask

#from flask_bcrypt import Bcrypt # delete lib => werkzeug.security is used 

from extensions import db,ma, migrate, login_manager

from os import path

from dotenv import load_dotenv

from api.views import blueprint


def create_app():

    app = Flask(__name__)
    # secret key for app - for encrypt config, session data for website 
    # db config
    app.config.from_object("config")
   
    app.app_context().push()

    # init db for flask
    db.init_app(app)

    # register-init blueprint => .view <=>website -> module(package) / views -> blueprint
    from .views import views # <=> from website import views
    from .auth import auth

    # adding blueprint to app
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/') # before you call url you must type /auth/..

    # creating database
    from .module import User

    # create_database()

    # login manager - login manipulation - user_loader, login_required
    login_manager.login_view = 'auth.login' # if you arent logged in where to go...
    login_manager.login_message_category = "info"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    # migration
    migrate.init_app(app,db)

    app.register_blueprint(blueprint=blueprint)

    ma.init_app(app)


    return app

# ----- create db

def create_database():

    load_dotenv()

    if not path.exists('website/'+os.environ.get('DB_NAME')):
        db.create_all()
        print("Created Database!")

# --------------------------------------

# Migration

# from flask_migrate import Migrate
# migrate = Migrate(app,db)
#flask --app 'abs_app_path' db init
#flask db migrate -m "Add age column to User table"(flask db migrate)
# flask db stamp head - create latest version of db in migration

#add new column into db 
#flask db migrate

# inside migrate/version
# def upgrade():
    # op.add_column('table_name',sqlalchemy.Colum('new_column',sqlalchemy.DateTime(),nullable=True))

#def downgrade():
    #op.drop_column('table','new_element')

#flask db upgrade

#* switch into production port and flask db upgrade - pull changes that you make on the development port

