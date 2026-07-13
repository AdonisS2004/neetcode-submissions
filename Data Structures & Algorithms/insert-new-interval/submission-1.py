class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        # variables
        idx = 0
        n = len(intervals)
        start, end = newInterval[0], newInterval[1]
        res = []

        # fast case
        if start > intervals[-1][-1]:
            intervals.append(newInterval)
            return intervals
        


        # check for start 
        while intervals[idx][-1] < start:
            res.append(intervals[idx])
            idx += 1
        start = min(intervals[idx][0], start)
        
        # check for end
        while idx < n and end > intervals[idx][-1]:
            idx += 1
        if idx >= n:
            res.append([start, end])
            return res
        
        if end < intervals[idx][0]:
            res.append([start, end])
        else:
            end = max(intervals[idx][-1], end)
            res.append([start, end])
            idx += 1

        while idx < n:
            res.append(intervals[idx])
            idx += 1

        return res
