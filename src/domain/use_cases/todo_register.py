from abc import ABC, abstractmethod
from typing import Dict

class ToDoRegister(ABC):

    @abstractmethod
    def register(self, title: str) -> Dict: pass
