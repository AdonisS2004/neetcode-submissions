class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n - 1
        while l < n and l < r:
            nl, nr = numbers[l], numbers[r]
            if nl + nr == target:
                return [l+1, r+1]
            if nl + nr > target:
                r -= 1
                continue
            if nl + nr < target:
                l += 1
        return []
