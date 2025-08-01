from flask import Flask
from app.config import Config
from app.routes import user_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(user_routes)

    return app