# 给定不同面额的硬币和一个总金额。
# 写出函数来计算可以凑成总金额的硬币组合数。
# 假设每一种面额的硬币有无限个。
# 示例 1:
# 输入: amount = 5, coins = [1, 2, 5]
# 输出: 4
# 解释: 有四种方式可以凑成总金额:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# 示例 2:
# 输入: amount = 3, coins = [2]
# 输出: 0
# 解释: 只用面额2的硬币不能凑成总金额3。
# 示例 3:
# 输入: amount = 10, coins = [10]
# 输出: 1
# 注意:
# 你可以假设：
# 0 <= amount (总金额) <= 5000
# 1 <= coin (硬币面额) <= 5000
# 硬币种类不超过 500 种
# 结果符合 32 位符号整数
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/coin-change-2
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
# 定义 f[i][j] 为考虑前 i 件物品，凑成总和为 j 的方案数量。
# f[i][j] = f[i-1][j] + f[i-1][j-k*val] val = nums[i-1]; 1 =< k <= j/val
# dp[0][0] = 1; 其他为0
# 返回dp[n][amount]
class Solution1:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            value = coins[i-1]
            for j in range(0, amount + 1):
                dp[i][j] = dp[i-1][j]
                k = 1
                while j >= k * value:
                    dp[i][j] += dp[i-1][j - k * value]
                    k += 1
        print(dp)
        return dp[n][amount]

# 优化
# 1. 在二维解法的基础上，直接取消「物品维度」
# 2. 确保「容量维度」的遍历顺序为「从小到大」（适用于「完全背包」）
# 3. 将形如 f[i−1][j−k∗val] 的式子更替为 f[j−val]，同时解决「数组越界」问题（将物品维度的遍历修改为从 val 开始）
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for j in range(coin, amount+1):
                dp[j] += dp[j-coin]
        print(dp)
        return dp[amount]

# https://leetcode-cn.com/problems/coin-change-2/solution/gong-shui-san-xie-xiang-jie-wan-quan-bei-6hxv/
# todo 所有的背包问题
if __name__ == '__main__':
    s = Solution()
    amount = 5; coins = [1, 2, 5]
    s.change(amount, coins)