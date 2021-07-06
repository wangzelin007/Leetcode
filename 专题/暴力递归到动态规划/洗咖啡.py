# coding: utf-8
# 给定一个数组，代表每个人喝完咖啡准备刷杯子的时间
# 只有一台咖啡机，一次只能洗衣歌杯子，耗时 a，洗完才能洗下一个。
# 每个咖啡杯也可以自己挥发干净，耗时 b，咖啡杯可以并行挥发。
# 返回让所有咖啡杯变干净的最早时间。

# 1. 使用咖啡机时，需要确定【咖啡机空闲的时间】和【喝完准备刷杯子的时间】的最大值
# 2. 可以直接选择挥发。
# 3. 求两种方案的最小值

def process(drinks, a, b, index, washtime):
    if index == len(drinks) - 1:
        return min(max(drinks[-1], washtime) + a, drinks[-1] + b)
    # 洗
    newWashTime = max(drinks[index], washtime) + a
    next1 = process(drinks, a, b, index+1, newWashTime)
    p1 = max(newWashTime, next1)
    # 挥发
    dry = drinks[index] + b
    next2 = process(drinks, a, b, index+1, washtime)
    p2 = max(dry, next2)
    return min(p1, p2)

def dpway(drinks, a, b, index, washtime):
    n = len(drinks)
    # 每一个都洗
    limit = 0
    for i in drinks:
        limit = max(limit, i) + a
    dp = [[0] * (limit+1) for _ in range(n)]
    for j in range(limit+1):
        dp[n-1][j] = min(max(drinks[-1], j) + a, drinks[-1] + b)
    for i in range(n-2, -1, -1):
        for j in range(limit+1):
            newWashTime = max(drinks[i], j) + a
            p1 = float("inf")
            if newWashTime <= limit:
                next1 = dp[i+1][newWashTime]
                p1 = max(newWashTime, next1)
            p2 = max(drinks[i] + b, dp[i+1][j])
            dp[i][j] = min(p1, p2)
    return dp[0][0]

def test():
    drinks = [1,1,5,5,7,10,12,12,12,12,12,12,15]
    a = 3
    b = 10
    index = 0
    washtime = 0
    print(process(drinks, a, b, index, washtime))
    print(dpway(drinks, a, b, index, washtime))

if __name__ == '__main__':
    test()