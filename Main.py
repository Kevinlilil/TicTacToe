from random import randint


playerSymbol = "X"
computerSymbol = "O"


# check if the spot is free
def checkFree(x, board):
    if board[x] == " ":
        return True
    else:
        return False


# check if any side wins the game
def checkWin(s, board):
    return (board[0] == s and board[1] == s and board[2] == s) \
           or (board[3] == s and board[4] == s and board[5] == s) \
           or (board[6] == s and board[7] == s and board[8] == s) \
           or (board[0] == s and board[3] == s and board[6] == s) \
           or (board[1] == s and board[4] == s and board[7] == s) \
           or (board[2] == s and board[5] == s and board[8] == s) \
           or (board[0] == s and board[4] == s and board[8] == s) \
           or (board[2] == s and board[4] == s and board[6] == s)


# make a copy of the board
def getCopy(board):
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy


def count(board):
    count = 0
    for i in board:
        if i != ' ':
            count += 1
    return count


# get a random move for computer check ahead (j) for possible winning situation
def getRandomMove(board):
    remainSpots = []
    for i in range(9):
        if checkFree(i, board):
            remainSpots.append(i)
    return remainSpots[randint(0, len(remainSpots) - 1)]


# other instructions
def other(board):
    # take the side if the player has two opposite connors
    if board[4] == computerSymbol and count(board) < 6:
        print('here')
        checklist = [1, 3, 5, 7]
        freelist = []
        # prevent the strategy that place one on connor and one in the opposite middle
        if board[1] == playerSymbol:
            checklist.remove(7)
        if board[7] == playerSymbol:
            checklist.remove(1)
        if board[3] == playerSymbol:
            checklist.remove(5)
        if board[5] == playerSymbol:
            checklist.remove(3)
        for i in checklist:
            if checkFree(i, board):
                freelist.append(i)
        return freelist[randint(0, len(freelist) - 1)]
    else:
        return 0


# get the index of computer's move
def getComputerMove(board, step):
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
    # take the center first
    if checkFree(4, board):
        return 4
    # take the connors if the center is taken
    elif board[4] == playerSymbol and step == 1:
        values = [0, 2, 6, 8]
        return values[randint(0, 3)]
    elif other(board) != 0:
        return other(board)
    else:
        return getRandomMove(board)


# player's move
def move(x, board, sym):
    board[x] = sym


# print the board in the format
def printBoard(board):
    for i in range(3):
        print("|" + board[0 + 3 * i] + "|" + board[1 + 3 * i] + "|" + board[2 + 3 * i] + "|"
              + "          |" + str(0 + 3 * i) + "|" + str(1 + 3 * i) + "|" + str(2 + 3 * i) + "|")

