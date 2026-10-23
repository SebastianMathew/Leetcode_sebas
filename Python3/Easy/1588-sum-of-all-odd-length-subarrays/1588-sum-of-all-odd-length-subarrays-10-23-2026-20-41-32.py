class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        n = len(arr)
        re = 0
        for i in range(n):
            amo = (i+1)*(n-i)
            oc= (amo+1)//2
            re += oc*arr[i]

        return re