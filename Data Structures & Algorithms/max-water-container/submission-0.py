class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        n = len(heights)
        l, r = 0, n-1
        # length = r - l
        # height = min(heights[l], heights[r])
        while l < r:
            area = max(area, ((r-l)*min(heights[l], heights[r])))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return area