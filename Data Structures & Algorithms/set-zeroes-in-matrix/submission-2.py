class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        [
        [0,1,2,0],
        [3,4,5,2],
        [1,3,1,5]]
        """
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][j] = None
                    for cell in range(m):
                        if matrix[cell][j] != 0:
                            matrix[cell][j] = None
                    for cell in range(n):
                        if matrix[i][cell] != 0:
                            matrix[i][cell] = None
                    
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == None:
                    matrix[i][j] = 0
                    