# 给定正整数n，找到若干个完全平方数（比如1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
# 给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。
# 完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
# 示例1：
# 输入：n = 12
# 输出：3
# 解释：12 = 4 + 4 + 4
# 示例 2：
# 输入：n = 13
# 输出：2
# 解释：13 = 4 + 9
# 提示：
# 1 <= n <= 104
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/perfect-squares
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 完全背包DP
# f[i][j] 为考虑前 i 个数字，凑出数字总和 j 所需要用到的最少数字数量。
# 不失一般性的分析 f[i][j]，对于第 i 个数字（假设数值为 t），我们有如下选择：
# 选 0 个数字 i，此时有 f[i][j]=f[i−1][j]
# 选 1 个数字 i，此时有 f[i][j]=f[i−1][j−t]+1
# 选 2 个数字 i，此时有 f[i][j]=f[i−1][j−2∗t]+2
# ...
# 选 k 个数字 ii，此时有 f[i][j]=f[i−1][j−k∗t]+k
# 一维化 f[j]=min(f[j],f[j−t]+1)
class Solution:
    def numSquares(self, n: int) -> int:
        nums = [i*i for i in range(1, int(n**0.5)+1)]
        f = [0] + [float('inf')] * n
        for num in nums:
            for j in range(num, n+1):
                f[j] = min(f[j], f[j-num]+1)
        return f[-1]
