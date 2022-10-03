from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        
        for asteroid in asteroids:
            stack.append(asteroid)
            
            while len(stack) > 1 and stack[-1] < 0 and stack[-2] > 0:
                # print(stack)
                left = stack.pop()
                right = stack.pop()
                # print(left, right)

                if abs(left) > abs(right):
                    stack.append(left)
                elif abs(right) > abs(left):
                    stack.append(right)
            
                # print(stack)
        
        return stack