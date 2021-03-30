# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
#
# 示例 1：
# 输入：s = "We are happy."
# 输出："We%20are%20happy."
class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        ref = ''
        for i in s:
            if i == ' ':
                ref += '%20'
            else:
                ref += i
        return ref
# 一句话方式
# s.replace(' ','%20')
# '%20'.join(s.split())

if __name__ == '__main__':
    s = "We are happy."
    c = Solution()
    print(c.replaceSpace(s))