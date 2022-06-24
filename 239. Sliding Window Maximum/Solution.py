from typing import List
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = k-1
        
        max_sliding_window = [] # containing the indexes of the numbers
        q = collections.deque()
        
        # Iteratively add 1 number in the first window to the deque
        i = left
        while i <= right:
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
            i += 1
        max_sliding_window.append(nums[q[0]])
        
        # Iteratively shift the window by 1 and add 1 number to the deque
        left += 1
        right += 1
        while right < len(nums):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
            if q[0] < left:
                q.popleft()
            max_sliding_window.append(nums[q[0]])
            i += 1
            left += 1
            right += 1
        
        return max_sliding_window