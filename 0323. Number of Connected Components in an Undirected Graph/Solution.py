from typing import List
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # Edge Case
        if not edges:
            return n

        sets = [-1] * n

        def find(v):
            p = sets[v]
            while p != -1:
                p = sets[v]
            return v
        
        def union(vset, wset):
            sets[vset] = wset
        
        for edge in edges:
            vset = find(edge[0])
            wset = find(edge[1])
            if vset != wset:
                union(vset, wset)
        
        count = len(set(sets)) - 1
        for i in sets:
            if i == -1:
                count += 1
        return count