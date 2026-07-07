import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        n = 0
        for x, y in points:
            x2, y2 = x*x, y*y
            dis = x2 + y2
            heapq.heappush(heap, (-dis, [x,y]))
            n += 1
            if n > k: heapq.heappop(heap)
        res = [pair for _, pair in heap]
        return res