class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        if r==0:
            return nums[0]
        if nums[l] < nums[r]:
            return nums[l]
        while l < r:
            mid = (l+r)//2
            print(f"{l=}, {r=}, {mid=}, {nums[mid]=}")
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            # right half
            if nums[mid] > nums[l]:
                l = mid + 1
            # left half
            else:
                r = mid - 1
        print("base return")
        return min(nums[l], nums[r])