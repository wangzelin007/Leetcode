# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。不得使用库函数，同时不需要考虑大数问题。
#
# 示例 1：
# 输入：x = 2.00000, n = 10
# 输出：1024.00000
#
# 示例 2：
# 输入：x = 2.10000, n = 3
# 输出：9.26100
#
# 示例 3：
# 输入：x = 2.00000, n = -2
# 输出：0.25000
# 解释：2-2 = 1/22 = 1/4 = 0.25

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        res = 1
        while n:
            if n < 0: x = 1/x; n = -n
            if n&1: res *= x
            x *= x
            n >>= 1
        return res