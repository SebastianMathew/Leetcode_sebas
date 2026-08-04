from collections import defaultdict

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        dd = defaultdict(int)
        for rows in wall:
            pref = []
            pr = 0

            for num in rows:
                pr +=num
                pref.append(pr)
                dd[pr]+=1
        
        lar = max(dd)
        o = [freq for x,freq in dd.items() if x !=lar]
        a = max(o,default = 0)
        return len(wall) -a
