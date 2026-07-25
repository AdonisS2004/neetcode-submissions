class Solution:
    def numDecodings(self, s: str) -> int:
        def valid(s):
            if s[0] == '0':
                return False
            if int(s) > 26:
                return False
            return True

        n = len(s)
        memo = [0]*n
        memo[0] = 1 if valid(s[0]) else 0
        
        for i in range(1, n):
            if valid(s[i]):
                memo[i] = memo[i-1]
            if valid(s[i-1:i+1]):
                if i-2 >= 0:
                    memo[i] += memo[i-2]
                else:
                    memo[i] += 1
        return memo[-1]