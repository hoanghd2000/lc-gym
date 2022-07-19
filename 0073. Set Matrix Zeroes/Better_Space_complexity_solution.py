# Space complexity of O(1)
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        # Check if 1st row contain 0s
        row1_zero = False
        for num in matrix[0]:
            if num == 0:
                row1_zero = True
                break
        
        # Find the rows and cols with 0s, except 1st row, record the result by the first element of row/col
        for row in range(1, m):
            for col in range(n):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        # Make all elements in rows and cols with 0s to be 0s
        for row in range(1, m):
            if matrix[row][0] == 0:
                for col in range(1, n):
                    matrix[row][col] = 0
        
        for col in range(n):
            if matrix[0][col] == 0:
                for row in range(1, m):
                    matrix[row][col] = 0
        
        if row1_zero:
            for col in range(n):
                matrix[0][col] = 0