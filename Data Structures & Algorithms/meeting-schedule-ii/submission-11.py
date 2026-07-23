"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0
        starts = [i.start for i in intervals]
        ends = [i.end for i in intervals]
        starts.sort()
        ends.sort()
        n,s,e = len(intervals), 0, 0
        max_rooms = 0
        rooms = 0
        while s < n:
            while s < n and ends[e] > starts[s]:
                rooms += 1
                s += 1
                max_rooms = max(max_rooms, rooms)
            while s < n and ends[e] <= starts[s]:
                e += 1
                rooms -= 1
                max_rooms = max(max_rooms, rooms)
        return max_rooms
            
