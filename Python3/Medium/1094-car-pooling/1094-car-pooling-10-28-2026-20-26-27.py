class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        max_loc = max(x[2] for x in trips)
        der = [0]*(max_loc+2)

        for num, st,end in trips:
            der[st]+=num
            der[end]-=num

        p = 0
        for c in der:
            p+=c
            if p>capacity:
                return False

        return True