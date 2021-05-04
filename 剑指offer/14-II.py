# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m - 1] 。
# 请问 k[0]*k[1]*...*k[m - 1] 可能的最大乘积是多少？
# 例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
#
# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
#
# 示例 1：
# 输入: 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1
#
# 示例 2:
# 输入: 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
import math

class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <=3: return n-1
        a,b,p,x,rem = n//3-1,n%3,1000000007,3,1 # -1 是为了 b == 1时
        while a> 0:
            if a%2: rem = (rem*x)%p
            x = x**2%p
            a = a//2
        if b == 0: return (rem*3)%p # = 3^(a+1) % p
        elif b == 1: return (rem*4)%p # = 3^a * 4 % p
        else: return (rem*6)%p # = 3^(a+1) * 2  % p

def remainder1(x, a, p):
    rem = 1
    for _ in range(a):
        rem = (rem*x)%p
    return rem

def remainder2(x, a, p):
    rem = 1
    while a > 0:
        if a % 2: rem = (rem*x)%p
        x = x**2%p
        a = a//2
    return rem