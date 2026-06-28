class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if self.isRowValid(row):
                continue
            else:
                return False
        for col in zip(*board):
            if self.isColValid(col):
                continue
            else:
                return False
        
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True

    def isRowValid(self, row: List[str]):
        sofar = set()
        for i in row:
            if i == ".":
                continue
            if i in sofar:
                return False
            sofar.add(i)
        return True
    
    
    def isColValid(self, col: List[str]):
        return self.isRowValid(col)