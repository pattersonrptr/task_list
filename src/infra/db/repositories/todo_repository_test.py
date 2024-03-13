import pytest
from sqlalchemy import text
from src.infra.db.settings.connection import DBConnectionHandler
from .todo_repository import ToDoRepository

db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()

@pytest.mark.skip(reason="Sensive test")
def test_insert_todo():
    mocked_title = 'title_1'

    todo_repository = ToDoRepository()
    todo_repository.insert_todo(mocked_title)

    sql = '''
        SELECT * FROM todo
        WHERE title = '{}'
    '''.format(mocked_title)
    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.title == mocked_title

    connection.execute(text(f'''
        DELETE FROM todo WHERE id = {registry.id}
    '''))
    connection.commit()

@pytest.mark.skip(reason="Sensive test")
def test_select_todo():
    mocked_title = 'title_2'

    sql = '''
        INSERT INTO todo (title) VALUES ('{}')
    '''.format(mocked_title)
    connection.execute(text(sql))
    connection.commit()

    todo_repository = ToDoRepository()
    response = todo_repository.select_todo(mocked_title)

    assert response[0].title == mocked_title

    connection.execute(text(f'''
        DELETE FROM todo WHERE id = {response[0].id}
    '''))
    connection.commit()
