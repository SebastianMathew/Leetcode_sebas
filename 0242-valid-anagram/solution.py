from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False
        a = Counter(s)

        for c in t:
            if c not in a:
                return False
            a[c]-=1
            if a[c]<0:
                return False
        return True
