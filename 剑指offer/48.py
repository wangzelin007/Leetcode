# _*_ coding: utf-8 _*_
# 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
#
# 示例1:
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke"是一个子序列，不是子串。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 虫取法 + 动态方程
# 如果i 不在 dp[j-1] 中，dp[j] = dp[j-1] + 1 (dp[j-1] < j -i)
# 如果i 在 dp[j-1] 中，dp[j] = j - i(上次重复的值.index) (dp[j-1] >= j-i)
# 需要 dic 记录 key and index
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        dp1, dp0, dic = 0, 0, {} # dp1 dp[j] dp0 dp[j-1]
        for j in range(0, n):
            i = dic.get(s[j], -1)
            dic[s[j]] = j
            dp0 = dp0 + 1 if dp0 < j - i else j - i
            dp1 = max(dp1, dp0)
        return dp1

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        dic, res, i = {}, 0, -1
        for j in range(len(s)):
            if s[j] in dic:
                # "abba"
                i = max(dic[s[j]], i) # 为什么要取 max
            dic[s[j]] = j
            res = max(res, j - i)
        return res

if __name__ == '__main__':
    a = Solution()
    # s = " " # 1
    # s = " abc abc bb" # 4
    # s = "bbbbb" # 1
    # s = "pwwkew" # 3
    # s = "dvdf"
    s = "abba"
    print(a.lengthOfLongestSubstring(s))
