# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
# O(N) && O(1)
import random

class LNode(object):
    def __init__(self,x):
        self.data = x
        self.next = None

def createLinkedList(l,t,a):
    head = LNode(None)
    cur = head
    i = 1
    n = t
    while i <= l:
        tmp = LNode(n)
        cur.next = tmp
        cur = tmp
        i += 1
        n += 2
    while a:
        tmp = LNode(n)
        cur.next = tmp
        cur = tmp
        a -= 1
        n += 2
    return head

def printLinkedList(head):
    if head.data is None:
        cur = head.next
    else:
        cur = head
    while cur:
        print cur.data,
        cur = cur.next
    print '\n'

def merge(head1, head2):
    if head1 is None or head1.next is None:
        return head2
    if head2 is None or head2.next is None:
        return head1
    cur1 = head1.next
    cur2 = head2.next
    head = LNode(None)
    cur = head
    while cur1 is not None and cur2 is not None:
        if cur1.data < cur2.data:
            cur.next = cur1
            cur = cur1
            cur1 = cur1.next
        else:
            cur.next = cur2
            cur = cur2
            cur2 = cur2.next
    if cur1 is None:
        cur.next = cur2
    else:
        cur.next = cur1
    return head



if __name__ == '__main__':
    head1 = createLinkedList(5,0,0)
    head2 = createLinkedList(8,1,2)
    printLinkedList(head1)
    printLinkedList(head2)
    head = merge(head1,head2)
    printLinkedList(head)