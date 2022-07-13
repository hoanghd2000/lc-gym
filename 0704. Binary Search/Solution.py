from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bin_search(start, end):
            # base case 1
            if end - start < 0:
                return -1
            
            # base case 2
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            
            # recursive step
            elif nums[mid] > target:
                return bin_search(start, mid-1)
            else:
                return bin_search(mid+1, end)
            
        return bin_search(0, len(nums)-1)