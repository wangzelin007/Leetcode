# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 给你一个坐标
# coordinates ，它是一个字符串，表示国际象棋棋盘中一个格子的坐标。下图是国际象棋棋盘示意图。
# 如果所给格子的颜色是白色，请你返回 true，如果是黑色，请返回 false 。
# 给定坐标一定代表国际象棋棋盘上一个存在的格子。坐标第一个字符是字母，第二个字符是数字。
#
# 示例1：
# 输入：coordinates = "a1"
# 输出：false
# 解释：如上图棋盘所示，"a1" 坐标的格子是黑色的，所以返回 false 。

# 示例2：
# 输入：coordinates = "h3"
# 输出：true
# 解释：如上图棋盘所示，"h3" 坐标的格子是白色的，所以返回 true 。

# 示例3：
# 输入：coordinates = "c7"
# 输出：false

class Solution1(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        x1 = coordinates[0]
        x2 = int(coordinates[1])
        list1 = ['a','c','e','g']
        if x1 in list1:
            if x2 % 2: return False
            else: return True
        else:
            if x2 % 2: return True
            else: return False

# 异或法
# 异或概念：相同返回0=False，相异返回1=True
# (j-1) % 2 ^ ord(i)-ord(a) %2
# ord('a') = 97
class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        nums = (int(coordinates[1]) - 1) % 2
        stags = (ord(coordinates[0]) - ord('a')) % 2
        return True if nums ^ stags else False

if __name__ == '__main__':
    s = Solution()
    coordinates1 = 'a1'
    coordinates2 = 'h3'
    coordinates3 = 'c7'
    print(s.squareIsWhite(coordinates1))
    print(s.squareIsWhite(coordinates2))
    print(s.squareIsWhite(coordinates3))
