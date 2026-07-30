from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mc = Counter(magazine)

        for c in ransomNote:
            if mc[c]==0:  
                return False
            mc[c]-=1
        return True      
