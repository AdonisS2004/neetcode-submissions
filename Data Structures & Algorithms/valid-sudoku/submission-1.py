class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = len(board)
        row_map = {row:set() for row in range(m)}
        col_map = {col:set() for col in range(m)}
        box_map = {(x,y):set() for x in range(m) for y in range(m)}
        for row in range(m):
            for col in range(m):
                value = board[row][col]
                if value == ".":
                    continue
                # row check
                if value in row_map[row]:
                    return False
                row_map[row].add(value)
                # col check
                if value in col_map[col]:
                    return False
                col_map[col].add(value)
                # box check
                coord = (row//3, col//3)
                if value in box_map[coord]:
                    return False
                box_map[coord].add(value)
        return True