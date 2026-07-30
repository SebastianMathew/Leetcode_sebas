from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a  = Counter(nums1)
        o = []
        for i in nums2:
            if a[i] == 0:
                continue
            else:
                a[i]-=1
                o.append(i)
            
        return o
