#pylint: disable=broad-exception-raised
from typing import Dict, List
from src.domain.use_cases.todo_finder import ToDoFinder as ToDoFinderInterface
from src.data.interfaces.todo_repository import ToDoRepositoryInterface
from src.domain.models.todo import ToDo
from src.errors.types import HttpNotFoundError, HttpBadRequestError

class ToDoFinder(ToDoFinderInterface):
    def __init__(self, todo_repository: ToDoRepositoryInterface) -> None:
        self.__todo_repository = todo_repository

    def find(self, title: str) -> Dict:
        self.__validate_name(title)
        todo = self.__search_todo(title)
        response = self.__format_response(todo)
        return response

    @classmethod
    def __validate_name(cls, title: str) -> None:
        if not title.istitle():
            raise HttpBadRequestError('Título invalido para a busca')

        if len(title) > 18:
            raise HttpBadRequestError('Título muito grande para busca')

    def __search_todo(self, title: str) -> List[ToDo]:
        todo = self.__todo_repository.select_todo(title)
        if todo == []: raise HttpNotFoundError('Tarefa nao encontrada')
        return todo

    @classmethod
    def __format_response(cls, todos: List[ToDo]) -> Dict:
        attributes = []
        for todo in todos:
            attributes.append(
                { "id": todo.id, "title": todo.title }
            )

        response = {
            "type": "ToDo",
            "count": len(todos),
            "attributes": attributes
        }

        return response
