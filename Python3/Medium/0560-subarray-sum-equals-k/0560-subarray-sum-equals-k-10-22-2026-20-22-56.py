from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        n = len(nums)

        ps = 0
        o = 0
        for i in range(n):
            ps+=nums[i]
            need = ps-k
            if need in seen:
                o+=seen[need]
            seen[ps]+=1

        
        return o