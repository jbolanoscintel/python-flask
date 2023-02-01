from .routes import set_up_routes
from flask import Flask, jsonify
from flask_restx import Api
from flask_bcrypt import Bcrypt
from werkzeug.utils import secure_filename
from flask_mail import Mail
from flask_jwt_extended import JWTManager
from .models.db import initialize_db, db
from .resources import errors
import os

# Set folder configurations
UPLOAD_FOLDER = '../files'

# Init App
app = Flask(__name__)

# Application ENV config

app.config.from_object('src.config.DevelopmentConfig')

# configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
app.config['UPLOAD_FOLDER'] = os.environ.get('UPLOAD_FOLDER')

api = Api(app, errors=errors)

bcrypt = Bcrypt(app)

jwt = JWTManager(app)

initialize_db(app)

mail = Mail(app)


set_up_routes(api)
