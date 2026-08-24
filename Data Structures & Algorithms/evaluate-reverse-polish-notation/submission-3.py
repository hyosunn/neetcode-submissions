import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+": operator.add, "-": operator.sub,
                     "/": operator.truediv, "*": operator.mul}

        for t in tokens:
            if t not in "+-/*":
                stack.append(int(t))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                output = int(operators[t](num1, num2))
                stack.append(output)
        
        return stack.pop()