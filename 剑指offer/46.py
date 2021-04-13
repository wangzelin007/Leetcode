# _*_ coding: utf-8 _*_
# 给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
# 一个数字可能有多个翻译。
# 请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
#
# 示例 1:
# 输入: 12258
# 输出: 5
# 解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# dp
# 如果num[i-1] + num[i] 不可以被翻译 dp[i] = dp[i-1]
# 反之 dp[i] = dp[i-2] + dp[i-1]
class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        strs = str(num)
        if len(strs) < 2: return len(strs)
        dp = [0] * len(strs)
        dp[0] = 1
        # 只有10~25之间的两位数可以被翻译
        dp[1] = 2 if '10' <= strs[0:2] <= '25' else 1
        for i in range(2, len(strs)):
            if '10' <= strs[i-1:i+1] <= '25':
                dp[i] = dp[i-2] + dp[i-1]
            else:
                dp[i] = dp[i-1]
        return dp[-1]

# 大佬解法
class Solution:
    def translateNum(self, num):
        s = str(num)
        a = b = 1
        for i in range(2, len(s) + 1):
            tmp = s[i - 2:i]
            c = a + b if "10" <= tmp <= "25" else a
            b = a
            a = c
        return a

# 此题对称左右动态规划都一样
class Solution:
    def translateNum(self, num):
        s = str(num)
        a = b = 1
        for i in range(len(s) - 2, -1, -1):
            a, b = (a + b if "10" <= s[i:i + 2] <= "25" else a), a
        return a

# 又因为可以反向dp，可以使用 // 10 % 10 进行数字求余
class Solution:
    def translateNum(self, num):
        a = b = 1 # a: dp[i-1] b: dp[i-2]
        y = num % 10
        while num != 0:
            num // 10
            x = num % 10
            tmp = 10 * x + y
            c = a + b if 10 <= tmp <= 25 else a
            a, b = c, a
            y = x
        return a

if __name__ == '__main__':
    s = Solution()
    # num = 624
    # num = 1
    # num = 25
    num = 12258
    print(s.translateNum(num))
