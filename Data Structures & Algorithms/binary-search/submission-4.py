class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        mid = (l + r)//2
        while l <= r and mid < len(nums):
            curr = nums[mid]
            if curr == target:
                return mid
            if curr > target:
                r = mid - 1
                mid = (l + r)//2 
            if curr < target:
                l = mid + 1
                mid = (l + r)//2
        return -1