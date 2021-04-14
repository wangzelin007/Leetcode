# _*_ coding: utf-8 _*_
# 在字符串 s 中找出第一个只出现一次的字符。
# 如果没有，返回一个单空格。 s 只包含小写字母。
# 示例:
# s = "abaccdeff"
# 返回 "b"
# s = ""
# 返回 " "
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from collections import *
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        c = Counter(s)
        for k in s:
            if c[k] == 1:
                return k
        return " "

# dic
class Solution1(object):
    def firstUniqChar(self, s):
        dic = {}
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        for k in s:
            if dic[k] == 1:
                return k
        return " "

# order dic 默认为插入顺序
class Solution1(object):
    def firstUniqChar(self, s):
        dic = OrderedDict()
        for c in s:
            dic[c] = c not in dic
        for k, v in dic.items():
            if v: return k
        return " "

if __name__ == '__main__':
    a = Solution()
    s = "abaccdeff"
    # s = ""
    print(a.firstUniqChar(s))