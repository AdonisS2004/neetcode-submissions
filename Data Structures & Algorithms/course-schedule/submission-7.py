class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs cycle detection
        def hasCycles(u, graph, stack):
            if u in stack:
                return True
            stack.add(u)
            for v in graph[u]:
                if hasCycles(v, graph, stack):
                    return True
            stack.remove(u)
            return False
        
        # build graph
        graph = dict()
        for u,v in prerequisites:
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[v].append(u)
        
        # cycle detection
        reached = set()
        for u in graph:
            if hasCycles(u, graph, reached):
                return False
        
        return True