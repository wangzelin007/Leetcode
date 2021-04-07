# _*_ coding: utf-8 _*_
# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
#
# 示例 1：
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#
# 示例 2：
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 构筑四个边界
# left, right, top, bottom = 0, len(matrix[0]-1, 0, len(matrix)-1
# 每次循环，修改边界值
class Solution:
    def spiralOrder(self, matrix):
        if not matrix: return []
        left, right, top, bottom, res = 0, len(matrix[0])-1, 0, len(matrix)-1, []
        while matrix:
            # left to right
            if left > right: break
            for i in range(left, right + 1): res.append(matrix[top][i])
            top += 1
            # top to bottom
            if top > bottom: break
            for i in range(top, bottom + 1): res.append(matrix[i][right])
            right -= 1
            # right to left
            if left > right: break
            for i in range(right, left - 1, -1): res.append(matrix[bottom][i])
            bottom -= 1
            # bottom to top
            if top < bottom: break
            for i in range(bottom, top - 1, -1): res.append(matrix[i][left])
            left += 1
        return res

class Solution2:
    def spiralOrder(self, matrix):
        res = []
        while matrix:
            res += matrix.pop(0)
            # zip 接受可迭代参数，将对应的元素打包成一个个元组，返回这些元组组成的列表。
            # zip(*matrix) [(4, 7), (5, 8), (6, 9)]
            # 此处 list 可以省略
            # [::-1] 倒序
            matrix = list(zip(*matrix))[::-1]
        return res

if __name__ == '__main__':
    s = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(s.spiralOrder(matrix))