from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = Counter(nums)

        b = [[] for _ in range(len(nums)+1)]

        for num, freq in a.items():
            b[freq].append(num)

        o = []
        for i in range(len(nums), -1, -1):
            for num in b[i]:
                o.append(num)
                if len(o)==k:
                    return o
