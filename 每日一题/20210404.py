# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 781
# 森林中，每个兔子都有颜色。其中一些兔子（可能是全部）告诉你还有多少其他的兔子和自己有相同的颜色。
# 我们将这些回答放在 answers 数组里。
# 返回森林中兔子的最少数量。
#
# 示例:
# 输入: answers = [1, 1, 2]
# 输出: 5
# 解释:
# 两只回答了 "1" 的兔子可能有相同的颜色，设为红色。
# 之后回答了 "2" 的兔子不会是红色，否则他们的回答会相互矛盾。
# 设回答了 "2" 的兔子为蓝色。
# 此外，森林中还应有另外 2 只蓝色兔子的回答没有包含在数组中。
# 因此森林中兔子的最少数量是 5: 3 只回答的和 2 只没有回答的。
#
# 输入: answers = [10, 10, 10]
# 输出: 11
#
# 输入: answers = []
# 输出: 0

# 模拟占位法
class Solution1(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        dic = {}
        res = 0
        sums = 0
        for i in answers:
            if i == 0: res += 1
            if i in dic and dic[i] != 0:
                dic[i] = dic[i] - 1
                if dic[i] == 0:
                    res += i + 1
            else:
                dic[i] = i
        lists = filter(lambda i: dic[i] != 0, dic.keys()) # 没有归0的
        if lists: sums = sum([i+1 for i in lists]) # 每个+1 再求和
        return res + sums

# x 只兔子 回答 y
# x / y+1 * y+1 向上取整ceil
# ceil(x/(y+1))=(x+y)//(y+1) 向上取整转换为向下取整
from collections import Counter
class Solution2(object):
    def numRabbits(self, answers):
        dic = Counter(answers) # y:x
        ans = sum((x + y) // (y + 1) * (y + 1)for y,x in dic.items())
        return ans

# x/y+1 向上取整
import math
from collections import Counter
class Solution(object):
    def numRabbits(self, answers):
        dic = Counter(answers) # y:x
        list = [int(math.ceil(float(x) / float(y + 1)) * (y + 1))for y,x in dic.items()]
        print list
        ans = sum(list)
        return ans

if __name__ == '__main__':
    s = Solution()
    answers1 = [1, 1, 2]
    answers2 = [10, 10, 10]
    answers3 = []
    answers4 = [1, 0, 0, 0, 1] # 5
    answers5 =  [1, 0, 0, 0, 1, 1] # 6
    print(s.numRabbits(answers1)) # 5
    print(s.numRabbits(answers2)) # 11
    print(s.numRabbits(answers3)) # 0
    print(s.numRabbits(answers4))  # 5
    print(s.numRabbits(answers5))  # 7