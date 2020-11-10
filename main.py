# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template, request, redirect, url_for
import data
from data import board, keysBoard
from itertools import islice #for the printing of the chess board
#create a Flask instance
app = Flask(__name__)

#connects default URL of server to a python function
@app.route('/')
def home():
    #function use Flask import (Jinga) to render an HTML template
    return render_template("home.html", data=data.ship(), data2=data.chessOO(), data3=data.billards())

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
#---------------------------------------------------------------------------------------
@app.route("/yourName") #within the /yourName directory
def index():
    return render_template("yourName.html", display="") #this is the default what is displayed (right now it is nothing)

@app.route("/printName", methods=['GET','POST']) #this is is where the website directs to when clicking the submit button
def yourName():
    if request.method == 'POST': #if the meathod is post
        form = request.form
        first = str(form['inputName']) #takes the input and converts it to a string, if it was a integer data type be sure to change str to int
        last = str(form['inputLast'])
        allName = first + " " + last
        return render_template("yourName.html", display = allName) #feeds it back into the template using jinja
    return redirect("/yourName")#redirects the user back to the page where they entered in the form
#---------------------------------------------------------------------------------------

@app.route("/project/string/")
def string_route():
    return render_template("task.html", data=data.string())

@app.route("/project/billards/")
def billards_route():
    return render_template("task.html", data=data.billards())

@app.route("/project/ship/")
def ship_route():
    return render_template("task.html", data=data.ship())

@app.route("/project/chessOO/")
def chessOO_route():
    return render_template("task.html", data=data.chessOO())

@app.route("/project/pawnANI/")
def pawnANI_route():
    return render_template("task.html", data=data.pawnANI())

@app.route("/project/oldWeb/")
def oldWeb_route():
    return render_template("task.html", data=data.oldWebsite())

@app.route("/project/chessDrag/")
def chessDrag_route():
    return render_template("task.html", data=data.chessDrag())

@app.route("/project/chessDict/")
def chessDict_route():
    return render_template("chessDict.html")

@app.route("/createBoard", methods=['GET','POST']) #this is is where the website directs to when clicking the submit button
def createBoard():
    if request.method == 'POST': #if the meathod is post
        form = request.form
        return render_template("chessDict.html", rowList=board, keyRoutes=data.preCursor(keysBoard)) #feeds it back into the template using jinja
    return redirect("/project/chessDict/")

@app.route("/helloClicked", methods=['GET','POST']) #this is is where the website directs to when clicking the submit button
def helloClicked():
    if request.method == 'POST':
        form = request.form
        return render_template("chessDict.html", rowList=board, displayClicked="Hello!")
    return redirect("/project/chessDict/")

@app.route("/project/login/", methods=['GET','POST']) #this is is where the website directs to when clicking the submit button
def login():
    if request.method =="POST":
        user = request.form["nm"]
        render_template("user.html", userDisplay=user)
        return  redirect("/project/login/")
        #return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return render_template("user.html", userDisplay=usr)

@app.route("/all/")
def all_route():
    return render_template("taskall.html", datalist=data.alldata())

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True)