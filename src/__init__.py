from flask import Flask, jsonify
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy

# Init App

db = SQLAlchemy()

app = Flask(__name__)

api = Api(app)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)

# Application ENV config

app.config.from_object('src.config.DevelopmentConfig')

class Ping(Resource):
    def get(self):
        return{
            'status': 'success',
            'message': 'pong'
        }

api.add_resource(Ping, '/ping')