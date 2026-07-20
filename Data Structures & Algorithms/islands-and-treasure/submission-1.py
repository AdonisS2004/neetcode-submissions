from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        def neighbors(i,j):
            res = []
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                if i+di < 0 or i+di >= m: continue
                if j+dj < 0 or j+dj >= n: continue
                res.append((i+di, j+dj))
            return res
        
        treasure = [(i,j) for i in range(m) for j in range(n) if grid[i][j] == 0]
        for i, j in treasure:
            queue = deque([(i,j,0)])
            visited = {(i,j,0)}
            while queue:
                row,col,dist = queue.popleft()
                if grid[row][col] != -1:
                    grid[row][col] = min(dist, grid[row][col])
                    for nrow, ncol in neighbors(row,col):
                        if (nrow,ncol) in visited: continue
                        queue.append((nrow,ncol,dist+1))
                        visited.add((nrow, ncol))


