from typing import Dict

class ToDoFinderSpy:
    def __init__(self) -> None:
        self.find_attributes = {}

    def find(self, title: str) -> Dict:
        self.find_attributes["title"] = title

        return {
            "type": "ToDo",
            "count": 1,
            "attributes": [
                { "id": -1, "title": "something" }
            ]
        }
