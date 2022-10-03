import collections
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        noOfDays = len(temperatures)
        
        # Edge case
        if noOfDays == 1:
            return [0]
        
        answer = [0] * noOfDays
        stack = collections.deque() # Each element has format (day, temperature)
        
        # O(n)
        for day, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                cur = stack.pop()
                answer[cur[0]] = day - cur[0]
            stack.append((day, temp))
                    
        return answer