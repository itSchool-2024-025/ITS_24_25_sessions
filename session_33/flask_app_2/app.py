from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import Blueprint

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello world!"


@app.route('/story_upgrade')
def story_upgraded():
    return render_template("story_with_vars.html",
                           title="Titlu frumos",
                           name="Tumbuctu")


@app.route("/if")
def ifelse():
    user = "Adi"
    return render_template("if_template.html",
                           name=user)


@app.route("/for")
def for_loop():
    list_of_courses = ['Java', 'Python', 'C++', 'C#']
    return render_template("for_example.html",
                           prog_languages=list_of_courses)


@app.route("/choice/<pick>")
def choice(pick):
    if pick == 'story_upgrade':
        return redirect(url_for('story_upgraded'))
    if pick == 'if':
        return redirect(url_for('ifelse'))
    if pick == 'for':
        return redirect(url_for('for_loop'))

if __name__ == "__main__":
    app.run(debug=True)