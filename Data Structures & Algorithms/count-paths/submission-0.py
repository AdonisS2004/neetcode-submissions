class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        S - memo[i][j] represents the all possible unique paths
        R - memo[i][j] = memo[i][j-1] + memo[i-1][j]
        T - memo[i][j] is dependent on (i, j-1) and (i-1,j), so
        we go column by column, row by row filling the table
        B - memo[i][0] = 1 for all i in range(m), memo[0][j] = 1
        for all j in range(n)
        O - memo[m-1][n-1]
        T - O(m*n) space, O(m*n) tim
        """
        memo = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m): memo[i][0] = 1
        for j in range(n): memo[0][j] = 1

        for i in range(1,m):
            for j in range(1,n):
                memo[i][j] = memo[i][j-1] + memo[i-1][j]
        
        return memo[m-1][n-1]
