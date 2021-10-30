""" File: cb_utils_long.py
    Author: Xin Li
    Purpose: calculates all moves, all legal moves,
    checks a legal move and updates the board
"""
from moves import *

def legal_move(board,mov,s):
    """
    This function tells if a given move is legal or not
    Arguments: board is a list repersenting the board
    and mov is a tuple repersenting the move
    Return Value: True if legal move otherwise false
    Pre-condition: parameters not empty
    Note: NIL
    """
    # mov[0] is the starting position of move mov[1]
    # is the peg removed and mov[2] is the final position
    if(board[mov[0]]=='1' and board[mov[1]]=='1' and board[mov[2]]=='0'):
        return True
    else:
        return False

def legal_move_interface(board_str,mov,s):
    """
    This function converts the string of board into
    a array and calls the above function
    Arguments: board_str is a string repersenting
    the board and mov is a tuple repersenting the move
    Return Value: True if legal move otherwise false
    Pre-condition: parameters not empty
    Note: NIL
    """
    board=[]
    for x in range(0,len(board_str)):
        board.append(board_str[x])
    return legal_move(board,mov,s)

def all_legal_moves(size,board):
    """
    This function for a given board returns the legal moves array
    Arguments: board is a list repersenting the board
    and size is number of layers/levels of the board
    Return Value: a set of all legal moves
    Pre-condition: parameters not empty
    Note: NILNote: NILNote: NIL
    """
    legal=set()
    # uses all_move to calculate all moves
    allmove=all_moves(size)
    for x in allmove:
        # calls legal move to check if move is legal
        # if it is legal it appends to the array
        if(legal_move(board,x,size)):
            legal.add(x)
    return legal

def all_legal_moves_interface(size, board_str):
    """
    This function converts string to list and does same as above
    Arguments: board_str is a string repersenting the board
    and size is number of layers/levels of the board
    Return Value: a set of all legal moves
    Pre-condition: parameters not empty
    Note: NIL
    """
    board=[]
    for x in range(0,len(board_str)):
        board.append(board_str[x])
    return all_legal_moves(size,board)

def update_board(board,mov):
    """
    This function simply plays a given move on the board
    Arguments: board is a list repersenting the board
    and mov is tuple repersenting the move
    Return Value: The board after making the move
    Pre-condition: parameters not empty
    Note: NIL
    """
    board[mov[0]]="0"
    board[mov[1]]="0"
    board[mov[2]]="1"
    return board

def update_board_interface(board_str,mov):
    """
    This function converts the string into a board
    then calls above function and returns a string
    Arguments: board_str is a string repersenting
    the board and mov is tuple repersenting the move
    Return Value: A string of the new board
    Pre-condition: parameters not empty
    Note: NIL
    """
    board=[]
    for x in range(0,len(board_str)):
        board.append(board_str[x])
    temp=update_board(board,mov)
    s=""
    for c in temp:
        s=s+c
    return s
