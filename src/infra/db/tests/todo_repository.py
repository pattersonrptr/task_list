from typing import List
from src.domain.models.todo import ToDo

class ToDoRepositorySpy:

    def __init__(self) -> None:
        self.insert_todo_attributes = {}
        self.select_todo_attributes = {}

    def insert_todo(self, title: str) -> None:
        self.insert_todo_attributes["title"] = title


    def select_todo(self, title: str) -> List[ToDo]:
        self.select_todo_attributes["title"] = title
        return [
            ToDo(23, title),
            ToDo(23, title),
        ]
