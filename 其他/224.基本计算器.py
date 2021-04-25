# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
# 示例 1：
# 输入：s = "1 + 1"
# 输出：2
#
# 示例 2：
# 输入：s = " 2-1 + 2 "
# 输出：3
#
# 示例 3：
# 输入：s = "(1+(4+5+2)-3)+(6+8)"
# 输出：23
class Solution(object):
    def calculate(self, s):
        res, num, sign = 0, 0, 1 # res 返回结果；num 每一位数字；sign正负标记
        stack = []
        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
                # num = int(c)
            elif c == "+" or c == "-":
                res += sign * num
                num = 0
                sign = 1 if c == "+" else -1
                # print "+-",res
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ")":
                res += sign * num
                # print "res",res,"stack",stack
                num = 0
                res *= stack.pop()
                # print "res",res,"stack",stack
                res += stack.pop()
                # print "res",res,"stack",stack
                # print 'finish'
        res += sign * num #最后一位的处理
        print("sign",sign,"num",num)
        return res

if __name__ == '__main__':
    s = Solution()
    # print(s.calculate("1 + 1")) # 2
    # print(s.calculate(" 2-1 + 2")) # 3
    print(s.calculate("(1+(4+5+2)-3)+(6+8)")) # 23