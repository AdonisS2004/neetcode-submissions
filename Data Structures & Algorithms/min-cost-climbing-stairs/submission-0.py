class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [0] * n
        memo[0] = cost[0]
        memo[1] = cost[1]
        idx = 2
        while idx < n:
            memo[idx] = cost[idx] + min(memo[idx-1], memo[idx-2])
            idx += 1
        print(memo)
        return min(memo[n-1], memo[n-2])