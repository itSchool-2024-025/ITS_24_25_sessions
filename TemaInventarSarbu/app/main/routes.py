from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required

from app.main import main
from colorama import Back, Style, Fore
from app.main.models import Inventory, User
from app.extensions import db, bcrypt


@main.route('/',methods=['GET', 'POST'])
def home():
    inventory = Inventory.query.all()
    message=""
    if not current_user.is_authenticated:
        print(f"Debug1 Home- Page of for User not authenticated is displayed")
        #message = "User not authenticated"
        return render_template("home.html", inventory=inventory)

    # Allow actions only if user is authenticated
    elif request.method == "POST":
        #Get inventory number of the Booked item
        number = request.form.get('inventory_number')
        # retrieve item from DB
        item = Inventory.query.filter_by(inventory_number=number).first()
        print ("item: {item}")

        #Item can be Booked if Free
        if item.inventory_booked == "Free":
            # Book the item
            item.inventory_booked = "In Use"
            # Assign current user to the item
            item.user_id = current_user.user_name
            db.session.commit()
            print (f"Debug1 Home-Item : {item.inventory_number} is In Use by {current_user.user_name}")
            #message= f"Item {item.inventory_number} is \"In Use\" by user \"{current_user.user_name}\""

            # Item can be released only if booked by same user
        elif item.inventory_booked == "In Use" and (item.user_id == current_user.user_name or item.user_id==None):
            # Free the item
            item.inventory_booked = "Free"
            item.user_id = None
            db.session.commit()
            print(f"Debug2 Home-Item : {item.inventory_number} is now Free")
            #message = f"Item {item.inventory_number} is now \"Free\"."

        else:#User is not allowed to free the item when item already In Use by other user
            print(f"Debug3 : Item is already  \"In Use \" by other user: {current_user.user_name}")
            message = f"Action not allowed. Item is already  \"In Use \" by other user: \"{current_user.user_name}\""

            return render_template("home_user_authenticated.html",inventory=inventory,message=message ) # refresh page after update

    return render_template("home_user_authenticated.html",inventory=inventory,message=message )

@main.route('/users',methods=['GET', 'POST'])
def users():
    message = ""
    users = User.query.all()
    return render_template("users.html",users=users,message=message )

#Search route for users
@main.route('/search_user')
def search_user(inventory=None):
    message= ""
    search_query = request.args.get('search', '')
    found_item= Inventory.query.filter_by(inventory_state=search_query).first()

    #filtered_items = Inventory.query.all()

    if search_query == "":
        print("Empty search_query")
        filtered_items = Inventory.query.all()
        return redirect(url_for("main.home", message=message))  # refresh page after update

    filtered_items = Inventory.query.filter_by(user_id=search_query).all()
    if filtered_items:
        print(filtered_items)
        print("User has Searched by user")
    elif Inventory.query.filter_by(inventory_booked=search_query).all():
        print(filtered_items)
        print("User has Searched by Booked")
        filtered_items = Inventory.query.filter_by(inventory_booked=search_query).all()
    elif Inventory.query.filter_by(inventory_state=search_query).all():
        print(filtered_items)
        print("User has Searched by State")
        filtered_items = Inventory.query.filter_by(inventory_state=search_query).all()
    else:
        filtered_items = Inventory.query.filter_by(inventory_description=search_query).all()
        print(filtered_items)
        print("User has Searched by Description")

    return render_template("home_user_authenticated.html",  message=message, inventory=filtered_items)

@main.route('/admin',methods=['GET', 'POST'])
@login_required
def admin():

    inventory = Inventory.query.all()
    message= ""

    if request.method == "POST":

        number = request.form.get('inventory_number')
        description = request.form.get('inventory_description')
        state = request.form.get('inventory_state')
        booked = request.form.get('inventory_booked')

        # retrieve item from db after inventory_number
        item = Inventory.query.filter_by(inventory_number=number).first()

        print("Debug 1 Admin- Item to update has inventory " + Fore.GREEN +"number: " + Style.RESET_ALL + Fore.RED + f"{number}"+ Style.RESET_ALL +
              Fore.GREEN + ", description: " + Style.RESET_ALL + Fore.RED +f"{item.inventory_description}" + Style.RESET_ALL +
              Fore.GREEN + ", state: " + Style.RESET_ALL + Fore.RED + f"{item.inventory_state}" + Style.RESET_ALL +
              Fore.GREEN + ", booked: " + Style.RESET_ALL + Fore.RED + f"{item.inventory_booked}" + Style.RESET_ALL )


        item.inventory_description = description
        item.inventory_state= state
        item.inventory_booked = booked

        print(f"Debug 2 Admin- Item with inventory number:" + Fore.GREEN + f"{number}" +"was updated:")
        print(Fore.GREEN + "- inventory description: " + Style.RESET_ALL + Fore.RED + f"{item.inventory_description}" + Style.RESET_ALL)
        print(Fore.GREEN + "- inventory state: "  + Style.RESET_ALL + Fore.RED + f"{item.inventory_state}" + Style.RESET_ALL)
        print(Fore.GREEN + "- inventory booked: " + Style.RESET_ALL + Fore.RED + f"{item.inventory_booked}" + Style.RESET_ALL)
        message="OK"


        db.session.commit()

        return redirect(url_for('main.admin', message=message)) #refresh page after update

    return render_template("admin.html", inventory=inventory, message=message )

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
        print(f"debug1: number: {number}")

        #search item in DB by inventory number
        item = Inventory.query.filter_by(inventory_number=number).first()

        if item: #item with same inventory number is found in DB
            print(f"debug2: check_number: {item.inventory_number}")
            message = f"Inventory {item.inventory_number} exists. Number must be unique."
            print(message)

        else: #item not found in DB

            description = request.form.get('inventory_description')
            state = request.form.get('inventory_state')
            booked = request.form.get('inventory_booked')

            inventory_item = Inventory(
                inventory_number= number,
                inventory_description = description,
                inventory_state = state,
                inventory_booked = booked
            )

            db.session.add(inventory_item)
            db.session.commit()
            message = f"Inventory number: {number}, description: {description} , state: {state} , Owned: {booked} was added."
            print(message)

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
        message =f"User: {user_name} with e-mail: {user_email}, is now registered. You may now login."
        print(f"User {user_name}, email: {user_email} , passwd: {user_password}, password confirmed: {user_password_confirmed}.")

        if not user_name or not user_email or not user_password or not user_password_confirmed:
            print("Debug2- Register - some fields might be empty")
            message= "Debug2- Register - some fields might be empty"
        elif user_password != user_password_confirmed:
            print("Debug3- Register - password missmatch")
            message = "Debug3- Register - password missmatch"
        elif User.query.filter_by(user_name=user_name).first():
            print("Debug4- Register - user already exists")
            message = "Debug4- Register - user already exists"
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

    if current_user.is_authenticated:
        print("Debug1- Login: User is already authenticated")
        message = "User is already authenticated"
        return redirect(url_for('main.home', message=message))
    else:
        print("Debug2- Login: User is NOT authenticated")
        message = "User is NOT authenticated."
        if request.method == 'POST':
            # Process form data
            user_name = request.form.get('user_name')
            user_password = request.form.get('user_password')
            message = (f"User: {user_name}, passwd: {user_password} loged in")
            print(message)

            user = User.query.filter_by(user_name=user_name).first()

            if user and bcrypt.check_password_hash(user.user_password, user_password):
                print("Debug3: User and Password matching the database")
                message = "User and Password matching the database"
                login_user(user)
                return redirect(url_for('main.home', message=message))
            else:
                print("Debug4- User or Password not matching the database")
                message= "User or Password not matching the database"

    return render_template('login.html', message=message)

@main.route("/logout")
def logout():

    if current_user.is_authenticated:
        print("Debug1 Logout- Current user " + current_user.user_name + "is log-out")
        message = "Current user " + current_user.user_name + "is log-out"
        logout_user()

        return redirect(url_for('main.home', message=message))
    else:
        print("Debug2 Logout- No user is currently log in")
        message = "Logout- No user is currently log in"
        return redirect(url_for('main.login', message=message))
