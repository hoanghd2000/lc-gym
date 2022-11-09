from typing import List

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0
        remainders = [0] * 60
        for t in time:
            remainders[t % 60] += 1
        
        for i in range(1, 30):
            res += (remainders[i] * remainders[60-i])
        
        res += (remainders[0] * (remainders[0] - 1) // 2)
        res += (remainders[30] * (remainders[30] - 1) // 2)
        
        return res