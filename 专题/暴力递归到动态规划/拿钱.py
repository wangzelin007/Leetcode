# coding: utf-8
# array 都是正数且无重复值。
# 每一个值都代表一种面额的钱，每张钱的数量无限制。
# aim 代表需要金钱，从array选取不同面额的钞票，一共有多少组成aim的方式。
def ways(arr, aim):
    if not arr or len(arr) == 0 or aim < 0:
        return 0
    return process(arr, 0, aim)


def process(arr, index, rest):
    # 不需要，因为如果 rest 为0，后面的钱都取0张
    # if rest == 0:
    #     return 1
    # 不需要，while 条件保证了 rest 不会小于0
    # if rest < 0:
    #     return 0
    if index == len(arr):
        return 1 if rest == 0 else 0
    i = 0
    ways = 0
    while i * arr[index] <= rest:
        ways += process(arr, index + 1, rest - i * arr[index])
        i += 1
    return ways


def ways2(arr, aim):
    if not arr or len(arr) == 0 or aim < 0:
        return 0
    dp = [[-1] * (aim + 1) for _ in range(len(arr) + 1)]
    return process2(arr, 0, aim, dp)


def process2(arr, index, rest, dp):
    if dp[index][rest] != -1:
        return dp[index][rest]
    if index == len(arr):
        dp[index][rest] = 1 if rest == 0 else 0
        return dp[index][rest]
    i = 0
    ways = 0
    while i * arr[index] <= rest:
        ways += process2(arr, index + 1, rest - i * arr[index], dp)
        i += 1
    dp[index][rest] = ways
    return ways


def waysdp(arr, aim):
    n = len(arr)
    if not arr or n == 0 or aim < 0:
        return 0

    dp = [[0] * (aim + 1) for _ in range(n + 1)]
    dp[n][0] = 1

    for index in range(n-1, -1, -1):
        for rest in range(aim + 1):
            i = 0
            ways = 0
            while i * arr[index] <= rest:
                dp[index][rest] += dp[index+1][rest - i * arr[index]]
                # ways += dp[index+1][rest - i * arr[index]]
                i += 1
            # dp[index][rest] = ways
    return dp[0][aim]

def waysdp2(arr, aim):
    n = len(arr)
    if not arr or n == 0 or aim < 0:
        return 0

    dp = [[0] * (aim + 1) for _ in range(n + 1)]
    dp[n][0] = 1

    for index in range(n-1, -1, -1):
        for rest in range(aim + 1):
            # dp[10][100] = dp[11][97] + dp[11][94] + ...
            # dp[10][100] = dp[11][97] + dp[10][97]
            dp[index][rest] = dp[index+1][rest]
            if rest - arr[index] >= 0:
                 dp[index][rest] += dp[index][rest-arr[index]]
            # i = 0
            # ways = 0
            # while i * arr[index] <= rest:
                # dp[index][rest] += dp[index+1][rest - i * arr[index]]
                # i += 1
    return dp[0][aim]


def test():
    arr = [5, 10, 50, 100]
    aim = 1000
    print(ways(arr, aim))
    print(ways2(arr, aim))
    print(waysdp(arr, aim))
    print(waysdp2(arr, aim))
    # assert ways(arr, aim) == ways2(arr, aim)


if __name__ == '__main__':
    test()
