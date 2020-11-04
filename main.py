# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template, request, redirect
#create a Flask instance
app = Flask(__name__)

#connects default URL of server to a python function
@app.route('/')
def home():
    #function use Flask import (Jinga) to render an HTML template
    return render_template("home.html")

@app.route('/chessGame/')
def chessGame():
    #function use Flask import (Jinga) to render an HTML template
    return render_template("chessGame.html")

@app.route("/chessEmbed/")#for the dragable chess file
def chessEmbed():
    return render_template("chessEmbed.html")

@app.route('/hello/')
def helloThere():
    #function use Flask import (Jinga) to render an HTML template
    return render_template("helloThere.html")

@app.route("/yourName")
def index():
    return render_template("yourName.html", display="")

@app.route("/printName", methods=['GET','POST'])
def yourName():
    if request.method == 'POST':
        form = request.form
        returnName = str(form['inputName'])
        return render_template("yourName.html", display = returnName)
    return redirect("/yourName")

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True)