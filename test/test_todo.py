import pytest
import datetime
from src.services.todo_service import save_todo, update_todo, delete_todo, get_todos, get_todo_by_id
from src.models.todo import Todo


@pytest.mark.integration
def create_todo_and_get_id(db_session, client):
    """
    This test will call the create_item function from the item service and will assert that this call
    insert a new row in the database
    Arguments:
        db_session : a fixture that provide an open database session. It will helps us to retrieve row and assert
        that a new row was inserted
    """

    current_dateTime = datetime.now()

    description = "test",
    author = 1
    todo = save_todo(description, author, current_dateTime)

    assert todo.description == description
    assert todo.author == author
