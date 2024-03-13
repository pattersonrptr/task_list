from typing import List
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.todo import ToDo as ToDoEntity
from src.data.interfaces.todo_repository import ToDoRepositoryInterface
from src.domain.models.todo import ToDo

class ToDoRepository(ToDoRepositoryInterface):

    @classmethod
    def insert_todo(cls, title: str) -> None:
        with DBConnectionHandler() as database:
            try:
                new_registry = ToDoEntity(
                    title=title,
                )
                database.session.add(new_registry)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def select_todo(cls, title: str) -> List[ToDo]:
        with DBConnectionHandler() as database:
            try:
                todo = (
                    database.session
                        .query(ToDoEntity)
                        .filter(ToDoEntity.title == title)
                        .all()
                )
                return todo
            except Exception as exception:
                database.session.rollback()
                raise exception
