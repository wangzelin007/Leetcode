# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。
#
# 示例 1:
# 输入: n = 1
# 输出: [1,2,3,4,5,6,7,8,9]
import math

class Solution1(object):
    def printNumbers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(n):
            j = int(math.pow(10,i)) # 1 10 100
            while j < int(math.pow(10,i+1)): # 10 100 1000
                res.append(j)
                j += 1
        return res

class Solution2(object):
    def printNumbers(self, n):
        res = []
        for i in range(1, 10 ** n):
            res.append(i)
        return res

class Solution3(object):
    def printNumbers(self, n):
        return range(1, 10 ** n)

# 考虑大数时
class Solution4:
    def printNumbers(self, n):
        def dfs(x):
            if x == n: # 终止条件：已固定完所有位
                s = ''.join(num[self.start:]) # 删除高位多余的 0
                # 列表从1开始
                if s != '0': res.append(int(s)) # 拼接 num 并添加至 res 尾部
                if n - self.start == self.nine: self.start -= 1 # 位数 - 多余的0位数 = 实际位数 = 9的位数；即全为9，start - 1
                return
            for i in range(10): # 遍历 0 - 9
                if i == 9: self.nine += 1 # 9的位数加1
                num[x] = str(i) # 固定第 x 位为 i
                dfs(x + 1) # 开启固定第 x + 1 位
            self.nine -= 1 # x + 1位固定完成后，并在回溯前恢复 nine = nine - 1 比如 09 -> 10 时

        num, res = ['0'] * n, [] # 起始数字定义为 n 个 0 组成的字符列表
        self.nine = 0 # 9的位数，最多n位
        self.start = n - 1 # 高位多余的0，最多n-1
        dfs(0) # 开启全排列递归
        return res

# 全排列
# 输入：n = 1
# 输出："0,1,2,3,4,5,6,7,8,9"
# 输入：n = 2
# 输出："00,01,02,...,10,11,12,...,97,98,99"
# 输入：n = 3
# 输出："000,001,002,...,100,101,102,...,997,998,999"
class Solution45:
    def printNumbers(self, n):
        def dfs(x):
            if x == n:  # 终止条件：已固定完所有位
                res.append(''.join(num))  # 拼接 num 并添加至 res 尾部
                return
            for i in range(10):  # 遍历 0 - 9
                num[x] = str(i)  # 固定第 x 位为 i
                dfs(x + 1)  # 开启固定第 x + 1 位

        num = ['0'] * n  # 起始数字定义为 n 个 0 组成的字符列表
        res = []  # 数字字符串列表
        dfs(0)  # 开启全排列递归
        return ','.join(res)

if __name__ == '__main__':
    s = Solution()
    # print(s.printNumbers(1))
    print(s.printNumbers(2))
    # print(s.printNumbers(3))