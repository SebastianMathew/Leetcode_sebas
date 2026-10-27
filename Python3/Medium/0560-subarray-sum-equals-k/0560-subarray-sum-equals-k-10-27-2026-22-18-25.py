from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        ps = 0
        n = len(nums)
        o = 0
        for i in range(n):
            ps+=nums[i]
            need = ps-k
            if need in count:
                o+=count[need]
            count[ps]+=1

        return o
