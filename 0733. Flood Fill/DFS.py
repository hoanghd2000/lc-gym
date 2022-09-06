from typing import List

# Solve using DFS, to find all the connected nodes in the graph (connected when they have the same color in the original image)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # m = no. of rows, n = no. of cols
        m = len(image)
        n = len(image[0])
        
        # Source node color
        s_color = image[sr][sc]
        
        # Set of visited nodes
        visited = set()
        # Directions that I can take from my current position
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        
        # Find all connected node in the image and change their color
        def dfs(r, c):
            if (r, c) not in visited:
                visited.add((r, c)) # Lesson: List is not hashable
                
                # Exploring neighboring nodes
                for direction in directions:
                    new_r = r + direction[1]
                    new_c = c + direction[0]
                    
                    if 0 <= new_r < m and 0 <= new_c < n and image[new_r][new_c] == s_color:
                        dfs(new_r, new_c)
                        
        dfs(sr, sc)
        for visited_node in visited:
            image[visited_node[0]][visited_node[1]] = color
        
        return image