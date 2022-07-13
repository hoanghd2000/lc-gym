from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        stack = []
        res = []
        
        def dfs_bt(h):
            if h == k:
                res.append(list(stack))
                return
            
            if h == 0:
                prev = 0
            else:
                prev = stack[-1]
            for next in range(prev+1, n-k+len(stack)+2):
                stack.append(next)
                dfs_bt(h+1)
                stack.pop()
        
        dfs_bt(0)
        return res