# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 给定结点p,在p前面插入q(k)
# 1.在p后面插入 q
# 2.复制p.data -> q.data
# 3.p.data = k
import random

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
    if head.data is None:
        cur = head.next
    else:
        cur = head
    while cur:
        print cur.data,
        cur = cur.next

def insert(p,x):
    q = LNode(x)
    tmp = p.next
    p.next = q
    q.next = tmp
    q.data = p.data
    p.data = x

if __name__ == '__main__':
    head = createLinkedList(8)
    printLinkedList(head)
    p = head.next.next.next.next
    insert(p,11)
    print '\n'
    printLinkedList(head)