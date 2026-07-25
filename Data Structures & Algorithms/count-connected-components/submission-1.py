class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(u, graph, visited):
            if u in visited:
                return
            visited.add(u)
            for v in graph[u]:
                dfs(v, graph, visited)
        
        graph = dict()
        for u,v in edges:
            if u not in graph: graph[u] = []
            if v not in graph: graph[v] = []
            graph[u].append(v)
            graph[v].append(u)
        
        count = 0 + (n-len(graph))
        visited = set()
        for u in graph:
            if u not in visited:
                count += 1
                dfs(u, graph, visited)
        return count 
                