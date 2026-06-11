class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(', '{', '['}
        matches = {
            ')':'(', 
            '}':'{',
            ']':'['
        }
        for c in s:
            if c in brackets: 
                stack.append(c)
            else:
                if not stack or stack[-1] != matches[c]:
                    return False
                stack.pop()
        return True if not stack else False
