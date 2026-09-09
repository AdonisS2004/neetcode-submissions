class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        max_water = 0
        while l<r:
            water = min(heights[l], heights[r])*(r-l)
            max_water = max(water, max_water)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max_water