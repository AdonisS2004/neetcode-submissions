class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, combination, csum):
            if csum == target:
                res.append(combination[::])
                return
            if csum > target or i >= len(nums):
                return
            combination.append(nums[i])
            backtrack(i, combination, csum + nums[i])
            combination.pop()
            backtrack(i+1, combination, csum)
            return
        backtrack(0, [], 0)
        return res