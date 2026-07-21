class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]*(n+1)
        for num in range(n+1):
            res[num] = num.bit_count()
        return res