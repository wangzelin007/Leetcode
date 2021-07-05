# coding: utf-8
# 给定两个长度都是 N 的数组 weights 和 values
# weights[i] 和 values[i] 分表代表物品的重量和价值
# 给定一个正数 bag 代表一个载重为 bag 的袋子
# 你装的物品不能超过这个重量
# 返回所能装下的最大价值
def maxValue(w, v, bag):
    return process(w, v, 0, bag)

def process(w, v, i, rest):
    if rest <= 0:
        return 0
    if i == len(w):
        return 0
    p1 = process(w, v, i+1, rest)
    p2 = -1
    if rest >= w[i]:
        p2 = process(w, v, i+1, rest - w[i]) + v[i]
    return max(p1, p2)

def maxValue3(w, v, bag):
    n = len(w)
    dp = [[0] * (bag + 1) for _ in range(n + 1)]
    for i in range(n-1, -1, -1):
        for rest in range(bag+1):
            p1 = dp[i + 1][rest]
            p2 = -1
            if rest >= w[i]:
                p2 = v[i] + dp[i + 1][rest - w[i]]
            dp[i][rest] = max(p1, p2)
    return dp[0][bag]

def maxValue2(w, v, bag):
    return process2(w, v, 0, 0, bag)

def process2(w, v, i, weight, bag):
    if weight > bag:
        return -1
    if i == len(w):
        return 0
    p1 = process2(w, v, i+1, weight, bag)
    p2 = -1
    p2next = process2(w, v, i+1, weight+w[i], bag)
    if p2next != -1:
        p2 = p2next + v[i]
    return max(p1, p2)

def test():
    w = [3,2,1,1,5]
    v = [2,3,1,4,1]
    bag = 5
    print(maxValue(w,v,bag))
    assert maxValue(w, v, bag) == maxValue2(w, v, bag) == maxValue3(w, v, bag)

if __name__ == '__main__':
    test()
