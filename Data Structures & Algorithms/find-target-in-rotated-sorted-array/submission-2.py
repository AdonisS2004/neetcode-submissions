class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0,len(nums) - 1
        while l < r:
            k = (l + r)//2
            if nums[k] < nums[r]:
                r = k
            else:
                l = k + 1
        # l is the index of the minimum element
        l1, r1 = 0, l-1
        l2, r2 = l, len(nums) - 1
        while l1 < r1:
            k = (l1 + r1)//2
            if nums[k] == target: return k
            if target > nums[k]: l1 = k+1
            else: r1 = k-1
        if nums[l1] == target:
            return l1

        while l2 < r2:
            k = (l2 + r2)//2
            if nums[k] == target: return k
            if target > nums[k]: l2 = k+1
            else: r2 = k-1
        if nums[l2] == target:
            return l2
            
        return -1