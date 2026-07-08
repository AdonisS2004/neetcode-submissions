class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        boards = []

        def checkRow(queen, board):
            row, _ = queen
            for col in range(n):
                if (row, col) != queen and board[row][col] == 'Q':
                    return False
            return True

        def checkCol(queen, board):
            _, col = queen
            for row in range(n):
                if (row, col) != queen and board[row][col] == 'Q':
                    return False
            return True
        
        def checkDiag(queen, board):
            row, col = queen
            while row >= 0 and col >= 0:
                if (row, col) != queen and board[row][col] == 'Q':
                    return False
                row -= 1
                col -= 1

            row, col = queen
            while row < n and col < n:
                if (row, col) != queen and board[row][col] == 'Q':
                    return False
                row += 1
                col += 1
            
            row, col = queen
            while row >= 0 and col < n:
                if (row, col) != queen and board[row][col] == 'Q':
                    return False
                row -= 1
                col += 1
            
            row, col = queen
            while row < n and col >= 0:
                if (row, col) != queen and board[row][col] == 'Q':
                    return False
                row += 1
                col -= 1
            
            return True

        def checkBoard(board, queens):
            for queen in queens:
                if not checkCol(queen, board):
                    return False
                if not checkRow(queen, board):
                    return False
                if not checkDiag(queen, board):
                    return False
            return True

        def constructBoard(board):
            output = []
            for row in board:
                r = "".join(row)
                output.append(r)
            return output

        def generateBoards(board, nqueens, row):
            # base case: nqueens satisfied
            if nqueens == n:
                output = constructBoard(board)
                boards.append(output)
                return

            # place queen
            for col in range(n):
                if not checkCol((row, col), board):
                    continue
                if not checkRow((row, col), board):
                    continue
                if not checkDiag((row, col), board):
                    continue

                board[row][col] = 'Q'
                generateBoards(board, nqueens + 1, row + 1)
                board[row][col] = '.'
            
            return
        
        generateBoards([['.' for _ in range(n)] for _ in range(n)], 0, 0)
        return boards
        

        