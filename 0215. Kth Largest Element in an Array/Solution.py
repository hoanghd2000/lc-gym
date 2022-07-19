from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        needed_index = len(nums) - k
        
        def swap(i1, i2):
            if i1 == i2:
                return
            temp = nums[i1]
            nums[i1] = nums[i2]
            nums[i2] = temp
        
        def quick_select(start, end):
            if start == end:
                return nums[start]
            
            mid = (start+end) // 2
            pivot = nums[mid]
            swap(start, mid)
            last_small = start
            
            # Arrange the elements according to the pivot
            for i in range(start+1, end+1):
                if nums[i] < pivot:
                    last_small += 1
                    swap(last_small, i)
            
            # Put the pivot to its final position
            fin = last_small
            swap(start, fin)
            
            # Check if the pivot position is the value needed
            if fin == needed_index:
                return nums[fin]
            elif needed_index < fin:
                return quick_select(start, fin-1)
            else:
                return quick_select(fin+1, end)

        
        return quick_select(0, len(nums)-1)