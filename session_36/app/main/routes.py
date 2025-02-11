from werkzeug.utils import redirect

from app.main import main
from flask import render_template, request, session, url_for
from app.main.models import Event
from app.extensions import db


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
        print(message)
        event = Event(
            name_event = name,
            date = date,
            time = time,
            description = description
        )
        db.session.add(event)
        db.session.commit()

    return render_template('add_event.html', message=message)


@main.route('/delete_event', methods=['GET', 'POST'])
def delete_event():

    list_of_events = Event.query.all()
    print(list_of_events)

    if request.method == "POST":
        event_name= request.form.get('event_name')
        print(event_name)
        event = Event.query.filter_by(name_event=event_name).first()
        db.session.delete(event)
        db.session.commit()
        #list_of_events = Event.query.all()
        return redirect(url_for('main.delete_event'))


    return render_template("delete_event.html",events=list_of_events)


@main.route('/')
def show_events():
    list_of_events = Event.query.all()
    print(list_of_events)


    return render_template("main_view.html",  events=list_of_events)