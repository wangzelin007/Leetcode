# 集团里有 n 名员工，他们可以完成各种各样的工作创造利润。
# 第i种工作会产生profit[i]的利润，它要求group[i]名成员共同参与。
# 如果成员参与了其中一项工作，就不能参与另一项工作。
# 工作的任何至少产生minProfit 利润的子集称为 盈利计划 。并且工作的成员总数最多为 n 。
# 有多少种计划可以选择？因为答案很大，所以 返回结果模10^9 + 7的值。
# 示例 1：
# 输入：n = 5, minProfit = 3, group = [2,2], profit = [2,3]
# 输出：2
# 解释：至少产生 3 的利润，该集团可以完成工作 0 和工作 1 ，或仅完成工作 1 。
# 总的来说，有两种计划。
# 示例 2：
# 输入：n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
# 输出：7
# 解释：至少产生 5 的利润，只要完成其中一种工作就行，所以该集团可以完成任何工作。
# 有 7 种可能的计划：(0)，(1)，(2)，(0,1)，(0,2)，(1,2)，以及 (0,1,2) 。
# 提示：
# 1 <= n <= 100
# 0 <= minProfit <= 100
# 1 <= group.length <= 100
# 1 <= group[i] <= 100
# profit.length == group.length
# 0 <= profit[i] <= 100
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/profitable-schemes
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
# 定义 f[i][j][k] 为考虑前 i 件物品，使用人数不超过 j，所得利润至少为 k 的方案数。
# 不选 j < group[i - 1]
# f[i][j][k]=f[i−1][j][k]
# 选 j >= group[i - 1] 人数富余
# f[i][j][k]=f[i−1][j][k] + f[i−1][j−group[i−1]][k−profit[i−1]]
# 由于我们定义的第三维是工作利润至少为 k
# 如果直接令「利润维度」为 k - profit[i - 1] 可能会出现负值，那么负值是否为合法状态呢？
# 这需要结合「状态定义」来看，由于是「利润至少为 k」，因此属于「合法状态」，需要参与转移。
# 由于我们没有设计动规数组存储「利润至少为负权」状态，我们需要根据「状态定义」做一个等价替换，
# 将这个「状态」映射到 f[i][j][0]。这主要是利用所有的任务成本都为“非负数”，所以不可能出现利润为负的情况，
# 这时候「利润不超过某个负数」的方案数其实是完全等价于「利润不超过 0」的方案数。
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7

        length = len(group)
        # 构建和解析是相反的！
        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(length + 1)]
        dp[0][0][0] = 1
        for i in range(1, length + 1):
            # 由于 dp 是从 0 件物品开始的
            # 但是 group 和 profit 其实是从 1 件物品开始的，下标是从 0 开始
            # 所以 dp 中的的 i ,即 group 和 profit 中的 i-1
            # 举例说明，比如 dp 中 i = 2，代表 0 1 2 第二件事，对应 group 和 profit 中的 0 1(第二件事)
            members, earn = group[i - 1], profit[i - 1]
            for j in range(n + 1):
                for k in range(minProfit + 1):
                    if j < members:
                        dp[i][j][k] = dp[i - 1][j][k]
                    else:
                        dp[i][j][k] = (dp[i - 1][j][k] + dp[i - 1][j - members][max(0, k - earn)]) % MOD

        total = sum(dp[length][j][minProfit] for j in range(n + 1))
        return total % MOD

# 优化
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        # 构建利益+人数 去除物品
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        for i in range(0, n + 1):
            # 对于最小工作利润为 0 的情况，无论当前在工作的员工有多少人，
            # 我们总能提供一种方案，所以初始化 dp[i][0]=1
            dp[i][0] = 1
        for earn, members in zip(profit, group):
            for j in range(n, members - 1, -1):
                for k in range(minProfit, -1, -1):
                    dp[j][k] = (dp[j][k] + dp[j - members][max(0, k - earn)]) % MOD;
        return dp[n][minProfit]

# 可以学习的解题思路
# https://leetcode-cn.com/problems/profitable-schemes/solution/python-ji-yi-hua-sou-suo-by-qubenhao-tq3o/