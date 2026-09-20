class Solution:
    def tribonacci(self, n: int) -> int:
        memo = [0]*(max(n,3)+1)
        memo[0] = 0
        memo[1] = 1
        memo[2] = 1
        if n < 3:
            return memo[n]
        else:
            for i in range(3, n+1):
                memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
        return memo[n]
        