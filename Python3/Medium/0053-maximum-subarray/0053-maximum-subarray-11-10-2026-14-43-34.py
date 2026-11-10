class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        psa = [0]* n
        ps = 0
        diff = [0]*n
        minn = 0
        maxx = float("-inf")
        msum = 0
        for i in range(n):
            ps+=nums[i]
            psa[i] = ps
            
            diff[i] = ps-minn
            minn = min(minn, ps)
            maxx = max(maxx,diff[i])
            
            

        return maxx

        