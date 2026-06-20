class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        ml, mr, row = 0, m - 1, 0
        nl, nr, col = 0, n - 1, 0

        # find row
        while ml < mr:
            mid = (ml+mr)//2
            lower, upper = matrix[mid][0], matrix[mid][-1]
            if ( # x <= target <= y
                lower <= target and
                upper >= target  
            ):
                row = mid
                break
            if upper < target:
                ml = mid + 1
                row = ml
            if lower > target:
                mr = mid - 1
                row = mr

        # find col
        while nl < nr:
            mid = (nl+nr)//2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] < target:
                nl = mid + 1
                col = nl
            if matrix[row][mid] > target:
                nr = mid - 1
                col = nr

        if matrix[row][col] == target:
            return True
        return False