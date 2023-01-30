from flask import request, jsonify, Response
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from ..services.user_service import create_user, get_users, login, update_user, delete_user, activate_user


class SignUpApi(Resource):
    def post(self):
        body = request.get_json()
        create_user(body)
        return {'id': str(id)}, 200

    @jwt_required()
    def get(self):
        users = get_users()
        return jsonify(users)


class LoginApi(Resource):
    def post(self):
        body = request.get_json()
        result = login(body)
        return result


class UserApi(Resource):
    def post(self, id):
        result = activate_user(id)
        return result

    def put(self, id):
        body = request.get_json()
        result = update_user(id, body)
        return result

    def delete(self, id):
        result = delete_user(id)
        return result
