# Given an image represented by an N x N matrix, where each pixel in the image is 4 bytes,
# write a method to rotate the image by 90 degrees. Can you do this in place?
#
# Example 1:
# Given matrix =
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
# Rotate the matrix in place. It becomes:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
# Example 2:
# Given matrix =
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ],
# Rotate the matrix in place. It becomes:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]
from typing import List



class Solution:
    # Use auxiliary array
    # matrix[col][n - row - 1] = matrix[row][col]
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # python 不能直接 matrix_new = matrix or matrix_new = matrix[:] 引用拷贝
        matrix_new = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                matrix_new[j][n - i - 1] = matrix[i][j]
        matrix[:] = matrix_new

    # tmp = matrix[row][col]
    # matrix[row][col] = matrix[n - col - 1][row]
    # matrix[n - col - 1][row] = matrix[n - row - 1][n - col - 1]
    # matrix[n - row - 1][n - col - 1] = matrix[col][n - row - 1]
    # matrix[col][n - row - 1] = tmp
    def rotate2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] = \
                    matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]

    # horizontal flip + main diagonal flip
    # matrix[row][col] = matrix[n-row-1][col]
    # matrix[n-row-1][col] = matrix[col][n-row-1]
    def rotate3(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def test():
    s = Solution()
    matrix11 = [
      [7, 4, 1],
      [8, 5, 2],
      [9, 6, 3]
    ]
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    s.rotate(matrix1)
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    s.rotate2(matrix1)
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    s.rotate3(matrix1)
    assert matrix1== matrix11
    matrix22 = [
      [15, 13, 2, 5],
      [14, 3, 4, 1],
      [12, 6, 8, 9],
      [16, 7, 10, 11]
    ]
    matrix2 = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    s.rotate(matrix2)
    matrix2 = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    s.rotate2(matrix2)
    matrix2 = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    s.rotate3(matrix2)
    assert matrix2 == matrix22


if __name__ == '__main__':
    test()