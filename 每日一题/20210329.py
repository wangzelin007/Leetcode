# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 颠倒二进制位 leetcode 190
# 60      00111100
# <<	左移动运算符：运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0。
# a << 2 输出结果 240 ，二进制解释： 1111 0000
# >>	右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，>> 右边的数字指定了移动的位数
# a >> 2 输出结果 15 ，二进制解释： 0000 1111
# a << 20 11110000000000000000000000
# a >> 20 0
# ---------
#    10 = 0000 0100
# &   1 = 0000 0001
# ------------------
#         0000 0000
#
#   11 = 0000 1011 (不整除 2)                 28 = 0001 1100 (整除 2)
# &  1 = 0000 0001                         &  1 = 0000 0001
# ----------------                         ----------------
#        0000 0001
# ---------
# 所以 n & 1 也常用来判断 奇数偶数
# 位运算 或者 分治法
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res


if __name__ == '__main__':
    s = Solution()
    int = 00000010100101000001111010011100L
    print int
    print(s.reverseBits(int))