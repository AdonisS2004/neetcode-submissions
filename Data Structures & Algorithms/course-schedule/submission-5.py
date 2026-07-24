class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
        
        print(graph)
        for u in graph:
            if hasCycles(u, graph, set()):
                return False
        
        return True
        # graph must be acyclic and each point must be reachable fro