class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        print(intervals)
        idx, n = 0, len(intervals)
        remove = 0
        while idx < n:
            s, e = intervals[idx]
            idx += 1
            while idx < n and e > intervals[idx][0]:
                remove += 1
                idx += 1
        return remove