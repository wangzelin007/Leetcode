# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 某乐团的演出场地可视作 num * num 的二维矩阵 grid（左上角坐标为 [0,0])，每个位置站有一位成员。
# 乐团共有 9 种乐器，乐器编号为 1~9，每位成员持有 1 个乐器。
#
# 为保证声乐混合效果，成员站位规则为：自 grid 左上角开始顺时针螺旋形向内循环以 1，2，...，9 循环重复排列。
#
# 请返回位于场地坐标 [Xpos,Ypos] 的成员所持乐器编号。
#
# 示例 1：
# 输入：num = 3, Xpos = 0, Ypos = 2
# 输出：3
#
# 示例 2：
# 输入：num = 4, Xpos = 1, Ypos = 2
# 输出：5

# 数学找规律
# 先看在第几圈，再看在哪条边
class Solution:
    def orchestraLayout(self, num, xPos, yPos):
        layer = min([xPos, num - xPos - 1, yPos, num - yPos - 1])  # 位于第几圈
        v = (num*layer*4 - layer*layer*4) % 9  # 前几圈有多少个元素

        start, end = layer, num - layer

        if xPos == start:
            return (v + yPos - start) % 9 + 1

        if yPos == end - 1:
            return (v + end - start - 1 + xPos - start) % 9 + 1

        if xPos == end - 1:
            return (v + (end - start)*2 - 2 + end - yPos - 1) % 9 + 1

        if yPos == start:
            return (v + (end - start)*3 - 3 + end - xPos - 1) % 9 + 1

        return 0