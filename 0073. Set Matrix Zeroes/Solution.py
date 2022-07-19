# Space complexity of O(m+n)
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows = set()
        zero_cols = set()
        m = len(matrix)
        n = len(matrix[0])
        
        # Find the rows and cols with 0s
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zero_rows.add(row)
                    zero_cols.add(col)

        # Make all elements in rows and cols with 0s to be 0s
        for row in zero_rows:
            for col in range(n):
                matrix[row][col] = 0
        
        for col in zero_cols:
            for row in range(m):
                matrix[row][col] = 0