class Solution:
    def isHappy(self, n: int) -> bool:
        temp = n
        sum = 0
        a = set()
        if n==1:
            return True
        while True:

            while temp>0:
                digit = temp%10
                sum +=digit*digit
                temp = temp//10
            if sum == 1:
                return True
            if sum in a:
                return False
            a.add(sum)
            temp = sum
            sum = 0
