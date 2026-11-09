class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        n = len(arr)
        summ = 0
        for i in range(n):
            cn = (((i+1)*(n-i))+1)//2
            mn = cn*arr[i]
            summ+=mn

        return summ