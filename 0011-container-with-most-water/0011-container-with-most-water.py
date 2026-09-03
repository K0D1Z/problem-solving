class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        area = 0
        while left <= right:
            w = right - left
            h = min(height[left], height[right])
            if w * h > area:
                area = w * h
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
                
        return area

        
