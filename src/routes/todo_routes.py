from flask_restx import Resource
from flask_jwt_extended import jwt_required


class Todo(Resource):
    @jwt_required
    def get(self):
        return {
            'status': 'success',
            'data': []
        }
