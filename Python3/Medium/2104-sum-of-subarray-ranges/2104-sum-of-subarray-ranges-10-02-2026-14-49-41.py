class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:

        minn = min(nums)
        nl = nums+ [minn-1]

        n = len(nl)
        stack = []
        summ = 0
        for i in range(n):
                while stack and nl[i]<=nl[stack[-1]]:
                    idx = stack.pop()
                    l = idx+1 if not stack else idx - stack[-1]
                    r = i - idx
                    summ = summ+(l*r*nl[idx])
                    
                stack.append(i)


        print(summ)

        summax = summ
        summ = 0
        stack = []

        maxx = max(nums)
        nm = nums + [maxx+1]
        print(nm)

        for i in range(n):
                while stack and nm[i]>=nm[stack[-1]]:
                    idx = stack.pop()
                    l = idx+1 if not stack else idx - stack[-1]
                    r = i - idx
                    summ = summ+(l*r*nm[idx])
                    
                stack.append(i)

        summin = summ
        print(summin)
        return summin - summax
