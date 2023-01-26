from .ping import Ping
from .todo_routes import Todo
from .user_routes import SignUpApi


def set_up_routes(api):
    api.add_resource(Ping, '/api/ping')
    api.add_resource(Todo, '/api/todos')
    api.add_resource(SignUpApi, '/api/auth/signup')
