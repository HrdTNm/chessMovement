from chessMovement import *
#from graphics import *

def showBoard(Board):
    for i in Board:
        s = ""
        for j in i:
            l = len(j)
            if len(j) == 0:
                s += "None"
                l = 4
            else:
                s += j
            s +=  ' ' * (8 - l)
            
        print(s)
        print()

def trueCoordinate(Crdnt):
    if len(Crdnt) != 2:
        return False
    elif not (((ord(Crdnt[0]) >= ord('a') and ord(Crdnt[0]) <= ord('h')) or (ord(Crdnt[0]) >= ord('A') and ord(Crdnt[0]) <= ord('H'))) and (ord(Crdnt[1]) >= ord('1') and ord(Crdnt[1]) <= ord('8'))):
        return False
    return True

def main():
    board = createBoard()
    
    move = []
    showBoard(board)
    j = 1
    stt = gameSituation(board)
    while stt == "Continue" or stt[3:] == "Change Pawn":
        print()
        print()
        print()
        stt = gameSituation(board)
        if stt[3:] == "Change Pawn":
            knd = input("You can change your pawn. Which kind do you want to change?")
            board = pawnChange(board, int(stt[2]), int(stt[0:2]), knd)
            showBoard(board)
            stt = gameSituation(board)
            continue
            
            
        move = []
        move.append(input("Which piece you want to move?"))
        move.append(input("Where do you want to move?"))
        print()
        print()
        print()
        if trueCoordinate(move[0]) == False or trueCoordinate(move[1]) == False:
            print("Enter again")
            continue
        bUpdate = pieceMove(board, move[0], move[1], j % 2)
        if len(bUpdate) == 8:
            board = bUpdate
            showBoard(board)
            stt = gameSituation(board)
            j += 1
        else:
            print(bUpdate)
main()
