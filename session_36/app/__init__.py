from flask import Flask
from app.items import items
from app.main import main
from app.extensions import db, migrate


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids a warning
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    ###

    app.register_blueprint(main)
    app.register_blueprint(items)
    return app



