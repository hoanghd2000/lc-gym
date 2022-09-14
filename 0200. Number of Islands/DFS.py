from typing import List
import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        # To keep track of "1" cells visited
        visited = set()
        
        def bfs(r, c):
            directions = ((-1, 0), (1, 0), (0, 1), (0, -1))
            q = collections.deque()
            
            q.append((r, c))
            
            while q:
                cur = q.pop()
                visited.add(cur)
                
                for direction in directions:
                    new_r = cur[0] + direction[0]
                    new_c = cur[1] + direction[1]
                    if 0 <= new_r < m and 0 <= new_c < n:
                        if grid[new_r][new_c] == '1' and (new_r, new_c) not in visited:
                            q.append((new_r, new_c))
        
        
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1' and (r, c) not in visited:
                    res += 1
                    bfs(r, c)
        
        return res