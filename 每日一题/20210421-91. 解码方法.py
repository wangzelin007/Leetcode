# 一条包含字母A-Z 的消息通过以下映射进行了 编码 ：
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。
# 例如，"11106" 可以映射为：
# "AAJF" ，将消息分组为 (1 1 10 6)
# "KJF" ，将消息分组为 (11 10 6)
# 注意，消息不能分组为 (1 11 06) ，因为 "06" 不能映射为 "F" ，这是由于 "6" 和 "06" 在映射中并不等价。
# 给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数 。
# 题目数据保证答案肯定是一个 32 位 的整数。
# 示例 1：
# 输入：s = "12"
# 输出：2
# 解释：它可以解码为 "AB"（1 2）或者 "L"（12）。
# 示例 2：
# 输入：s = "226"
# 输出：3
# 解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
# 示例 3：
# 输入：s = "0"
# 输出：0
# 解释：没有字符映射到以 0 开头的数字。
# 含有 0 的有效映射是 'J' -> "10" 和 'T'-> "20" 。
# 由于没有字符，因此没有有效的方法对此进行解码，因为所有数字都需要映射。
# 示例 4：
# 输入：s = "06"
# 输出：0
# 解释："06" 不能映射到 "F" ，因为字符串含有前导 0（"6" 和 "06" 在映射中并不等价）。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/decode-ways
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 前导0: 第一位为0，直接输出0
# dp
# 1 2 3 4 5 6 7 8 9
# 10 11 12 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26
# if s[i]==0:
#     if s[i-1] == 0: return 0
#     if s[i-1] < 3: dp[i] = dp[i-2]
#     else: return 0
# else: # s[i] != 0 (1~9)
#     if s[i-1] == 0: dp[i] = dp[i-1]
#     else: # s[i-1] !=0
#         if s[i-1] == 1 dp[i] = dp[i-1] + dp[i-2]
#         elif s[i-1] == 2 s[i] = (1~6) dp[i] = dp[i-1] + dp[i-2]
#         elif s[i-1] == 2 s[i] = (7~9) dp[i] = dp[i-1]
#         elif s[i-1] > 2 dp[i] = dp[i-1]

class Solution1:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        if len(s) == 1: return 1
        dp = [0] * len(s)
        dp[0] = 1
        if s[1] == '0':
            if int(s[0]) < 3: dp[1] = 1
            else: return 0
        else:
            if s[0] == '1': dp[1] = 2
            elif s[0] == '2' and int(s[1]) <= 6: dp[1] = 2
            elif s[0] == '2' and int(s[1]) > 6: dp[1] = 1
            elif int(s[0]) > 2: dp[1] = 1
        for i in range(2,len(s)):
            if s[i] == '0':
                if s[i-1] == '0': return 0
                elif int(s[i-1]) < 3: dp[i] = dp[i-2]
                else: return 0
            else: # s[i] != 0
                if s[i-1] == '0': dp[i] = dp[i-1]
                elif s[i-1] == '1': dp[i] = dp[i-1] + dp[i-2]
                elif s[i-1] == '2' and int(s[i]) <= 6 : dp[i] = dp[i-1] + dp[i-2]
                elif s[i-1] == '2' and int(s[i]) > 6: dp[i] = dp[i-1]
                else: dp[i] = dp[i-1]
        return dp[len(s)-1]

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':return 0
        if len(s) == 1:return 1

        legalstr = set(str(i) for i in range(1, 27))

        a = 1
        b = 1

        for i in range(1, len(s)):
            if s[i] not in legalstr:
                if s[i - 1: i + 1] not in legalstr:
                    return 0
                else:
                    c = a
            else:
                if s[i - 1: i + 1] in legalstr:
                    c = b+a
                else:
                    c = b
            a = b
            b = c # 滚动起来
        return c

if __name__ == '__main__':
    a = Solution()
    s = '12' # 2
    print(a.numDecodings(s))
    s = '226' # 3
    print(a.numDecodings(s))
    s = '0' # 0
    print(a.numDecodings(s))
    s = '06' # 0
    print(a.numDecodings(s))
    s = '1' # 1
    print(a.numDecodings(s))
    s = "10011" # 0
    print(a.numDecodings(s))
    s = "230" # 0
    print(a.numDecodings(s))

