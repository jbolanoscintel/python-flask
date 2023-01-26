from flask import request, jsonify
from ..models import User
from ..models.db import db
from flask_restx import Resource


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
