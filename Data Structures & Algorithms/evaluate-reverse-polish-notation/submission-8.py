import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                num2, num1 = stack.pop(), stack.pop()
                stack.append(num1 - num2)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                num2, num1 = stack.pop(), stack.pop()
                stack.append(int(num1 / num2))
            else:
                stack.append(int(t))
            
        return stack.pop()
        
        
        
        
        
        
        
        
        
        
        
        """ OPTIMAL SOLUTION (O(n) time and space)
        Other method is no hashmap, and just do if elif statements for corresponding 
        each operator string to the correct operator (Neetcode's method) 


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
        """