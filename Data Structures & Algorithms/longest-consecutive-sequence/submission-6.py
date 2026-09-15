class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(list(set(nums)))
        res = 0
        curr = 0
        prev = nums[0]
        for num in nums:
            if num - 1 == prev:
                curr += 1
            else:
                curr = 1
            prev = num
            res = max(res, curr)
        return res
