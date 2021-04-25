# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
# 例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123"都表示数值，
# 但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。
class Solution(object):
    def isNumber1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        states = [
            {' ': 0, 's': 1, 'd': 2, '.': 4},  # 0. start with 'blank'
            {'d': 2, '.': 4},  # 1. 'sign' before 'e'
            {'d': 2, '.': 3, 'e': 5, ' ': 8},  # 2. 'digit' before 'dot'
            {'d': 3, 'e': 5, ' ': 8},  # 3. 'digit' after 'dot'
            {'d': 3},  # 4. 'digit' after 'dot' (‘blank’ before 'dot')
            {'s': 6, 'd': 7},  # 5. 'e'
            {'d': 7},  # 6. 'sign' after 'e'
            {'d': 7, ' ': 8},  # 7. 'digit' after 'e'
            {' ': 8}  # 8. end with 'blank'
        ]
        p = 0  # start with state 0
        for c in s:
            if '0' <= c <= '9':
                t = 'd'  # digit
            elif c in "+-":
                t = 's'  # sign
            elif c in "eE":
                t = 'e'  # e or E
            elif c in ". ":
                t = c  # dot, blank
            else:
                t = '?'  # unknown
            if t not in states[p]: return False
            p = states[p][t]
        return p in (2, 3, 7, 8)

# 0. 开始的空格
# 1. 幂符号前的正负号
# 2. 小数点前的数字
# 3. 小数点、小数点后的数字
# 4. 当小数点前为空格时，小数点、小数点后的数字（意思是没有正数部分，直接以小数点开始）
# 5. 幂符号（过渡状态）
# 6. 幂符号后的正负号（过渡状态）
# 7. 幂符号后的数字
# 8. 结尾的空格

    def isNumber2(self, s):
        states = [
            { ' ': 0, 's': 1, 'd': 2, '.': 4 }, # 0. start with 'blank'
            { 'd': 2, '.': 4 } ,                # 1. 'sign' before 'e'
            { 'd': 2, '.': 3, 'e': 5, ' ': 8 }, # 2. 'digit' before 'dot'
            { 'd': 3, 'e': 5, ' ': 8 },         # 3. 'digit' after 'dot'
            { 'd': 3 },                         # 4. is dot: 'digit' after 'dot' (‘blank’ before 'dot')
            { 's': 6, 'd': 7 },                 # 5. 'e'
            { 'd': 7 },                         # 6. 'sign' after 'e'
            { 'd': 7, ' ': 8 },                 # 7. 'digit' after 'e'
            { ' ': 8 }                          # 8. end with 'blank'
        ]
        print('状态states 长度为：',len(states))
        p = 0                           # start with state 0
        print('字符串s 的总长度为：',len(s))
        for c in s:
            if '0' <= c <= '9':
                t = 'd' # digit
                print('当前字符c=%s,\t属于 数字digit'%c)
            elif c in "+-":
                t = 's'     # sign
                print('当前字符c = %s,\t属于 正负号sign'%c)
            elif c in "eE":
                t = 'e'     # e or E
                print('当前字符c = %s,\t属于 幂符号e'%c)
            elif c in ". ":
                t = c       # dot, blank
                print('当前字符c = %s,\t属于 小数点.dot'%c)
            else:
                t = '?'               # unknown
                print('当前字符c = %s,Unknown'%c)
            if t not in states[p]:
                return False
            print('当前状态p =',p,end='\t')
            print('记录字符t =',t)
            p = states[p][t]
            print('故得到新状态p =',p,end='\t')
            print('跳转到states[%s]的字典中 找下一个状态\n'%p)
        # 为什么 4 dot 前为空时，dot 后的digit 不是最终状态？
        # 4 属于中间状态，实际是.
        # 比如测试用例 "." 会失败。
        return p in (2, 3, 7, 8)

if __name__ == '__main__':
    a = Solution()
    s = '5.2e-3'
    s = '.4'
    print(a.isNumber2(s))
    # s = 'a'
    # s = "e"
    # print(a.isNumber(s))