class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums:
            nums[abs(i)-1] = -abs(nums[abs(i)-1])

        print(nums)
        o = []
        for i in range(len(nums)):
            if nums[i]>0:
                o.append(i+1)
        return o
