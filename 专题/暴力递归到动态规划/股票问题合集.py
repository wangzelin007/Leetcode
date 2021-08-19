# 121 buy and sell one time
# 123 buy and sell at most two transactions
# 122 buy and sell as many as you like
# 309 buy and sell as many as you like with cool down(after you sell your stock, you need cool down one day.)
# 714 buy and sell as many as you like with transaction fee
# 188 buy and sell at most k transactions
from typing import List


# 121
# i 天 k 交易次数 j 是否持有股票
# k = 1
# dp[i][0][0] = dp[i-1][0][0]
# dp[i][0][1] = max(dp[i-1][0][1], dp[i-1][0][0] - prices[i])
# dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][0][1] + prices[i])
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0] * 2 for _ in range(2)] for _ in range(n)]
        dp[0][0][1] = - prices[0]
        for i in range(1, n):
            dp[i][0][0] = dp[i-1][0][0]
            dp[i][0][1] = max(dp[i-1][0][1], dp[i-1][0][0] - prices[i])
            dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][0][1] + prices[i])
        return dp[n-1][1][0]

# 123
# i 天 k 交易次数 j 是否持有股票
# k = 2
# dp[i][0][0] = dp[i-1][0][0]
# dp[i][0][1] = max(dp[i-1][0][1], dp[i-1][0][0] - prices[i])
# dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][0][1] + prices[i])
# dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][1][0] - prices[i])
# dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][1][1] + prices[i])
    def maxProfit2(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0] * 2 for _ in range(3)] for _ in range(n)]
        dp[0][0][1] = - prices[0]
        dp[0][1][0], dp[0][1][1], dp[0][2][0] = float('-inf'), float('-inf'), float('-inf')
        for i in range(1, n):
            dp[i][0][0] = dp[i-1][0][0]
            dp[i][0][1] = max(dp[i-1][0][1], dp[i-1][0][0] - prices[i])
            dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][0][1] + prices[i])
            dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][1][0] - prices[i])
            dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][1][1] + prices[i])
        return max(dp[n-1][0][0],dp[n-1][1][0], dp[n-1][2][0])

# 122
# i 天 j 是否持有股票
# dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])  # 不动 or 卖出
# dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])  # 不动 or 买入
    def maxProfit3(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][1] = - prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[n-1][0]

# 309
# dp[i][0]: 手上持有股票的最大收益
# dp[i][1]: 手上不持有股票，并且处于冷冻期中的累计最大收益
# dp[i][2]: 手上不持有股票，并且不在冷冻期中的累计最大收益
    def maxProfit4(self, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        dp = [[-prices[0], 0, 0]] +[[0] * 3 for _ in range(n-1)]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][2], dp[i-1][1])
        return max(dp[n-1][1], dp[n-1][2])

# 714
# i 天 j 是否持有股票
# dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)  # 不动 or 卖出
# dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])  # 不动 or 买入
    def maxProfit6(self, prices: List[int], fee: int) -> int:
        if not prices: return 0
        n = len(prices)
        dp = [[0, -prices[0]]] + [[0] * 2 for _ in range(n-1)]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[n-1][0]

# 188
# k 未知
# dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k-1][1] + prices[i])
# dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
    def maxProfit5(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if not prices: return 0
        dp = [[[None, None] for _ in range(k+1)] for _ in range(n)]
        for i in range(n):
            dp[i][0][0] = 0
            dp[i][0][1] = -prices[0]
        for j in range(1, k+1):
            dp[0][j][0] = 0
            dp[0][j][1] = -prices[0]
        for i in range(1, n):
            for j in range(1, k+1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
        return dp[-1][-1][0]

def test():
    s = Solution()
    assert s.maxProfit2(prices=[1, 2, 3, 4, 5]) == 4
    assert s.maxProfit4(prices=[1, 2 ,3, 0, 2]) == 3
    assert s.maxProfit5(k=2, prices=[3, 2, 6, 5, 0, 3]) == 7

if __name__ == '__main__':
    test()