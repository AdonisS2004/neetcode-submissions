class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = set(coins)
        memo = [-1]*(amount+1)
        memo[0] = 0
        for coin in coins:
            if coin <= amount:
                memo[coin] = 1
        for i in range(amount+1):
            if i in coins: continue
            possibilities = []
            for coin in coins:
                if i - coin >= 0 and memo[i-coin] != -1:
                    possibilities.append(memo[i-coin] + 1)
            if possibilities:
                memo[i] = min(possibilities)
        return memo[amount]