from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        noOfDays = len(temperatures)
        
        # Edge case
        if noOfDays == 1:
            return [0]
        
        answer = [0] * noOfDays
        
        for i, temp in enumerate(temperatures):
            for j in range(i+1, noOfDays):
                if temperatures[j] > temp:
                    answer[i] = j - i
                    break
                    
        return answer