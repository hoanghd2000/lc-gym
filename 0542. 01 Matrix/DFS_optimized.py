from typing import List
import collections
# Approach: For each cell, BFS to find the nearest 0. Report the distance of the nearest 0 for that cell
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # m = no. of rows, n = no. of cols
        m = len(mat)
        n = len(mat[0])
        
        # Matrix to store each cell's distance to the nearest 0
        dis_to_0_mat = [[float('inf')]*n for r in range(m)]
            
        directions = ((0, 1), (0, -1), (-1, 0), (1, 0))
        # Queue for BFS
        q = collections.deque()
        
        # Enqueue all cells that are 0 onto the queue
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    dis_to_0_mat[r][c] = 0
                    q.append((r, c))
        
        while q:
            # print(q)
            cur = q.popleft()
            
            # For each of the cur node's neighbour, do the following:
            for direction in directions:
                new_r = cur[0] + direction[0]
                new_c = cur[1] + direction[1]
                if 0 <= new_r < m and 0 <= new_c < n:
                    if mat[new_r][new_c] != 0 and dis_to_0_mat[new_r][new_c] > dis_to_0_mat[cur[0]][cur[1]] + 1:
                        dis_to_0_mat[new_r][new_c] = dis_to_0_mat[cur[0]][cur[1]] + 1
                        q.append((new_r, new_c))
        
        return dis_to_0_mat