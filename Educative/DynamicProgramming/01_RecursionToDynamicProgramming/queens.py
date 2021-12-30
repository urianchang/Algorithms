"""
You are given an NxN chessboard, and you are required to place N queens 
on this chessboard such that no queen is under threat from any other queen.

This means that no queen should share a row, column, or diagonal with another queen.
"""
from typing import List


def isSafe(i, j, board) -> bool:
    # Provided helper function
    for c in range(len(board)):
        for r in range(len(board)):
            # check rows
            if board[c][r] == 'q' and i==c and j!=r:
                return False
            # check columns
            elif board[c][r] == 'q' and j==r and i!=c:
                return False
            # check diagonal
            elif (i+j == c+r or i-j == c-r) and board[c][r] == 'q':
                return False
    return True 


def nQueens(r, n, board) -> (bool, List[str]):
    # base case
    if r == n:
        return True, board
    for i in range(n):
        if isSafe(r, i, board):
            board[r][i] = "q"
            # Check if next queen can be placed safely
            isOk, newBoard = nQueens(r+1, n, board)
            if isOk:
                return True, newBoard
            # Else: not a suitable place to put this queen
            board[r][i] = "-"
    return False, board


def placeNQueens(n, board) -> List[str]:
    # Time complexity is high: O(n^n)
    _, board = nQueens(0, n, board)
    return board


n = 5
board = [["-" for _ in range(n)] for _ in range(n)]

qBoard = placeNQueens(n, board)
qBoard =  "\n".join(["".join(x) for x in qBoard])
print (qBoard)
