# 给你一个 m x n 的矩阵 matrix 和一个整数 k ，找出并返回矩阵内部矩形区域的不超过 k 的最大数值和。
# 题目数据保证总会存在一个数值和不超过 k 的矩形区域。
# 示例 1：
# 输入：matrix = [[1,0,1],[0,-2,3]], k = 2
# 输出：2
# 解释：蓝色边框圈出来的矩形区域 [[0, 1], [-2, 3]] 的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。
# 示例 2：
# 输入：matrix = [[2,2,-1]], k = 3
# 输出：3
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# 大概懂了
# 20210422
from sortedcontainers import SortedList
from typing import List
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        ans = float("-inf")
        m, n = len(matrix), len(matrix[0])

        for i in range(m):   # 枚举上边界
            total = [0] * n
            for j in range(i, m):   # 枚举下边界
                for c in range(n):
                    total[c] += matrix[j][c]   # 更新每列的元素和

                totalSet = SortedList([0])
                s = 0
                for v in total:
                    s += v
                    # lb = totalSet.bisect_left(s - k)
                    import bisect
                    lb = bisect.bisect_left(totalSet,s-k)
                    if lb != len(totalSet):
                        ans = max(ans, s - totalSet[lb])
                    totalSet.add(s)

        return ans

    def findMaxSubArray(self, nums, k):
        ans = float('-inf')
        totalSet = SortedList([0])
        s = 0
        for v in nums:
            s += v
            lb = totalSet.bisect_left(s - k)
            if lb != len(totalSet):
                ans = max(ans, s - totalSet[lb])
            totalSet.add(s)
        return ans


if __name__ == '__main__':
    s = Solution()
    assert s.maxSumSubmatrix([[1,0,1],[0,-2,3]], 2) == 2
    assert s.maxSumSubmatrix([[2,2,-1]], 3) == 3
    # nums = [1,4,7,1,1]
    # assert s.findMaxSubArray(nums, 2) == 2

