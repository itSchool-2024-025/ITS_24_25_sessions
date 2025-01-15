from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello world!"

@app.route('/about')
def about():
    return """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Flask App</title>
            </head>
            <body>
                <h1>Welcome to Flask!</h1>
            </body>
            </html>"""

@app.route('/story')
def story_2():
    return render_template("story.html")

@app.route('/story_upgrade')
def story_upgraded():
    return render_template("story_with_vars.html",
                           title="Titlu frumos",
                           name="Tumbuctu")

if __name__ == "__main__":
    app.run(debug=True)