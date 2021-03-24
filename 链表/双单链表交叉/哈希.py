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
    head1 = LNode(None)
    head2 = LNode(None)
    cur1 = head1
    cur2 = head2
    i = 1
    tmp1 = LNode(1)
    tmp2 = LNode(2)
    cur1.next = tmp1
    cur1 = tmp1
    cur2.next = tmp2
    cur2 = tmp2
    while i <= l:
        n = random.randint(0,9)
        tmp = LNode(n)
        cur1.next = tmp
        cur1 = tmp
        cur2.next = tmp
        cur2 = tmp
        i += 1
    return head1,head2

def printLinkedList(head):
    if head.data:
        cur = head
    else:
        cur = head.next
    while cur:
        print cur.data,
        cur = cur.next

def cross(head1, head2):
    if not head1 or not head2:
        return False
    cur1 = head1.next
    cur2 = head2.next
    tmp = []
    while cur1:
        tmp.append(cur1.next)
        cur1 = cur1.next
    while cur2:
        if cur2 in tmp:
            return True
        else:
            cur2 = cur2.next
    return False

if __name__ == '__main__':
    head1,head2 = createLinkedList(8)
    printLinkedList(head1)
    print '\n'
    printLinkedList(head2)
    print(cross(head1, head2))
