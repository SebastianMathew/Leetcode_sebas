class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        n = len(arr)
        summ = 0
        for i in range(n):
            nc = (i+1)*(n-i)
            odd = (nc+1)//2
            summ += arr[i] *odd

        return summ