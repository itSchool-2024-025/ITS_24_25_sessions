from flask import Flask
from flask_login import LoginManager
from app.extensions import db, migrate, login_manager
from app.config import Config
from app.main import main_bp
from app.users import bp as users_bp

def create_app():
    app = Flask(__name__)

    #you can also configure your flask app here :)
    # Configure SQLite database
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids a warning
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Set login view
    login_manager.login_view = 'login'

    #Register Blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(users_bp, url_prefix='/users')

    return app