from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Define m and n
        m = len(matrix)
        n = len(matrix[0])
        
        def locate(pos):
            row = pos // n
            col = pos % n
            return (row, col)
        
        def bin_search(start, end):
            # if there is 0 remaining values to be searched
            if end < start:
                return False
            
            # if there are still value(s) to be searched
            mid = (start+end) // 2
            row, col = locate(mid)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                return bin_search(start, mid-1)
            else:
                return bin_search(mid+1, end)
        
        return bin_search(0, m*n-1)