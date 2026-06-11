class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        n = len(nums)
        nums.sort()
        print(nums)
        for i in range(n):
            print(nums[i])
            l, r = i + 1, n - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    if (nums[i], nums[l], nums[r]) not in seen:
                        res.append([nums[i], nums[l], nums[r]])
                        seen.add((nums[i], nums[l], nums[r]))
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
        return res