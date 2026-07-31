from collections import defaultdict

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = 0
        rc = defaultdict(int)
        rc[0] = -1
        for i,num in enumerate(nums):
            prefix+=num
            modu = prefix%k
            if modu not in rc:
                rc[modu] = i
            else:
                if i-rc[modu] >1:
                    return True
        return False
