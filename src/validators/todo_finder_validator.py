from cerberus import Validator
from src.errors.types import HttpUnprocessableEntityError

def todo_finder_validator(request: any):

    query_validator = Validator({
        "title": { "type": "string", "required": True, "empty": False }
    })
    response = query_validator.validate(request.args)

    if response is False:
        raise HttpUnprocessableEntityError(query_validator.errors)
