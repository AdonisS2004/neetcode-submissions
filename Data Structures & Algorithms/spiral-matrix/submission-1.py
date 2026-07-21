class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix), len(matrix[0])
        i, j = 0, -1
        direction = 0 # 0:right, 1:down, 2:left, 3:up
        res = []
        while m > 0 and n > 0:
            match direction:
                case 0:
                    for _ in range(n):
                        j += 1
                        res.append(matrix[i][j])
                    direction = 1
                    m -= 1
                case 1:
                    for _ in range(m):
                        i += 1
                        res.append(matrix[i][j])
                    direction = 2
                    n -= 1
                case 2:
                    for _ in range(n):
                        j -= 1
                        res.append(matrix[i][j])
                    direction = 3
                    m -= 1
                case 3:
                    for _ in range(m):
                        i -= 1
                        res.append(matrix[i][j])
                    direction = 0
                    n -= 1
        return res