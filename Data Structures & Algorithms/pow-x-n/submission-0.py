class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        for _ in range(abs(n)):
            if n < 0: res /= x
            else: res *= x
        return res