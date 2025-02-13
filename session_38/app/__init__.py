from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.main import main
from app.extensions import db, migrate, bcrypt, login_manager


def create_app():

    app = Flask (__name__)

    #configure DB
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids a warning
    app.secret_key="1234" #key for data decryption!!

    #initialise db and migrate extension
    db.init_app(app) #allwas refers to app.db
    migrate.init_app(app)

    #initialize bcrypt and login_manager
    bcrypt.init_app(app)
    login_manager.init_app(app)

    #protect some urls unless user is login
    login_manager.login_view = "main.login"

    #register main blueprint
    app.register_blueprint(main)

    return app