from src.infra.db.repositories.todo_repository import ToDoRepository
from src.data.use_cases.todo_register import ToDoRegister
from src.presentation.controllers.todo_register_controller import ToDoRegisterController

def todo_register_composer():
    repository = ToDoRepository()
    use_case = ToDoRegister(repository)
    controller = ToDoRegisterController(use_case)

    return controller.handle
