# 在一个小城市里，有m个房子排成一排，你需要给每个房子涂上 n种颜色之一（颜色编号为 1 到 n）。
# 有的房子去年夏天已经涂过颜色了，所以这些房子不需要被重新涂色。
# 我们将连续相同颜色尽可能多的房子称为一个街区。
# 比方说 houses = [1,2,2,3,3,2,1,1] ，它包含 5 个街区 [{1}, {2,2}, {3,3}, {2}, {1,1}]
# 给你一个数组houses，一个m * n的矩阵cost和一个整数target，其中：
# houses[i]：是第i个房子的颜色，0表示这个房子还没有被涂色。
# cost[i][j]：是将第i个房子涂成颜色j+1的花费。
# 请你返回房子涂色方案的最小总花费，使得每个房子都被涂色后，恰好组成target个街区。
# 如果没有可用的涂色方案，请返回-1。
# 示例 1：
# 输入：houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
# 输出：9
# 解释：房子涂色方案为 [1,2,2,1,1]
# 此方案包含 target = 3 个街区，分别是 [{1}, {2,2}, {1,1}]。
# 涂色的总花费为 (1 + 1 + 1 + 1 + 5) = 9。
# 示例 2：
# 输入：houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
# 输出：11
# 解释：有的房子已经被涂色了，在此基础上涂色方案为 [2,2,1,2,2]
# 此方案包含 target = 3 个街区，分别是 [{2,2}, {1}, {2,2}]。
# 给第一个和最后一个房子涂色的花费为 (10 + 1) = 11。
# 示例 3：
# 输入：houses = [0,0,0,0,0], cost = [[1,10],[10,1],[1,10],[10,1],[1,10]], m = 5, n = 2, target = 5
# 输出：5
# 示例 4：
# 输入：houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3
# 输出：-1
# 解释：房子已经被涂色并组成了 4 个街区，分别是 [{3},{1},{2},{3}] ，无法形成 target = 3 个街区。
# 提示：
# m == houses.length == cost.length
# n == cost[i].length
# 1 <= m <= 100
# 1 <= n <= 20
# 1 <= target<= m
# 0 <= houses[i]<= n
# 1 <= cost[i][j] <= 10^4
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/paint-house-iii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
# 房子的编号为 [0, m-1]；
# 颜色的编号为 [0, n-1]，如果房子没有涂上颜色，那么记为 −1；
# 街区的编号为 [0,target−1]。
# 设dp(i,j,k) 表示将 [0,i] 的房子都涂上颜色，最末尾的第 i 个房子的颜色为 j，并且它属于第 k 个街区时，需要的最少花费。
# 设第 i−1 个房子的颜色为 j0，我们可以分类讨论出不同情况下的状态转移方程：
# 1. 如果 houses[i] != −1，说明第 i 个房子已经涂过颜色了。
# 由于我们不能重复涂色，那么必须有 houses[i]=j。
# 我们可以写出在 houses[i] != j 时的状态转移方程：
# 1.special dp(i,j,k)=∞,如果houses[i] != −1并且houses[i] != j
# 这里我们用极大值 ∞ 表示不满足要求的状态，由于我们需要求出的是最少花费，因此极大值不会对状态转移产生影响。
# 当 houses[i] = j 时，如果 j=j0，那么第 i−1 个房子和第 i 个房子属于同一个街区，状态转移方程为：
# 1.a dp(i,j,k)=dp(i−1,j,k),如果houses[i]=j
# 如果 j != j0，那么它们属于不同的街区，状态转移方程为：
# 1.b dp(i,j,k)=min(dp(i−1,j0,k−1)) and (j0 != j),如果houses[i]=j
# 2. 如果 houses[i] = −1，说明我们需要将第 i 个房子涂成颜色 j，花费为 cost[i][j]。
# 此外的状态转移与上一类情况类似。如果 j=j0，那么状态转移方程为：
# 2.a dp(i,j,k)=dp(i−1,j,k)+cost[i][j],如果houses[i]=−1
# 如果 j != j0，那么状态转移方程为：
# 2.b dp(i,j,k)=min(dp(i−1,j0,k−1)) and (j0 != j)+cost[i][j],如果houses[i]=−1
# 3. 最终的答案即为min(dp(m−1,j,target−1) for j in range(n))
# 细节
# 以下的细节有助于写出更简洁的代码：
# 我们可以将所有的状态初始化为 ∞。在进行状态转移时，我们是选择转移中的最小值，因此 ∞ 不会产生影响；
# 两类情况下的状态转移方程十分类似，因此我们可以先不去管 cost[i][j] 的部分，在求出 dp(i,j,k) 的最小值之后，如果发现 houses[i]=−1，再加上 cost[i][j] 即可；
# 当 k=0 时，不能从包含 k−1 的状态转移而来；
# 当 i=0 时，第 0 个房子之前没有房子，因此 k 也必须为 0。此时状态转移方程为：
# dp(0,j,0) = ∞, 如果houses[i] != −1 并且 houses[i] != j
# dp(0,j,0) = 0, 如果houses[i] != −1 并且 houses[i] = j
# dp(0,j,0) = cost[i][j], 如果houses[i] = −1
# 当i = 0 且 k != 0 时, dp(0,j,k) = ∞

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # 将颜色调整为从 0 开始编号，没有被涂色标记为 -1
        houses = [c-1 for c in houses]
        # dp 所有元素初始化为极大值
        dp = [[[float('inf')] * target for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if houses[i] != -1 and houses[i] != j:
                    continue

                for k in range(target):
                    for j0 in range(n):
                        if j == j0:
                            if i == 0:
                                if k == 0:
                                    dp[i][j][k] = 0
                            else:
                                dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][k])
                        elif i > 0 and k > 0:
                            dp[i][j][k] = min(dp[i][j][k], dp[i-1][j0][k-1])

                    if dp[i][j][k] != float('inf') and houses[i] == -1:
                        dp[i][j][k] += cost[i][j]

        ans = min(dp[m-1][j][target-1] for j in range(n))
        return -1 if ans == float('inf') else ans

# 在方法一的基础上优化 1.b 和 2.b
# 1.b dp(i,j,k)=min(dp(i−1,j0,k−1)) and (j0 != j),如果houses[i]=j
# 2.b dp(i,j,k)=min(dp(i−1,j0,k−1)) and (j0 != j)+cost[i][j],如果houses[i]=−1
# 我们可以令 best(i,k)=(first,first_idx,second)，表示所有的状态 dp(i,j,k) 中的最小值为 first，取到最小值对应的 j 值为 first_idx，次小值为 second。
# 即优化求解 min(dp(i−1,j0,k−1) for j0 in range(n) and j0 != j)
# 我们取出 best(i−1,k−1)，它包含的三个值为 (first,first_idx,second)；
# 如果 j = first_idx，因为 j0 != j, 那么 dp(i,j,k)=second；
# 如果 j != first_idx，因为 j0 != j, 那么 dp(i,j,k)=first。
class Entry:
    def __init__(self):
        self.first = float("inf")
        self.first_idx = -1
        self.second = float("inf")

class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # 将颜色调整为从 0 开始编号，没有被涂色标记为 -1
        houses = [c - 1 for c in houses]

        # dp 所有元素初始化为极大值
        dp = [[[float("inf")] * target for _ in range(n)] for _ in range(m)]
        # 优化：初始化best
        best = [[Entry() for _ in range(target)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if houses[i] != -1 and houses[i] != j:
                    continue

                for k in range(target):
                    if i == 0:
                        if k == 0:
                            dp[i][j][k] = 0
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]
                        if k > 0:
                            # 优化：使用 best(i-1,k-1) 直接得到 dp(i,j,k) 的值
                            info = best[i - 1][k - 1]
                            dp[i][j][k] = min(dp[i][j][k], (info.second if j == info.first_idx else info.first))

                    if dp[i][j][k] != float("inf") and houses[i] == -1:
                        dp[i][j][k] += cost[i][j]

                    # 优化：用 dp(i,j,k) 更新 best(i,k)
                    info = best[i][k]
                    if dp[i][j][k] < info.first:
                        info.second = info.first
                        info.first = dp[i][j][k]
                        info.first_idx = j
                    elif dp[i][j][k] < info.second:
                        info.second = dp[i][j][k]

        ans = min(dp[m - 1][j][target - 1] for j in range(n))
        return -1 if ans == float("inf") else ans


