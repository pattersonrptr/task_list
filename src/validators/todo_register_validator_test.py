from .todo_register_validator import todo_register_validator

class MockRequest:
    def __init__(self) -> None:
        self.json = None


def test_todo_register_validator():
    print()
    request = MockRequest()
    request.json = {
        "title": "MyTitle",
    }

    todo_register_validator(request)
