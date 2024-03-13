from flask import Flask
from src.main.routes.routes import todo_route_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(todo_route_bp)
