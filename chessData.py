#this is the file that you will be editing to edit the display on the buttons

board = {
    "a8": "BR1n", "b8": "BN1", "c8": "BB1", "d8": "BQ1", "e8": "BK1n", "f8": "BB2", "g8": "BN2", "h8": "BR2n",
    "a7": "bp1", "b7": "bp2", "c7": "bp3", "d7": "bp4", "e7": "bp5", "f7": "bp6", "g7": "bp7", "h7": "bp8",
    "a6": "  ", "b6": "  ", "c6": "  ", "d6": "  ", "e6": "  ", "f6": "  ", "g6": "  ", "h6": "  ",
    "a5": "  ", "b5": "  ", "c5": "  ", "d5": "  ", "e5": "  ", "f5": "  ", "g5": "  ", "h5": "  ",
    "a4": "  ", "b4": "  ", "c4": "  ", "d4": "  ", "e4": "  ", "f4": "  ", "g4": "  ", "h4": "  ",
    "a3": "  ", "b3": "  ", "c3": "  ", "d3": "  ", "e3": "  ", "f3": "  ", "g3": "  ", "h3": "  ",
    "a2": "wp1", "b2": "wp2", "c2": "wp3", "d2": "wp4", "e2": "wp5", "f2": "wp6", "g2": "wp7", "h2": "wp8",
    "a1": "WR1n", "b1": "WN1", "c1": "WB1", "d1": "WQ1", "e1": "WK1n", "f1": "WB2", "g1": "WN2", "h1": "WR2n"}

piece = ["♜ ", "♞ ", "♝ ", "♛ ", "♚ ", "♟ ", "♜ ", "♞ ", "♝ ", "♛ ", "♚ ", "♟ "]

#can you implement these messages below into the loose screen with jinja?
lose = {"took the wrong turn", "squashed by an anvil", "fell too hard", "ate bad meat", "fell over"}

keysBoard, valuesBoard = zip(*board.items()) #isolates the board keys and board values

routesList =[]#emply list to fill with "/key "
imagesList =[]#list filled with the first two values of the key "BR" from "BR1n"
imagesInList =[]#list to fill with images


def preCursor(keys):#create the formaction list to pick from
    a = 0
    for x in keys:
        input = str(keys[a])
        final = "/" + input
        routesList.append(final)
        a = a+1
    return routesList

def sliceValues(values):#creates the list to translate into pieces
    a = 0
    for x in values:
        input = str(values[a])
        final = input[0:3]
        imagesList.append(final)
        a = a + 1
    return imagesList

"""def replaceValues(list): #using images will not work as there is no defalut image with a blank square
    for x in list:
        if x == "BR":
            imagesInList.append("https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Chess_rdt45.svg/50px-Chess_rdt45.svg.png")#black rook
        if x == "BN":
            imagesInList.append("https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Chess_ndt45.svg/50px-Chess_ndt45.svg.png")#black knight
        if x == "BB":
            imagesInList.append("https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Chess_bdt45.svg/50px-Chess_bdt45.svg.png")#black bishop
        if x == "BQ":
            imagesInList.append("https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Chess_qdt45.svg/50px-Chess_qdt45.svg.png")
        if x == "BK":
            imagesInList.append("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Chess_kdt45.svg/50px-Chess_kdt45.svg.png")
        if x == "bp":
            imagesInList.append("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Chess_pdt45.svg/50px-Chess_pdt45.svg.png")
        if x == "WR":
            imagesInList.append("https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Chess_rlt45.svg/50px-Chess_rlt45.svg.png")
        if x == "WN":
            imagesInList.append("https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Chess_nlt45.svg/50px-Chess_nlt45.svg.png")
        if x == "WB":
            imagesInList.append("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Chess_blt45.svg/50px-Chess_blt45.svg.png")
        if x == "WQ":
            imagesInList.append("https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Chess_qlt45.svg/50px-Chess_qlt45.svg.png")
        if x == "WK":
            imagesInList.append("https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Chess_klt45.svg/50px-Chess_klt45.svg.png")
        if x == "wp":
            imagesInList.append("https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Chess_plt45.svg/50px-Chess_plt45.svg.png")
        if x == "  ":
            imagesInList.append(" ")"""
# unicode chess pieces: https://en.wikipedia.org/wiki/Chess_symbols_in_Unicode

def replaceValues(list):
  for x in list:
    if x == "BR":
      imagesInList.append("♜")
    if x == "BN":
      imagesInList.append("♞")
    if x == "BB":
      imagesInList.append("♝")
    if x == "BQ":
      imagesInList.append("♛")
    if x == "BK":
      imagesInList.append("♚")
    if x == "bp":
      imagesInList.append("♟")
    if x == "WR":
      imagesInList.append("♖")
    if x == "WN":
      imagesInList.append("♘")
    if x == "WB":
      imagesInList.append("♗")
    if x == "WQ":
      imagesInList.append("♕")
    if x == "WK":
      imagesInList.append("♔")
    if x == "wp":
      imagesInList.append("♙")
    if x == "  ":
      imagesInList.append(" ")

#the row dictonaries that the board is split out two
board1 = {}
board2 = {}
board3 = {}
board4 = {}
board5 = {}
board6 = {}
board7 = {}
board8 = {}

for square,piece in board.items(): #spliting the dictonary into 8 dictonaries, if the second value within the cell "a8" is 8 then update the row of the board with that value
    if int(square[1]) == 1:
        board1.update({square:piece})
    elif int(square[1]) == 2:
        board2.update({square:piece})
    elif int(square[1]) == 3:
        board3.update({square:piece})
    elif int(square[1]) == 4:
        board4.update({square:piece})
    elif int(square[1]) == 5:
        board5.update({square:piece})
    elif int(square[1]) == 6:
        board6.update({square:piece})
    elif int(square[1]) == 7:
        board7.update({square:piece})
    elif int(square[1]) == 8:
        board8.update({square:piece})

allBoard = [board8, board7, board6, board5, board4, board3, board2, board1]

#keeping track of the moves
movelist = []

def movesdata(toAppend):
    movelist.append(toAppend)
    sets = [movelist[x:x+2] for x in range(0, len(movelist), 2)]
    return sets

sets = [movelist[x:x+2] for x in range(0, len(movelist), 2)]
