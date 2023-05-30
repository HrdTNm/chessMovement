ChessBoard = ["Rook", "Knight", "Bishop", "Queen", "King", "Bishop", "Knight", "Rook"]
pieceColour = ["B", "W"]
kingMoved = [False, False]

def createBoard(): #Create a chess board
    Board = []
    Line = []
    for i in range(0, 8):     #Each line
        for j in range(0, 8): #Each colomn
            if i == 0:        #Line 1
                Line.append('B' + ChessBoard[j])     #Add black pieces
            elif i == 7:      #Line 8
                Line.append('W' + ChessBoard[j]) #Add white pieces 
            elif i == 1:      #Line 2
                Line.append("BPawn")                 #Add black pawns
            elif i == 6:      #Line 7
                Line.append("WPawn")                 #Add white pawns
            else:
                Line.append("")                      #Empty; no piece here
        Board.append(Line)
        Line = []
    return Board

def checkPlace(Board, Piece):    #check where is each pieces
    l = []
    bp = []                      #black pieces
    wp = []                      #white pieces
    k = 0                        #counter
    p = 0                        #counter
    for i in Board:
        for j in i:
            if j[1:] == Piece:
                if j[0] == 'W': #if it's white, go to white pieces list
                    wp.append(p*10 + k)
                else:
                    bp.append(p*10 + k)
            k += 1              #move to next colomns
        k = 0                   #go back to the first column
        p += 1                  #move to next line
        
    l.append(bp)
    l.append(wp)
    return l

def pawnMovement(Board, Colour, Place): #Colour should be 0 or 1, 0 means black, 1 means white; Board: the chess boardl; Place: the coordinate of the pawn
    p = [[70, 71, 72, 73, 74, 75, 76, 77],[0, 1, 2, 3, 4, 5, 6, 7]]
    if Place in checkPlace(Board, "Pawn")[Colour] and int(Place / 10) < 7 and int(Place / 10) > 0: #check if Place
        l = [] #list that will be return
        if Colour == 0: #check if it's black or not
            if len(Board[int(Place / 10) + 1][Place % 10]) == 0: #check is the front of the pieces empty or not
                l.append(Place + 10)                             #add the coordinate of that place into list
                if int(Place / 10) == 1 and len(Board[int(Place / 10) + 2][Place % 10]) == 0: #check if the pawn haven't move before and let it move 2 girds
                    l.append(Place + 20)
            if Place / 10 < 7 and Place % 10 < 7:                #avoid out of range
                if len(Board[int(Place / 10) + 1][Place % 10 + 1]) > 0: #check it's right front
                    if (Board[int(Place / 10) + 1][Place % 10 + 1][0] == "W"):
                        l.append(Place + 11)
            if Place / 10 < 0 and Place % 10 > 0:
                if len(Board[int(Place / 10) +1][Place % 10 - 1]) > 0: #check it's left front
                    if (Board[int(Place / 10) + 1][Place % 10 - 1][0] == "W"):
                        l.append(Place + 9)
        else: #if the piece is in another colour
            if len(Board[int(Place / 10) - 1][Place % 10]) == 0:
                l.append(Place - 10)
                if int(Place / 10) == 6 and len(Board[int(Place / 10) - 2][Place % 10]) == 0:
                    l.append(Place - 20)
            if Place / 10 > 0 and Place % 10 > 0:
                if len(Board[int(Place / 10) - 1][Place % 10 - 1]) > 0:
                    if (Board[int(Place / 10) - 1][Place % 10 - 1][0] == "B"):
                        l.append(Place - 11)
            if Place / 10 > 0 and Place % 10 < 7:
                if len(Board[int(Place / 10) - 1][Place % 10 + 1]) > 0:
                    if (Board[int(Place / 10) - 1][Place % 10 + 1][0] == "B"):
                        l.append(Place - 9)
            
            
        return l
    elif Place in p[Colour]:
        return "Changeable" #check that is the piece can be changed into another kind of it or not
    else:
        return None

def pawnChange(Board, Colour, Place, Kind):
    changeList = ["Rook", "Bishop", "Knight", "Queen"]
    if pawnMovement(Board, Colour, Place) == "Changeable" and Kind in changeList:
        Board[int(Place / 10)][Place % 10] = Board[int(Place / 10)][Place % 10][0] + Kind
    return Board

def rookMovement(Board, Colour, Place): #Colour should be 0 or 1, 0 means black, 1 means white
    l = []
    if Place in checkPlace(Board, "Rook")[Colour]:
        b = False #if b is true, then stop the loop
        j = 1     #counter
        while b == False: #check front
            if Place % 10 + j > 7: #if it's on the edge of the board
                b = True
                break
            if len(Board[int(Place / 10)][Place % 10 + j]) == 0: #if it's empty at front
                l.append(Place + j)
            elif Board[int(Place / 10)][Place % 10 + j][0] != pieceColour[Colour]: #if it can eat the piece at that point
                l.append(Place + j)
                b = True
            else:
                b = True
            j += 1
        b = False
        j = 1
        while b == False: #check back
            
            if Place % 10 - j < 0:
                b = True
                continue
            if len(Board[int(Place / 10)][Place % 10 - j]) == 0:
                l.append(Place - j)
            elif Board[int(Place / 10)][Place % 10 - j][0] != pieceColour[Colour]:
                l.append(Place - j)
                b = True
            else:
                b = True
            j += 1

        b = False
        j = 1
        while b == False: #check left
            if int(Place / 10) + j > 7:
                b = True
                break
            if len(Board[int(Place / 10) + j][Place % 10]) == 0:
                l.append(Place + j * 10)
            elif Board[int(Place / 10) + j][Place % 10][0] != pieceColour[Colour]:
                l.append(Place + j * 10)
                b = True
            else:
                b = True
            j += 1
        b = False
        j = 1
        while b == False: #check right
            if int(Place / 10) - j < 0:
                b = True
                break
            if len(Board[int(Place / 10) - j][Place % 10]) == 0:
                l.append(Place - j * 10)
            elif Board[int(Place / 10) - j][Place % 10][0] != pieceColour[Colour]:
                l.append(Place - j * 10)
                b = True
            else:
                b = True
            j += 1
        return l
    else:
        return None

def bishopMovement(Board, Colour, Place): #Colour should be 0 or 1, 0 means black, 1 means white
    if Place in checkPlace(Board, "Bishop")[Colour]:
        l = []
        b = False #similar as the rook's one, but changed some value
        j = 1
        while b == False:
            if Place % 10 + j > 7 or int(Place / 10) + j > 7:
                b = True
                break
            if len(Board[int(Place / 10) + j][Place % 10 + j]) == 0:
                l.append(Place + j * 11)
            elif Board[int(Place / 10) + j][Place % 10 + j][0] != pieceColour[Colour]:
                l.append(Place + j * 11)
                b = True
            else:
                b = True
            j += 1


        
        b = False
        j = 1
        while b == False:
            if Place % 10 - j < 0 or int(Place / 10) - j < 0:
                b = True
                break
            if len(Board[int(Place / 10) - j][Place % 10 - j]) == 0:
                l.append(Place - j * 11)
            elif Board[int(Place / 10) - j][Place % 10 - j][0] != pieceColour[Colour]:
                l.append(Place - j * 11)
                b = True
            else:
                b = True
            j += 1


        
        b = False
        j = 1
        while b == False:
            if Place % 10 - j < 0 or int(Place / 10) + j > 7:
                b = True
                break
            if len(Board[int(Place / 10) + j][Place % 10 - j]) == 0:
                l.append(Place + j * 9)
            elif Board[int(Place / 10) + j][Place % 10 - j][0] != pieceColour[Colour]:
                l.append(Place + j * 9)
                b = True
            else:
                b = True
            j += 1


        
        b = False
        j = 1
        while b == False:
            if Place % 10 + j > 7 or int(Place / 10) - j < 0:
                b = True
                break
            if len(Board[int(Place / 10) - j][Place % 10 + j]) == 0:
                l.append(Place - j * 9)
            elif Board[int(Place / 10) - j][Place % 10 + j][0] != pieceColour[Colour]:
                l.append(Place - j * 9)
                b = True
            else:
                b = True
            j += 1


        
        return l
        
    else:
        return None

def queenMovement(Board, Colour, Place): #Colour should be 0 or 1, 0 means black, 1 means white
    if Place in checkPlace(Board, "Queen")[Colour]: #it's the comblination of Rook and Bishop
        l = []





        
        l2 = [] #check Queen's straight movement
        b = False #if b is true, then stop the loop
        j = 1     #counter
        while b == False: #check front
            if Place % 10 + j > 7: #if it's on the edge of the board
                b = True
                break
            if len(Board[int(Place / 10)][Place % 10 + j]) == 0: #if it's empty at front
                l2.append(Place + j)
            elif Board[int(Place / 10)][Place % 10 + j][0] != pieceColour[Colour]: #if it can eat the piece at that point
                l2.append(Place + j)
                b = True
            else:
                b = True
            j += 1
        b = False
        j = 1
        while b == False: #check back
            if Place % 10 - j < 0:
                b = True
                continue
            if len(Board[int(Place / 10)][Place % 10 - j]) == 0:
                l2.append(Place - j)
            elif Board[int(Place / 10)][Place % 10 - j][0] != pieceColour[Colour]:
                l2.append(Place - j)
                b = True
            else:
                b = True
            j += 1
        b = False
        j = 1
        while b == False: #check left
            if int(Place / 10) + j > 7:
                b = True
                break
            if len(Board[int(Place / 10) + j][Place % 10]) == 0:
                l2.append(Place + j * 10)
            elif Board[int(Place / 10) + j][Place % 10][0] != pieceColour[Colour]:
                l2.append(Place + j * 10)
                b = True
            else:
                b = True
            j += 1
        b = False
        j = 1
        while b == False: #check right
            if int(Place / 10) - j < 0:
                b = True
                break
            if len(Board[int(Place / 10) - j][Place % 10]) == 0:
                l2.append(Place - j * 10)
            elif Board[int(Place / 10) - j][Place % 10][0] != pieceColour[Colour]:
                l2.append(Place - j * 10)
                b = True
            else:
                b = True
            j += 1

        l.append(l2)





        
        l2 = []
        b = False #check Queen's diagnal movement
        j = 1
        while b == False:
            if Place % 10 + j > 7 or int(Place / 10) + j > 7:
                b = True
                break
            if len(Board[int(Place / 10) + j][Place % 10 + j]) == 0:
                l2.append(Place + j * 11)
            elif Board[int(Place / 10) + j][Place % 10 + j][0] != pieceColour[Colour]:
                l2.append(Place + j * 11)
                b = True
            else:
                b = True
            j += 1


        
        b = False
        j = 1
        while b == False:
            if Place % 10 - j < 0 or int(Place / 10) - j < 0:
                b = True
                break
            if len(Board[int(Place / 10) - j][Place % 10 - j]) == 0:
                l2.append(Place - j * 11)
            elif Board[int(Place / 10) - j][Place % 10 - j][0] != pieceColour[Colour]:
                l2.append(Place - j * 11)
                b = True
            else:
                b = True
            j += 1


        
        b = False
        j = 1
        while b == False:
            if Place % 10 - j < 0 or int(Place / 10) + j > 7:
                b = True
                break
            if len(Board[int(Place / 10) + j][Place % 10 - j]) == 0:
                l2.append(Place + j * 9)
            elif Board[int(Place / 10) + j][Place % 10 - j][0] != pieceColour[Colour]:
                l2.append(Place + j * 9)
                b = True
            else:
                b = True
            j += 1


        
        b = False
        j = 1
        while b == False:
            if Place % 10 + j > 7 or int(Place / 10) - j < 0:
                b = True
                break
            if len(Board[int(Place / 10) - j][Place % 10 + j]) == 0:
                l2.append(Place - j * 9)
            elif Board[int(Place / 10) - j][Place % 10 + j][0] != pieceColour[Colour]:
                l2.append(Place - j * 9)
                b = True
            else:
                b = True
            j += 1

        l.append(l2)

        
        
        return l
    else:
        return None

def knightMovement(Board, Colour, Place): #Colour should be 0 or 1, 0 means black, 1 means white
    if Place in checkPlace(Board, "Knight")[Colour]:
        l = []
        if int(Place / 10) - 2 > 0 and Place % 10 + 1 < 7:  #back right(lower)
            if len(Board[int(Place / 10) - 2][Place % 10 + 1]) == 0:
                l.append(Place - 19)
            elif Board[int(Place / 10) - 2][Place % 10 + 1][0] != pieceColour[Colour]:
                l.append(Place - 19)

        
        if int(Place / 10) - 1 > 0 and Place % 10 + 2 < 7: #back right(higher)
            if len(Board[int(Place / 10) - 1][Place % 10 + 2]) == 0:
                l.append(Place - 8)
            elif Board[int(Place / 10) - 1][Place % 10 + 2][0] != pieceColour[Colour]:
                l.append(Place - 8)

        
        if int(Place / 10) + 2 < 7 and Place % 10 + 1 < 7: #front right(higher)
            if len(Board[int(Place / 10) + 2][Place % 10 + 1]) == 0:
                l.append(Place + 21)
            elif Board[int(Place / 10) + 2][Place % 10 + 1][0] != pieceColour[Colour]:
                l.append(Place + 21)

        
        if int(Place / 10) + 1 < 7 and Place % 10 + 2 < 7: #front right(lower)
            if len(Board[int(Place / 10) + 1][Place % 10 + 2]) == 0:
                l.append(Place + 12)
            elif Board[int(Place / 10) + 1][Place % 10 + 2][0] != pieceColour[Colour]:
                l.append(Place + 12)


        
        if int(Place / 10) + 2 < 7 and Place % 10 - 1 > 0: #front left(higher)
            if len(Board[int(Place / 10) + 2][Place % 10 - 1]) == 0:
                l.append(Place + 19)
            elif Board[int(Place / 10) + 2][Place % 10 - 1][0] != pieceColour[Colour]:
                l.append(Place + 19)

        
        if int(Place / 10) + 1 < 7 and Place % 10 - 2 > 0: #front left(lower)
            if len(Board[int(Place / 10) + 1][Place % 10 - 2]) == 0:
                l.append(Place + 8)
            elif Board[int(Place / 10) + 1][Place % 10 - 2][0] != pieceColour[Colour]:
                l.append(Place + 8)

        
        if int(Place / 10) - 2 > 0 and Place % 10 - 1 > 0: #back left(lower)
            if len(Board[int(Place / 10) - 2][Place % 10 - 1]) == 0:
                l.append(Place - 21)
            elif Board[int(Place / 10) - 2][Place % 10 - 1][0] == pieceColour[Colour]:
                l.append(Place - 21)

        
        if int(Place / 10) - 1 > 0 and Place % 10 - 2 > 0: #back left(higher)
            if len(Board[int(Place / 10) - 1][Place % 10 - 2]) == 0:
                l.append(Place - 12)
            elif Board[int(Place / 10) - 1][Place % 10 - 2][0] != pieceColour[Colour]:
                l.append(Place - 12)

        
        return l
    else:
        return None















def rookMovementNoLimit(Board, Colour, Place): #Colour should be 0 or 1, 0 means black, 1 means white
    l = []
    if Place in checkPlace(Board, "Rook")[Colour]:
        b = False #if b is true, then stop the loop
        j = 1     #counter
        while b == False: #check front
            if Place % 10 + j > 7: #if it's on the edge of the board
                b = True
                break
            if len(Board[int(Place / 10)][Place % 10 + j]) == 0: #if it's empty at front
                l.append(Place + j)
            else: #if it can eat the piece at that point(No limit version, it can even eat it's pieces)
                l.append(Place + j)
                b = True
            j += 1
        b = False
        j = 1
        while b == False: #check back
            
            if Place % 10 - j < 0:
                b = True
                continue
            if len(Board[int(Place / 10)][Place % 10 - j]) == 0:
                l.append(Place - j)
            else:
                l.append(Place - j)
                b = True
            j += 1

        b = False
        j = 1
        while b == False: #check left
            if int(Place / 10) + j > 7:
                b = True
                break
            if len(Board[int(Place / 10) + j][Place % 10]) == 0:
                l.append(Place + j * 10)
            else:
                l.append(Place + j * 10)
                b = True
            j += 1
        b = False
        j = 1
        while b == False: #check right
            if int(Place / 10) - j < 0:
                b = True
                break
            if len(Board[int(Place / 10) - j][Place % 10]) == 0:
                l.append(Place - j * 10)
            else:
                l.append(Place - j * 10)
                b = True
            j += 1
        return l
    else:
        return None

def bishopMovementNoLimit(Board, Colour, Place): #Colour should be 0 or 1, 0 means black, 1 means white
    if Place in checkPlace(Board, "Bishop")[Colour]:
        l = []
        b = False #similar as the rook's one, but changed some value
        j = 1
        while b == False:
            if Place % 10 + j > 7 or int(Place / 10) + j > 7:
                b = True
                break
            if len(Board[int(Place / 10) + j][Place % 10 + j]) == 0:
                l.append(Place + j * 11)
            else:
                l.append(Place + j * 11)
                b = True
            j += 1


        
        b = False
        j = 1
        while b == False:
            if Place % 10 - j < 0 or int(Place / 10) - j < 0:
                b = True
                break
            if len(Board[int(Place / 10) - j][Place % 10 - j]) == 0:
                l.append(Place - j * 11)
            else:
                l.append(Place - j * 11)
                b = True
            j += 1


        
        b = False
        j = 1
        while b == False:
            if Place % 10 - j < 0 or int(Place / 10) + j > 7:
                b = True
                break
            if len(Board[int(Place / 10) + j][Place % 10 - j]) == 0:
                l.append(Place + j * 9)
            else:
                l.append(Place + j * 9)
                b = True
            j += 1


        
        b = False
        j = 1
        while b == False:
            if Place % 10 + j > 7 or int(Place / 10) - j < 0:
                b = True
                break
            if len(Board[int(Place / 10) - j][Place % 10 + j]) == 0:
                l.append(Place - j * 9)
            else:
                l.append(Place - j * 9)
                b = True
            j += 1


        
        return l
        
    else:
        return None

def queenMovementNoLimit(Board, Colour, Place): #Colour should be 0 or 1, 0 means black, 1 means white
    if Place in checkPlace(Board, "Queen")[Colour]: #it's the comblination of Rook and Bishop
        l = []
        Board[int(Place / 10)][Place % 10] = pieceColour[Colour] + "Rook"
        l.append(rookMovementNoLimit(Board, Colour, Place))
        
        Board[int(Place / 10)][Place % 10] = pieceColour[Colour] + "Bishop"
        l.append(bishopMovementNoLimit(Board, Colour, Place))
        
        Board[int(Place / 10)][Place % 10] = pieceColour[Colour] + "Queen"
        
        return l
    else:
        return None

def knightMovementNoLimit(Board, Colour, Place): #Colour should be 0 or 1, 0 means black, 1 means white
    if Place in checkPlace(Board, "Knight")[Colour]:
        l = []
        if int(Place / 10) - 2 > 0 and Place % 10 + 1 < 7:  #back right(lower)
            l.append(Place - 19)
        
        if int(Place / 10) - 1 > 0 and Place % 10 + 2 < 7: #back right(higher)
            l.append(Place - 8)

        
        if int(Place / 10) + 2 < 7 and Place % 10 + 1 < 7: #front right(higher)
            l.append(Place + 21)

        
        if int(Place / 10) + 1 < 7 and Place % 10 + 2 < 7: #front right(lower)
            l.append(Place + 12)


        
        if int(Place / 10) + 2 < 7 and Place % 10 - 1 > 0: #front left(higher)
            l.append(Place + 19)

        
        if int(Place / 10) + 1 < 7 and Place % 10 - 2 > 0: #front left(lower)
            l.append(Place + 8)

        
        if int(Place / 10) - 2 > 0 and Place % 10 - 1 > 0: #back left(lower)
            l.append(Place - 21)

        
        if int(Place / 10) - 1 > 0 and Place % 10 - 2 > 0: #back left(higher)
                l.append(Place - 12)

        
        return l
    else:
        return None

















def kingCanNotGo(Board, Colour): #Colour should be 0 or 1, 0 means black, 1 means white; This colour is for king's colour
    #check where king can go, where king can't
    forbidenArea = [] #the place that king can't move to
    for i in range(0, 4):
        for j in checkPlace(Board, ChessBoard[i])[1 - Colour]: #check each piece's movement
            if ChessBoard[i] == "Rook":
                for k in rookMovementNoLimit(Board, 1 - Colour, j): #Avoid repeating values
                    if k not in forbidenArea:
                        forbidenArea.append(k)
            
            elif ChessBoard[i] == "Knight":
                for k in knightMovementNoLimit(Board, 1 - Colour, j):
                    if k not in forbidenArea:
                        forbidenArea.append(k)
            
            elif ChessBoard[i] == "Bishop":
                for k in bishopMovementNoLimit(Board, 1 - Colour, j):
                    if k not in forbidenArea:
                        forbidenArea.append(k)
            
            elif ChessBoard[i] == "Queen":
                for k in queenMovementNoLimit(Board, 1 - Colour, j)[0]: #Queen moves straitly
                    if k not in forbidenArea:
                        forbidenArea.append(k)
                for k in queenMovementNoLimit(Board, 1 - Colour, j)[1]: #Queen moves diagonally
                    if k not in forbidenArea:
                        forbidenArea.append(k)
            
    for i in checkPlace(Board, "Pawn")[1 - Colour]: #check pawns' move
        if Colour == 1:
            if int(i / 10) + 1 >= 0 and int(i / 10) + 1 < 8:
                if i % 10 + 1 < 8: #avoid out of range
                    if (i + 11) not in forbidenArea:
                        forbidenArea.append(i + 11)
                if i % 10 - 1 >= 0:
                    if (i + 9) not in forbidenArea:
                        forbidenArea.append(i + 9)
        else:
            if int(i / 10) - 1 >= 0 and int(i / 10) - 1 < 8:
                if i % 10 - 1 >= 0: #avoid out of range
                    if (i - 11) not in forbidenArea:
                        forbidenArea.append(i - 11)
                if i % 10 + 1 < 8:
                    if (i - 9) not in forbidenArea:
                        forbidenArea.append(i - 9)
    
    kMovelist = [-11, -10, -9, -1, 1, 9, 10, 11] #the difference between two coordinate of king's place and place it can move to
    kPlace = checkPlace(Board, "King")[1 - Colour][0] #check another king's place
    for move in kMovelist:
        if (kPlace + move) / 10 >= 0 and (kPlace + move) / 10 < 8 and (kPlace + move) % 10 >= 0 and (kPlace + move) % 10 < 8: #avoid go out the board
            if kPlace + move not in forbidenArea:
                forbidenArea.append(kPlace + move)
            
    return forbidenArea


def checkKing(Board, Colour): #to determine check king
    if checkPlace(Board, "King")[Colour][0] in kingCanNotGo(Board, Colour):
        return True
    return False

def castling(Board, P1, P2):
    x1 = P1 % 10
    y1 = int(P1 / 10)
    x2 = P2 % 10
    y2 = int(P2 / 10)
    Colour = 0
    k = 1
    if Board[y1][x1][0] == "W":
        Colour = 1
        k = 1
    if checkKing(Board, Colour) == True:
        return False
    if len(Board[y1][x1][0]) == 0 or len(Board[y2][x2]) == 0:
        return False
    RookPlace = [[0, 7], [70, 77]]
    if Board[y1][x1][0] == Board[y2][x2][0]:
        if Board[y1][x1][1:] == "King" and Board[y2][x2][1:] == "Rook":
            if kingMoved[Colour] == False:
                if P2 in RookPlace[Colour]:
                    b = True
                    r1 = x1 + 1
                    r2 = x2
                    if x1 < x2:
                        r1 = x2 + 1
                        r2 = x1
                    for i in range(r1, r2):
                        if len(Board[y1][i]) > 0:
                            b = False
                        if (y1 * 10 + i) in kingCanNotGo(Board, Colour):
                            b = False
                    return b
    return False
                        

def kingMovement(Board, Colour, Place): #Colour should be 0 or 1, 0 means black, 1 means white
    kMovelist = [-11, -10, -9, -1, 1, 9, 10, 11] #the difference between two coordinate of king's place and place it can move to
    kForbidenList = kingCanNotGo(Board, Colour)
    if Place in checkPlace(Board, "King")[Colour]:
        l = []
        for move in kMovelist: 
            if Place + move not in kForbidenList:
                if (Place + move) / 10 >= 0 and (Place + move) / 10 < 8 and (Place + move) % 10 >= 0 and (Place + move) % 10 < 8: #avoid go out the board
                    if len(Board[int((Place + move) / 10)][(Place + move) % 10]) == 0:
                        l.append(Place + move)
                    elif Board[int((Place + move) / 10)][(Place + move) % 10][0] != pieceColour[Colour]: #check the colour to avoid eat itself's pieces
                        l.append(Place + move)
        k = 1
        if kingMoved[Colour] == False:
            if castling(Board, Place, Place + k * 3) == True:
                l.append(Place + k * 2)
            if castling(Board, Place, Place - k * 4) == True:
                l.append(Place - k * 3)
            
        return l
    else:
        return None



def pieceMovement(Board, P1, P2): #Detect if a piece can go from P1 to P2

    d = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 5, 'F' : 6, 'G' : 7}
    P1 = d[P1[0].upper()] + int(P1[1]) * 10 - 11
    P2 = d[P2[0].upper()] + int(P2[1]) * 10 - 11
    
    
    if len(Board[int(P1 / 10)][P1 % 10]) == 0:
        return "NO PIECE IN THIS PLACE"
    else:
        b = False
        pieceKind = Board[int(P1 / 10)][P1 % 10][1:]
        Colour = 0
        if Board[int(P1 / 10)][P1 % 10][0] == 'W':
            Colour = 1
        if pieceKind == "Pawn":
            if P2 in pawnMovement(Board, Colour, P1):
                b = True
            elif pawnMovement(Board, Colour, P1) == "Changeable":
                return "Changeable"
        elif pieceKind == "Rook":
            if P2 in rookMovement(Board, Colour, P1):
                b = True
        elif pieceKind == "Bishop":
            if P2 in bishopMovement(Board, Colour, P1):
                b = True
        elif pieceKind == "Queen":
            if P2 in queenMovement(Board, Colour, P1)[0] or  P2 in queenMovemnt(Board, Colour, P1)[1]:
                b = True
        elif pieceKind == "Knight":
            if P2 in knightMovement(Board, Colour, P1):
                b = True
        elif pieceKind == "King":
            if P2 in kingMovement(Board, Colour, P1):
                b = True
        return b

def pieceMove(Board, P1, P2, C): #move a piece on board to another place
    d = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 5, 'F' : 6, 'G' : 7}
    a = d[P1[0].upper()] + int(P1[1]) * 10 - 11
    b = d[P2[0].upper()] + int(P2[1]) * 10 - 11
    Colour = 0
    if len(Board[int(a / 10)][a % 10]) == 0:
        return "No piece here"
    if Board[int(a / 10)][a % 10][0] == "W":
        Colour = 1
    if C != Colour:
        return "You can't move this piece"
    if checkKing(Board, Colour) == True and Board[int(a / 10)][a % 10][1:] != "King":
        return "Move your king first"
    else:
        if pieceMovement(Board, P1, P2) == True:
    
            if Board[int(a / 10)][a % 10] == "King": # check if the king moved
                kingMoved[Colour] = True
            Board[int(b / 10)][b % 10] = Board[int(a / 10)][a % 10]
            Board[int(a / 10)][a % 10] = ""
            return Board
        elif pieceMovement(Board, P1, P2) != False:
            return pieceMovement(Board, P1, P2)
        else:
            return "Can't move"

def hasValidMoves(Board, Colour):
    valid_moves = []
    for row in range(8):
        for col in range(8):
            piece = Board[row][col]
            if piece != '' and piece[0] == 'B' and Colour == 0:  # Black piece
                if piece == 'BPawn' and pawnMovement(Board, Colour, row * 10 + col) != None:
                    valid_moves = pawnMovement(Board, Colour, row * 10 + col)
                elif piece == 'BRook' and rookMovement(Board, Colour, row * 10 + col) != None:
                    valid_moves = rookMovement(Board, Colour, row * 10 + col)
                elif piece == 'BBishop' and bishopMovement(Board, Colour, row * 10 + col) != None:
                    valid_moves = bishopMovement(Board, Colour, row * 10 + col)
                elif piece == 'BKnight' and knightMovement(Board, Colour, row * 10 + col) != None:
                    valid_moves = knightMovement(Board, Colour, row * 10 + col)
                elif piece == 'BQueen' and queenMovement(Board, Colour, row * 10 + col) != None:
                    valid_moves = queenMovement(Board, Colour, row * 10 + col)
                elif piece == 'BKing' and  kingMovement(Board, Colour, row * 10 + col) != None:
                    valid_moves = kingMovement(Board, Colour, row * 10 + col)
                else:
                    valid_moves = []
                if len(valid_moves) > 0:
                    return True
            elif piece != '' and piece[0] == 'W' and Colour == 1:  # White piece
                if piece == 'WPawn':
                    valid_moves = pawnMovement(Board, Colour, row * 10 + col)
                elif piece == 'WRook':
                    valid_moves = rookMovement(Board, Colour, row * 10 + col)
                elif piece == 'WBishop':
                    valid_moves = bishopMovement(Board, Colour, row * 10 + col)
                elif piece == 'WKnight':
                    valid_moves = knightMovement(Board, Colour, row * 10 + col)
                elif piece == 'WQueen':
                    valid_moves = queenMovement(Board, Colour, row * 10 + col)
                elif piece == 'WKing':
                    valid_moves = kingMovement(Board, Colour, row * 10 + col)
                else:
                    valid_moves = []
                if len(valid_moves) > 0:
                    return True
    return False


def gameSituation(Board):
    if len(kingMovement(Board, 0, checkPlace(Board, "King")[0][0])) == 0:
        if checkKing(Board, 0) == True:
            return "White wins"
    if len(kingMovement(Board, 1, checkPlace(Board, "King")[1][0])) == 0:
        if checkKing(Board, 1) == True:
            return "Black wins"
    if hasValidMoves(Board, 1) == False or hasValidMoves(Board, 0) == False:
        return "Draw"
    else:
        return "Continue"
