class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # helper: a function to find the seam of the list
        # upper bound binary search: O(log(n))
        def findSeam(nums) -> int:
            l,r = 0, len(nums)-1
            while l<r:
                m = l + (r - l) // 2
                if nums[m] < nums[r]:
                    r = m
                else:
                    l = m + 1
            return l
        
        # initialize l, r pointers
        l,r = 0, len(nums)-1
        if nums[l] >= nums[r]:
            seam = findSeam(nums)
            if target <= nums[r]:
                l = seam
            else:
                r = seam - 1
        
        # binary search for target
        while l<r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        # return
        if nums[l] == target:
            return l
        return -1


    
        
