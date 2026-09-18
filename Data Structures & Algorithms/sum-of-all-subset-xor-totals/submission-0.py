class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        def backtrack(i, total):
            nonlocal res
            if i >= len(nums):
                return
            # start new
            res += (total ^ nums[i])
            backtrack(i+1, total ^ nums[i])
            backtrack(i+1, total)

        for i, num in enumerate(nums):
            res += num
            backtrack(i+1, num)

        return res
        
            