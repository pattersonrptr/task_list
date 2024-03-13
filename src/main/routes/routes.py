from flask import Blueprint, request, jsonify

# Import adapters
from src.main.adapters.request_adapter import request_adapter

# Import composers
from src.main.composers.todo_finder_composer import todo_finder_composer
from src.main.composers.todo_register_composer import todo_register_composer

# Import Validators
from src.validators.todo_register_validator import todo_register_validator
from src.validators.todo_finder_validator import todo_finder_validator

# Import error handler
from src.errors.error_handler import handle_errors


todo_route_bp = Blueprint("todo_routes", __name__)


@todo_route_bp.route("/todo/find", methods=["GET"])
def find_todo():
    http_response = None

    try:
        todo_finder_validator(request)
        http_response = request_adapter(request, todo_finder_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code


@todo_route_bp.route("/todo", methods=["POST"])
def register_todo():
    http_response = None

    try:
        todo_register_validator(request)
        http_response = request_adapter(request, todo_register_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code
