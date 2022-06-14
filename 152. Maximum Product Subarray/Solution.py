class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        temp_max = nums[0]
        temp_min = nums[0]
        
        for i in range(1, len(nums)):
            a = temp_max * nums[i]
            b = temp_min * nums[i]
            temp_max = max(max(a,b), nums[i])
            temp_min = min(min(a,b), nums[i])
            max_prod = max(temp_max, max_prod)
        
        return max_prod