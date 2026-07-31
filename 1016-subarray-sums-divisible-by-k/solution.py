from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = 0
        count= 0
        rc = defaultdict(int)
        rc[0] = 1

        for num in nums:
            prefix +=num
            rem = prefix%k
            count+=rc[rem]
            rc[rem]+=1

        return count
