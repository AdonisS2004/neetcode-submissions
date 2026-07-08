class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        board=[
            ["A","B","C","E"],
            ["S","F","E","S"],
            ["A","D","E","E"]]

        word="ABCESEEEFS"
        """
        
        m, n, t = len(board), len(board[0]), len(word)
        def getNeighbors(row, col, visited):
            offsets = [(0,1), (0,-1), (1,0), (-1,0)]
            res = []
            for row_off, col_off in offsets:
                nrow, ncol = row + row_off, col + col_off
                if nrow >= 0 and nrow < m and ncol >= 0 and ncol < n:
                    if (nrow, ncol) not in visited:
                        res.append((nrow, ncol))
            return res

        def search(row, col, i, visited):
            # check: board[row][col] == word[i]
            if board[row][col] != word[i]:
                return False
            visited.add((row, col))
            # word found check
            if i+1 == t:
                return True
            # dfs
            neighbors = getNeighbors(row, col, visited)
            for nrow, ncol in neighbors:
                if search(nrow, ncol, i+1, visited.copy()):
                    return True
            return False

        # search
        for row in range(m):
            for col in range(n):
                if search(row, col, 0, set()):
                    return True
        
        return False