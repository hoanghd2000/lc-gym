from typing import List
import collections
# Approach: For each cell, BFS to find the nearest 0. Report the distance of the nearest 0 for that cell
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # m = no. of rows, n = no. of cols
        m = len(mat)
        n = len(mat[0])
        
        # Matrix to store each cell's distance to the nearest 0
        dis_to_0_mat = [[0]*n for r in range(m)]
        
        # For each cell, BFS to find the nearest 0
        def bfs(r, c):
            visited = set()
            directions = ((0, 1), (0, -1), (-1, 0), (1, 0))
            
            q = collections.deque()
            q.append((r, c))
            while q:
                # print(q)
                cur = q.popleft()
                if cur is not visited:
                    visited.add(cur)
                    if mat[cur[0]][cur[1]] == 0:
                        # print(cur[0], cur[1])
                        return abs(cur[0]-r) + abs(cur[1]-c)
                    for direction in directions:
                        new_r = cur[0] + direction[0]
                        new_c = cur[1] + direction[1]
                        if 0 <= new_r < m and 0 <= new_c < n and (new_r, new_c) not in visited:
                            q.append((new_r, new_c))
        
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    continue
                else:
                    dis_to_0_mat[r][c] = bfs(r, c)
        
        return dis_to_0_mat