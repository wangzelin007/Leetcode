# 给出矩阵matrix和目标值target，返回元素总和等于目标值的非空子矩阵的数量。
# 子矩阵x1, y1, x2, y2是满足 x1 <= x <= x2且y1 <= y <= y2的所有单元matrix[x][y]的集合。
# 如果(x1, y1, x2, y2) 和(x1', y1', x2', y2')两个子矩阵中部分坐标不同（如：x1 != x1'），那么这两个子矩阵也不同。
# 示例 1：
# 输入：matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
# 输出：4
# 解释：四个只含 0 的 1x1 子矩阵。
# 示例 2：
# 输入：matrix = [[1,-1],[-1,1]], target = 0
# 输出：5
# 解释：两个 1x2 子矩阵，加上两个 2x1 子矩阵，再加上一个 2x2 子矩阵。
# 示例 3：
# 输入：matrix = [[904]], target = 0
# 输出：0
# 提示：
# 1 <= matrix.length <= 100
# 1 <= matrix[0].length <= 100
# -1000 <= matrix[i] <= 1000
# -10^8 <= target <= 10^8
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/number-of-submatrices-that-sum-to-target
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 相似题型：https://leetcode-cn.com/problems/subarray-sum-equals-k/submissions/
# 1074 首先降维到1维数组，解法就和560一样
from typing import List
from collections import Counter

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        def subarraySum(nums: List[int], k: int) -> int:
            mp = Counter([0])
            count = pre = 0
            for num in nums:
                pre += num
                if pre - k in mp:
                    count += mp[pre - k]
                mp[pre] += 1
            return count

        m, n = len(matrix), len(matrix[0])
        ans = 0
        for i in range(m):
            # 每次都重新初始化
            total = [0] * n
            for j in range(i, m):
                for c in range(n):
                    total[c] += matrix[j][c]
                # 构建玩total就需要累加
                ans += subarraySum(total, target)
        return ans
