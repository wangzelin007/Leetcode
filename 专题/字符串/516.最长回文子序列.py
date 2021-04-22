# _*_ coding：utf-8 _*_
# 给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。
# 可以假设 s 的最大长度为 1000 。
# 示例 1:
# 输入:
# "bbbab"
# 输出:
# 4
# 一个可能的最长回文子序列为 "bbbb"。
# 示例 2:
# 输入:
# "cbbd"
# 输出:
# 2
# 一个可能的最长回文子序列为 "bb"。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-palindromic-subsequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# dp[i][j] 代表 i到j最长子序列长度
# 1. if s[i] = s[j] dp[i][j] = dp[i+1][j-1] + 2
# 2. else dp[i][j] = max(dp[i+1][j], dp[i][j-1])
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if n < 2: return s
        dp = [[0]* n for _ in range(n)]
        for i in range(n): dp[i][i] = 1
        for j in range(1,n):
            # 保证dp[0][n-1] 最后产生
            for i in range(j-1,-1,-1):
                if s[i] == s[j]:
                    # 可以省略 因为初始化为0
                    if j-i < 3: dp[i][j] = j-i+1
                    else: dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        print(dp)
        return dp[0][n-1]

if __name__ == '__main__':
    a = Solution()
    s = 'aabaca'
    # s = 'aaaa'
    # s = 'cbbd'
    print(a.longestPalindromeSubseq(s))