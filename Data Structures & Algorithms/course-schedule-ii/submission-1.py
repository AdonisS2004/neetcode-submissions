class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        G is a directed graph
        - must be acyclic
        
        We can use the topological sorting 
        algorithm (dfs or bfs) to get ordering
        """
        G = {i:[] for i in range(numCourses)}
        for u,v in prerequisites:
            G[u].append(v)
        
        # cycle detection
        def is_acyclic_dfs(u, visited):
            if u in visited: 
                return False
            visited.add(u)
            for v in G[u]:
                if not is_acyclic_dfs(v, visited):
                    return False
            visited.remove(u)
            return True
        
        for u in G:
            if not is_acyclic_dfs(u, set()):
                return []
        

        # topological sort dfs
        res = []
        def toposort_dfs(u, visited):
            if u in visited: return
            visited.add(u)
            for v in G[u]:
                toposort_dfs(v, visited)
            res.append(u)

        visited = set()
        for u in G:
            toposort_dfs(u, visited)
        
        return res