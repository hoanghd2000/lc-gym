import collections
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        
        # Edge case: When there is only 1 cell
        if m == n == 1:
            return [[0, 0]]
        
        result = []
        # result.append([0, 4], [4, 0])
        
        def dfs(r, c):
            s = collections.deque()
            s.append((r, c))
            directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
            status = 'N'
            # Status: N, P, A, B
            
            while s:
                cur = s.pop()
                
                if cur[0] == 0 or cur[1] == 0:
                    if status == 'A':
                        return True
                    else:
                        status = 'P'
                
                if cur[0] == m-1 or cur[1] == n-1:
                    if status == 'P':
                        return True
                    else:
                        status = 'A'
                
                for direction in directions:
                    new_r = cur[0] + direction[0]
                    new_c = cur[1] + direction[1]

                    if 0 <= new_r < m and 0 <= new_c < n and heights[new_r][new_c] <= heights[cur[0]][cur[1]]:
                        s.append((new_r, new_c))
            
            return False
        
        for r in range(m):
            for c in range(n):
                if dfs(r, c):
                    result.append([r, c])
            
        return result 