class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(comb, i, k):
            if len(comb) == k:
                res.append(comb[::])
                return
            if i > n:
                return
            comb.append(i)
            backtrack(comb, i+1, k)
            comb.pop()
            backtrack(comb, i+1, k)

        backtrack([],1,k)

        return res