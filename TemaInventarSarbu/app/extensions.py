from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# declaration of DB and Migrate
db = SQLAlchemy()
migrate = Migrate()

# declaration of Bcrypt and LoginManager
bcrypt = Bcrypt() #  pass management for a registered user
login_manager = LoginManager() #

