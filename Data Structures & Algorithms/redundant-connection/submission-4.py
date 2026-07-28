class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]

        def find(x):
            if parent[x] != x:
                return find(parent[x])
            return x
        
        def union(x, y):
            parent[find(y)] = find(x)
        
        for u, v in edges:
            if find(u) == find(v):
                return [u, v]
            union(u, v)
        