from src.infra.db.repositories.todo_repository import ToDoRepository
from src.data.use_cases.todo_finder import ToDoFinder
from src.presentation.controllers.todo_finder_controller import ToDoFinderController

def todo_finder_composer():
    repository = ToDoRepository()
    use_case = ToDoFinder(repository)
    controller = ToDoFinderController(use_case)

    return controller.handle
