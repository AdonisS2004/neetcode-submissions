class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        memo = [1]*n
        memo[1] = 2
        idx = 2
        while idx < n:
            memo[idx] = memo[idx-1] + memo[idx-2]
            idx += 1
        return memo[n-1]