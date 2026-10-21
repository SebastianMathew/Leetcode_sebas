class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mpsf = prices[0]

        n = len(prices)
        if n <2:
            return 0
        mprof = 0
        for i in range(1,n):
            mpsf = min(mpsf,prices[i])
            prof = prices[i] - mpsf
            mprof = max(mprof,prof)

        return mprof