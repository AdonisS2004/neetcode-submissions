import math
class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0: return [0]
        if n == 1: return [0, 1]
        # setup
        memo = [0]*(n+1)
        memo[0] = 0
        memo[1] = 1
        # build memo
        offset = 2
        for i in range(2, n+1):
            if offset*2 == i:
                offset = i
            memo[i] = 1+memo[i-offset]
        return memo
        