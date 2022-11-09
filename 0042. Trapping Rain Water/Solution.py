from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0
        
        for i, h in enumerate(height):            
            while stack and h > height[stack[-1]]:
                cur = stack.pop()
                if stack:
                    distance = i - stack[-1] - 1
                    bounded_height = min(height[stack[-1]], h) - height[cur]
                    water += (distance * bounded_height)
            stack.append(i)
                
        return water