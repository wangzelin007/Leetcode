有一堆石头，用整数数组stones 表示。其中stones[i] 表示第 i 块石头的重量。
# 每一回合，从中选出任意两块石头，然后将它们一起粉碎。
# 假设石头的重量分别为x 和y，且x <= y。那么粉碎的可能结果如下：
# 如果x == y，那么两块石头都会被完全粉碎；
# 如果x != y，那么重量为x的石头将会完全粉碎，而重量为y的石头新重量为y-x。
# 最后，最多只会剩下一块 石头。返回此石头 最小的可能重量 。如果没有石头剩下，就返回 0。
# 示例 1：
# 输入：stones = [2,7,4,1,8,1]
# 输出：1
# 解释：
# 组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
# 组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
# 组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
# 组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。
# 示例 2：
# 输入：stones = [31,26,33,21,40]
# 输出：5
# 示例 3：
# 输入：stones = [1,2]
# 输出：1
# 提示：
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 100
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/last-stone-weight-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 转换为 0 1 背包问题，背包的容量为 sum / 2
# 选出容量最接近 sum/2 的方案 j
# 那么最小重量即为 sum - 2j
from typing import List
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        n, m = len(stones), total // 2
        dp = [[False] * (m+1) for _ in range(n+1)]
        dp[0][0] = True

        for i in range(n):
            for j in range(m+1):
                if j < stones[i]:
                    dp[i+1][j] = dp[i][j]
                else:
                    dp[i+1][j] = dp[i][j] or dp[i-1][j-stones[i]]

        ans = None
        for j in range(m, -1, -1):
            if dp[n][j]:
                ans = total - 2 * j
                break
        return ans

# 由于dp[i+1]的结果只和dp[i]有关，所以可以使用滚动数组的方式降维
# 但是如果仍旧采用正序遍历，计算dp[i]时，dp[j-stones[i]]的值已经被覆盖了
# 所以需要采用倒序遍历
# dp[i+1][j] = dp[i][j] or dp[i][j-stones[i]]
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        n, m = len(stones), total // 2
        dp = [False] * (m+1)
        dp[0] = True

        for weight in stones:
            for j in range(m, weight - 1, -1):
                dp[j] |= dp[j - weight]

        ans = None
        for j in range(m, -1, -1):
            if dp[j]:
                ans = total - 2 * j
                break
        return ans