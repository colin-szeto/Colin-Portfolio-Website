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
    titleImage = [
        "____",
        "dP9CGG88@b",
        "IP..... _.......Y888@@b",
        "dIi .........(_)  .............G888@b",
        "dCII.........(_)..........G888@@b",
        "GCCIi.....................GG88@@@",
        "GGCCCCCCCGG88888@@@",
        "GGGCGG88)))))888@@@@...",
        "Y8GGGG88))888@@@@P.....",
        "Y88888))88@@@@@P......",
        "`Y88888@@@@@P......",
        "`@@@@@@P.......",
        "........ "]
    info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "description": description, "embed": embed, "titleImage": titleImage}

    return info

def ship():
   greeting = "Ship with Star Trails"
   name = "Ship with Star Trails"
   doa = "Week 3"
   job = "Testing Print with Color"
   description = "press run and scroll down to see the animation"
   embed = "https://repl.it/@colinszeto/Ship-moving-test?lite=true"
   titleImage = ["         __/__     //", "    ____/_____|   // ", "___/___\______\__//__", "\    < < < < < < <    /", " \_________________/ "]
   info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "description": description,"embed": embed,"titleImage": titleImage}
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
   titleImage = [

       "         ",
       "         ",
       "         ",
       "         ",
       "         ",
       "    _    ",
       "   (_)   ",
       "  (___)  ",
       "  _|_|_  ",
       " (_____) ",
       " /_____\ "
   ]
   info = {"greeting": greeting, "name": name, "doa": doa, "job": job, "description": description, "embed": embed, "titleImage": titleImage}
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

def alldata():
    return [string(), billards(),ship(),chessOO(), pawnANI(), oldWebsite(), chessDrag()]

board = {
    "a8": "BR1n", "b8": "BN1", "c8": "BB1", "d8": "BQ1", "e8": "BK1n", "f8": "BB2", "g8": "BN2", "h8": "BR2n",
    "a7": "bp1", "b7": "bp2", "c7": "bp3", "d7": "bp4", "e7": "bp5", "f7": "bp6", "g7": "bp7", "h7": "bp8",
    "a6": "  ", "b6": "  ", "c6": "  ", "d6": "  ", "e6": "  ", "f6": "  ", "g6": "  ", "h6": "  ",
    "a5": "  ", "b5": "  ", "c5": "  ", "d5": "  ", "e5": "  ", "f5": "  ", "g5": "  ", "h5": "  ",
    "a4": "  ", "b4": "  ", "c4": "  ", "d4": "  ", "e4": "  ", "f4": "  ", "g4": "  ", "h4": "  ",
    "a3": "  ", "b3": "  ", "c3": "  ", "d3": "  ", "e3": "  ", "f3": "  ", "g3": "  ", "h3": "  ",
    "a2": "wp1", "b2": "wp2", "c2": "wp3", "d2": "wp4", "e2": "wp5", "f2": "wp6", "g2": "wp7", "h2": "wp8",
    "a1": "WR1n", "b1": "WN1", "c1": "WB1", "d1": "WQ1", "e1": "WK1n", "f1": "WB2", "g1": "WN2", "h1": "WR2n"
}
"""boardKeys = board.keys()#these are the key values found with board

def convertToRoute(keys):#places "/" to the front of each key
    for x in keys:
        keys[x]= "/"+ keys[x]
    return keys"""
keysBoard, values = zip(*board.items()) #isolates the board keys
routesList =[]
def preCursor(keys):
    a = 0
    for x in keys:
        input = str(keys[a])
        final = "/" + input
        routesList.append(final)
        a = a+1
    return routesList

def chunks(data, SIZE=10000):
    it = iter(data)
    for i in range(0, len(data), SIZE):
        yield {k:data[k] for k in islice(it, SIZE)}

rowList = []
def createBoard(board):
    for item in chunks(board, 8):
        rowList.append(item)
    return rowList #this should have each dictonary for each value of the row