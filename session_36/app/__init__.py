from flask import Flask

from app.items import items
from app.main import main
def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    app.register_blueprint(items)
    return app



