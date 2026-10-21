class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        max_left = []
        max_right = [0]*n

        ml = 0
        for i in range(n):
            max_left.append(ml)
            ml = max(ml,height[i])

        mr = 0
        for i in range(n-1,-1,-1):
            max_right[i] = mr
            mr = max(mr,height[i])

        water = 0
        for i in range(n):
            stow = min(max_left[i],max_right[i])-height[i]
            water+=stow if stow>0 else 0

        return water