from typing import List
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRows(board):
            for row in board:
                items = []
                for item in row:
                    if item != '.' and item in items:
                        return False
                    else:
                        items.append(item)
            return True
        
        def checkSquares(board):
            for row1 in range(0, 7, 3):
                for col1 in range(0, 7, 3):
                    items = []
                    for row in range(row1, row1+3):
                        for col in range(col1, col1 + 3):
                            item = board[row][col]
                            if item != '.' and item in items:
                                return False
                            else:
                                items.append(item)
            return True
        
        # Actual code
        transpose_board = zip(*board)
        return checkRows(board) and checkRows(transpose_board) and checkSquares(board)