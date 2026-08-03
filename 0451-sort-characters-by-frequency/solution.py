from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        a = Counter(s)
        print(a)

        b = [[] for _ in range(len(s)+1)]

        for num, freq in a.items():
            b[freq].append(num)
        
        o = []
        for i in range(len(s),0,-1):
            for c in b[i]:
                for _ in range(i):
                    o.append(c)
        return "".join(o)

