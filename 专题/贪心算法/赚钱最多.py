# costs 代表每个项目的花费
# profits 代表每个项目的净利润
# k 代表最多只能接k个项目
# M 代表初始的启动资金
# 每做完一个项目，可以马上获得收益，然后启动下一个项目，项目只能串行的做。
# 输出最后获得的最大利润
from heapq import *

def maxValue(costs, profits, k, M):
    costs = [(cost,id) for id, cost in enumerate(costs)]
    profits = [(-profit, id) for id, profit in enumerate(profits)]
    heapify(costs)
    maxProfitQ = []
    # cost 小跟堆
    heapify(costs)
    for i in range(k):
        while len(costs) != 0 and costs[0][0] <= M:
            heappush(maxProfitQ, profits[heappop(costs)[1]])
        if len(maxProfitQ) == 0:
            return M
        M += -heappop(maxProfitQ)[0]
    return M

def test():
    costs = [1,1,2,3,1]
    profits = [3,5,8,3,18]
    k = 2
    M = 1
    print(maxValue(costs, profits, k, M)) # 14

if __name__ == '__main__':
    test()
