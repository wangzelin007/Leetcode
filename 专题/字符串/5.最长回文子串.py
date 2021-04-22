# _*_ coding: utf-8 _*_
# 给你一个字符串 s，找到 s 中最长的回文子串。
# 示例 1：
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
# 示例 2：
# 输入：s = "cbbd"
# 输出："bb"
# 示例 3：
# 输入：s = "a"
# 输出："a"
# 示例 4：
# 输入：s = "ac"
# 输出："a"
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-palindromic-substring
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 1. 区间dp
# 2. 中心扩散 需要考虑基偶
# 3. 马拉车算法 填充#去基偶 并且使用辅助数组

# dp[i][j] 代表 i开始j结束是一个回文数
# 1. s[i] = s[j] 首位相等
# 2. dp[i+1][j-1] 是一个回文数
class Solution1:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        dp = [[1]*length for _ in range(length)]
        left, right = 0, 0 # 长度为1
        for i in range(1, length):
            for j in range(length-i):
                if s[j] == s[j+i] and dp[j+1][j+i-1]:
                    dp[j][j+i] = 1
                    left, right = j, j+i
                else:
                    dp[j][j+i] = 0
        # 为什么能取到最大值，因为i代表长度，从小到大，最后一次更新的必然最大
        return s[left:right+1]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start, max = 0, 1
        if n < 2: return s
        for i in range(n): dp[i][i] = True
        # 只能先终点后起点
        # 终点
        for j in range(1,n):
            # 起点
            for i in range(j):
                if s[i] == s[j]:
                    if j-i < 3: dp[i][j] = True # 否则j-1越界
                    else: dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
                if dp[i][j] and j-i+1 > max:
                    start = i
                    max = j-i+1
        return s[start:start+max]

# https://leetcode-cn.com/problems/longest-palindromic-substring/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-bao-gu/
# https://leetcode-cn.com/problems/longest-palindromic-substring/solution/5-zui-chang-hui-wen-zi-chuan-cc-by-bian-bian-xiong/
# https://leetcode-cn.com/problems/longest-palindromic-substring/solution/tu-jie-ma-la-che-suan-fa-by-wang_ni_ma-if33/
# https://leetcode-cn.com/problems/longest-palindromic-substring/solution/c-python3-fa-1zhong-xin-kuo-zhan-fa-zui-3zapg/
# todo
if __name__ == '__main__':
    a = Solution()
    s = "babad"
    s = "aaaa"
    s = "bbabdb"
    print(a.longestPalindrome(s))






