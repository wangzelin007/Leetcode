# 分割金条花费的金钱等于金条的的长度
# 比如三个人，每个人需要10，20，30 长度的金条
# 方案1：将60的金条分为10 + 50 ，再将50 的金条分为20+30；花费110
# 方案2：将60的金条分为30 + 30 ，再将30 的金条分为10+20；花费90
# 请给出最优的分金条方案，让花费最少。

# 暴力递归:
def lessMoney2(arr):
    if not arr or len(arr) == 0:
        return 0
    return process(arr, 0)

def process(arr, pre):
    if len(arr) == 1:
        return pre
    ans = float('inf')
    # 任意两个数合在一起求后续
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            ans = min(ans, process(copyAndMergeTwo(arr, i, j), pre + arr[i] + arr[j]))
    return ans

def copyAndMergeTwo(arr, i ,j):
    ans = [0 for _ in range(len(arr)-1)]
    ansi = 0
    for arri in range(len(arr)):
        if arri != i and arri != j:
            ans[ansi] = arr[arri]
            ansi += 1
        arri += 1
    ans[ansi] = arr[i] + arr[j]
    return ans

from heapq import *
def lessMoney(arr):
    heapify(arr)
    sum, cur = 0, 0
    while (len(arr) > 1):
        cur = heappop(arr) + heappop(arr)
        sum += cur
        heappush(arr, cur)
    return sum

def test():
    arr = [1, 3, 5, 7, 9]
    # assert lessMoney(arr) == 54
    assert lessMoney2(arr) == lessMoney(arr)
    arr = [30, 10, 20]
    # assert lessMoney(arr) == 90
    assert lessMoney2(arr) == lessMoney(arr)

if __name__ == '__main__':
    test()


