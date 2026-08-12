class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []

        leftB = [-1] * n
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftB[i] = stack[-1]
            stack.append(i)
        
        stack = []
        rightB = [n] * n
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightB[i] = stack[-1]
            stack.append(i)

        maxArea = 0
        for i in range(n):
            area = heights[i] * (rightB[i] - leftB[i] - 1)
            maxArea = max(maxArea, area)
        
        return maxArea