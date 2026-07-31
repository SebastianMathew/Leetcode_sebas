class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        o = [0]*len(word)
        num = 0
        i = 0
        for c in word:
            digit = int(c)
            num = ((num*10)+digit)%m
            if num==0:
                o[i] +=1
            i+=1

        return o
