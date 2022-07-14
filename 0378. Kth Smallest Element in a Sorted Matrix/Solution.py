from typing import List
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        leftright = list([matrix[0][0], matrix[n-1][n-1]])
        
        # Supporting function to count the numbers less than a value, and record the number to its immediate left and immediate right
        def count_less_than(mid):
            count = 0
            n = len(matrix)
            row = n - 1
            col = 0
            
            while (row >= 0 and col < n):
                # Why is it >= not ok here?
                if matrix[row][col] > mid:
                    leftright[1] = min(leftright[1], matrix[row][col])
                    row -= 1
                else:
                    count += (row+1)
                    leftright[0] = max(leftright[0], matrix[row][col])
                    col += 1
                    
            return count
        
        # Binary Search, value based, not index based
        start = matrix[0][0]
        end = matrix[n-1][n-1]
        while (start < end):
            mid = (start+end)//2
            leftright = list([matrix[0][0], matrix[n-1][n-1]])
            count = count_less_than(mid)
            if count == k:
                return leftright[0]
            elif count < k:
                start = leftright[1]
            else:
                end = leftright[0]
        return start