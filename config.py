

from dotenv import load_dotenv
import os


load_dotenv()

FLASK_DEBUG=os.environ.get('FLASK_DEBUG')
FLASK_DEVELOPMENT_PORT=os.environ.get('FLASK_DEVELOPMENT_PORT')
APP_HOST=os.environ.get('APP_HOST')
DB_NAME=os.environ.get('DB_NAME')
SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI')
SECRET_KEY=os.environ.get('SECRET_KEY')
ENV=os.environ.get('ENV')