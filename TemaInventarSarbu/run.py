from app import create_app
from colorama import Back, Style, Fore
from app.extensions import db

app = create_app()

with app.app_context():
    db.create_all()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(Fore.GREEN +'Inventory App project loaded'+ Style.RESET_ALL)
    app.run(debug= True, port=8000)


