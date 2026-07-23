class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        stack = []
        stars = []
        len_stack = 0
        len_stars = 0
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
                        len_stars -= 1
                else:
                    stack.pop()
                    len_stack -= 1
            elif s[i] == '*':
                stars.append((s[i], i))
                len_stars += 1
            else:
                stack.append((s[i], i))
                len_stack += 1
            i += 1

        if len_stars < len_stack:
            return False

        while stack:
            if stars[-1][-1] < stack[-1][-1]:
                return False
            stars.pop()
            stack.pop()

        return True
            