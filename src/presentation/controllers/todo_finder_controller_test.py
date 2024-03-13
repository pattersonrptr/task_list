from src.presentation.controllers.todo_finder_controller import ToDoFinderController
from src.data.tests.todo_finder import ToDoFinderSpy
from src.presentation.http_types.http_response import HttpResponse

class HttpRequestMock():
    def __init__(self) -> None:
        self.query_params = { "title": "meuTeste" }

def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = ToDoFinderSpy()
    todo_finder_controller = ToDoFinderController(use_case)

    response = todo_finder_controller.handle(http_request_mock)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["data"] is not None
