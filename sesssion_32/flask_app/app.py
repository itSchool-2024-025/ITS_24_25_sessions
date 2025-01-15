from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/about')
def about():
    return "This is a dummy text!"

@app.route('/math')
def sum_web():
    return str(14+15)

@app.route('/story')
def story():
# #### **Slide 9: Rendering Templates**
# - Use HTML templates stored in the `templates/` folder.
# - **Example Template (index.html):**
# ```
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

@app.route('/story_ren')
def story_ren():
    return render_template("story.html")


@app.route('/story_ren_upgraded')
def story_ren_upgraded():
    dict_vars = {
        "name": "Dan",
        "title": "Flask App"
    }
    return render_template("story_with_vars.html",
                           name=dict_vars["name"], title=dict_vars["title"])

if __name__ == '__main__':
    app.run(debug=True)












