class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i, num in enumerate(nums):
            if num == val:
                nums[i] = None
            else:
                k += 1
        n = len(nums)
        l, r = 0, 1
        while r < n:
            if nums[l] == None:
                while r < n and nums[r] == None:
                    r += 1
                if r < n:
                    tmp = nums[l]
                    nums[l] = nums[r]
                    nums[r] = tmp
            l += 1
            r += 1
        return k
