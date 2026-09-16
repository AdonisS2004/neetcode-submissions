class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            l,r = i+1,n-1
            while l<r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l+1] == nums[l]:
                        l += 1
                    l+=1
                elif threeSum < 0:
                    while l<r and nums[l+1] == nums[l]:
                        l += 1
                    l+=1
                else:
                    while l<r and nums[r-1] == nums[r]:
                        r-=1
                    r-=1
        return res