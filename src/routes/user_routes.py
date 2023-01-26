from flask import request, jsonify, Response
from ..models import User
from ..models.db import db
from flask_restx import Resource
from flask_jwt_extended import create_access_token
import datetime


class SignUpApi(Resource):
    def post(self):
        body = request.get_json()
        user = User(**body)
        user.hash_password()
        db.session.add(user)
        db.session.commit()
        return {'id': str(id)}, 200

    def get(self):
        users = User.query.all()
        result = []
        for u in users:
            result.append(u.serialize())
        return jsonify(result)


class SignInApi(Resource):
    def post(self):
        body = request.get_json()
        user = User.query(body.get('email'))
        if user:
            authorized = user.check_password(body.get('password'))
            if not authorized:
                return {'error': 'Incorrect Email or Password'}, 401
            expires = datetime.timedelta(days=7)
            access_token = create_access_token(
                identity=str(user.id), expires_delta=expires)
            return {'token': access_token}, 200
        return {'error': 'Incorrect Email or Password'}, 401
