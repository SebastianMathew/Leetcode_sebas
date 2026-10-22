from collections import defaultdict

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        seen[0] = -1
        ps = 0
        maxo = 0
        for i in range(len(nums)):
            ps = ps +1 if nums[i] == 1 else ps - 1
            if ps not in seen:
                seen[ps] = i
            else:
                maxo = max(maxo, i-seen[ps])

        return maxo