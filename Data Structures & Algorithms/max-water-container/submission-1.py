class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        n = len(heights)
        l, r = 0, n-1

        while l < n and l < r:
            hl, hr = heights[l], heights[r]
            width = r - l
            height = min(hl, hr)
            max_water = max(width*height, max_water)
            if hl < hr:
                l += 1
            else:
                r -= 1

        return max_water