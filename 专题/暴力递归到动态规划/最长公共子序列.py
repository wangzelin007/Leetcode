# coding: utf-8
# 两个字符串的最长公共子序列
# "ab1cd2ef345gh"
# "OPQ123RS4tx5yz"
# 最长公共子序列 "12345"
# if s1[i] != s2[j]:
# 1.1 dp[i][j] = dp[i-1][j-1] 第一种不用考虑了,肯定不是最优解。
# 1.2 dp[i][j] = dp[i-1][j]
# 1.3 dp[i][j] = dp[i][j-1]
# if s1[i] == s2[j]
# 2.  dp[i][j] = dp[i-1][j-1] + 1
# 初始化第 0 行，第 0 列
# dp[i][j] = max(dp[i][j-1], dp[i-1][j])
# dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1 if s1[i] == s2[j] else dp[i-1][j-1])
# 为什么第一种情况必定最小，因为第一种相当于二维图标中左上方位置
# 第二种情况相当于正上方位置，第三种情况相当于左侧位置。又知每个位置的决策依赖于自己的左上、左、上
# 所以计算第二种和第三种情况是必然包含了第一种情况。

def longestStr(s1, s2):
    n1, n2 = len(s1), len(s2)
    dp = [[0] * n2 for _ in range(n1)]
    dp[0][0] = 1 if s1[0] == s2[0] else 0
    for i in range(1, n1):
        dp[i][0] = max(dp[i-1][0], 1 if s1[i] == s2[0] else 0)
    for j in range(1, n2):
        dp[0][j] = max(dp[0][j-1], 1 if s1[0] == s2[j] else 0)
    for i in range(1, n1):
        for j in range(1, n2):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            if s1[i] == s2[j]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
    return dp[n1-1][n2-1]

def test():
    s1 = "ab1cd2ef345gh"
    s2 = "OPQ123RS4tx5yz"
    print(longestStr(s1, s2))

if __name__ == '__main__':
    test()