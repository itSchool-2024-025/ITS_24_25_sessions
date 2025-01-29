from flask import jsonify, request, render_template
from app.users.models import User
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import login_manager, db

# Use the blueprint
from app.users import bp


@bp.route('/')
def users_home():
    return jsonify({"message": "Welcome to the Users Module!"})


@bp.route('/list')
def user_list():
    users = User.query.all()
    return jsonify([{"id": u.id, "username": u.username, "email": u.email} for u in users])


@bp.route('/form', methods=['GET', 'POST'])
def form():
    message = ""
    if request.method == 'POST':
        # Process form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = f"Hello {name}, your email is {email}."
    return render_template('form.html', message=message)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Example user registration
@bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('e-mail')

        if not username or not password or not email:
            return 'Username, password and e-mail are required', 400

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password, email=email)
        db.session.add(new_user)
        db.session.commit()
        return 'User registered successfully', 201

    return render_template('register.html')

# Example login
@bp.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        login_user(user)
        return 'Logged in successfully'
    return 'Invalid credentials'

# Example logout
@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logged out'