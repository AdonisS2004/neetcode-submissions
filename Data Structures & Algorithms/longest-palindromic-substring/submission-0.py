class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res_l, res_r = 0, 0
        longest = 0

        for i in range(n):
            # construct odd
            l,r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if r-l+1 > longest:
                    res_l, res_r = l, r
                    longest = r-l+1
                l -= 1
                r += 1

            # construct even
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                if r-l+1 > longest:
                    res_l, res_r = l, r
                    longest = r-l+1
                l -= 1
                r += 1
        
        return s[res_l:res_r+1]
