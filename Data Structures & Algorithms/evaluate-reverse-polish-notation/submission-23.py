class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {'+', '-', '*', '/'}
        for token in tokens:
            if token in operations:
                op1 = stack.pop()
                op2 = stack.pop()
                if token == "+": 
                    stack.append(int(op2 + op1))
                    continue
                if token == "-": 
                    stack.append(int(op2 - op1))
                    continue
                if token == "*": 
                    stack.append(int(op2 * op1))
                    continue
                if token == "/":
                    stack.append(int(op2 / op1))
                    continue
            else:
                stack.append(int(token))
        return stack[-1]