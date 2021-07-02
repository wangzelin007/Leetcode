# coding: utf-8
# 假设一行有 N 个位置，记为 1~N，N 一定大于或者等于 2
# 开始时机器人在其中的 M 位置上(M 一定是 1-N 中的一个)
# 如果机器人来到 1 位置，下一步只能往 2 走
# 如果机器人来到 N 位置，下一步只能往 N-1 走
# 如果机器人处于其他位置，可以选择下一步往左走或者往右走。
# 规定机器人必须走 K 步，最终能来到 P 位置(P 也是 1-N 中的一步)的方法一共有多少种。

def robotWalk(N, M, K, P):
    if (N < 2 or M < 1 or M > N or K < 1 or P < 1 or P > N):
        return 0
    return process(N, M, K, P)

def process(N, cur, rest, P):
    # M 初始位置 K 步数
    if rest == 0:
        if cur == P: return 1
        else: return 0
    if cur == 1:
        return process(N, 2, rest-1, P)
    if cur == N:
        return process(N, N-1, rest-1, P)
    return process(N, cur+1, rest-1, P) + process(N, cur-1, rest-1, P)

def robotWalk2(N, M, K, P):
    if (N < 2 or M < 1 or M > N or K < 1 or P < 1 or P > N):
        return 0
    dp = [[-1] * (K+1) for i in range(N+1)]
    # return walkCache(N, M, K, P, dp)
    walkCache(N, M, K, P, dp)
    return dp[M][K]

def walkCache(N, cur, rest, P, dp):
    if dp[cur][rest] != -1:
        return dp[cur][rest]
    if rest == 0:
        dp[cur][rest] = 1 if cur == P else 0
        return dp[cur][rest]
    if cur == 1:
        dp[cur][rest] = walkCache(N, 2, rest-1, P, dp)
        return dp[cur][rest]
    if cur == N:
        dp[cur][rest] = walkCache(N, N-1, rest-1, P, dp)
        return dp[cur][rest]
    dp[cur][rest] = walkCache(N, cur-1, rest-1, P, dp) + walkCache(N, cur+1, rest-1, P, dp)
    return dp[cur][rest]

def test():
    N = 5
    M = 2
    K = 3
    P = 3
    assert robotWalk(N, M, K, P) == 3
    assert robotWalk2(N, M, K, P) == 3

if __name__ == '__main__':
    test()
