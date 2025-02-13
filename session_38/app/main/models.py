from app.extensions import db, login_manager
from flask_login import UserMixin


class Inventory(db.Model):
    inventory_id = db.Column(db.Integer, primary_key=True)
    inventory_number = db.Column(db.Integer, unique=True, nullable=False)
    inventory_description = db.Column(db.String(80), unique=False, nullable=True)
    inventory_state= db.Column(db.String(80), unique=False, nullable=True)
    inventory_booked = db.Column(db.String(80), unique=False, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=True)


class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), unique=True, nullable=False)
    user_email = db.Column(db.String(80), unique=True, nullable=False)
    user_password = db.Column(db.String(80), unique=False, nullable=False)
    items = db.relationship('Inventory', backref='owner', lazy=True) #relation establish to Inventory: 1 to many
    #items2 = db.relationship('Inventory2', backref='owner', lazy=True)  # relation establish to Inventory 1 to many

    def get_id(self):
        return self.user_id


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))