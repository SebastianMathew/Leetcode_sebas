class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(int(token))
            else:
                o2 = stack.pop()
                o1 = stack.pop()

                match token:
                    case '+':
                        stack.append(o1 + o2)
                    case '-':
                        stack.append(o1 - o2)
                    case '*':
                        stack.append(o1 * o2)
                    case '/':
                        # Use int(o1 / o2) to truncate toward zero for negative division
                        stack.append(int(o1 / o2))

        return stack[0]