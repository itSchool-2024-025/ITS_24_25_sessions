from flask import Blueprint, render_template, request

main_bp = Blueprint("main", __name__, template_folder="templates")

@main_bp.route("/")
def home():
    return render_template("main.html", title="Home")

@main_bp.route("/about")
def about():
    return render_template("about.html", title="About")

@main_bp.route('/form', methods=['GET', 'POST'])
def form():
    message = ""
    if request.method == 'POST':
        # Process form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = f"Hello {name}, your email is {email}."
    return render_template('form.html', message=message)