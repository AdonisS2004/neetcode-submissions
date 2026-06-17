class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r,mid = 0,n,n//2
        while mid < n and l <= r:
            curr = nums[mid]
            if curr == target:
                return mid
            if curr < target:
                l = mid + 1
            else:
                r = mid - 1
            mid = (l + r)//2
        return -1