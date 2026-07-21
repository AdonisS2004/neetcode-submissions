class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, power):
            if power == 0: return 1
            if power == 1: return x
            # odd case
            odd = 1
            if power % 2 > 0: odd = x
            return helper(x, power//2)**2*odd
        
        if n < 0: 
            x = 1/x
            n *= -1
        return helper(x, n)
            