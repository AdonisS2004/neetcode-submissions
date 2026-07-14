class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        memo = [0]*n
        for i in range(n):
            # construct from center
            l,r = i,i
            while l >= 0 and r < n and s[l] == s[r]:
                memo[i] += 1
                l -= 1
                r += 1
            # construct from even
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                memo[i] += 1
                l -= 1
                r += 1
        return sum(memo)