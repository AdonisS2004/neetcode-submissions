class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        S - memo[i] is the max amount of money
        R - memo[i] = max(memo[i-1], nums[i] + memo[i-2])
        T - memo[i] is depenedent on nums[i] and memo[j] where
        j < i
        B - memo[0] = nums[0] memo[1] = nums[1]
        O - max(memo[0], memo[-1])
        T - O(n) space, O(n) Time
        """
        n = len(nums)
        if n <= 3: return max(nums)

        memo_first = [0]*(n-1)
        memo_last = [0]*(n-1)

        memo_first[0] = nums[0]
        memo_first[1] = max(nums[0], nums[1])
        memo_last[0] = nums[1]
        memo_last[1] = max(nums[1], nums[2])

        i = 2
        while i < n-1:
            memo_first[i] = max(memo_first[i-1], nums[i]+memo_first[i-2])
            memo_last[i] = max(memo_last[i-1], nums[i+1]+memo_last[i-2])
            i += 1

        print(memo_first)
        print(memo_last)
        return max(memo_first[-1], memo_last[-1])
        