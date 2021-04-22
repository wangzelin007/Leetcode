# 假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
# 示例 1:
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
# 注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
# 示例 2:
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 第 i 日卖出的最高利润 = max(第 i-1 日卖出的最高利润，prices[i]-min(prices[:i]))
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a, b, n = 0, 0, len(prices)
        if n < 2: return b
        for i in range(1, n):
            b = max(a, prices[i]-min(prices[:i]))
            a = b
        return b

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost, profit = float("+inf"), 0
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit

if __name__ == '__main__':
    s = Solution()
    prices = [7,1,5,3,6,4]
    assert s.maxProfit(prices) == 5


