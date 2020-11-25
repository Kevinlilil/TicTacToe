import math

gameBoard = ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
playerSymbol = "X"
computerSymbol = "O"


def evaluate(board):
    global playerSymbol

    if (board[0] == playerSymbol and board[1] == playerSymbol and board[2] == playerSymbol) \
            or (board[3] == playerSymbol and board[4] == playerSymbol and board[5] == playerSymbol) \
            or (board[6] == playerSymbol and board[7] == playerSymbol and board[8] == playerSymbol) \
            or (board[0] == playerSymbol and board[3] == playerSymbol and board[6] == playerSymbol) \
            or (board[1] == playerSymbol and board[4] == playerSymbol and board[7] == playerSymbol) \
            or (board[2] == playerSymbol and board[5] == playerSymbol and board[8] == playerSymbol) \
            or (board[0] == playerSymbol and board[4] == playerSymbol and board[8] == playerSymbol) \
            or (board[2] == playerSymbol and board[4] == playerSymbol and board[6] == playerSymbol):
        return +10

    if (board[0] == computerSymbol and board[1] == playerSymbol and board[2] == playerSymbol) \
            or (board[3] == computerSymbol and board[4] == computerSymbol and board[5] == computerSymbol) \
            or (board[6] == computerSymbol and board[7] == computerSymbol and board[8] == computerSymbol) \
            or (board[0] == computerSymbol and board[3] == computerSymbol and board[6] == computerSymbol) \
            or (board[1] == computerSymbol and board[4] == computerSymbol and board[7] == computerSymbol) \
            or (board[2] == computerSymbol and board[5] == computerSymbol and board[8] == computerSymbol) \
            or (board[0] == computerSymbol and board[4] == computerSymbol and board[8] == computerSymbol) \
            or (board[2] == computerSymbol and board[4] == computerSymbol and board[6] == computerSymbol):
        return -10
    return 0


def countRemain(board):
    count = 0
    for i in board:
        if i == " ":
            count += 1
    return count


def minimax(board, depth, isMax):
    score = evaluate(board)
    if score == 10:
        return score - depth

    if score == -10:
        return score + depth

    if countRemain(board) == 0:
        return 0

    if isMax:
        bestValue = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = playerSymbol
                bestValue = max(bestValue, minimax(board, depth + 1, not isMax))
                board[i] = ' '
        return bestValue

    else:
        bestValue = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = computerSymbol
                bestValue = min(bestValue, minimax(board, depth + 1, not isMax))
                board[i] = ' '
        return bestValue


def findMove(board):
    bestValue = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = playerSymbol
            value = minimax(board, 0, False)
            board[i] = ' '
            if value > bestValue:
                bestValue = value
                print(bestValue)
                move = i
    return move


def checkWin(s, board):
    return (board[0] == s and board[1] == s and board[2] == s) \
           or (board[3] == s and board[4] == s and board[5] == s) \
           or (board[6] == s and board[7] == s and board[8] == s) \
           or (board[0] == s and board[3] == s and board[6] == s) \
           or (board[1] == s and board[4] == s and board[7] == s) \
           or (board[2] == s and board[5] == s and board[8] == s) \
           or (board[0] == s and board[4] == s and board[8] == s) \
           or (board[2] == s and board[4] == s and board[6] == s)


# def printBoard(board):
#     for i in range(3):
#         print("|" + board[0 + 3 * i] + "|" + board[1 + 3 * i] + "|" + board[2 + 3 * i] + "|"
#               + "          |" + str(0 + 3 * i) + "|" + str(1 + 3 * i) + "|" + str(2 + 3 * i) + "|")

