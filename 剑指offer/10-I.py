# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：
#
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
# 斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。
# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
#
# 示例 1：
# 输入：n = 2
# 输出：1
#
# 示例 2：
# 输入：n = 5
# 输出：5

# 递归
class Solution1(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2: return n
        else:
            return self.fib(n-1) + self.fib(n-2)

#迭代
class Solution(object):
    def fib(self, n):
        a,b = 0,1
        for _ in range(n):
            a,b = b,a+b
        return a % 1000000007

if __name__ == '__main__':
    s = Solution()
    print(s.fib(0))
    print(s.fib(1))
    print(s.fib(2))
    print(s.fib(3))
    print(s.fib(4))
    print(s.fib(5))
    print(s.fib(37))
    print(s.fib(1000))
