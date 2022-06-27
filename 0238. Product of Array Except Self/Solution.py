class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = 1
        answer = [1] * len(nums)
        for i in range(1, len(nums)):
            product *= nums[i-1]
            answer[i] *= product
        product = 1
        for i in range(len(nums) - 2, -1, -1):
            product *= nums[i+1]
            answer[i] *= product
        return answer