from flask import Blueprint

items = Blueprint('items', __name__, template_folder="templates")

from app.items import routes