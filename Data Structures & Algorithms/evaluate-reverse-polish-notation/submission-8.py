class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def evalHelper(n1, n2, op):
            if op == "+":
                return n1 + n2
            if op == "-":
                return n1 - n2
            if op == "*":
                return n1 * n2
            if op == "/":
                return int(float(n1) / n2)
        stack = []
        ops = {"+", "-", "*", "/"}
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(evalHelper(n1, n2, token))
        return stack[0]