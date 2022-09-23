import collections
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        
        # Edge case: When there is only 1 cell
        if m == n == 1:
            return [[0, 0]]
        
        pac, atl = set(), set()
        
        
        # Instead of DFS each cell, find the cells that the oceans can reach
        
        def dfs(r, c, visited):
            # Stack
            s = collections.deque()
            s.append((r, c))
            directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
            
            while s:
                cur = s.pop()
                
                if cur not in visited:
                    visited.add(cur)
                
                for direction in directions:
                    new_r = cur[0] + direction[0]
                    new_c = cur[1] + direction[1]

                    if 0 <= new_r < m and 0 <= new_c < n and (new_r, new_c) not in visited and heights[new_r][new_c] >= heights[cur[0]][cur[1]]:
                        s.append((new_r, new_c))
        
        for c in range(n):
            dfs(0, c, pac)
            dfs(m-1, c, atl)
        for r in range(m):
            dfs(r, 0, pac)
            dfs(r, n-1, atl)
            
        return pac & atl