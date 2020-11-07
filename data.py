def string():
    greeting = "Testing with Strings"
    name = "Testing with Strings"
    doa = "Week 1"
    job = "Ideating"
    description = "press run and answer the question in the program"
    embed = "https://repl.it/@colinszeto/Testing?lite=true"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "description": description, "embed": embed}
    return info

def billards():
    greeting = "Billiards Balls"
    name = "Billiards Balls"
    doa = "Week 2"
    job = "Testing Print with Color"
    description = "type in 8 into the terminal and press enter to run the program"
    embed = "https://repl.it/@colinszeto/Python-Hello-Series?lite=true"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "description": description, "embed": embed}
    return info

def ship():
    greeting = "Ship with Star Trails"
    name = "Ship with Star Trails"
    doa = "Week 3"
    job = "Testing Print with Color"
    description = "press run and scroll down to see the animation"
    embed = "https://repl.it/@colinszeto/Ship-moving-test?lite=true"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "description": description,"embed": embed}
    return info

def chessOO():
    greeting = "Chess OO"
    name = "Chess OO"
    doa = "Week 4"
    job = "able to use concatenation to save the move characters as variables to move the ship"
    description = "press run and scroll down to see the print"
    embed = "https://repl.it/@colinszeto/OG-ASCII-Class-test?lite=true"
    titleImage = [
        "                            ",
        "       _                    ",
        "   ___| |__   ___  ___ ___  ",
        "  / __| '_ \ / _ \/ __/ __| ",
        " | (__| | | |  __/\__ \__ \ ",
        "  \___|_| |_|\___||___/___/ "
    ]
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "description": description,"embed": embed, "titleImage": titleImage}
    return info

def pawnANI():
    greeting = "Pawn Animation"
    name = "Pawn Animation"
    doa = "Week 5"
    job = "able to use concatenation to move ascii art to different pieces"
    description = "press run and scroll down to see the animation automatically run"
    embed = "https://repl.it/@colinszeto/Chess-ANI?lite=true"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "description": description, "embed": embed}
    return info

def oldWebsite():
    greeting = "Old Website"
    name = "Old Website"
    doa = "Week 6"
    job = "repl portfolio"
    description = "press run and scroll down to see website within REPL"
    embed = "https://repl.it/@colinszeto/Python-Web-Portfolio-Series?lite=true"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "description": description, "embed": embed}
    return info

def chessDrag():
    greeting = "Chess Dragable"
    name = "Chess Dragable"
    doa = "Week 7"
    job = "Using JS to move chess pieces"
    embed = "https://repl.it/@colinszeto/Chess-in-Website-Dragable?lite=true"
    description = "scroll down to drag pieces of the chess board"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "description": description,"embed": embed}
    return info

def chessDrag():
    greeting = "Chess in Tiles"
    name = "Chess in Tiles"
    doa = "Week 7"
    job = "Using JS to move chess pieces into cells which allow for snap to middle"
    embed = "https://repl.it/@colinszeto/Chess-in-Titles?lite=true"
    description = "scroll down to drag pieces of the chess board"
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "description": description,"embed": embed}
    return info
"""
def proj1 ():
    name = "hello there"
    embed = "embed link"
    date =""
    linkOut = " "
    info = {"name ":name, "embed": embed, "date": date, "linkOut": lineout}
    return info
"""

def alldata():
    return [string(), billards(),ship(),chessOO(), pawnANI(), oldWebsite(), chessDrag()]