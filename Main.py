from random import randint

playerSymbol = "X"
computerSymbol = "O"
gameWin = False


# Determine player and symbol
def getPlayer():
    global playerSymbol
    global computerSymbol
    print("Do you want to be 'X' or 'O'")
    ip = input()
    if ip == "O":
        playerSymbol = "O"
        computerSymbol = "X"
        return
    elif ip != "X" and ip != "O":
        print("Try again")
        getPlayer()
    else:
        return


# check if the spot is free
def checkFree(x, board):
    if board[x] == " ":
        return True
    else:
        return False


# check if any side wins the game
def checkWin(s, bo):
    return (bo[0] == s and bo[1] == s and bo[2] == s) \
           or (bo[3] == s and bo[4] == s and bo[5] == s) \
           or (bo[6] == s and bo[7] == s and bo[8] == s) \
           or (bo[0] == s and bo[3] == s and bo[6] == s) \
           or (bo[1] == s and bo[4] == s and bo[7] == s) \
           or (bo[2] == s and bo[5] == s and bo[8] == s) \
           or (bo[0] == s and bo[4] == s and bo[8] == s) \
           or (bo[2] == s and bo[4] == s and bo[6] == s)


# make a copy of the board
def getCopy(board):
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy


# get a random move for computer
def getRandomMove(board):
    remainSpots = []
    for i in range(9):
        if checkFree(i, board):
            remainSpots.append(i)
    return remainSpots[(randint(0, len(remainSpots) - 1))]


# get the index of computer's move
def getComputerMove(board):
    global step
    copyComputer = getCopy(board)
    for j in range(9):
        if checkFree(j, copyComputer):
            move(j, copyComputer, computerSymbol)
            if checkWin(computerSymbol, copyComputer):
                return j
            else:
                copyComputer[j] = board[j]

    copyPlayer = getCopy(board)
    for i in range(9):
        if checkFree(i, copyPlayer):
            move(i, copyPlayer, playerSymbol)
            if checkWin(playerSymbol, copyPlayer):
                return i
            else:
                copyPlayer[i] = board[i]

    if checkFree(4, board):
        return 4
    elif board[4] == playerSymbol and step == 1:
        values = [0, 2, 6, 8]
        return values[randint(0, 3)]
    else:
        return getRandomMove(board)


# print the board in the format
def printBoard(board):
    for i in range(3):
        print("|" + board[0 + 3 * i] + "|" + board[1 + 3 * i] + "|" + board[2 + 3 * i] + "|"
              + "          |" + str(0 + 3 * i) + "|" + str(1 + 3 * i) + "|" + str(2 + 3 * i) + "|")


# player's move
def move(x, board, sym):
    board[x] = sym


# gameBoard = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
# getPlayer()
#
# gameEnd = False
# step = 0
#
# while not gameEnd:
#     printBoard(gameBoard)
#     print("player's turn:")
#
#     indexPlayer = int(input("number between 0-8: "))
#     while indexPlayer > 8 or not checkFree(indexPlayer, gameBoard):
#         indexPlayer = int(input("out of range, try again: "))
#
#     move(indexPlayer, gameBoard, playerSymbol)
#     step += 1
#
#     if step >= 9 or checkWin(playerSymbol, gameBoard):
#         break
#     print("computer's turn:")
#     move(getComputerMove(gameBoard), gameBoard, computerSymbol)
#     step += 1
#     if checkWin(computerSymbol, gameBoard):
#         break
#
# printBoard(gameBoard)
# print("game over")
