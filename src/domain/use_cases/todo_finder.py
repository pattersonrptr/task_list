from abc import ABC, abstractmethod
from typing import Dict

class ToDoFinder(ABC):

    @abstractmethod
    def find(self, title: str) -> Dict: pass
