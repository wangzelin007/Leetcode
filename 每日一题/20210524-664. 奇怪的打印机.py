# 有台奇怪的打印机有以下两个特殊要求：
# 打印机每次只能打印由 同一个字符 组成的序列。
# 每次可以在任意起始和结束位置打印新字符，并且会覆盖掉原来已有的字符。
# 给你一个字符串 s ，你的任务是计算这个打印机打印它需要的最少打印次数。
# 示例 1：
# 输入：s = "aaabbb"
# 输出：2
# 解释：首先打印 "aaa" 然后打印 "bbb"。
# 示例 2：
# 输入：s = "aba"
# 输出：2
# 解释：首先打印 "aaa" 然后在第二个位置打印 "b" 覆盖掉原来的字符 'a'。
# 提示：
# 1 <= s.length <= 100
# s 由小写英文字母组成
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/strange-printer
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# f[i][j] 代表打印完区间[i,j] 所需要的最小次数
# f[i][j] = f[i][j-1] # s[i]=s[j]
# f[i][j] = min(for k in (i,j-1)(f[i][k] + f[k+1][j]))
# 对于长度为 1 的区间，需要打印 1 次。f[i][i] = 1
# 为了保证动态规划的计算过程满足无后效性，在实际代码中，我们需要改变动态规划的计算顺序，
# 从大到小地枚举 i，并从小到大地枚举 j，这样可以保证当计算 f[i][j] 时，f[i][k] 和 f[k+1][j] 都已经被计算过。

class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for L in range(n-1,-1,-1):
            for R in range(L+1, n):
                if s[L] == s[R]:
                    dp[L][R] = dp[L][R-1]
                else:
                    tmp = 100
                    for mid in range(L, R, 1):
                        tmp = min(tmp, dp[L][mid] + dp[mid+1][R])
                    dp[L][R] = tmp
        return dp[0][n-1]

