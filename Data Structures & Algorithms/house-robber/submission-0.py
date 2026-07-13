class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        memo = [0]*n
        memo[0] = nums[0]
        idx = 1
        while idx < n:
            memo[idx] = max(nums[idx] + memo[idx-2], memo[idx-1])
            idx += 1
        return memo[-1]