from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        m, n = len(grid), len(grid[0])
        def dfs(i,j,island):
            if (i,j) in visited: return
            if i < 0 or i >= m: return
            if j < 0 or j >= n: return
            visited.add((i, j))
            if grid[i][j] == "0": return
            island.append((i, j))
            offsets = [(0,1), (0,-1), (1,0), (-1, 0)]
            for di, dj in offsets:
                dfs(i+di, j+dj, island)

        res = 0
        for i in range(m):
            for j in range(n):
                tmp = []
                dfs(i, j, tmp)
                if tmp: res += 1
        return res


