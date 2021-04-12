# _*_ coding: utf-8 _*_
# 给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
# 回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/palindrome-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# return str(nums) == str(nums)[::-1]

# 双指针法

# 进阶要求不转换为字符串
# 数学方法
class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        ans = 0
        while x > ans:
            ans = ans * 10 + x % 10
            x //= 10
        return x == ans or x == (ans // 10)
