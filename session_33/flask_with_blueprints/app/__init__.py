from flask import Flask
from .main.routes import main_bp

def create_app():
    app = Flask(__name__)

    #you can also configure your flask app here :)

    #Register Blueprints
    app.register_blueprint(main_bp)

    return app