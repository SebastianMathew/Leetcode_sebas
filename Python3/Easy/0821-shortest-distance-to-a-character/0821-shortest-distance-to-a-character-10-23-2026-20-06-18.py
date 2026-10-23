class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n = len(s)
        answer = [0]*n

        j = float('inf')
        for i in range(n):
            if not s[i] == c:
                j+=1
                answer[i] = j
            else:
                j = 0
                answer[i] = j


        j = float('inf')
        for i in range(n-1,-1,-1):
            if not s[i] == c:
                j+=1
                answer[i] = min(answer[i], j)
            else:
                j = 0
                answer[i] = min(answer[i], j)

        return answer




        