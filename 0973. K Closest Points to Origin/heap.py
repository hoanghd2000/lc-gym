import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Edge case
        if len(points) == k == 1:
            return points
        
        dists = []
        for point in points:
            dist = point[0]**2 + point[1]**2
            dists.append((dist, point))
        
        heapq.heapify(dists)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(dists)[1])
        
        return res