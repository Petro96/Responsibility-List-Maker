
import os
from flask import Flask

#from flask_bcrypt import Bcrypt # delete lib => werkzeug.security is used 

from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager

from flask_migrate import Migrate

from os import path


# sglAlchemy(ORM) initialize
db = SQLAlchemy()
DB_NAME="database.db"


def create_app():

    app = Flask(__name__)
    # secret key for app - for encrypt config, session data for website 
    app.config['SECRET_KEY'] = 'generate secret_key'

    # db config
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # init db for flask
    app.app_context().push()
    db.init_app(app)

    # register-init blueprint => .view <=>website -> module(package) / views -> blueprint
    from .views import views # <=> from website import views
    from .auth import auth

    # adding blueprint to app
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/') # before you call url you must type /auth/..

    # creating database
    from .module import User, Note

    create_database()

    # login manager - login manipulation - user_loader, login_required
    login_manager = LoginManager(app)
    login_manager.login_view = 'auth.login' # if you arent logged in where to go...
    login_manager.login_message_category = "info"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    # migration
    migrate= Migrate(app,db)


    return app

def create_database():

    if not path.exists('website/'+ DB_NAME):
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

