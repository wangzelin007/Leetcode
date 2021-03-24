# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# a 起点到环入口点
# b 环入口点到相遇点
# c 相遇点到环入口点
# L 链长
# R 环长
# s 慢指标 2s 快指标
# L = a + b + c && R = b + c 推导出
# R = L - a && c = L - a - b
# s = a + b && 2s = a + b + nR 推导出
# s = nR = （n-1)R + R
# a + b = (n-1)R + L - a 推导出
# a = （n-1）R + c
# 即两个指标分别从起点和相遇点触发，第一次会在环入口相遇
import random

class LNode(object):
    def __init__(self,x):
        self.data = x
        self.next = None

def createLinkedList(l):
    head = LNode(None)
    cur = head
    i = 1
    while i < l:
        n = random.randint(0,9)
        tmp = LNode(n)
        cur.next = tmp
        cur = tmp
        i += 1
    # 构造环
    cur.next = head.next.next.next.next
    return head

def printLinkedList(head):
    cur = head.next
    hash = []
    while cur.next not in hash:
        print cur,cur.data,cur.next
        hash.append(cur.next)
        cur = cur.next
    print cur,cur.data,cur.next


def isLoop(head):
    if head is None or head.next is None:
        return None
    fast = head.next
    slow = head.next
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return slow
    return None

def findLoop(head, meetNode):
    first = head.next
    second = meetNode
    while first != second:
        first = first.next
        second = second.next
    return first

if __name__ == '__main__':
    head = createLinkedList(9)
    meetNode = isLoop(head)
    if meetNode is not None:
        printLinkedList(head)
        print '\n有环： 相遇点',meetNode,meetNode.data,meetNode.next,
        loopNode = findLoop(head, meetNode)
        print '\n环入口：', loopNode, loopNode.data
    else:
        print ('\n无环')