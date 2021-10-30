""" File: cb_solver.py
    Author: Xin Li
    Purpose: calculates the solution of a set of solutions
    to a given board
"""

from cb_utils import *
# boolean variable used to break look is solution is found in cb_one
solutionbool=False

def solution(board):
    """
    This function tells if solution has been reached or not
    Arguments: board is a list repersenting the board
    Return Value: true if solution is reached false if not
    Pre-condition: parameters not empty
    Note: NIL
    """
    global solutionbool
    c=0
    for x in range(0,len(board)):
        if(int(board[x])==1):
            c=c+1
    if(c==1):
        solutionbool=True
        return True
    else:
        return False
    # an arrary used by cb_one
solutionarr=[]

def cb_one(size,config):
    """
    This function returns a string of a possible solution
    Arguments: size is the level of the board and config
    a string repersenting the board
    Return Value: A string of a possible solution
    Pre-condition: parameters not empty
    Note: NIL
    """
    # calculates all legal moves possible on a board
    moves=all_legal_moves_interface(size,config)
    # base statement of the recurrsion if no moves
    # possible check solution is reached
    if(len(moves)==0):
        if(solution(config)):
            return
        else:
            # if solution not reached by a move remove the move from array
            return
    else:
        # play one move from the legal moves and itself again
        for move in moves:
            board=update_board_interface(config,move)
            # append the moves played
            solutionarr.append(move)
            cb_one(size,board)
            # if solution reached break loop
            if(solutionbool):
                break
            solutionarr.pop()
    if(len(solutionarr)==0):
        return None
    else:
        return str(solutionarr)



# set used by cb_all
solutions=set()

def cb_all(size,config,s=[]):
    """
    This function returns a set of all possible solution
    Arguments: size is the level of the board and config a string
    repersenting the board and s in a empty array
    Return Value: A set of all possible solution
    Pre-condition: parameters not empty
    Note: NIL
    """
    # calculates all legal moves possible on a board
    moves=all_legal_moves(size,config)
    # base statement of the recurrsion if no moves
    # possible check solution is reached
    if(len(moves)==0):
        if(solution(config)):
            ar=s
            # is solution is reached add to set
            solutions.add(str(ar))
            return
        else:
            return
    else:
        # play one move from the legal moves and itself again
        for move in moves:
            board=update_board_interface(config,move)
            s.append(move)
            cb_all(size,board,s)
            # pop the array when returning from a recursion
            if(len(s)!=0):
                s.pop()
    if(len(solutions)==0):
        return None
    else:
        return solutions
