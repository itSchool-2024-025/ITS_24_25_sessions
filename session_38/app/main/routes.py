from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_user, logout_user

from app.main import main
from colorama import Back, Style, Fore
from app.main.models import Inventory, User
from app.extensions import db, bcrypt


@main.route('/',methods=['GET', 'POST'])
def home():

    print(Fore.GREEN +"Home page loaded"+ Style.RESET_ALL)

    inventory = Inventory.query.all()
    print(Fore.GREEN +"Inventory loaded"+ Style.RESET_ALL)
    print(inventory)
    return render_template("home.html",inventory=inventory )


@main.route('/admin',methods=['GET', 'POST'])
def admin():
    #print(Fore.GREEN +"Admin page loaded"+ Style.RESET_ALL)

    inventory = Inventory.query.all()
    #print(Fore.GREEN +"Inventory loaded"+ Style.RESET_ALL)
    #print(inventory)

    if request.method == "POST":

        number = request.form.get('inventory_number')
        description = request.form.get('inventory_description')
        state = request.form.get('inventory_state')
        booked = request.form.get('inventory_booked')
        message = "Item to update has inventory number:"


        print(Fore.GREEN +"number:" + Style.RESET_ALL + Fore.RED + number + Style.RESET_ALL +
              Fore.GREEN + ", description: " + Style.RESET_ALL + Fore.RED + description + Style.RESET_ALL + ", state: "+ state + ", booked: "+ booked)

        """

        # retrieve item from db after inventory_number
        item = Inventory.query.filter_by(inventory_number=number).first()

        item.inventory_description = description
        item.inventory_state= state
        item.inventory_booked = booked

        print(Fore.GREEN + "Item to update has:")
        print(Fore.GREEN + "- inventory number: " + Style.RESET_ALL + Fore.RED +item.inventory_description)
        print(Fore.GREEN + "- inventory state: " + Style.RESET_ALL + Fore.RED + item.inventory_state)
        print(Fore.GREEN + "- inventory booked: " + Style.RESET_ALL + Fore.RED + item.inventory_booked)

        print (f"Item updated!")
        db.session.commit()
        """

        return redirect(url_for('main.admin')) #refresh page after update

    return render_template("admin.html", inventory=inventory )


@main.route('/about')
def about():
    print(Fore.GREEN +"About page loaded"+ Style.RESET_ALL)
    return render_template("about.html")

@main.route('/add_item',methods=['GET', 'POST'])
def add_item():
    message = ""
    if request.method == 'POST':
        # Process form data
        number = request.form.get('inventory_number')
        description = request.form.get('inventory_description')
        state = request.form.get('inventory_state')
        booked = request.form.get('inventory_booked')
        message = f"Inventory number: {number}, description: {description} , state: {state} booked: {booked} was added."
        print(message)
        inventory_item = Inventory(
            inventory_number= number,
            inventory_description = description,
            inventory_state = state,
            inventory_booked = booked
        )
        db.session.add(inventory_item)
        db.session.commit()

    return render_template('add_item.html', message=message)

@main.route('/register',methods=['GET', 'POST'])
def register():
    message = ""
    if request.method == 'POST':
        # Process form data
        user_name = request.form.get('user_name')
        user_email = request.form.get("user_email")
        user_password = request.form.get('user_password')
        user_password_confirmed = request.form.get('user_password_confirmed')
        message = (f"User: {user_name}, Email: {user_email} , "
                   f"passwd: {user_password}, password confirmed: {user_password_confirmed}.")
        print(message)
        if not user_name or not user_email or not user_password or not user_password_confirmed:
            print("Debug - some fields might be empty")
            message= "Debug - some fields might be empty"
        elif user_password != user_password_confirmed:
            print("Debug - password missmatch")
            message = "Debug - password missmatch"
        elif User.query.filter_by(user_name=user_name).first():
            print("Debug - user already exists")
            message = "Debug - user already exists"
        else:
            hashed_password = bcrypt.generate_password_hash(user_password).decode('utf-8')

            user = User(
                user_name= user_name,
                user_password = hashed_password,
                user_email = user_email
            )

            db.session.add(user)
            db.session.commit()

    return render_template('register.html', message=message)

@main.route('/login',methods=['GET', 'POST'])
def login():
    message = ""
    if current_user.is_authenticated:
        print("Debug1: User is already authenticated")
        return redirect(url_for('main.home'))
    else:
        print("Debug2: User is NOT authenticated")
        message = "Debug2: User is NOT authenticated"
        if request.method == 'POST':
            # Process form data
            user_name = request.form.get('user_name')
            user_password = request.form.get('user_password')
            message = (f"User: {user_name}, passwd: {user_password} loged in")
            print(message)

            user = User.query.filter_by(user_name=user_name).first()

            if user and bcrypt.check_password_hash(user.user_password, user_password):
                print("debug3: User and Password matching the database")
                login_user(user)
                return redirect(url_for('main.home'))
            else:
                print("debug4- User or Password not matching the database")


    return render_template('login.html', message=message)

@main.route("/logout")
def logout():
    print("debug5- Current user " + current_user.user_name + "is log-out")
    logout_user()
    return redirect(url_for('main.login'))