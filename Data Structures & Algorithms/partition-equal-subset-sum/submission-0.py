class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        Property: the number of times a number is used to make
        half should be equal for each number iff
        """
        n = len(nums)
        def recur(i, curSum, target):
            if i >= n: 
                return False
            if curSum > target:
                return False
            if curSum == target:
                return True
            return recur(i+1, curSum+nums[i], target) or recur(i+1, curSum, target)

        # base checks
        total = sum(nums)
        max_num = max(nums)
        if total % 2 > 0: return False
        half = total//2
        if max_num > half: return False

        return recur(0, 0, half)
