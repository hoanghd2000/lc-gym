import collections
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Edge cases
        if numCourses == 1:
            return True
        if not prerequisites:
            return True
        
        nodes = {}
        order = []
        q = collections.deque()
        
        for node in range(numCourses):
            nodes[node] = {'in': 0, 'out': set()}
        
        for edge in prerequisites:
            nodes[edge[0]]['in'] += 1
            nodes[edge[1]]['out'].add(edge[0])
         
        for node in range(numCourses):
            if nodes[node]['in'] == 0:
                q.append(node)
        
        while q:
            cur = q.popleft()
            
            order.append(cur)
            for neigh in nodes[cur]['out']:
                nodes[neigh]['in'] -= 1
                if nodes[neigh]['in'] == 0:
                    q.append(neigh)
        
        if len(order) == numCourses:
            return True
        else:
            return False