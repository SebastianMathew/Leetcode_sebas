class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        rule = {'(': ')', '{': '}', '[': ']'}
        
        for c in s:
            if c in rule:
                stack.append(c)
            elif stack and rule[stack[-1]] == c:
                stack.pop()
            else:
                return False
                
        return not stack