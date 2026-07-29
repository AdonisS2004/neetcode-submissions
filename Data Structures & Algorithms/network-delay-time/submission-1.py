import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        V, E = n+1, len(times)

        # build adjacency matrix
        adj = [[] for _ in range(V)]
        for u,v,w in times: adj[u].append((v,w))
        
        # distance array and priority queue
        dist = [sys.maxsize] * V
        pq = [] # stores (dist, node)
    
        # initialize pq
        dist[0] = 0
        dist[k] = 0
        heapq.heappush(pq, (0, k)) 

        # dijkstra's algorithm
        while pq:
            d, u = heapq.heappop(pq)

            if d > dist[u]:
                continue
            
            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
        
        res = max(dist)
        return res if res < sys.maxsize else -1
        
