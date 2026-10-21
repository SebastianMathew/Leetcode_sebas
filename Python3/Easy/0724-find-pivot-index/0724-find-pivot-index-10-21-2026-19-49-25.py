class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        ls = [0]*len(nums)
        rs = [-1001]*len(nums)

        le = 0
        for i in range(len(nums)):
            ls[i] = le
            le+=nums[i]

        re = 0
        for i in range(len(nums)-1,-1,-1):
            rs[i] = re
            re+=nums[i]
        

        for i in range(len(nums)):
            if rs[i]==ls[i]:
                return i
        return -1