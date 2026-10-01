class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        stack = []
        area = 0
        for i in range(n):
            while stack and height[i]>=height[stack[-1]]:
                idx = stack.pop()
                if stack:
                    h = min(height[i],height[stack[-1]]) - height[idx]
                    width = i - stack[-1]-1
                    area += h*width
            stack.append(i)

        return area