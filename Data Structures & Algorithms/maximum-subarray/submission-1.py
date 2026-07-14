class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subSum = 0
        maxSub = nums[0]
        i, n = 0, len(nums)
        while i < n:
            if subSum + nums[i] > maxSub or subSum + nums[i] > 0:
                subSum += nums[i]
                maxSub = max(maxSub, subSum)
            else:
                subSum = 0
            i += 1
        return maxSub