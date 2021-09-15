# Write an algorithm such that if an element in an MxN matrix is 0,
# its entire row and column are set to 0.
#
# Example 1:
# Input:
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# Output:
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
# Example 2:
# Input:
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# Output:
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        rows = [False] * m
        cols = [False] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True

        for i in range(m):
            for j in range(n):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0

    def setZeroes2(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        # any()用于判断给定的可迭代参数iterable
        # 全部为False，则返回False，
        # 如果有一个为True，则返回True。
        # 记录原始的 0行 0列 状态
        flag_col0 = any(matrix[i][0] == 0 for i in range(m))
        flag_row0 = any(matrix[0][j] == 0 for j in range(n))

        # 通过 0行 0列 记录需要置0 的行和列
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        # 置0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 通过0列flag 置0 0列
        if flag_col0:
            for i in range(m):
                matrix[i][0] = 0
        # 通过0行flag 置0 0行
        if flag_row0:
            for j in range(n):
                matrix[0][j] = 0

    def setZeroes3(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        flag_col0 = False

        for i in range(m):
            # 记录0列flag
            if matrix[i][0] == 0:
                flag_col0 = True
            # 通过 0行 0列 记录需要置0 的行和列
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        # 行方向上逆序置0，0列通过flag置0
        # 第一列的第一个元素即可以标记第一行是否出现0。
        # 但为了防止每一列的第一个元素被提前更新，我们需要从最后一行开始，倒序地处理矩阵元素。
        for i in range(m - 1, -1, -1):
        # for i in range(m): # error
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if flag_col0:
                matrix[i][0] = 0

def test():
    s = Solution()
    matrix1 = [
      [1,1,1],
      [1,0,1],
      [1,1,1]
    ]
    matrix11 = [
      [1,0,1],
      [0,0,0],
      [1,0,1]
    ]
    s.setZeroes(matrix1)
    assert matrix1 == matrix11
    matrix2 = [
      [0,1,2,0],
      [3,4,5,2],
      [1,3,1,5]
    ]
    matrix22 = [
      [0,0,0,0],
      [0,4,5,0],
      [0,3,1,0]
    ]
    s.setZeroes3(matrix2)
    assert matrix2 == matrix22

if __name__ == '__main__':
    test()