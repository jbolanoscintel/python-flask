from flask import Flask, jsonify
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from .routes import set_up_routes
import os

# Init App

db = SQLAlchemy()

app = Flask(__name__)

api = Api(app)

# configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
# initialize the app with the extension
db.init_app(app)

# Application ENV config

app.config.from_object('src.config.DevelopmentConfig')

set_up_routes(api)

