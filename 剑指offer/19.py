# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。
# 在本题中，匹配是指字符串的所有字符匹配整个模式。
# 例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。
#
# 示例 1:
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
#
# 示例 2:
# 输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
#
# 示例 3:
# 输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
#
# 示例 4:
# 输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
#
# 示例 5:
# 输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false

# dp[i][j] s[0:i] p[0:j]
# 五种情况：
# p[j-1] != * :
# 1. dp[i-1][j-1] & s[i-1] = p[j-1]      ab ab
# 2. dp[i-1][j-1] & p[j-1] = .           ab a.
# p[j-1] = * :
# 1. dp[i][j-2]                          a  a?*
# 2. dp[i-1][j] & s[i-1] = p[j-2]        aa a*
# 3. dp[i-1][j] & p[j-2] = .             ab .*

# "aaa"
# "ab*a*c*a"

class Solution:
    def isMatch(self, s, p):
        m, n = len(s) + 1, len(p) + 1 # 补0位 m行n列
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True
        print dp
        # 初始化首行 ?* ?*?* ?*?*?* 都是True
        for j in range(2, n, 2):
            dp[0][j] = dp[0][j-2] and p[j - 1] == '*'
        print dp
        for i in range(1, m):
            for j in range(1, n):
                if p[j-1] == '*':
                    if dp[i][j-2]: return True
                    elif dp[i-1][j] and s[i-1] == p[j-2]: dp[i][j] = True # aa a* | aa ab*a*c*
                    elif dp[i-1][j] and p[j-2] == '.': dp[i][j] = True # ab .* | "aaa" ".*"
                else:
                    if dp[i-1][j-1] and s[i-1] == p[j-1]: dp[i][j] = True
                    elif dp[i-1][j-1] and p[j-1] == '.': dp[i][j] = True
        return dp[-1][-1]

if __name__ == '__main__':
    a = Solution()
    s = "ab"
    p = ".*"
    # s = "mississippi"
    # p = "mis*is*p*."
    print(a.isMatch(s, p))
