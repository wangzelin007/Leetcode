# Determine if a 9 x 9 Sudoku board is valid.
# Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# 36. return True or False
# 37. return the board
from typing import List
from pprint import pprint

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for c in range(1, 10):
                        if self.isValid(board, i, j, str(c)):
                            board[i][j] = str(c)
                            if self.isValidSudoku(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True

    def isValid(self, board, row, col, c):
        for i in range(9):
            if board[i][col] != '.' and board[i][col] == c:
                return False
            if board[row][i] != '.' and board[row][i] == c:
                return False
            if board[3 * (row // 3) + int(i / 3)][3 * (col // 3) + i % 3] != '.' and \
                board[3 * (row // 3) + int(i / 3)][3 * (col // 3) + i % 3] == c:
                return False
        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board is None or len(board) == 0:
            return
        self.isValidSudoku(board)

def test():
    s = Solution()
    board =[
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"],]
    assert s.isValidSudoku(board) == True
    pprint(board)
    board = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"],]
    assert s.isValidSudoku(board) == False

if __name__ == '__main__':
    test()


