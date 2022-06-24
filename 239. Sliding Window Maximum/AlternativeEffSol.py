from typing import List
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque() # store the indexes of the values
        l = r = 0

        while r < len(nums):
            # pop smaller values from q before appending the next value
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            # remove out-of-bound left val from the deque
            if l > q[0]:
                q.popleft()
            
            # append the sliding window maxima to the output array
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output
