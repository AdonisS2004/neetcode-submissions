class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        for i in range(n-2):
            a = nums[i]
            l, r = i + 1, n - 1
            while l < n and l < r:
                b, c = nums[l], nums[r]
                alrSum  = a + b + c
                if alrSum == 0:
                    res.append((a, b, c))
                    l += 1
                    continue
                if alrSum > 0:
                    r -= 1
                if alrSum < 0:
                    l += 1
        return [list(x) for x in set(res)]
