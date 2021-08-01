# coding: utf-8
from typing import List
# N 皇后问题
# N 皇后问题是指在 N*N 的棋盘上摆 N 个皇后
# 要求任意两个皇后不同行、不同列，也不再一条斜线上
# 给定一个整数n， 返回 n 皇后的摆法总数

# 51 Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
# 08.12 Input: 4
#  Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# same as 51
# 52 Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n < 1: return []
        self.col = set()
        # 左对角线
        self.left_diagonal = set()
        self.right_diagonal = set()
        self.n = n
        self.res = []
        self._dfs(0, [])
        return self._generate_result()

    def _dfs(self, row, result):
        if row == self.n:
            self.res.append(result)
            return

        for col in range(self.n):
            if col in self.col or row + col in self.left_diagonal or row - col in self.right_diagonal:
                continue

            self.col.add(col)
            self.left_diagonal.add(row + col)
            self.right_diagonal.add(row - col)
            self._dfs(row + 1, result + [col])
            self.col.remove(col)
            self.left_diagonal.remove(row + col)
            self.right_diagonal.remove(row - col)

    def _generate_result(self):
        board = []
        for res in self.res:
            for i in res:
                board.append('.' * i + 'Q' + '.' * (self.n - i - 1))
        print(board)
        return [board[i: i + self.n] for i in range(0, len(board), self.n)]

def test():
    s = Solution()
    print(s.solveNQueens(4))

if __name__ == '__main__':
    test()