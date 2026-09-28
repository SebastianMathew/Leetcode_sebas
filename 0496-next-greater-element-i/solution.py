from collections import defaultdict

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = defaultdict(lambda : -1)

        stack = []
        for num in nums2:
            while stack and num>stack[-1]:
                el = stack.pop()
                result[el] = num
            stack.append(num)

        return [result[i] for i in nums1]
