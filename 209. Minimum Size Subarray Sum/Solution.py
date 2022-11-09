from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minSize = float("inf")
        l = r = 0
        sum = 0
        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target and l < len(nums):
                minSize = min(minSize, r - l + 1)
                sum -= nums[l]
                l += 1
        
        if minSize == float("inf"):
            return 0
        
        return minSize