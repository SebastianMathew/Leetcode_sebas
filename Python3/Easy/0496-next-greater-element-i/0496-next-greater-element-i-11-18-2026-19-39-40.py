class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next_greater = {}
        stack = []
        for num in nums2:
            while stack and num>stack[-1]:
                smaller = stack.pop()
                next_greater[smaller] = num
            stack.append(num)

        return [next_greater.get(x,-1) for x in nums1]