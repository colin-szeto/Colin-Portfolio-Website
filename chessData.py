#this is the file that you will be editing to edit the display on the buttons

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
#can you implement these messages below into the loose screen with jinja?
lose = {"took the wrong turn", "squashed by an anvil", "fell too hard", "ate bad meat", "fell over"}

keysBoard, values = zip(*board.items()) #isolates the board keys

routesList =[]#emply list to fill with "/key "

def preCursor(keys):#create the formaction list to pick from
    a = 0
    for x in keys:
        input = str(keys[a])
        final = "/" + input
        routesList.append(final)
        a = a+1
    return routesList

"""
endRoutesList =[]#empty list to fill with "/id=c4/" not implemented yet

def routeMaker(keys):#creates the paths that main.py has to create to respond to chessDict, this has not been immplemnted yet
    a = 0
    for x in keys:
        input = str(keys[a])
        final = "/id=" + input + "/"
        routesList.append(final)
        a = a+1
    return endRoutesList"""
