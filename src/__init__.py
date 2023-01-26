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
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Application ENV config

app.config.from_object('src.config.DevelopmentConfig')

jwt = JWTManager(app)


@jwt.expired_token_loader
def my_expired_token_callback(jwt_header, jwt_payload):
    return jsonify(code="dave", err="I can't let you do that"), 401


@jwt.invalid_token_loader
def token_invalid_callback(jwt_header, jwt_payload):
    return jsonify(code="emergency", err="I can't let you do that, not authorized"), 401


@jwt.token_verification_failed_loader
def token_invalid_callback_2(jwt_header, jwt_payload):
    return jsonify(code="emergency", err="I can't let you do that, not authorized"), 401


@jwt.user_lookup_error_loader
def token_invalid_callback_2(jwt_header, jwt_payload):
    return jsonify(code="emergency", err="I can't let you do that, not authorized"), 401


initialize_db(app)

set_up_routes(api)
