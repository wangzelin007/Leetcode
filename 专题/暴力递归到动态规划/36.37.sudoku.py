# Determine if a 9 x 9 Sudoku board is valid.
# Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# 36. A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#     Only the filled cells need to be validated according to the mentioned rules.
# 37. return the board
from typing import List
from pprint import pprint

# 36
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = 3 * (i // 3) + j // 3
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1

                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                        return False
        return True


# 37
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
            if board[i][col] == c:
                return False
            if board[row][i] == c:
                return False
            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c:
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
    s.solveSudoku(board)
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
    board =[
        [".","8","7","6","5","4","3","2","1"],
        ["2",".",".",".",".",".",".",".","."],
        ["3",".",".",".",".",".",".",".","."],
        ["4",".",".",".",".",".",".",".","."],
        ["5",".",".",".",".",".",".",".","."],
        ["6",".",".",".",".",".",".",".","."],
        ["7",".",".",".",".",".",".",".","."],
        ["8",".",".",".",".",".",".",".","."],
        ["9",".",".",".",".",".",".",".","."]]
    assert s.isValidSudoku(board) == False

if __name__ == '__main__':
    test()


