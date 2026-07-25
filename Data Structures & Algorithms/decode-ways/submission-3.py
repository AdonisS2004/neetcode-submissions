class Solution:
    def numDecodings(self, s: str) -> int:
        """
        S - memo[i] = numbers of ways to decode s[:i+1]
        R - memo[i] = memo[i-1] + (memo[i-2] if i-2 >= 0 else 1) {valid checks needed}
        T - i is depenedent on i-1, so we can build the table in increasing i
        B - memo[0] = 1 if s[0] != 0 else 0
        O - memo[-1]
        T - O(n) time, O(n) space
        """
        # valid check
        def valid(s):
            if s[0] == '0':
                return False
            if int(s) > 26:
                return False
            return True

        # default variables
        n = len(s)
        memo = [0]*n
        memo[0] = 1 if valid(s[0]) else 0
        
        # build memo
        for i in range(1, n):
            if valid(s[i]):
                memo[i] = memo[i-1]
            if valid(s[i-1:i+1]):
                if i-2 >= 0:
                    memo[i] += memo[i-2]
                else:
                    memo[i] += 1
        return memo[-1]