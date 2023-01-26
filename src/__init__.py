from flask import Flask, jsonify
from flask_restx import Api
from flask_bcrypt import Bcrypt
from werkzeug.utils import secure_filename
from flask_jwt_extended import JWTManager
from .routes import set_up_routes
from .models.db import initialize_db, db
import os

# Set folder configurations
UPLOAD_FOLDER = '../files'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Init App

app = Flask(__name__)

api = Api(app)

bcrypt = Bcrypt(app)

# configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Application ENV config

app.config.from_object('src.config.DevelopmentConfig')

jwt = JWTManager(app)

initialize_db(app)

set_up_routes(api)
