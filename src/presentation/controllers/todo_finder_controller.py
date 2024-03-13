from src.presentation.interfaces.crontroller_interface import ControllerInterface
from src.domain.use_cases.todo_finder import ToDoFinder as ToDoFinderInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


class ToDoFinderController(ControllerInterface):
    def __init__(self, use_case: ToDoFinderInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        title = http_request.query_params["title"]

        response = self.__use_case.find(title)

        return HttpResponse(
            status_code=200,
            body={ "data": response }
        )
