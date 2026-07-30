from collections import Counter

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        nf = Counter(nums)
        
        first = {}
        last = {}

        for i in range(len(nums)):
            if nums[i] not in first:
                first[nums[i]] = i
            last[nums[i]] = i

        degree = max(nf.values())
        n = len(nums)
        for i in nums:
            if nf[i]==degree:
                n = min(n,last[i]-first[i]+1)
        return n




