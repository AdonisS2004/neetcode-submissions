class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        res = []
        n = len(nums)
        nums.sort()
        def backtrack(subset, i):
            if tuple(subset) not in visited:
                res.append(subset[::])
                visited.add(tuple(subset))
            if i >= n: return
            # pick i
            subset.append(nums[i])
            backtrack(subset, i+1)
            subset.pop()
            # don't pick i
            while i+1 < n and nums[i] == nums[i+1]:
                i += 1
            backtrack(subset, i+1)
            return
        backtrack([], 0)
        return res