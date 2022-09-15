from typing import List
import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        # Queue for BFS
        q = collections.deque()
        # directions
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        
        # Init
        numFresh = 0
        numMinute = -1
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    numFresh += 1
        
        # Edge cases
        if numFresh == 0:
            return 0
        if not q:
            return -1
        
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                
                for dir in directions:
                    new_r = cur[0] + dir[0]
                    new_c = cur[1] + dir[1]
                    if 0 <= new_r < m and 0 <= new_c < n:
                        if grid[new_r][new_c] == 1:
                            q.append((new_r, new_c))
                            grid[new_r][new_c] = 2
                
            numMinute += 1
        
        # Result
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    return -1
        return numMinute