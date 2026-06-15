class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n - 1
        while l < n and l < r:
            lrsum = numbers[l] + numbers[r]
            if lrsum == target:
                return [l+1, r+1]
            if lrsum > target:
                r -= 1
                continue
            if lrsum < target:
                l += 1
        return []
