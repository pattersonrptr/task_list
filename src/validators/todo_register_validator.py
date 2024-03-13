from cerberus import Validator
from src.errors.types import HttpUnprocessableEntityError

def todo_register_validator(request: any):

    body_validator = Validator({
        "title": { "type": "string", "required": True, "empty": False },
    })
    response = body_validator.validate(request.json)

    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)
