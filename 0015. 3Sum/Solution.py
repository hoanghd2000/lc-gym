from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Handle special case, len < 3:
        if len(nums) < 3:
            return []
        
        # Sort the array
        nums.sort()
        
        # Create a hash map of the array with the values as the keys and the last position of the values as the values
        hash_map = {}
        for i in range(len(nums)-1, -1, -1):
            if nums[i] in hash_map:
                continue
            else:
                hash_map[nums[i]] = i
        
        # Find the triplet in O(n^2)
        triplets = []
        i = 0
        while i < len(nums):
            if nums[i] > 0:
                break
            j = i+1
            while j < len(nums):
                third_no = -(nums[i] + nums[j])
                if third_no < 0 or third_no < nums[j]: 
                    break
                elif third_no in hash_map:
                    if hash_map[third_no] > j:
                        l = [nums[i], nums[j], third_no]
                        if l not in triplets:
                            triplets.append(l)
                j = hash_map[nums[j]]
                j += 1
            i = hash_map[nums[i]]
            i += 1
        return triplets