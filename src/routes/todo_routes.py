from flask_restx import Resource
from flask_jwt_extended import jwt_required
from ..services.todo_service import save_todo, update_todo, delete_todo, get_todo_by_id, get_todos_by_user, get_todos


class Todo(Resource):
    @jwt_required
    def get(self):
        return {
            'status': 'success',
            'data': []
        }
