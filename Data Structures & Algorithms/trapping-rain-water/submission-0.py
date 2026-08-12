class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left = 0
        right = 1
        while right < len(height):
            if height[right] >= height[left]:
                bound_height = height[left]
                left += 1
                while left < right:
                    res += bound_height - height[left]
                    left += 1
            right += 1
        right = len(height) - 1
        left = right - 1
        while left >= 0:
            if height[left] > height[right]:
                bound_height = height[right]
                right -= 1
                while left < right:
                    res += bound_height - height[right]
                    right -= 1
            left -= 1

        return res
