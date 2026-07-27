from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Valid Tree:
        - undirected, connected, acyclic
        """
        # edge case check
        if edges == []:
            return n == 1
        
        # quick check for cycles and full connectedness
        if len(edges) > n-1 or len(edges) < n-1:
            return False

        # build graph
        G = dict()
        for u,v in edges:
            if u not in G: G[u] = []
            if v not in G: G[v] = []
            G[u].append(v)
            G[v].append(u)

        # bfs check for connectviity
        queue = deque([(None, edges[0][0])]) # (parent, node)
        visited = {edges[0][0]}
        count = 0
        while queue:
            parent, u = queue.popleft()
            count += 1
            for v in G[u]:
                if v not in visited and v != parent:
                    queue.append((u, v))
                    visited.add(v)
        return count == n
                

