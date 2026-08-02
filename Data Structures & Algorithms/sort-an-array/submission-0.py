class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(arr):
            if len(arr) == 0 or len(arr) == 1:
                return arr
            left = mergesort(arr[:len(arr)//2])
            right = mergesort(arr[len(arr)//2:])
            l = 0
            r = 0
            res = []
            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    res.append(left[l])
                    l += 1
                else:
                    res.append(right[r])
                    r += 1
            while l < len(left):
                res.append(left[l])
                l += 1
            while r < len(right):
                res.append(right[r])
                r += 1
            return res
        return mergesort(nums)