class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        cand = None
        count = 0

        for num in nums:
            if count == 0:
                cand = num

            count+=(1 if num == cand else -1)

        return cand