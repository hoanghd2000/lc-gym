from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minSize = len(nums)+1
        l = sum = 0
        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target and l < len(nums):
                minSize = min(minSize, r - l + 1)
                sum -= nums[l]
                l += 1
        
        return 0 if minSize == len(nums)+1 else minSize