class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, power):
            if power == 0:
                return 1
            if power == 1:
                return x
            # odd case
            if power % 2 > 0:
                return helper(x, power//2)**2*x
            else:
                return helper(x, power//2)**2
        res = helper(x, abs(n))
        if n < 0:
            return 1/res
        return res
            