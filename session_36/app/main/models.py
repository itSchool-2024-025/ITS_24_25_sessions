from app.extensions import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_event = db.Column(db.String(80), unique=True, nullable=False)
    date = db.Column(db.String(80), unique=True, nullable=False)
    time = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(80), unique=True, nullable=True)