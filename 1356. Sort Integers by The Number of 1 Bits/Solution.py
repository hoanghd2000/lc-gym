from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        bit_nums = {}
        for num in arr:
            bin_num = format(num, 'b')
            count = 0
            for ch in bin_num:
                if ch == '1':
                    count += 1
            if count in bit_nums:
                bit_nums[count].append(num)
            else:
                bit_nums[count] = [num]
        
        res = []
        for key in sorted(bit_nums.keys()):
            res.extend(sorted(bit_nums[key]))
        
        return res