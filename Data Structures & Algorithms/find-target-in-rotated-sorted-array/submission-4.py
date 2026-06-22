class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # helper function
        def findSeam(nums: List[int]) -> int:
            n = len(nums)
            l,r = 0, n-1
            # base case: 1 element
            if n == 1:
                return 0
            # base case: regular sorted list
            if nums[l] < nums[r]:
                return l
            
            # fallback: find the seem
            while l < r:
                mid = (l+r)//2
                if nums[mid] > nums[mid+1]: return mid + 1
                if nums[mid] < nums[mid-1]: return mid
                if nums[mid] > nums[l]: l = mid + 1 # mid is in right half
                else: r = mid - 1                   # mid is inleft half
            # return seem
            return l

        n = len(nums)
        l, r = 0, n-1
        if nums[l] > nums[r]:
            seam = findSeam(nums)
            if target >= nums[l]: r = seam
            else: l = seam
        
        print(f"{l=}, {r=}")
        while l < r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        if nums[l] == target:
            return l
        return -1

    
        
