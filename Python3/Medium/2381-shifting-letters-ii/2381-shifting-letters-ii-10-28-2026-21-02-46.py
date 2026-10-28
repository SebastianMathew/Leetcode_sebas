class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        sa = [0]*(n+1)

        for start,end,direction in shifts:
            val = 1 if direction == 1 else -1
            sa[start]+=val
            sa[end+1]-=val

        res = []
        ps = 0
        for i,c in enumerate(s):
            ps+=sa[i]
            ci = ord(c)-ord('a')
            ni = (ci+ps)%26
            res.append(chr(ni+ord('a')))

        return "".join(res)

            


        