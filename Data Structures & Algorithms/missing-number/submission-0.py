class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        out = 0
        for i in range(n+1):
            out ^= i
        for num in nums:
            out ^= num
        return out