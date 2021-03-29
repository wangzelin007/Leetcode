# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
import math

# class Solution:
#     # def integerBreak(self, n):
#     #     if n <= 3: return n
#     #     # // 代表地板除，先做除法，再向下取整。
#     #     a, b = n // 3, n % 3
#     #     if b == 0: return int(math.pow(3, a))
#     #     if b == 1: return int(math.pow(3, a - 1) * 4)
#     #     return int(math.pow(3, a) * 2)
#
#     def integerBreak(self,n):
#         if n <=3: return n
#         a,b = n//3,n%3
#         if b == 0: return self.quickMul(3,a)
#         if b == 1: return self.quickMul(3,a-1)*4
#         return self.quickMul(3,a)*2
#
#     #会溢出，所以pow需要优化
#     def quickMul(self,x,a):
#         if a == 0:
#             return 1
#         y = self.quickMul(x,a // 2)
#         return int(y * y) if a % 2 == 0 else int(y * y * x)


class Solution(object):
    def maxNiceDivisors(self, p):
        # 快速幂
        def kmi(x, n, mod):
            res = 1
            while n:
                if n & 1: res = (res * x) % mod
                x = x * x % mod
                n >>= 1
            return res

        mod = 10 ** 9 + 7
        if p <= 4: return p
        p, m = divmod(p, 3)
        if m == 0: return kmi(3, p, mod)
        if m == 1: return kmi(3, p - 1, mod) * 4 % mod
        return kmi(3, p, mod) * 2 % mod
# 拆分规则：
# 把数字 n 可能拆为多个因子 3 ，余数可能为 0,1,2 三种情况。
# 最优：0 若余数为0 math.pow(3, a)
# 次优：2 若余数为2 math.pow(3, a)*2
# 最差：1 若余数为1 math.pow(3, a-1)*4; 应把一份 3 + 1 替换为 2 + 2，因为 2 * 2 > 3 * 1。
# https://www.zhihu.com/question/49374703
# 1e9+7这个数，满足[0,1e9+7)内所有数，两个数相加不爆int，两个数相乘不爆long long
# 还有一点，由于1e9+7是质数，所以在[1,1e9+7)内所有数都存在关于1e9+7的逆元（这样就可以做除法）


if __name__ == '__main__':
    s = Solution()
    print(s.integerBreak(73))
    # 572712676???