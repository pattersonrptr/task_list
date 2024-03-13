#pylint: disable=broad-exception-raised
from typing import Dict
from src.domain.use_cases.todo_register import ToDoRegister as ToDoRegisterInterface
from src.data.interfaces.todo_repository import ToDoRepositoryInterface
from src.errors.types import HttpBadRequestError

class ToDoRegister(ToDoRegisterInterface):
    def __init__(self, todo_repository: ToDoRepositoryInterface) -> None:
        self.__todo_repository = todo_repository

    def register(self, title: str) -> Dict:
        self.__validate_name(title)
        self.__registry_todo_informations(title)
        response = self.__format_response(title)
        return response

    @classmethod
    def __validate_name(cls, title: str) -> None:
        print("__validate_name: ", title)
        if not title.istitle():
            raise HttpBadRequestError('Título invalido para o cadastro')

        if len(title) > 18:
            raise HttpBadRequestError('Título muito grande para o cadastro')

    def __registry_todo_informations(self, title: str) -> None:
        self.__todo_repository.insert_todo(title)

    @classmethod
    def __format_response(cls, title: str) -> Dict:
        response = {
            "type": "ToDo",
            "count": 1,
            "attributes": {
                "title": title,
            }
        }
        return response
