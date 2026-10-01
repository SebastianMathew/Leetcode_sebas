class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        arr.append(0)
        n = len(arr)
        stack = []
        summ = 0
        MOD = 10**9 + 7

        for i in range(n):
            while stack and arr[i]< arr[stack[-1]]:
                idx = stack.pop()
                L = idx+1 if not stack else idx - stack[-1]
                R = i - idx
                nS = L*R
                summ = (summ + nS * arr[idx]) % MOD
            stack.append(i)

        return summ