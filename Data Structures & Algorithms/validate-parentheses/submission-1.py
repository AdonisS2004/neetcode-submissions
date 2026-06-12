import collections
class Solution:
    def isValid(self, s: str) -> bool:
        open_par = {'(', '[', '{'}
        close2open = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        n = 0
        for par in s:
            if par in open_par:
                stack.append(par)
                n += 1
                continue
            if n == 0 or close2open[par] != stack[-1]:
                return False
            stack.pop()
            n -= 1
        if n > 0:
            return False
        return True