# 给你一个二进制字符串数组 strs 和两个整数 m 和 n 。
# 请你找出并返回 strs 的最大子集的大小，该子集中 最多 有 m 个 0 和 n 个 1 。
# 如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。
# 示例 1：
# 输入：strs = ["  10", "0001", "111001", "1", "0"], m = 5, n = 3
# 输出：4
# 解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
# 其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。
# {"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。
# 示例 2：
# 输入：strs = ["10", "0", "1"], m = 1, n = 1
# 输出：2
# 解释：最大的子集是 {"0", "1"} ，所以答案是 2 。
# 提示：
# 1 <= strs.length <= 600
# 1 <= strs[i].length <= 100
# strs[i]仅由 '0' 和 '1' 组成
# 1 <= m, n <= 100
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/ones-and-zeroes
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
# f[k][i][j] 代表考虑前 k 件物品，在数字 1 容量不超过 i，数字 0 容量不超过 j 的条件下的「最大价值」（每个字符串的价值均为 1）。
# f[k][i][j]=max(f[k−1][i][j],f[k−1][i−cnt[k][0]][j−cnt[k][1]]+1)
# 1. 不选择第K件物品
# 2. 有足够的 m 和 n 额度可使用来选择第K件物品
# 其中 cntcnt 数组记录的是字符串中出现的 01 数量。
# 三维dp
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        Len = len(strs)
        dp = [[[0 for _ in range(n + 1)] for _ in  range(m + 1)] for _ in range(Len + 1)]
        for k in range(1, Len + 1):
            cnt0 = strs[k-1].count('0')
            cnt1 = strs[k-1].count('1')
            for i in range(m + 1):
                for j in range(n + 1):
                    dp[k][i][j] = dp[k-1][i][j]             #继承
                    if i - cnt0 >= 0 and j - cnt1 >= 0:     #可更新则更新
                        dp[k][i][j] = max(dp[k][i][j], dp[k-1][i-cnt0][j-cnt1] + 1)

        return dp[Len][m][n]
# 由三维状态转移方程得知：更新某个物品的状态时，只依赖于上一个物品的状态。
# 二维dp 宫水三叶 背包问题学习
# todo
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for s in strs:
            cnt0 = s.count('0')
            cnt1 = s.count('1')
            for i in range(m, cnt0 - 1, -1):    #0-1背包问题，内循环逆序
                for j in range(n, cnt1 - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-cnt0][j-cnt1] + 1)
        return dp[m][n]

if __name__ == '__main__':
    s = Solution()
    s.findMaxForm(["10", "0", "1"], 1, 1)