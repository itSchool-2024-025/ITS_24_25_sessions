from flask import Blueprint, render_template, request

main_bp = Blueprint("main", __name__, template_folder="templates")

from app.main.routes import home, about