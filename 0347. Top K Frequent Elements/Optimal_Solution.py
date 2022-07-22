from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Edge case
        if len(nums) == 1:
            return nums
        
        # Freq counter -> n
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        
        # Hashmap (array of n elements), in which count -> count - 1 as index, values are the nums with that count -> m (number of unique numbers in nums, O(n))
        counts = [[] for i in range(len(nums))]
        for num in counter:
            counts[counter[num]-1].append(num)
        
        res = []
        n = len(nums) - 1
        
        # O(n)
        while k > 0:
            if counts[n]:
                res.extend(counts[n])
                k -= len(counts[n])
            n -= 1
        
        # Overall, O(n)
        return res