from src.presentation.interfaces.crontroller_interface import ControllerInterface
from src.domain.use_cases.todo_register import ToDoRegister as ToDoRegisterInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


class ToDoRegisterController(ControllerInterface):
    def __init__(self, use_case: ToDoRegisterInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        title = http_request.body["title"]

        response = self.__use_case.register(title)

        return HttpResponse(
            status_code=200,
            body={ "data": response }
        )
