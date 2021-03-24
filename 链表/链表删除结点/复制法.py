# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# 之给出结点p，如何删除p本身
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

def remove(p):
    if p is None or p.next is None:
        return False
    p.data = p.next.data
    p.next = p.next.next
    return True


if __name__ == '__main__':
    head = createLinkedList(8)
    printLinkedList(head)
    p = head.next.next.next.next # 4.next delet 4
    remove(p)
    print '\n'
    printLinkedList(head)