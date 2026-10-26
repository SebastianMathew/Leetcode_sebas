class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        ps = [0]*len(nums)
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            ps[i] = summ

        for i in range(len(nums)):
            if ps[i]-nums[i]==summ-ps[i]:
                return i

        return -1
        
