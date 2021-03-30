# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
#
# 示例
# 输入：head = [1, 3, 2]
# 输出：[2, 3, 1]

# 递归
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reversePrint(self, head):
        if not head: return []
        else: return self.reversePrint(head.next) + [head.val]

# 辅助栈
class Solution(object):
    def reversePrint(self, head):
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]