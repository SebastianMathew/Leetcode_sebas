class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        msf = 0
        c = 0
        for i in range(len(arr)):
            msf = max(msf, arr[i])

            if msf == i:
                c+=1

        return c

            
        