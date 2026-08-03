class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        S - m[i][j] = LCS of text[:i+1] and text[:j+1]
        R - m[i][j] = max(m[i][j-1], m[i-1][j], m[i-1][j-1]) + 1*(text1[i] == text2[j])
        T - m[i][j] is dependent on the a and b where i >= a, j >= b
        B - m[i][j] = 1 if text1[i] == text2[j] else 0
        O - max(m)
        T - O(n^2) time, O(n^2) space
        """
        res = 0
        m, n = len(text1), len(text2)
        memo = [[0 for j in range(n+1)] for i in range(m+1)]

        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    memo[i+1][j+1] = 1 + memo[i][j]
                else:
                    memo[i+1][j+1] = max(
                        memo[i+1][j], 
                        memo[i][j+1]
                    )
                res = max(res, memo[i+1][j+1])
        return res
            