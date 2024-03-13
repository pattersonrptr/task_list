from src.infra.db.tests.todo_repository import ToDoRepositorySpy
from .todo_register import ToDoRegister

def test_register():
    title = "Hello World"

    repo = ToDoRepositorySpy()
    todo_register = ToDoRegister(repo)

    response = todo_register.register(title)

    assert repo.insert_todo_attributes["title"] == title

    assert response["type"] == "ToDo"
    assert response["count"] == 1
    assert response["attributes"]

def test_register_title_error():
    title = "ola3131313"

    repo = ToDoRepositorySpy()
    todo_register = ToDoRegister(repo)

    try:
        todo_register.register(title)
        assert False
    except Exception as exception:
        assert str(exception) == "Título invalido para o cadastro"
