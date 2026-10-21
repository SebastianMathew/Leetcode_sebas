class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1]* len(nums)

        lp = 1
        for i in range(n):
            res[i]*=lp
            lp*=nums[i]

        rp = 1
        for i in range(n-1,-1,-1):
            res[i]*=rp
            rp*=nums[i]

        return res