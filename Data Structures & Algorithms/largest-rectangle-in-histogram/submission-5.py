class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, rect in enumerate(heights):
            pop_count = 0
            start_idx = i
            while stack and stack[-1][0] > rect:
                width = abs(i-stack[-1][1])
                height = stack[-1][0]
                #print(f"for ({rect=},{i=}): {width=}, {height=}")
                area = width*height
                max_area = max(area, max_area)
                pop_count += i-stack[-1][1]
                start_idx = stack[-1][1]
                stack.pop()
            stack.append((rect, start_idx))
            #print(f"stack state:{stack}")
        
        i = len(heights)
        while stack:
            width = abs(i-stack[-1][1])
            height = stack[-1][0]
            #print(f"for {i=}: {width=}, {height=}")
            area = width*height
            max_area = max(area, max_area)
            stack.pop()
        return max_area

            
