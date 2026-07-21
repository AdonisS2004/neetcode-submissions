class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, power):
            if power == 0: return 1
            if power == 1: return x
            # odd case
            odd = 1
            if power % 2 > 0: odd = x
            return helper(x, power//2)**2*odd
        res = helper(x, abs(n))
        if n < 0: 
            return 1/res
        return res
            