from app.main import main
from flask import render_template, request


@main.route('/assignment')
def show_assignment():
    return render_template("assignment.html")

@main.route('/add_event',methods=['GET', 'POST'])
def add_event():

    message = ""
    if request.method == 'POST':
        # Process form data
        name = request.form.get('name')
        date = request.form.get('date')
        time = request.form.get('time')
        description = request.form.get('description')
        message = f"A new {name}, was added on  {date} at {time}."

    return render_template('add_event.html', message=message)


@main.route('/delete_event')
def delete_event():
    return render_template("delete_event.html")


@main.route('/')
def show_events():
    list_of_events = [
        {
            "name": "cina cu Elena",
            "date": "2025-01-21",
            "time": "11:50",
            "description": "in Bucuresti, la restaurant Vatra"
        },
    {
        "name": "pranz cu Andrei",
        "date": "2025-01-25",
        "time": "13:30",
        "description": "la restaurant Casa Verona"
    },
    {
        "name": "intalnire de afaceri",
        "date": "2025-01-30",
        "time": "10:00",
        "description": "in Bucuresti, biroul principal"
    }
    ]

    return render_template("main_view.html",  events=list_of_events)