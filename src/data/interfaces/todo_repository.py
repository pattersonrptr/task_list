from abc import ABC, abstractmethod
from typing import List
from src.domain.models.todo import ToDo

class ToDoRepositoryInterface(ABC):

    @abstractmethod
    def insert_todo(self, title: str) -> None: pass

    @abstractmethod
    def select_todo(self, title: str) -> List[ToDo]: pass
