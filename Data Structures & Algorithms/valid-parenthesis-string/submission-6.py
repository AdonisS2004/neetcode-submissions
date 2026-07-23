class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        stack = []
        stars = []
        i = 0
        while i < n:
            if s[i] == ')':
                if not stack and not stars:
                    return False
                if not stack:
                    if not stars:
                        return False
                    else:
                        stars.pop()
                else:
                    stack.pop()
            elif s[i] == '*':
                stars.append((s[i], i))
            else:
                stack.append((s[i], i))
            i += 1

        if len(stars) < len(stack):
            return False

        while stack:
            if stars[-1][-1] < stack[-1][-1]:
                return False
            stars.pop()
            stack.pop()

        return True
            