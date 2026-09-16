import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Lower bound binary search --> k <= h (l<=target)
        Binary Space: [0, max(piles)]
        Eating Rate: sum[ceil(pile[i]/k) for i in n]
        """
        l,r = 1, max(piles)
        res = r
        while l<=r:
            k = l + ((r-l)//2)
            curr_h = 0
            for pile in piles:
                curr_h += math.ceil(float(pile)/k)
            if curr_h <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res



