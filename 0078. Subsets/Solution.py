# DFS
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        stack = []
        res = []
        n = len(nums)
        
        def dfs(h):
            # base case
            if h == n:
                res.append(list(stack))
                return
            
            # recursive step
            ## nums[h] not present in the subset
            dfs(h+1)
            
            ## nums[h] present in the subset
            stack.append(nums[h])
            dfs(h+1)
            stack.pop()
        
        dfs(0)
        return res