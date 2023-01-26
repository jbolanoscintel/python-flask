from src import db
from ..models import Todo
from ..models import User

def save_todo(todo):
    new_todo = Todo(description= todo["description"], author= todo["autor"]. estimated_complete_date= todo["estimated_complete_date"])
    db.session.add(new_todo)
    db.session.commit()
    return {
        'todo': new_todo,
        'message': 'Success'
    }
    
def update_todo(todo_to_update):
    if todo_to_update:
        db.session.commit()
        
def get_todos():
    all_todos = Todo.query.all()
    return all_todos

def get_todos_by_user(user_id):
    user = User.query.get(user_id)
    if user:
        return user.todos
    else
        return False
    
    
def get_todo_by_id(todo_id):
    todo = Todo.query.get(id)
    return todo
    
def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
        return True
    else:
        return False
    