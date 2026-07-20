class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        [
        [2,1,1],
        [0,1,1],
        [1,0,1]
        ]
        """
        
        # helpers
        m,n = len(grid), len(grid[0])
        def check(i,j):
            return (
                i >= 0 and 
                i < m and 
                j >= 0 and 
                j < n
            )
        def neighbors(i,j):
            return [
                (i+di, j+dj) 
                for di, dj 
                in [(1,0), (-1,0), (0,1), (0,-1)] 
                if check(i+di, j+dj)
            ]
        
        # build data
        remaining = 0
        state = []
        for i in range(m):
            for j in range(n):
                cell = grid[i][j]
                if cell == 1:
                    remaining += 1
                if cell == 2:
                    state.append((i,j))

        
        # bfs
        minutes = 0
        visited = set()
        while state and remaining > 0:
            next_state = []
            minutes += 1
            for (i,j) in state:
                for (ni, nj) in neighbors(i,j):
                    if (ni, nj) in visited: continue
                    if grid[ni][nj] == 0: continue
                    if grid[ni][nj] == 1:
                        remaining -= 1
                    visited.add((ni,nj))
                    next_state.append((ni,nj))
            state = next_state

        return -1 if remaining > 0 else minutes
        
        visited = set()