# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 输入一个链表，输出该链表中倒数第k个节点。
# 为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
# 例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。
#
# 示例：
# 给定一个链表: 1->2->3->4->5, 和 k = 2.
# 返回链表 4->5.

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        len = 0
        cur = head
        while cur:
            cur = cur.next
            len += 1
        a = len - k
        while a:
            head = head.next
            a -= 1
        return head

# 双指针法，
# 指针i=0,j=k
# 指针i=n-k,j=尾
class Solution(object):
    def getKthFromEnd(self, head, k):
        s, f = head, head
        while k:
            f = f.next
            k -= 1
        while f:
            s = s.next
            f = f.next
        return s
