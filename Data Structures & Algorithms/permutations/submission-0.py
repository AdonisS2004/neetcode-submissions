class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def backtrack(p, visited, k):
            if k == n: 
                res.append(p[::])
                return
            for num in nums:
                if num not in visited:
                    visited.add(num)
                    p.append(num)
                    backtrack(p, visited, k+1)
                    p.pop()
                    visited.remove(num)
            return
        backtrack([], set(), 0)
        return res