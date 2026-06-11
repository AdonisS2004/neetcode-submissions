class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        concat = []
        for row in matrix:
            concat = concat + row
        l, r = 0, len(concat) - 1
        while l <= r:
            mid = (l+r)//2
            if concat[mid] == target:
                return True
            elif concat[mid] > target:
                r = mid - 1
            elif concat[mid] < target:
                l = mid + 1
        return False