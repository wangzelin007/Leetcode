# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# leetcode 74
# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。
#
# 示例 1：
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# 输出：true
# 思路：
# 1. 暴力
# 2. 坐标轴法
# 3. 二分查找 列 && 行
# 4. 一维化 一次二分查找
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in matrix:
            for j in i:
                if j == target:
                    return True
        return False

    def searchMatrix2(self, matrix, target):
        if not matrix or not matrix[0]: return False
        m = len(matrix)
        n = len(matrix[0])
        i,j = 0,n-1
        while True:
            if i < m and j > 0:
                if target == matrix[i][j]: return True
                elif target < matrix[i][j]: j -= 1
                else: i += 1
            else:
                return False

    # def searchMatrix3(self, matrix, target):
    #     M, N = len(matrix), len(matrix[0])
    #     col0 = [row[0] for row in matrix]
    #     target_row = bisect.bisect_right(col0, target) - 1
    #     if target_row < 0:
    #         return False
    #     target_col = bisect.bisect_left(matrix[target_row], target)
    #     if target_col >= N:
    #         return False
    #     if matrix[target_row][target_col] == target:
    #         return True
    #     return False
    def searchMatrix3(self, matrix, target):
        m,n = len(matrix),len(matrix[0])
        i,j = 0,m*n-1
        while i <= j:
            mid = (j-i)//2 + i
            num = matrix[mid//n][mid%n]
            if target < num: j = mid-1
            elif target > num: i = mid+1
            else: return True
        return False

if __name__ == '__main__':
    s = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    print(s.searchMatrix3(matrix,target))
    target = 4
    print(s.searchMatrix3(matrix,target))
