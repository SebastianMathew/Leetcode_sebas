from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        a = Counter(arr1)
        o = []
        for num in arr2:
            i = a[num]
            for _ in range(i):
                o.append(num)
                a[num]-=1

        e = [ex for ex, freq in a.items() if freq >0]
        e.sort()
        for num in e:
            i = a[num]
            for _ in range(i):
                o.append(num)
                a[num]-=1

        return o
        
