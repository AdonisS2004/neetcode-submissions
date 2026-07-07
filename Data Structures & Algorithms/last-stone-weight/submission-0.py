import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        n = len(stones)
        
        # simulate
        while n > 1:
            # make s1 always the smaller
            s1, s2 = -heapq.heappop(heap), -heapq.heappop(heap)
            tmp = min(s1, s2)
            s2 = max(s1, s2)
            s1 = tmp
            if s1 == s2:
                n -= 2
                continue
            else:
                s2 -= s1
                heapq.heappush(heap, -s2)
                n -= 1
        return -heap[0] if n > 0 else 0