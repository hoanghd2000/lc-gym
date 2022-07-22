from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_sequence_length = 0
        nums = set(nums)
        
        for num in nums:
            # For each number num, if nums does not contain num-1, then the number does not belong to an existing consecutive sequence.
            if num-1 not in nums:
                sequence_length = 1
                nxt = num + 1
                
                # Obtain the length of the consecutive sequence starting with num
                while nxt in nums:
                    sequence_length += 1
                    nxt += 1
                
                # Update the longest_sequence_length if needed
                longest_sequence_length = max(longest_sequence_length, sequence_length)
            
            # For num which num-1 is in the set, the num has already been counted as part of an existing consecutive sequence
        return longest_sequence_length