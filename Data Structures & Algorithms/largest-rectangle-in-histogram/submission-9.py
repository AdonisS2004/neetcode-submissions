class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Key Notes:
            - Monotonically increasing stack with heights
            - Stack contains (rect_height, index) pairs
            - Stack additions also extend backwards to adjust
              for true rectangle width (look at [7,1,7,2,2,4] example)
            - Max area checks when calculating areas
            - One final stack passthrough to re-check for max area, with
              starting index i starting at the end
        """
        stack = []
        max_area = 0
        for i, rect in enumerate(heights):
            start_idx = i
            while stack and stack[-1][0] > rect:
                width = abs(i-stack[-1][1])
                height = stack[-1][0]
                area = width*height
                max_area = max(area, max_area)
                start_idx = stack[-1][1]
                stack.pop()
            stack.append((rect, start_idx))
        
        i = len(heights)
        while stack:
            width = abs(i-stack[-1][1])
            height = stack[-1][0]
            area = width*height
            max_area = max(area, max_area)
            stack.pop()
        return max_area

            
