from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        n = len(s)
        t = max(freq.values())
        if t > n//2 + 1:
            return ""
        
        res = []
        pq = []
        for key, val in freq.items():
            heapq.heappush_max(pq, (val, key))
        while pq:
            if len(pq) == 1:
                freq, c = heapq.heappop_max(pq)
                if c == res[-1]:
                    return ""
                res.append(c)
                freq -= 1
                if freq != 0:
                    heapq.heappush_max(pq, (freq, c))
            else:
                freqA, cA = heapq.heappop_max(pq)
                freqB, cB = heapq.heappop_max(pq)
                if not res or (res and res[-1] != cA):
                    res.append(cA)
                    res.append(cB)
                else:
                    res.append(cB)
                    res.append(cA)
                freqA -= 1
                freqB -= 1
                if freqA != 0:
                    heapq.heappush_max(pq, (freqA, cA))
                if freqB != 0:
                    heapq.heappush_max(pq, (freqB, cB))
        return "".join(res)