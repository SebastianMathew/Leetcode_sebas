class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ng = {}

        stack = []

        for num in nums2:
            while stack and num>stack[-1]:
                smaller = stack.pop()
                ng[smaller] = num
            stack.append(num)

        return [ng.get(x,-1) for x in nums1]