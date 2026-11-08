class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        lp = 1
        r = [1]*len(nums)

        for i in range(len(nums)):
            r[i] *= lp
            lp*= nums[i]

        rp = 1

        for i in range(len(nums)-1,-1,-1):
            r[i]*= rp
            rp*= nums[i]

        return r
        