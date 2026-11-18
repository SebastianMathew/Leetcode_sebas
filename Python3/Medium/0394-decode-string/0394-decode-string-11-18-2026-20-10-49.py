class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num = 0
        currst = ""
        for c in s:
            if c.isdigit():
                curr_num = curr_num*10+int(c)
            elif c == '[':
                stack.append((currst,curr_num))
                currst = ""
                curr_num = 0
            elif c == ']':
                prevst,num = stack.pop()
                currst = prevst+currst*num
            else:
                currst += c
        return currst
