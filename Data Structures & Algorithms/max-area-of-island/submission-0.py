class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        visited = set()
        def dfs(i,j,count):
            if (i,j) in visited: return count
            if i < 0 or i >= m: return count
            if j < 0 or j >= n: return count
            visited.add((i,j))
            if grid[i][j] == 0: return count
            count += 1
            for di, dj in [(0,1), (0,-1), (1,0), (-1, 0)]:
                count = dfs(i+di, j+dj, count)
            return count
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i,j,0))
        return res