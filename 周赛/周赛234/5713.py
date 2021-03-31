# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
import re
class Solution(object):
    def numDifferentIntegers(self, word):
        # type: (object) -> object
        """
        :type word: str
        :rtype: int
        """
        # 去除非数字，使用空格代替
        word = re.sub("\D", " ", word)
        # 查找不重复的数字
        return len(set([int(i) for i in word.split()]))

if __name__ == '__main__':
    s = Solution()
    # word = "leet1234code234"
    word = '1abc01cdfd001fddg'
    print(s.numDifferentIntegers(word))


