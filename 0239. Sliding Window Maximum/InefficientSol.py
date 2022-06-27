from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_sliding_window = [max(nums[0:k])]
        for i in range(1,len(nums)-k+1):
            prev_max = max_sliding_window[-1]
            if nums[i+k-1] >= prev_max:
                    max_sliding_window.append(nums[i+k-1])
            else:
                if nums[i-1] < prev_max:
                    max_sliding_window.append(prev_max)
                else:
                    max_sliding_window.append(max(nums[i:i+k]))
        return max_sliding_window