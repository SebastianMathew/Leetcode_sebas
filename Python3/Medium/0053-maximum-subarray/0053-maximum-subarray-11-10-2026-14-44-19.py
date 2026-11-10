class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        ps = 0
        minn = 0
        maxx = float("-inf")
        
        for num in nums:
            ps += num
            maxx = max(maxx, ps - minn) # Your diff logic on the fly
            minn = min(minn, ps)         # Update min prefix sum
            
        return maxx