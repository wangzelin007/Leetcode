# _*_ coding: utf-8 _*_
# 输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。
# 例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。
#
# 示例 1：
# 输入：n = 12
# 输出：5
# 示例 2：
# 输入：n = 13
# 输出：6
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 想象成密码锁，固定一位为1，旋转其他位，该位为1的可能组合。
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit, res = 1, 0
        high, cur, low = n // 10, n % 10, 0
        while high != 0 or cur != 0:
            if cur == 0: res += high * digit
            elif cur == 1: res += high * digit + low + 1
            else: res += (high + 1) * digit
            low += digit * cur
            cur = high % 10
            high //= 10
            digit *= 10
        return res

if __name__ == '__main__':
    n = 1999
    s = Solution()
    print(s.countDigitOne(n))