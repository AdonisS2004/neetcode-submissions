class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        starts = []
        visited = set()
        for num in nums:
            if num in visited:
                continue
            visited.add(num)

            if num-1 not in num_set:
                curr = num
                size = 1
                while curr + 1 in num_set:
                    visited.add(curr+1)
                    curr += 1
                    size += 1
                if size > res:
                    res = size
        return res