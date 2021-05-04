# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 请实现一个函数，输入一个整数（以二进制串形式），输出该数二进制表示中 1 的个数。
# 例如，把 9表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 2。
#
# 示例 1：
# 输入：00000000000000000000000000001011
# 输出：3
# 解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
#
# 示例 2：
# 输入：00000000000000000000000010000000
# 输出：1
# 解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。
#
# 示例 3：
# 输入：11111111111111111111111111111101
# 输出：31
# 解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。

# 1&0 = 0
# 1&1 = 1
# n>>1 右移 n<<1左移
class Solution1(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n:
            res += n&1
            n >>= 1
        return res

# n&(n-1) 将 n化为0
class Solution2(object):
    def hammingWeight(self, n):
        res = 0
        while n:
            res += 1
            n &= n-1
        return res