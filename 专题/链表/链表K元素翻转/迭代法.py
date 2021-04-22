# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 0.初始化 pre begin end next
# 1.指定 end
# 2.指定 next
# 3.end->None
# ----
# 放到rotate 里面做
# 4.begin end 之间倒序
# 5.pre->end
# ----
# 6.begin->next
# 7.指定pre
# 8.指定begin
import random

def rotateK(head, k):
    if head is None or head.next is None:
        return
    pre = head
    begin = head.next
    end = None
    next = None
    i = 1
    while begin != None:
        end = begin
        while i < k:
            if end.next is not None:
                end = end.next
            else:
                return
            i += 1
        next = end.next
        end.next = None
        pre.next = reverse(begin)
        begin.next = next
        pre = begin
        begin = next
        i = 1

def reverse(head):
    if head is None or head.next is None:
        return head
    newHead = reverse(head.next)
    head.next.next = head
    head.next = None
    return newHead

class LNode(object):
    def __init__(self,x):
        self.data = x
        self.next = None

def createLinkedList(l):
    head = LNode(None)
    cur = head
    i = 1
    while i <= l:
        n = random.randint(0,9)
        tmp = LNode(n)
        cur.next = tmp
        cur = tmp
        i += 1
    return head

def printLinkedList(head):
    if head.data is not None:
        cur = head
    else:
        cur = head.next
    while cur:
        print cur.data,
        cur = cur.next

if __name__ == '__main__':
    head = createLinkedList(10)
    printLinkedList(head)
    print '\n'
    rotateK(head, 3)
    printLinkedList(head)
    # print '\n 逆序'
    # head = reverse(head.next)
    # printLinkedList(head)
