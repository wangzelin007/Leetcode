# _*_ coding: utf-8 _*_
# 数字以0123456789101112131415…的格式序列化到一个字符序列中。
# 在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。
# 请写一个函数，求任意第n位对应的数字。
#
# 示例 1：
# 输入：n = 3
# 输出：3
#
# 示例 2：
# 输入：n = 11
# 输出：0
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 超时
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        data = [str(i) for i in range(n+1)]
        return int(''.join(data)[n])

# 找规律。。。
class Solution:
    def findNthDigit(self, n):
        digit, start, count = 1, 1, 9
        while n > count: # 1
            n -= count
            start *= 10
            digit += 1
            count = 9 * start * digit
        num = start + (n - 1) // digit # 2
        return int(str(num)[(n-1) % digit]) # 3
