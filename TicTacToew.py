from numpy import *
import random
import time


board = [[" "," "," "],
       [" "," "," "],
       [" "," "," "]]

pc = 0
player = 1

sym = [" ","O","X"]


def validatePos(pos):
    row = int(pos / 3)
    col = int(pos % 3)
    if board[row][col]==sym[0]:
        #print(f" computer valid move {pos}")
        return True
    else:
        #print(f" computer invalid move {pos}")
        return False


def computerTurn():
    pos = random.randrange(1,10)
    while not validatePos(pos-1):
        pos = random.randrange(1, 10)
    return pos


#check win chances
def rowWin(player):
    len = board.__len__()
    x = 0
    for row in range(len):
        for col in range(len):
            if board[row][col]==sym[player]:
                x = x + 1
            else:
                x=0
                break
        if x==len:
            print(f"player {player} won")
            return True
    return False

def colWin(player):
    len = board.__len__()
    x = 0
    for row in range(len):
        for col in range(len):
            if board[col][row]==sym[player]:
                x = x + 1
            else:
                x=0
                break
        if x==len:
            print(f"player {player} won")
            return True
    return False

def tedaWin(player):
    len = board.__len__()
    x = 0
    y = 0
    for row in range(len):
        if board[row][row] == sym[player]:
            x = x + 1
        if board[row][len-row-1] == sym[player]:
            y = y + 1
    if x == len or y == len:
        print(f"player {player} won")
        return True
    return False

def changeTurn():
    # change turn
    global player
    player = 1 if player == 2 else 2

def printBoard():
    len = board.__len__()
    print("")
    for row in range(len):
        if row>0 :
            print("__  __  __")
        for col in range(len):
            print(board[row][col],end=" ")
            if col<2:
                print("|",end=" ")
        print("")
    print("")

def addMove(player,pos):
    if pos<0 or pos>8:
        print(f"invalid input {pos}")
        return False
    row = int(pos / 3)
    col = int(pos % 3)
    if board[row][col]==sym[0]:
        board[row][col] = sym[player]
    else:
        print("invalid move")
        return False
    printBoard()
    return True

while(pc<9):
    if player == 1:
        # pos = computerTurn()
        # print("player 1 move : ", end="")
        # time.sleep(1)
        # print(pos)
        print("player 1 move : ",end=" ")
        pos = int(input("Enter your choioce : "))

    else :
        # pos = computerTurn()
        # print("player 2 move : ", end="")
        # time.sleep(1)
        # print(pos)
        print("player 2 move : ",end=" ")
        pos = int(input("Enter your choioce : "))
    if addMove(player,pos-1):
        pc = pc + 1
        if pc > 3:
            if rowWin(player) or colWin(player) or tedaWin(player):
                break
            elif pc == 9:
                print("It's a tie")
        changeTurn()

