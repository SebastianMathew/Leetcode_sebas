class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        ps = 0
        for i, num in enumerate(nums):
            if ps == total_sum - ps-num:
                return i

            ps+=num

        return -1