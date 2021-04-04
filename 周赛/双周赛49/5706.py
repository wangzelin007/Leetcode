# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 一个句子是由一些单词与它们之间的单个空格组成，且句子的开头和结尾没有多余空格。
# 比方说，"Hello World" ，"HELLO" ，"hello world hello world" 都是句子。
# 每个单词都 只 包含大写和小写英文字母。
#
# 如果两个句子 sentence1 和 sentence2 ，可以通过往其中一个句子插入一个任意的句子（可以是空句子）而得到另一个句子，那么我们称这两个句子是 相似的 。
# 比方说，sentence1 = "Hello my name is Jane" 且 sentence2 = "Hello Jane" ，我们可以往 sentence2 中 "Hello" 和 "Jane" 之间插入 "my name is" 得到 sentence1 。
# 给你两个句子 sentence1 和 sentence2 ，如果 sentence1 和 sentence2 是相似的，请你返回 true ，否则返回 false 。
#
# 示例 1：
# 输入：sentence1 = "My name is Haley", sentence2 = "My Haley"
# 输出：true
# 解释：可以往 sentence2 中 "My" 和 "Haley" 之间插入 "name is" ，得到 sentence1 。
#
# 示例 2：
# 输入：sentence1 = "of", sentence2 = "A lot of words"
# 输出：false
# 解释：没法往这两个句子中的一个句子只插入一个句子就得到另一个句子。
#
# 示例 3：
# 输入：sentence1 = "Eating right now", sentence2 = "Eating"
# 输出：true
# 解释：可以往 sentence2 的结尾插入 "right now" 得到 sentence1 。
#
# 示例 4：
# 输入：sentence1 = "Luky", sentence2 = "Lucccky"
# 输出：false

# 插入方式只有三种，头、中间、尾
# 如果是头插入，尾必然相等 -> 去头
# 如果是中间插入，头尾都相等 -> 去头尾
# 如果是尾插入，头必然相等 -> 去尾
# 去到有一个list 为0，即为需要插入的字符串
class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2):
        """
        :type sentence1: str
        :type sentence2: str
        :rtype: bool
        """
        s1, s2 = sentence1, sentence2
        if s1 == s2: return True
        if len(s1) > len(s2): s1, s2 = s2, s1 # 短长
        l1 = s1.split()
        l2 = s2.split()
        while l1:
            if not (l1[0] == l2[0] or l1[-1] == l2[-1]): return False
            if l1[0] == l2[0]:
                l1.pop(0)
                l2.pop(0)
            if l1 and l1[-1] == l2[-1]:
                l1.pop()
                l2.pop()
        return True

if __name__ == '__main__':
    s = Solution()
    sentence1 = 'Hello my name is Jane'
    sentence2 = 'Hello Jane'
    sentence3 = 'of'
    sentence4 = 'A lot of words'
    sentence5 = 'Eating right now'
    sentence6 = 'Eating'
    sentence7 = 'Luky'
    sentence8 = 'Lucccky'
    sentence9 = 'a b c d e'
    sentence10 = 'a c e'
    print(s.areSentencesSimilar(sentence1,sentence2)) # True
    print(s.areSentencesSimilar(sentence3, sentence4)) # False
    print(s.areSentencesSimilar(sentence5, sentence6)) # True
    print(s.areSentencesSimilar(sentence7, sentence8)) # False
    print(s.areSentencesSimilar(sentence9, sentence10)) # False