import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r , n = 1, max(piles), len(piles)
        kmin = r
        while l <= r:
            k = (l+r)//2
            # simulate eating bananas
            idx = 0
            hours = 0
            while idx < n:
                hours += math.ceil(piles[idx]/k)
                idx += 1
            if hours <= h:
                kmin = min(k, kmin)
                r = k-1
            else:
                l = k+1
        return kmin