from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        current_left = 0
        current_right = len(height) - 1
        max_area = (right - left) * min((height[left], height[right]))
        while current_left < current_right:
            if height[current_left] < height[current_right]:
                while current_left < len(height) and height[left] >= height[current_left]:
                    current_left += 1
                area = (current_right - current_left) * min((height[current_left], height[current_right]))
                if area > max_area:
                    max_area = area
                left = current_left
                right = current_right
            else:
                while current_right >= 0 and height[right] >= height[current_right]:
                    current_right -= 1
                area = (current_right - current_left) * min((height[current_left], height[current_right]))
                if area > max_area:
                    max_area = area
                left = current_left
                right = current_right
        return max_area