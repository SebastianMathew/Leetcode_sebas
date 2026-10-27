from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        o = 0
        count = defaultdict(int)
        count[0] = 1
        ps = 0
        n = len(nums)
        for i in range(n):
            ps+=nums[i]
            need = ps-goal
            if need in count:
                o+=count[need]
            count[ps]+=1
        return o