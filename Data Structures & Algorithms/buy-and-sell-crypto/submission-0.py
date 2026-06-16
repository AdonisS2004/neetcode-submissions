class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,0
        n = len(prices)
        max_profit = 0 
        while r < n:
            while prices[l] > prices[r]:
                l += 1
            max_profit = max(prices[r] - prices[l], max_profit)
            r += 1
        return max_profit