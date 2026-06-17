class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r,mid = 0,len(nums),len(nums)//2
        while l < r:
            curr = nums[mid]
            if curr == target:
                return mid
            if curr < target:
                l = mid + 1
            else:
                r = mid - 1
            mid = (l + r)//2
        if mid < len(nums) and nums[mid] == target:
            return mid
        return -1