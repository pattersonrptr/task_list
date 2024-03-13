from src.infra.db.tests.todo_repository import ToDoRepositorySpy
from .todo_finder import ToDoFinder

def test_find():
    title = 'title'

    repo = ToDoRepositorySpy()
    todo_finder = ToDoFinder(repo)

    response = todo_finder.find(title)

    assert repo.select_todo_attributes["title"] == title

    assert response["type"] == "ToDo"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"]


def test_find_error_in_valid_name():
    title = 'title123'

    repo = ToDoRepositorySpy()
    todo_finder = ToDoFinder(repo)

    try:
        todo_finder.find(title)
        assert False
    except Exception as expection:
        assert str(expection) == "Título invalido para a busca"


def test_find_error_in_long_name():
    title = 'titleahlfksjhfsjkalhkfjhsalfkshfkljshalkjsh'

    repo = ToDoRepositorySpy()
    todo_finder = ToDoFinder(repo)

    try:
        todo_finder.find(title)
        assert False
    except Exception as expection:
        assert str(expection) == "Título muito grande para busca"


def test_find_error_todo_not_found():
    class ToDoRepositoryError(ToDoRepositorySpy):
        def select_todo(self, title: str):
            return []

    title = 'title'

    repo = ToDoRepositoryError()
    todo_finder = ToDoFinder(repo)

    try:
        todo_finder.find(title)
        assert False
    except Exception as expection:
        assert str(expection) == "Tarefa nao encontrada"
