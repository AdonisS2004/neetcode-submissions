class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0]*n
        suffix = [0]*n
        res = [0]*n

        # construct prefix
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1]*nums[i]
        # construct suffix
        suffix[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]
        # construct result
        res[0] = suffix[1]
        res[-1] = prefix[-2]
        for i in range(1,n-1):
            res[i] = prefix[i-1] * suffix[i+1]
        return res