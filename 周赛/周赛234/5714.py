# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 替换字符串中的括号内容 超时
import re
# class Solution(object):
#     def evaluate(self, s, knowledge):
#         """
#         :type s: str
#         :type knowledge: List[List[str]]
#         :rtype: str
#         """
#         p = re.compile(r'[(](.*?)[)]', re.S)
#         paras = re.findall(p, s)
#         print paras
#         myDict = dict()
#         s2 = []
#         for i in knowledge:
#             myDict[i[0]] = i[1]
#             if i[0] in paras:
#                 s2.append(i[0])
#         print myDict
#         s1 = list(set(paras) - set(myDict.keys()))
#         print s1
#         i = 0
#         while s1:
#             tmp = s1.pop()
#             s = s.replace('('+str(tmp)+')','?')
#             print s
#         if s2:
#             s = s.replace('(','{').replace(')','}').format(**myDict)
#         return s

# class Solution(object):
#     def evaluate(self, s, knowledge):
#         """
#         :type s: str
#         :type knowledge: List[List[str]]
#         :rtype: str
#         """
#         p = re.compile(r'[(](.*?)[)]', re.S)
#         paras = re.findall(p, s)
#         myDict = dict()
#         for i in knowledge:
#             myDict[i[0]] = i[1]
#         keys = myDict.keys()
#         for i in paras:
#             if i not in keys:
#                 myDict[i] = '?'
#         s = s.replace('(','{').replace(')','}').format(**myDict)
#         return s

class Solution(object):
    def evaluate(self,s,knowledge):
        d = dict()
        for k,v in knowledge:
            d[k] = v
        ans = ""
        isKey = False
        key = ""
        for c in s:
            if c == '(':
                isKey = True
            elif c == ')':
                isKey = False
                if key in d:
                    ans += d[key]
                else:
                    ans += '?'
                key = ""
            elif not isKey:
                ans += c
            else:
                key += c
        return ans

if __name__ == '__main__':
    # s = "(name)is(age)yearsold(a)"
    # knowledge = [["name", "bob"], ["age", "two"]]
    # s = "hi(name)"
    # knowledge = [["a", "b"]]
    s = "(fy)(kj)(ege)r"
    knowledge = [["uxhhkpvp", "h"], ["nriroroa", "m"], ["wvhiycvo", "z"], ["qsmfeing", "s"], ["hbcyqulf", "q"], ["xwgfjnrf", "b"],
     ["kfipazun", "s"], ["wnkrtxui", "u"], ["abwlsese", "e"], ["iimsmftc", "h"], ["pafqkquo", "v"], ["kj", "tzv"],
     ["fwwxotcd", "t"], ["yzgjjwjr", "l"]]
    a = Solution()
    print(a.evaluate(s,knowledge))