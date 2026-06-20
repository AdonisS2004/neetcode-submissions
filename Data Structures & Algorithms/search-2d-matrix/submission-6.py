class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        ml, mr, midx = 0, m - 1, 0
        nl, nr, nidx = 0, n - 1, 0

        while ml < mr:
            mid = (ml+mr)//2
            lower, upper = matrix[mid][0], matrix[mid][-1]
            if ( # x <= target <= y
                lower <= target and
                upper >= target  
            ):
                midx = mid
                break
            if upper < target:
                ml = mid + 1
                midx = ml
            if lower > target:
                mr = mid - 1
                midx = mr

        while nl < nr:
            mid = (nl+nr)//2
            if matrix[midx][mid] == target:
                return True
            if matrix[midx][mid] < target:
                nl = mid + 1
                nidx = nl
            if matrix[midx][mid] > target:
                nr = mid - 1
                nidx = nr
                
        if matrix[midx][nidx] == target:
            return True
        return False