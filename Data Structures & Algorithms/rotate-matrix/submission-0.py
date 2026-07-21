class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        [
            [1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15], 
            [16,17,18,19,20], 
            [21,22,23,24,25]
        ]

        [
            [21,16,11,4,1],
            [6,17,12,7,2],
            [23,18,13,8,3],
            [24,19,14,9,20],
            [25,22,15,10,5]
        ]


        [
            [21,16,11,6,1],
            [22,17,12,7,2],
            [23,18,13,8,3],
            [24,19,14,9,4],
            [25,20,15,10,5]
        ]

        """
        n = len(matrix)
        for i in range(n):
            for j in range(i,n-i-1):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n-j-1][i]
                matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
                matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
                matrix[j][n-i-1] = tmp
        