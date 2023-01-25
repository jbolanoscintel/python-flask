from .ping import Ping
from .todo_routes import Todo

def set_up_routes(api):
    api.add_resource(Ping, '/ping')
    api.add_resource(Todo, '/todos')
    #api.add_resource()