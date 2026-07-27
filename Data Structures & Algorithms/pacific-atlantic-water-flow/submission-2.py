class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # variable setup
        m, n = len(heights), len(heights[0])
        pacific_egdes = [[0,i] for i in range(n)] + [[i, 0] for i in range(m)]
        atlantic_edges = [[m-1,i] for i in range(n)] + [[i, n-1] for i in range(m)]
        grid = [[[False, False] for _ in range(n)] for _ in range(m)]

        # helper functions
        def validNeighbors(i, j):
            offsets = [(0,1), (0,-1), (1, 0), (-1, 0)]
            res = []
            for di, dj in offsets:
                if i + di >= 0 and i + di < m:
                    if j + dj >= 0 and j + dj < n:
                        res.append((i + di, j + dj))
            return res

        def dfs(row, col, i, condition, update, visited):
            if (row, col) in visited: return
            visited.add((row, col))
            update(row, col, i)
            for nrow, ncol in validNeighbors(row, col):
                if condition(row, col, nrow, ncol):
                    dfs(nrow, ncol, i, condition, update, visited)
    
        def condition(r1, c1, r2, c2):
            return heights[r1][c1] <= heights[r2][c2]

        def update(row, col, i):
            grid[row][col][i] = True

        # updating starting at pacific
        visited = set()
        for row, col in pacific_egdes:
            dfs(row, col, 0, condition, update, visited)

        # updating starting at atlantic
        visited = set()
        for row, col in atlantic_edges:
            dfs(row, col, 1, condition, update, visited)

        # result
        return [[i,j] for i in range(m) for j in range(n) if grid[i][j] == [True, True]]