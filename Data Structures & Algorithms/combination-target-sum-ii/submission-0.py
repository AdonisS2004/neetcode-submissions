class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        n = len(candidates)
        def dfs(i, csum, c):
            if csum == target:
                res.append(c[::])
                return
            if i >= n or csum > target:
                return
            # choose to use candidates[i]
            c.append(candidates[i])
            dfs(i+1, csum+candidates[i], c)
            c.pop()
            # chose not to use candidates[i] (make sure the duplicates are handled)
            while (i+1 < n and candidates[i+1] == candidates[i]): 
                i += 1
            dfs(i+1, csum, c)
            return
        dfs(0, 0, [])
        return res