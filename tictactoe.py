"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None
boardlen = 3
starter = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    numX = 0
    numO = 0
    global starter
    for i in range(boardlen):
        for j in range(boardlen):
            if board[i][j] == X:
                numX += 1
            elif board[i][j] == O:
                numO += 1
    if numX == numO:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionset = []
    for i in range(boardlen):
        for j in range(boardlen):
            if board[i][j] == EMPTY:
                actionset.append((i,j))
    return actionset


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise NameError("This tile has already Occupied")
    boardtemp = board.copy()
    user = player(boardtemp)
    boardtemp[action[0]][action[1]] = user
    return boardtemp

def line(board,user):
    for i in range(boardlen):
        num = 0
        for j in range(boardlen):
            if board[i][j] == user:
                num += 1
        if num == boardlen:
            return True
    for i in range(boardlen):
        num = 0
        for j in range(boardlen):
            if board[j][i] == user:
                num += 1
        if num == boardlen:
            return True
    num = 0
    for i in range(boardlen):
        if board[i][i] == user:
                num += 1
    if num == boardlen:
        return True
    num = 0
    for i in range(boardlen):
        if board[i][boardlen-1-i] == user:
            num += 1
    if num == boardlen:
        return True
    return False


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if line(board,X):
        return X
    if line(board,O):
        return O
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    for i in range(boardlen):
        for j in range(boardlen):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0

def utilityhelp(board):
    """
    Returns the optimal action for the current player on the board.
    """
    user = player(board)
    v = -math.inf if user == X else math.inf
    actionset = actions(board)
    for (i,j) in actionset:
        boardtemp = [row[:] for row in board]
        boardtemp[i][j] = user
        if terminal(boardtemp):
            res = utility(boardtemp)
        else:
            res = utilityhelp(boardtemp)

        if user == X:
            if res > v:
                v = res
        else:
            if res < v:
                v = res
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    user = player(board)
    v = -math.inf if user == X else math.inf
    actionset = actions(board)
    if terminal(board):
        return None
    ansset = (-1,-1)
    for (i,j) in actionset:
        boardtemp = [row[:] for row in board]
        boardtemp[i][j] = user
        if terminal(boardtemp):
            res = utility(boardtemp)
        else:
            res = utilityhelp(boardtemp)
        if user == X:
            if res > v:
                v = res
                ansset = (i,j)
        else:
            if res < v:
                v = res
                ansset = (i,j)
    return ansset



