class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        idx, n = 0, len(intervals)
        res = []
        start, end = intervals[idx]
        while idx < n:
            start_i, end_i = intervals[idx]
            if end > end_i:
                idx += 1
            elif end < start_i:
                res.append([start, end])
                start, end  = start_i, end_i
                idx += 1
            else:
                end = end_i
                idx += 1
        res.append([start, end])
        return res
