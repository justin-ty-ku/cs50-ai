"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


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
    num_X = 0
    num_O = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                num_X += 1
            elif board[i][j] == O:
                num_O += 1
    if num_X > num_O:
        return O
    elif num_O == num_X:
        return X
    return None


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] != X and board[i][j] != O:
                actions.add((i, j))
    if len(actions) == 0:
        return None
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError
    new_board = copy.deepcopy(board)
    (i, j) = action
    new_board[i][j] = player(board)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Horizontal
    for row in board:
        if len(set(row)) == 1 and row[0] is not None:
            return row[0]
    # Vertical
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not None:
            return board[0][j]
    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    # No winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return (winner(board) is not None) or actions(board) is None


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    optimal_action = None

    # Maximizing player
    if player(board) == X:
        v = -float('inf')
        for action in actions(board):
            if min_value(result(board, action)) > v:
                v = min_value(result(board, action))
                optimal_action = action
        return optimal_action
    
    # Minimizing player
    else:
        v = float('inf')
        for action in actions(board):
            if max_value(result(board, action)) < v:
                v = min_value(result(board, action))
                optimal_action = action
        return optimal_action

def max_value(board):
    v = -float('inf')
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    v = float('inf')
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v