from flask_restx import Resource

class Todo(Resource):
    def get(self):
        return {
            'status': 'success',
            'data': []
        }