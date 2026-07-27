class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # idea: every cell touching an edge is safe,
        # if the cell is connected to a safe cell, it is
        # also safe

        # solution variables and functions
        m, n = len(board), len(board[0])
        def valid_neighbors(i, j):
            offsets = [(1,0), (-1,0), (0,1), (0,-1)]
            res = []
            for di, dj in offsets:
                if i + di >= 0 and i + di < m:
                    if j + dj >= 0 and j + dj < n:
                        res.append((i+di, j+dj))
            return res
        
        def dfs(row, col, visited, update, condition):
            if (row, col) in visited:
                return
            update(row, col, visited)
            for nrow, ncol in valid_neighbors(row, col):
                if condition(nrow, ncol):
                    dfs(nrow, ncol, visited, update, condition)

        # structs and helpers
        visited = set()

        def update(row, col, visited):
            visited.add((row, col))
        
        def condition(row, col):
            if board[row][col] == "O":
                return True
            return False

        # update board
        for r in range(m):
            for c in range(n):
                # Check if the cell is on any of the 4 borders
                if (r == 0 or r == m - 1 or c == 0 or c == n - 1) and board[r][c] == "O":
                    dfs(r, c, visited, update, condition)
        
        # solution
        for r in range(m):
            for c in range(n):
                if (r, c) not in visited:
                    board[r][c] = "X"
        
        