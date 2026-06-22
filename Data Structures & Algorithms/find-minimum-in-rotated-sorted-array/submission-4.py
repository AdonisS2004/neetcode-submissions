class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0, n-1
        # base case: 1 element
        if n == 1:
            return nums[0]
        # base case: regular sorted list
        if nums[l] < nums[r]:
            return nums[l]
        
        # fallback: find the seem
        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[mid+1]: return nums[mid+1]
            if nums[mid] < nums[mid-1]: return nums[mid]
            if nums[mid] > nums[l]: l = mid + 1 # mid is in right half
            else: r = mid - 1                   # mid is inleft half

        return min(nums[l], nums[r])