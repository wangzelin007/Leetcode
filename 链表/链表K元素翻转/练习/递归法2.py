# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
import random

class LNode(object):
    def __init__(self,x):
        self.data = x
        self.next = None

def createLinkedList(l):
    head = LNode(1)
    cur = head
    i = 1
    while i < l:
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

def rotateK(head, k):
    if head is None or head.next is None:
        return
    i = 0
    cur = head
    while cur and i != k:
        cur = cur.next
        i += 1
    if i == k:
        cur = rotateK(cur, k)
        while i:
            next = head.next
            head.next = cur
            cur = head
            head = next
            i -= 1
        head = cur
    return head

if __name__ == '__main__':
    head = createLinkedList(15)
    printLinkedList(head)
    print '\n'
    head = rotateK(head, 4)
    printLinkedList(head)