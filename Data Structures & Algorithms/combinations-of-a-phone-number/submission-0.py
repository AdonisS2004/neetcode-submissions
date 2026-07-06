class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []
        keypad = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        n = len(digits)
        res = []
        def dfs(i, chars):
            if i >= n:
                res.append("".join(chars))
                return
            for char in keypad[digits[i]]:
                chars.append(char)
                dfs(i+1, chars)
                chars.pop()
            return
        dfs(0, [])
        return res