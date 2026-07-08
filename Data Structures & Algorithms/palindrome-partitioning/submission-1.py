class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # palidrom checker
        res = []
        n = len(s)

        def isPalindrome(s):
            l, r = 0, len(s)-1
            if s == "": return False
            while l < r:
                if s[l] != s[r]: return False
                l += 1
                r -= 1
            return True

        def buildSub(sub, start, i):
            if start >= n:
                res.append(sub[::])
                return
            while i < n:
                substring = s[start:i+1]
                if isPalindrome(substring):
                    sub.append(substring)
                    buildSub(sub, i+1, i+1)
                    sub.pop()
                i += 1
            return

        # make result
        buildSub([], 0, 0)
        return res