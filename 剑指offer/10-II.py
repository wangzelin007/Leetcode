# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
#
# 示例 1：
# 输入：n = 2
# 输出：2
#
# 示例 2：
# 输入：n = 7
# 输出：21
#
# 示例 3：
# 输入：n = 0
# 输出：1
# 0 1 0
# 1 1 1
# 2 2 1
# 3 3 2
# 4 5 3
# 5 8 5
# 6 13 8
# 7 21 13
# fn = fn-1 + fn-2
# a,b = b,a+b
class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        a,b = 1,1 # 只是初始值变化了
        for _ in range(n):
            a,b = b,a+b
        return a