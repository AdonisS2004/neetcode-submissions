class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        for num in nums:
            if num-1 not in num_set:
                curr = num
                size = 1
                while curr + 1 in num_set:
                    curr += 1
                    size += 1
                if size > res:
                    res = size
        return res